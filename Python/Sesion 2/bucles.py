numero = 7
# primera parte
if numero > 5:
    print("El número es mayor a 5")
else:
    print("El número es menor o igual a 5")
    
# segunda parte    
if numero > 5 and numero % 2 == 0:
    print("El número es mayor a 5 y es par")
else:
    print("El número no cumple ambas condiciones")
    
# tercera parte
for i in range(1, 6):
    print(f"El cuadrado de {i} es {i**2}")
    
#cuarta parte
i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1