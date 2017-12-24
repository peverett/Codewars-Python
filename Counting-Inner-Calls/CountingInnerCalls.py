#!/usr/python
"""

The aim of this kata is to determine the number of sub-function calls made by 
an unknown function.

You have to write a function named count_calls which:
* takes as parameter a function and its arguments (args, kwargs)
* calls the function
* returns a tuple containing:

The number of function calls made inside it and inside all the sub-called 
functions recursively the function return value.
NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.
"""
from __future__ import print_function
import sys


def count_calls(func, *args, **kwargs):
  """Count calls in function func"""
  calls = -1

  def call_trace(frame, event, arg):
      nonlocal calls
      if event != 'call':
          return
      calls += 1
      return

  sys.settrace(call_trace)
  rv = func(*args, **kwargs)
  sys.settrace(None)
  
  return calls, rv

if __name__ == "__main__":

    def quick_inner():
        value = 1

        def add_one():
            nonlocal value
            value += 1
            return value
            
        return add_one

    f = quick_inner()
    print("f returns {}".format( f() ))

