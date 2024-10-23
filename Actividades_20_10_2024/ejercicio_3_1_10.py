def menor_y_mayor(precios: list):
    menor = mayor = precios[0]
    
    for precio in precios:
        if precio < menor:
            menor = precio
        if precio > mayor:
            mayor = precio
            
    return menor,mayor

