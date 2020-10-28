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