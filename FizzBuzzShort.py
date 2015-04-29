'''Problem Statement

Write a program that prints (to STDOUT) the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

The goal is to write the shortest code possible.
'''


for i in range(1,101):
    print ('FizzBuzz' if i%15==0 else ('Buzz' if i%5==0 else \
    	  ('Fizz' if i%3==0 else i) ) )