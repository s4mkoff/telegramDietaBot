from enum import Enum
from typing import Dict

class KiloType(Enum):
    K_1300 = 1300
    K_1500 = 1500
    K_1700 = 1700

class Answer:
    def __init__(
        self,
        imageSrc: str,
        text: Dict[KiloType, str]
    ):
        self.imageSrc = imageSrc
        self.text = text