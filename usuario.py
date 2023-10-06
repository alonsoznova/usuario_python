class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0
    def hacer_deposito(self, amount):
        self.balance += amount
    def hacer_retiro(self, amount):
        self.balance -= amount
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")
    def transfer_dinero(self, other_user, amount):
        other_user.hacer_deposito(amount)
        self.balance -= amount
    
Martin = Usuario("Martín")
Paloma = Usuario("Paloma")
Angel = Usuario("Ángel")

Martin.hacer_deposito(160)
Martin.hacer_deposito(100)
Martin.hacer_retiro(20)
Martin.mostrar_balance_usuario()

Paloma.hacer_deposito(200)
Paloma.hacer_deposito(100)
Paloma.hacer_retiro(50)
Paloma.hacer_retiro(100)
Paloma.mostrar_balance_usuario()

Angel.hacer_deposito(300)
Angel.hacer_retiro(100)
Angel.hacer_retiro(100)
Angel.hacer_retiro(50)
Angel.mostrar_balance_usuario()

Martin.transfer_dinero(Angel, 40)
Martin.mostrar_balance_usuario()
Angel.mostrar_balance_usuario()
