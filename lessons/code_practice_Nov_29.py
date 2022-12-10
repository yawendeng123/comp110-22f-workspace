class Staff:
    name: str
    is_cs: bool

    def __init__(self, name: str, is_cs: bool):
        self.name = name
        self.is_cs = is_cs
    
    def greet(self) -> str:
        msg: str = f"Hello, I'm {self.name} "
        if not self.is_cs:
            msg += "NOT "
        return msg + "in CS"
