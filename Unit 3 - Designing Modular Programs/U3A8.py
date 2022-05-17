# n = int(input()) - 2

def fibonacci(n):
    fibonacci = [1, 2]
    for i in range(n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

# fibonacci(n)
from turtle import *
import turtle as tur
  
tur.circle(90)