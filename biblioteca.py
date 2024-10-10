class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.fala = False
        self.sono = False
        self.fome = False

    def falar(self):
        if self.sono == False and self.fome == False and self.fala == False:
            print(f"{self.nome} foi falar")
            self.fala = True
        elif self.sono == False and self.fome == True:
            print(f"{self.nome} Não pode falar, pois está comendo.")
        elif self.fala == True:
            print(f"{self.nome} já está falando")
        else:
            print(f"{self.nome} Não pode falar, pois está dormindo")

    def dormir(self):
        if self.fala == False and self.fome == False and self.sono == False:
            print(f"{self.nome} foi dormir")
            self.sono = True
        elif self.fala == True and self.fome == False:
            print(f"{self.nome} Não pode dormir, pois está dormindo")
        elif self.sono == True:
            print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} Não pode dormir, pois está comendo")

    def comer(self):
        if self.sono == False and self.fala == False and self.fome == False:
            print(f"{self.nome} foi comer")
            self.fome = True
        elif self.sono == False and self.fala == True:
            print(f"{self.nome} não pode comer, pois está falando")
        elif self.fome == True:
            print(f"{self.nome} já está comendo")
        else:
            print(f"{self.nome} não pode comer, pois está dormindo")

    def pararDeComer(self):
        self.fome = False

    def pararDeDormir(self):
        self.sono = False

    def pararDeFalar(self):
        self.fala = False