from config import * # noqa
from enum import Enum, auto
from pathlib import Path
import sys

ROOT = Path(sys.executable).parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets"

class RodneyState(Enum):
    IDLE = auto()
    ENTER = auto()
    TALKING = auto()
    EXIT = auto()