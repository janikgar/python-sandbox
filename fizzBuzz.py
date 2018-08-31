#!/usr/bin/python3

def fizzBuzz(limit):
  for num in range(1,limit+1):
    if num % 5 == 0 & num % 3 == 0:
      print("FizzBuzz")
    elif num % 5 == 0:
      print("Buzz")
    elif num % 3 == 0:
      print("Fizz")
    else:
      print(num)

fizzBuzz(15)