import sys
import traceback
from pathlib import Path
import flet as ft

# Injeta a raiz no caminho de busca do Python
ROOT_DIR = Path(__file__).parent.resolve()
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Importação direta da aba
import oraculo_tab

def main(page: ft.Page):
    page.title = "Grimório v2.0"
    page.theme_mode = ft.ThemeMode.DARK
    
    try:
        page.clean()
        # Se oraculo_tab tiver a função de montagem da interface:
        if hasattr(oraculo_tab, "build_oraculo_tab"):
            page.add(oraculo_tab.build_oraculo_tab(page))
        else:
            page.add(ft.Text("Oráculo carregado!"))
        page.update()
    except Exception as e:
        page.clean()
        page.add(
            ft.Text("Erro na interface:", color="red", size=18),
            ft.Text(str(e), color="yellow"),
            ft.Text(traceback.format_exc(), color="white70", size=10)
        )
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
