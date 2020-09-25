# Python_Code_Timer
A simple Python class for tracking code execution time.

Copy the class to your script and use:
my_timer = gTimer()
my_timer.print_start_time()
my_timer.print_end_time()

Prints:
  Started on  Fri Sep 25 15:10:05 2020
  Finished in  0.0  minutes on  Fri Sep 25 15:10:05 2020
############################################################## 


or place python_code_time.py in the same directory as your script. In your script use:

from python_code_timer import gTimer

my_timer = gTimer()
my_timer.print_start_time()
my_timer.print_end_time()
