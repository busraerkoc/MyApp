#!/usr/bin/env python3
# The package folder contains a special file called __init__.py , which stores the package's content. It serves two proposes:
#1-The Python interpreter recognizes a folder as the pacakge if it contains __init__.py file
#2-__init.py__.py exposes specified resources from its modules to be imported.
#An empty __init__.py file makes all functions from above modules available when this package is imported.
#The __init__.py file is normally kept empty. 

from .functions import average, power
from .greet import SayHello

#The specified functions can now be imported in the interpreter session or another executable script.`
