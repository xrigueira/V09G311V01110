"""
Escribe un programa que acepte tres parámetros: dos números y un carácter. Si el
carácter es + los números se suman, con - se restan, con * se multiplican, con / se
dividen, y con ˆ se eleva el primero al segundo
"""

def operation(num1, num2, caracter):
    
    if caracter == '+':
        return num1 + num2
    
    elif caracter == '-':
        return num1 - num2
    
    elif caracter == '*':
        return num1 * num2
    
    elif caracter == '/':
        return num1 / num2
    
     elif caracter == '^':
        return num1**num2
    
    else:
        print(TypeError)

print(operation(num1=1, num2=2, caracter='+'))