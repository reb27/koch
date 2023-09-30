##******************************************************************************
## Fractal 2: Floco de Neve
## Grupo 4 (Maria Fernanda, Rebeca Freitas, Thiago Lopes Chaves) 

import turtle as t
import tkinter as tk
from tkinter import simpledialog
import random

colors = ['yellow', 'orange', 'pink', 'green', 'blue', 'red', 'violet']

#Essa função é responsável por desenhar recursivamente a curva de koch, a cada vez que o nível é decrementado
def desenha_sub_triangulo(nivel, lado):
    if nivel == 0:
        t.forward(lado)
    else:
        for angulo in [60, -120, 60, 0]:
            desenha_sub_triangulo(nivel - 1, lado / 3)
            t.left(angulo)
            
def main():
    i = 1
    window = tk.Tk()
    window.withdraw() 
    lado = simpledialog.askinteger("Tamanho do lado", "Informe o tamanho do lado do triângulo:")
    n = simpledialog.askinteger("Níveis", "Digite quantos níveis deseja:")
    window.destroy() 
    window = t.Screen()
    t.speed(0)
    t.colormode(255)
    t.penup()
    t.pendown()
    t.shape("turtle")
    t.pensize(3)
    # Itera por cada lado do triângulo, fazendo uma curva à esquerda para cada um dos ângulos e iniciando a construção dos subtriângulos.
    while i<=3:
        t.color(random.choice(colors),random.choice(colors) )
        for angulo in [60, 240, 240]:
            t.left(angulo)
            desenha_sub_triangulo(n, lado)
            i += 1

    window.exitonclick()

main()

#################################################################################
## REFERÊNCIAS -----------------------------------------------------------------
#################################################################################
## https://vegibit.com/change-pen-color-in-python-turtle/
## [Fractal floco de neve de Koch] https://www.youtube.com/watch?v=7iFy7KRaLQ8&t=302s
## [Percorrendo a Curva de Koch] https://docs.ufpr.br/~ewkaras/ensino/fractais/Koch.pdf
## [A Curva de Koch (Fractal Floco de Neve)] https://www.batebyte.pr.gov.br/Pagina/Curva-de-Koch-Fractal-Floco-de-Neve
## ******************************************************************************