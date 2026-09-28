# script_principal.py
import class_calculadora
s = class_calculadora.somar (2, 3)

# script_alternativo.py
from class_calculadora import somar 
s = somar (2, 3) 

import class_calculadora as calc 
s = calc.somar (2, 3)