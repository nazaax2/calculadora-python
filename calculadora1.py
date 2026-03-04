print(" ")
print("Calculadora Inteligente")
print(" ")
5
num1 = float(input("dime un numero:"))
op = input("dime una operacion (+,-,*,/):")
num2 = float(input("dime otro numero:"))

print(" ")


if op == "+":
    result = num1 + num2 
    print("tu resultado es:",result)
elif op == "-":
    result = num1 - num2 
    print("tu resultado es:",result)
elif op == "*":
    result = num1 * num2
    print("tu resultado es:",result)
elif op == "/":
    if num2 == "0":
     print("no se puede divir por 0")
     result = None
    else:
     result = num1 / num2
     print("tu resultado es:",result) 

else:
   print("operacion no valida")
   result = None
if result is not None:
   if result > 0:
    print("tu resultado es positivo")
   elif result <0:
    print("tu resultado es negativo")
   else:
      print("tu resultado es 0")

print(" ")
