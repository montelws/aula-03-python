# principal.py -> usa o modulo
import class_calculadora as c 
print (c.somar (2, 3 ))  # 5
print (c.pi)  # 3.14159

# importando_modulo_script.py
from  class_calculadora import somar, subtrair, multiplicar, dividir
print (somar (2, 3))  # 5
