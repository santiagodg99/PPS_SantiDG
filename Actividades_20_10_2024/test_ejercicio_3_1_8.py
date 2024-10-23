from ejercicio_3_1_8 import *

def test_esPalindroma():
    palabra = "radar"
    assert esPalindroma(palabra) == True
    
    palabra = "santi"
    assert esPalindroma(palabra) == False