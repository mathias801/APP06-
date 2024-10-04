import flet as ft
import random


def main(page: ft.Page):
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar,contenedor_principal
    
    page.title="Adivina el numero"
    
    
    #generar un numero aleatorio
    numero_secreto=random.randint(1,100)
    
    #crear los elementos de la interfaz
    titulo=ft.Text("Adivina el numero secreto entre 1 y 100",size=20,color="black")
    entrada_numero=ft.TextField(label="Tu adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar")
    texto_resultado=ft.Text("",color="black")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="#E6E6FA",
        width=page.window.width,
        height=page.window.height,
        padding=20
        
        
    )

ft.app(main)
