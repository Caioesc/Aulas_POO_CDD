class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.dormindo = False
        self.comendo = False

    def falar(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome} foi falar.")
                    self.falando = True
                else:
                    print(f"{self.nome} já está falando.")
            else:
                print(f"{self.nome} não pode falar, pois está comendo.")
        else:
            print(f"{self.nome} não pode falar, pois está dormindo.")

    def dormir(self):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} foi dormir.")
                    self.dormindo = True
                else:
                    print(f"{self.nome} já está dormindo.")
            else:
                print(f"{self.nome} não pode dormir, pois está comendo.")
        else:
            print(f"{self.nome} não pode dormir, pois está falando.")

    def comer(self):
        if self.dormindo == False:
            if self.falando == False:
                if self.comendo == False:
                    print(f"{self.nome} foi comer.")
                    self.comendo = True
                else:
                    print(f"{self.nome} já está comendo.")
            else:
                print(f"{self.nome} não pode comer, pois está falando.")
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

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"{self.nome} foi miando...")

class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"{self.nome} foi mugindo...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} foi latindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def chiar(self):
        print(f"{self.nome} foi chiando...")

class Atleta():
    def __init__(self,nome, peso):
        self.nome = nome
        self.aposentado = False
        self.peso = peso
        self.aquecido = False
    def aposentar(self):
        if self.aposentado == False:
            print(f"O atleta {self.nome} se aposentou.")
            self.aposentado = True
        else:
            print(f"O atleta {self.nome} não pode se aposentar, pois já é aposentado")
    def aquecer(self):
        if self.aposentado == False:
            if self.aquecido == False:
                print(f"O atleta {self.nome} está aquecendo!")
                self.aquecido = True
            else:
                print(f"{self.nome} não vai aquecer, pois já está aquecido!")
        else:
            print(f"{self.nome} não pode aquecer, pois está aposentado.")

    def desaposentar(self):
        if self.aposentado == True:
            self.aposentado = False
            print(f"{self.nome} não está mais aposentado.")
        else:
            print(f"{self.nome} já não é aposentado!")

class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def correr(self):
        if self.aposentado == True:
            print(f"{self.nome} não pode correr, pois é aposentado.")
        elif self.aquecido == True:
            print(f"{self.nome} foi correr.")
        else:
            print(f"{self.nome} precisa aquecer antes de correr")

class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        if self.aposentado == True:
            print(f"{self.nome} não pode nadar, pois é aposentado.")
        elif self.aquecido == True:
            print(f"{self.nome} foi nadar.")
        else:
            print(f"{self.nome} precisa aquecer antes de nadar")

class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def pedalar(self):
        if self.aposentado == True:
            print(f"{self.nome} não pode pedalar, pois é aposentado.")
        elif self.aquecido == True:
            print(f"{self.nome} foi pedalar.")
        else:
            print(f"{self.nome} precisa aquecer antes de pedalar")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

def gravar(nome):
    with open("Nomes.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")

def mostrar():
    with open("Nomes.txt", "r") as arq:
        conteudo = arq.read()
        print(conteudo)







