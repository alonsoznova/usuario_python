class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0
    def hacer_deposito(self, amount):
        self.balance += amount
        return self
    def hacer_retiro(self, amount):
        self.balance -= amount
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")
        return self
    def transfer_dinero(self, other_user, amount):
        other_user.hacer_deposito(amount)
        self.balance -= amount
        return self
    
Martin = Usuario("Martín")
Paloma = Usuario("Paloma")
Angel = Usuario("Ángel")

Martin.hacer_deposito(160).hacer_deposito(100).hacer_retiro(20).mostrar_balance_usuario()

Paloma.hacer_deposito(200).hacer_deposito(100).hacer_retiro(50).hacer_retiro(100).mostrar_balance_usuario()

Angel.hacer_deposito(300).hacer_retiro(100).hacer_retiro(100).hacer_retiro(50).mostrar_balance_usuario()

Martin.transfer_dinero(Angel, 40).mostrar_balance_usuario()
Angel.mostrar_balance_usuario()
