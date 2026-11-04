from enum import Enum, auto
from pathlib import Path
import importlib.util
import sys

ROOT = Path(sys.executable).parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets"
CONFIG_PY = ROOT / "config.py"

if not CONFIG_PY.is_file():
    raise FileNotFoundError(f"config.py not found")

spec = importlib.util.spec_from_file_location("_external_config", CONFIG_PY)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

for name in dir(config):
    if not name.startswith("_"):
        globals()[name] = getattr(config, name)

class RodneyState(Enum):
    IDLE = auto()
    ENTER = auto()
    TALKING = auto()
    EXIT = auto()