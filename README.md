# FizzBuzz_In_TensorFlow
Just for fun

As far as I know, FizzBuzz is a programming training in LeetCode, reference to https://leetcode.com/problems/fizz-buzz/description/

One day, I found a video on Youtube: https://www.youtube.com/watch?v=F1vek6ULo9w ,
and reference to the article: http://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/

A crazy guy used neural network to handle FizzBuzz problem!  (???)
The GitHub of the author: https://github.com/joelgrus/fizz-buzz-tensorflow

As a freshmen in machine learning, I should follow the master, practice it on my laptop!

In this project, there are 2 major files: training_data_generator.py and FizzBuzz_in_NN.py

- training_data_generator.py
	As file name, this file is used to generate the label date and the data set for training. 
	The idea here is to convert the decimal into binary, and store its' binary digital separately. 
	For example, convert 5 into 101b, and store into list [1, 0, 1]. 
	We will convert amount of numbers into the format as our training data, create the label target as well. 
	The generated data will be stored at folder name "data"

- FizzBuzz_in_NN.py
	A simple neural network built via Keras for training

The accuracy in this project is roughly at 98%
