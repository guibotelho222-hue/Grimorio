import sys
import os
from pathlib import Path

# Descobre o caminho exato onde o app está sendo executado no Android
APP_DIR = Path(__file__).parent.resolve()

# Adiciona a raiz e todas as subpastas principais ao sys.path do Python
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

COMPONENTS_DIR = APP_DIR / "components"
if COMPONENTS_DIR.exists() and str(COMPONENTS_DIR) not in sys.path:
    sys.path.insert(0, str(COMPONENTS_DIR))

TABS_DIR = APP_DIR / "tabs"
if TABS_DIR.exists() and str(TABS_DIR) not in sys.path:
    sys.path.insert(0, str(TABS_DIR))
