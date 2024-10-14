class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.dormindo = False
        self.comendo = False

    def falar(self):
        if self.dormindo == False and self.comendo == False and self.falando == False:
            print(f"{self.nome} foi falar.")
            self.falando = True
        elif self.dormindo == False and self.comendo == True:
            print(f"{self.nome} não pode falar, pois está comendo.")
        elif self.falando == True:
            print(f"{self.nome} já está falando.")
        else:
            print(f"{self.nome} não pode falar, pois está dormindo.")

    def dormir(self):
        if self.falando == False and self.comendo == False and self.dormindo == False:
            print(f"{self.nome} foi dormir.")
            self.dormindo = True
        elif self.falando == True and self.comendo == False:
            print(f"{self.nome} não pode dormir, pois está falando.")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo.")
        else:
            print(f"{self.nome} não pode dormir, pois está comendo.")

    def comer(self):
        if self.dormindo == False and self.falando == False and self.comendo == False:
            print(f"{self.nome} foi comer.")
            self.comendo = True
        elif self.dormindo == False and self.falando == True:
            print(f"{self.nome} não pode comer, pois está falando.")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo.")
        else:
            print(f"{self.nome} não pode comer, pois está dormindo.")

    def pararDeComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"Não tem como {self.nome} parar de comer, pois não está comendo.")

    def pararDeDormir(self):
        if self.comendo == True:
            self.dormindo = False
            print(f"{self.nome} parou de dormir.")
        else:
            print(f"Não tem como {self.nome} parar de dormir, pois não está dormindo.")

    def pararDeFalar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar.")
        else:
            print(f"Não tem como {self.nome} parar de falar, pois não está falando.")