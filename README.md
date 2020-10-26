# CA304 Computer Networks 2 - University Assignment

### Final submission containts 3 files (excluding this README).
1. **ip_calculator.py** is the main program. Can simply be run with ```python3 ip_calculator.py```. This program acts as a module from which the 3 primary functions (**get_class_stats(), get_subnet_stats() and get_supernet_stats()**) can be imported.

2. **gui_ip_calculator.py** is an interactive GUI program. It uses tkinter to render a useful GUI which allows the user to enter inputs and retrieve outputs easily from **ip_calculator.py**. Can also be simply run with ```python3 gui_ip_calculator.py```.

3. **tests_ip_calculator.py** are a series of unit test suites which can be run independently, again with ```python3 tests_ip_calculator.py```. They run tests over the main program.


### Additional Notes:
#### In terms of extra functionality for the final 10 marks, I have included:
- A GUI (**gui_ip_calculator.py**)
- Full help documentation (docstrings / pydoc)
- Thorough unit tests (pyunit)
- Calculating subnets for Class A addresses (also Class B).
- Supernetting Class B addresses.

One final comment I want to make is with regards to subnetting Class B addresses. The only issue I ran into pertained to Class B addresses where the subnet mask went into the extra octet (i.e non-default subnet mask for Class B). Essentially, whether Class B addresses can be subnet to numbers higher than /24.

In looking at your examples and methods, my first attempt resulted in a single (somewhat elegant) general case that worked for all Classes. However, upon further research and discussion, different results and a different method appeared to be the convention for this 'special' case. As such, I am still not 100% certain which output you would expect. (Overall, there is a high degree of discrepancy in resources online).

You will see on ```line 210``` of **ip_calculator.py** that I have a check for whether a class_b flag has been set. This check, and the flag are in place assuming the latter convention I came across is what you expected. However, if you expected results where the extra octet is not dealt with for Class B addresses and non-default Class B subnet masks, this check can easily be removed and the following code block not executed. Thus, the output will reflect the original method we followed.