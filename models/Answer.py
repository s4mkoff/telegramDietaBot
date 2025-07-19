
class MenuButton:
    def __init__(
        self,
        text: str,
        callback: str
    ):
        self.text = text
        self.callback = callback
        
class Answer:
    def __init__(
        self,
        imageSrc: str,
        text: str,
        buttons: list[MenuButton],
        isKeyboard: bool = True
    ):
        self.imageSrc = imageSrc
        self.text = text
        self.isKeyboard = isKeyboard
        self.buttons = buttons

    