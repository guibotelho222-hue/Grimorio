import sys
import traceback
from pathlib import Path
import flet as ft

# Adiciona o diretório raiz ao sys.path
ROOT_DIR = Path(__file__).parent.resolve()
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Importação direta dos ficheiros que estão na raiz
import oraculo_tabimport flet as ft
import sys
import traceback
from pathlib import Path

# =========================================================================
# GARANTE REGISTRO DE CAMINHOS NO ANDROID
# =========================================================================
APP_DIR = Path(__file__).parent.resolve()
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

# Adiciona diretórios de módulos caso existam
for folder in ["components", "tabs"]:
    folder_path = APP_DIR / folder
    if folder_path.exists() and str(folder_path) not in sys.path:
        sys.path.insert(0, str(folder_path))

def main(page: ft.Page):
    page.title = "Grimório v2.0 - Rei Joaquim"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    try:
        # Tenta aplicar o tema customizado se existir em theme.py
        try:
            import theme
            if hasattr(theme, "theme"):
                page.theme = theme.theme
            if hasattr(theme, "dark_theme"):
                page.dark_theme = theme.dark_theme
        except Exception:
            pass

        # Limpa a tela para carregar a interface principal
        page.clean()

        # =================================================================
        # CARREGAMENTO DAS ABAS PRINCIPAIS DO GRIMÓRIO
        # =================================================================
        # Importe e monte suas abas reais aqui (exemplo: oraculo_tab, etc.)
        import oraculo_tab

        tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Oráculo",
                    icon=ft.icons.AUTO_STORIES,
                    content=oraculo_tab.build_oraculo_tab(page) if hasattr(oraculo_tab, "build_oraculo_tab") else ft.Text("Aba Oráculo")
                ),
                # Adicione outras abas do seu projeto conforme necessário
            ],
            expand=True
        )

        page.add(tabs)
        page.update()

    except Exception as e:
        # Caso algum módulo específico das abas falhe, mostra exatamente qual foi na tela
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("ERRO AO CARREGAR ABAS:", color="red", size=18, weight="bold"),
                    ft.Text(str(e), color="yellow", size=14),
                    ft.Text(traceback.format_exc(), color="white70", size=10)
                ]),
                padding=20
            )
        )
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
