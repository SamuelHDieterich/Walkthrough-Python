# RPG SIMPLES

# BIBLIOTECAS
import os                   # Sistema operacional
import sys                  # Sistema-interpretador
from random import random   # Gerador de números aleatórios [0,1)
from time import sleep      # Aguardar


# CLASSES

class Jogador():

    """
    # JOGADOR
    ---------

    Classe primária para criar um objeto do tipo `jogador`.

    ## ATRIBUTOS

    - Vida
    - Mana
    - Ataque

    ## MÉTODOS

    - `atacar()`: Retorna um valor (inteiro) correspondente ao dano físico.
    - `magia()`: Retorna um valor (inteiro) correspondente ao dano por magia.
    - `descanso()`: Recupera uma fraçã de alguns status do personagem.
    - `status()`: Retorna um texto com os atributos do personagem.
    """
    
    # Atributos básicos do personagem
    # Aqui é possível configurar o balenceamento do jogo
    ATRIBUTOS = {
        "Vida"   : 500,
        "Mana"   : 200,
        "Ataque" : 100
    }

    # Valor que será aplicado nos atributos do personagem
    # conforme a especialidade/classe de cada um
    VANTAGENS = {
        "Fraqueza"  : 0.8,
        "Normal"    : 1.0,
        "Força"     : 1.2
    }

    # Fração mínima e máxima de dano, respectivamente
    DANO_AMPLITUDE = (0.5, 1.5)

    # Custo no uso de magia para a mana
    MAGIA_CUSTO = 50

    # Fração de vida e mana recuperada ao final de uma batalha
    RECUPERAÇÃO = 0.1


    def __init__(self):

        "Configura os atributos básicos."
        
        self.max_vida   = self.ATRIBUTOS["Vida"]
        self.vida       = self.max_vida
        self.max_mana   = self.ATRIBUTOS["Mana"]
        self.mana       = self.max_mana
        self.ataque     = self.ATRIBUTOS["Ataque"]

    def atacar(self):

        "Calcula o valor de dano físico que o personagem vai infligir nesse turno."

        return round(((self.DANO_AMPLITUDE[1]-self.DANO_AMPLITUDE[0])*random()+self.DANO_AMPLITUDE[0])*self.ataque)

    def magia(self):

        "Calcula o valor de dano mágico que o personagem vai infligir nesse turno."

        # Custo do uso da magia
        self.mana -= self.MAGIA_CUSTO

        return round(((self.DANO_AMPLITUDE[1]-self.DANO_AMPLITUDE[0])*random()+self.DANO_AMPLITUDE[0])*self.max_mana)
    
    def descanso(self):

        "Recupera uma parte das estatísticas do jogador: vida e mana."

        # Recuperação da vida
        self.vida += round(self.max_vida * self.RECUPERAÇÃO)
        if self.vida > self.max_vida:
            self.vida = self.max_vida
        
        # Recuperação da mana
        self.mana += round(self.max_mana * self.RECUPERAÇÃO)
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def status(self):

        "Retorna uma `str` com as estatísticas do personagem."

        return f"Vida: {self.vida}/{self.max_vida} | Mana: {self.mana}/{self.max_mana} | Ataque: {self.ataque}"


class Guerreiro(Jogador):

    """
    # GUERREIRO
    -----------

    Classe forte e resistente, com muitos pontos de vida.

    - Vida: +++
    - Mana: +
    - Ataque: ++
    """

    def __init__(self):
        
        "Atualiza os atributos básicos."
        
        # Resgata os atributos da classe pai.
        # Nese caso, não é necessário, pois não possuiu parâmetros.
        super().__init__()

        self.max_vida   = round(self.max_vida * self.VANTAGENS["Força"])
        self.vida       = self.max_vida
        self.max_mana   = round(self.max_mana * self.VANTAGENS["Fraqueza"])
        self.mana       = self.max_mana
        self.ataque     = round(self.ataque * self.VANTAGENS["Normal"])
        

class Ninja(Jogador):

    """
    # NINJA
    -------

    Classe preparada para o dano físico, com muitos pontos de ataque.

    - Vida: +
    - Mana: ++
    - Ataque: +++
    """

    def __init__(self):

        "Atualiza os atributos básicos."
        
        # Resgata os atributos da classe pai.
        # Nese caso, não é necessário, pois não possuiu parâmetros.
        super().__init__()

        self.max_vida   = round(self.max_vida * self.VANTAGENS["Fraqueza"])
        self.vida       = self.max_vida
        self.max_mana   = round(self.max_mana * self.VANTAGENS["Normal"])
        self.mana       = self.max_mana
        self.ataque     = round(self.ataque * self.VANTAGENS["Força"])


class Mago(Jogador):

    """
    # MAGO
    ------

    Classe especializada em magia, com muitos pontos de mana.

    - Vida: ++
    - Mana: +++
    - Ataque: +
    """

    def __init__(self):

        "Atualiza os atributos básicos."
        
        # Resgata os atributos da classe pai.
        # Nese caso, não é necessário, pois não possuiu parâmetros.
        super().__init__()

        self.max_vida   = round(self.max_vida * self.VANTAGENS["Normal"])
        self.vida       = self.max_vida
        self.max_mana   = round(self.max_mana * self.VANTAGENS["Força"])
        self.mana       = self.max_mana
        self.ataque     = round(self.ataque * self.VANTAGENS["Fraqueza"])


