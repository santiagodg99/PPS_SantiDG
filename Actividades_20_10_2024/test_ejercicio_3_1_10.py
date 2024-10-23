from ejercicio_3_1_10 import *

def test_menor_y_mayor():
    precios = [50, 75, 46, 22, 80, 65, 8]
    menor = 8
    mayor = 80
    
    assert menor_y_mayor(precios) == (8,80)