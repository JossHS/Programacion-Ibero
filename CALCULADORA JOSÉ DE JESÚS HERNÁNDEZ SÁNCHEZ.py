#CALCULADORA
#JOSÉ DE JESÚS HERNÁNDEZ SÁNCHEZ IME

op = input("Elige una operación (+,-,*,/): ")

num1 = float(input("Escribe el primer número: "))

num2 = float(input("Escribe el segundo número: "))

if op == "+":
        print (f"El resultado es: {num1+num2}")
elif op == "-":
        print (f"El resultado es:{num1-num2}")
elif op == "*":
        print (f"El resultado es: {num1*num2}")
elif op == "/":
        if num2 != 0:
            print(f"El resultado es: {num1 / num2} " )
        else:
            print("No se puede dividir entre cero!")





    








