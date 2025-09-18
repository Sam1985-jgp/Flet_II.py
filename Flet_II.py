# -*- coding: utf-8 -*-
import sys
import os

# Evitar criação de arquivos .pyc
sys.dont_write_bytecode = True

import Flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.window_width = 400
    page.window_height = 500

    # Campos
    nome = ft.TextField(label="Nome", width=350)
    email = ft.TextField(label="Email", width=350)
    mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=4, width=350)

    confirmacao = ft.Text(value="", color="green")

    # Função do botão
    def enviar_click(e):
        if nome.value and email.value and mensagem.value:
            confirmacao.value = f"Obrigado, {nome.value}! Sua mensagem foi enviada."
            confirmacao.color = "green"
            nome.value = ""
            email.value = ""
            mensagem.value = ""
        else:
            confirmacao.value = "⚠️ Por favor, preencha todos os campos."
            confirmacao.color = "red"
        page.update()

    # Botão
    enviar_btn = ft.ElevatedButton(text="Enviar", on_click=enviar_click)

    # Layout
    page.add(
        ft.Column(
            [
                ft.Text("Entre em contato", size=20, weight="bold"),
                nome,
                email,
                mensagem,
                enviar_btn,
                confirmacao
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START,
        )
    )

# Rodar app sem criar pycache
if __name__ == "__main__":
    ft.app(target=main)
