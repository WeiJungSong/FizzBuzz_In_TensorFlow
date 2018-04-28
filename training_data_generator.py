import numpy
import pickle
import os

########
# The function is used to convert the decimal into bianry "in charator list"
# /param n: the number ready for convert 
# /return : the charator list of the number in binary
########
def dec_to_bin(n):
    val = n
    binnary = []

    while val != 0:
        binnary.append(str(val % 2))
        val //= 2

    return binnary

########
# The function is used to fill the leading zero 
# /param num_str: the charator list which is waiting for fill the leading zero
# /param total_digital: how many digital this number should has
# /return : the charator list which is finished the zero filling
########
def fill_leading_zero(num_str, total_digital):
    fill_amount = total_digital - len(num_str)
    leading_zero = ["0"] * fill_amount
    num_str = num_str + leading_zero 

    return num_str

########
# The function is used to check the fizzbuzz result for label training data (?????)
# /param n: the number for distinguish
# /return : the label, reference to comment in below
########
def fizzbuzz_for_nn_training(n):
    
    if n % 15 == 0:
        # type 3 indicate "FizzBuzz"
        result = 3
    elif n % 3 == 0:
        # type 1 indicate "Fizz"
        result = 1
    elif n % 5 == 0:
        # type 2 indicate "Buzz"
        result = 2
    else:
        #type 0 for general number
        result = 0

    return result


def save_to_file(train_input_data, lable_data):
    if not os.path.exists("data"):
        os.makedirs("data")

    fd = open("data/train_input_data.dat", "wb")
    pickle.dump(train_input_data, fd)
    fd.close()

    fd = open("data/lable_data.dat", "wb")
    pickle.dump(lable_data, fd)
    fd.close()


def read_from_file():
    try:
        fd = open("data/train_input_data.dat", "rb")
        train_input_data = pickle.load(fd)
        fd.close()

        fd = open("data/lable_data.dat", "rb")
        lable_data = pickle.load(fd)
        fd.close()
    except FileNotFoundError:
        print("Read training/lable data file fail because file not found")
        print("Try to generate it...")
        main()
        print("Should be OK to run the FizzBuzz in NN again")
        exit()
    except Exception as e:
        print("Unknown error in read training/lable data file")
        print("Exception with: ", e)
        exit()

    return train_input_data, lable_data

# not important
def show_progress(n, prg1, prg2, prg3, prg4):
    if n == prg1:
        print("...25%", end = "")
    if n == prg2:
        print("...50%", end = "")
    if n == prg3:
        print("...75%", end = "")
    if n == prg4:
        print("...100%")


def main():
    number_list = []
    label_list = []
    RANGE_BEGIN = 1000
    RANGE_END = 200000

    # prepare for fill the leading zero in binary digital
    total_digital = len(dec_to_bin(RANGE_END))

    # just some output string on screen, doesn't matter
    print("data generating...0%", end = "")
    prg1 = (RANGE_END + RANGE_BEGIN) // 4
    prg2, prg3, prg4 = prg1 * 2, prg1 * 3, RANGE_END - 1

    # generate the training data from number RANGE_BEGIN to RANGE_END
    for n in range(RANGE_BEGIN, RANGE_END):
        show_progress(n, prg1, prg2, prg3, prg4)

        #convert the number and fill the leading zero
        arr = fill_leading_zero(dec_to_bin(n), total_digital)
        #convert the charator list into number list
        arr = list(map(int, arr))

        # save the training data into list
        number_list.append(arr)
        # create the label list
        label_list.append(fizzbuzz_for_nn_training(n))

    save_to_file(number_list, label_list)
     


if __name__ == '__main__':
    main()
