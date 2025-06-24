a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
operacion = input("Operación(+, -, *, /): ")

if operacion == "+":
    print (a + b)
elif operacion == "-":
    print (a - b)
elif operacion == "*":
    print (a * b)
elif operacion == "/":
    if b != 0:
        print (a / b)
    else:
        print ("Error: división por cero")
else:
    print ("Operacion no valida")
    