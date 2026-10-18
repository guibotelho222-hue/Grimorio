import flet as ft
import sys
import traceback
from pathlib import Path

# Garante o caminho correto dos módulos
APP_DIR = Path(__file__).parent.resolve()
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

def main(page: ft.Page):
    page.title = "Grimório v2.0 - Rei Joaquim"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    try:
        # Teste de importação do tema ou módulos para ver se rebenta aqui
        import theme
        
        # Se chegou aqui, a base carregou! Vamos mostrar uma tela de sucesso provisória
        page.add(
            ft.Icon(name=ft.icons.SHIELD, size=80, color="amber"),
            ft.Text("Grimório v2.0 Ativado!", size=22, weight="bold", color="amber"),
            ft.Text("O motor do Rei Joaquim está online.", size=14, color="white70"),
            ft.ElevatedButton(
                "Entrar no Grimório", 
                on_click=lambda e: page.add(ft.Text("Navegação principal em construção!", color="green"))
            )
        )
        page.update()

    except Exception as e:
        # Se houver qualquer erro de código ou importação, ele ESCREVE na tela do telemóvel!
        page.clean()
        page.add(
            ft.Text("FALHA CRÍTICA DE EXECUÇÃO:", color="red", size=18, weight="bold"),
            ft.Text(str(e), color="yellow", size=12),
            ft.Text(traceback.format_exc(), color="white70", size=10)
        )
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
