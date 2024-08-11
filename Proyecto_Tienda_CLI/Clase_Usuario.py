class Usuario:
    id: int
    nombre: str
    nick: str
    password: str
    role_admin: bool
    def __init__(self, id: int, nombre: str, nick: str, password: str, role_admin: bool) -> None:
        self.id = id
        self.nombre = nombre
        self.nick = nick
        self.password = password
        self.role_admin = role_admin
    def reset_password (self, password):
        self.password = password
    def __eq__(self, id: int):
        return self.id == id
    def __str__(self) -> str:
        return f"´{self.nombre} - {self.nick} - Admin: {self.role_admin}"
    def modificar(self, nombre: str, nick: str, role_admin: bool):
        self.nombre = nombre
        self.nick = nick
        self.role_admin = role_admin
    def check_user(self, nick: str, password: str):
        return True if self.nick == nick and self.password == password else False
    def check_role(self) -> str:
        return 'admin' if self.role_admin else 'user'