class Inimigo():

    """
    # INIMIGO
    ---------

    Classe primária para criar um objeto do tipo `inimigo`.

    ## ATRIBUTOS

    - Vida
    - Ataque

    ## MÉTODOS

    - `atacar()`: Retorna um valor (inteiro) correspondente ao dano físico.
    - `status()`: Retorna um texto com os atributos do personagem.
    """

    ATRIBUTOS = dict(zip(
        Jogador().ATRIBUTOS.keys(), 
        list(map(lambda x: x*0.65, list(Jogador.ATRIBUTOS.values())))
        ))
    
    DANO_AMPLITUDE = (0.5, 1.5)

    def __init__(self):

        "Configura os atributos básicos."
        
        self.max_vida   = round(self.ATRIBUTOS["Vida"] * (0.5 + random()))
        self.vida       = self.max_vida
        # self.max_mana   = self.ATRIBUTOS["Mana"]
        # self.mana       = self.max_mana
        self.ataque     = round(self.ATRIBUTOS["Ataque"] * (0.5 + random()))

    def atacar(self):

        "Calcula o valor de dano físico que o inimgo vai infligir nesse turno."

        return round(((self.DANO_AMPLITUDE[1]-self.DANO_AMPLITUDE[0])*random()+self.DANO_AMPLITUDE[0])*self.ataque)

    def status(self):

        "Retorna uma `str` com as estatísticas do inimigo."

        # return f"Vida: {self.vida}/{self.max_vida} | Mana: {self.mana}/{self.max_mana} | Ataque: {self.ataque}"
        return f"Vida: {self.vida}/{self.max_vida} | Ataque: {self.ataque}"


# FUNÇÕES

def clear():

    "Limpa o terminal."

    os.system('cls' if os.name=='nt' else 'clear')

# MAIN
# Roda apenas se este programa que está em execução e não caso tenha sido importado.
if __name__ == '__main__':

    # Opções de clases
    CLASSES = {
        "Guerreiro" : Guerreiro(),
        "Ninja"     : Ninja(),
        "Mago"      : Mago()
    }

    clear() # Limpa o terminal

    print("Classes disponíveis:")
    # Mostra as classes disponíveis
    for i in CLASSES:
        print(f"- {i}")
    
    # Escolha de classe
    while True:
        # Já "limpa" a string de entrada
        escolha = input("\nEscolha a sua classe:").capitalize().replace(" ","")
        try:
            player = CLASSES[escolha]
            break
        except:
            print("\nEscolha inválida!")

    # Pontuação do jogador
    score = 0
    
    while True:

        clear()  # Limpa o terminal

        print("Um novo inimigo aparece!\n")
        inimigo = Inimigo() # Gera um novo inimigo

        while True:
            
            # Estatística dos objetos
            print(f"INIMIGO: {inimigo.status()}")
            print(f"JOGADOR: {player.status()}")

            # Opções de ações
            print("\nATACAR | MAGIA | SAIR")

            while True:
                
                # Escolha de ação do usuário
                evento = input("\nO que fazer? ").lower().replace(" ","") 

                # ATACAR
                if evento == "atacar":
                    dano = player.atacar()  # Calcula o dano
                    print(f"\nVocê ataca o inimigo e inflige {dano} de dano.")
                    inimigo.vida -= dano    # Aplica o dano
                    break
                
                # MAGIA
                elif evento == "magia":
                    # Verifica se possui mana suficiente
                    if player.mana >= player.MAGIA_CUSTO:
                        dano = player.magia()   # Calcula o dano
                        print(f"\nVocê usa uma magia no inimigo e inflige {dano} de dano.")
                        inimigo.vida -= dano    # Aplica o dano
                        break
                    else:
                        print("Mana insuficiente!")
                
                # SAIR
                elif evento == "sair":
                    print(f"\nFim de jogo!\nPontuação: {score}")
                    sys.exit()  # Fecha o interpretador
                    
                else:
                    print("\nComando inválido!")
            
            # Inimigo vivo, ataca
            if inimigo.vida > 0:
                sleep(1)    # Espera
                dano = inimigo.atacar() # Calcula o dano
                print(f"O inimigo te ataca e inflige {dano} de dano.\n")
                sleep(1)    # Espera
                player.vida -= dano     # Aplica o dano

            # Inimigo morto
            else:
                score += 1  # Aumenta pontuação
                print("\nVocê aniquilou o inimigo!")
                sleep(1)    # Espera
                player.descanso()   # Restaura um pouco o player
                print("\nVocê consegue descansar um pouco.")
                sleep(2)    # Espera
                break
            
            # Se jogador está sem vida
            if player.vida <= 0:
                print(f"\nFim de jogo!\nPontuação: {score}")
                sys.quit()  # Fecha o interpretador
