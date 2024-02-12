from dataclasses import dataclass
from enum import Enum, auto
from typing import List
import json

class BookStatus(Enum):
    AVAILABLE = auto()
    BORROWED = auto()
    RESERVED = auto()

@dataclass
class Book