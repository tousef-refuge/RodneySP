from config import *
from enum import Enum, auto
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets"

class RodneyState(Enum):
    IDLE = auto()
    ENTER = auto()
    TALKING = auto()
    EXIT = auto()