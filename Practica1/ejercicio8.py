"""
Escribe un programa que calcule la media de una serie de notas introducidas por teclado.
Piensa en un método como determinar que el usuario ya no quiere introducir más datos.
"""
import random

num_grades = int(input('How many grades do you want to work with: '))

grades = []

while len(grades) < num_grades:
    new_grade = input('Insert new grade: ')

    if new_grade == 'q':
        break
    
    grades.append(int(new_grade))
    print('Lista de notas', grades)
mean = sum(grades)/len(grades)

print('The resulting mean is: ', mean)