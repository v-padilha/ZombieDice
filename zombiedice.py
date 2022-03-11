from random import shuffle

# criando jogador:
class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def rodada(self):
        print("-" * 40 + f"\nVez do jogador {self.name}: ")
        self.temp_score = {'Cérebros': 0, 'Tiros': 0}
        self.dados_na_mao = []
        self.dados = criar_dados()

        while True:
            print("\n" * 2)

            # Verificando dados na mão
            while len(self.dados_na_mao) < 3:
                self.dados_na_mao.append(self.dados.pop())

            #embaralha os lados dos dados, mostra para o usuário e verifica esses lados
            for i in range(2, -1, -1):
                shuffle(self.dados_na_mao[i].sides)
                self.face_para_cima = self.dados_na_mao[i].sides[-1]
                print(f"Dado {self.dados_na_mao[i].color}, Face: {self.face_para_cima}")

                if self.face_para_cima == 'tiro':
                    self.temp_score['Tiros'] += 1
                    self.dados.append(self.dados_na_mao.pop(i))
                elif self.face_para_cima == 'cerebro':
                     self.temp_score['Cérebros'] += 1
                     self.dados.append(self.dados_na_mao.pop(i))

            print(self.temp_score)

            #Verificação de tiros tomados e se o jogador deseja continuar a rodada
            if self.temp_score['Tiros'] < 3:
                continuar = input("Continuar jogando? (S/N): ")
                if continuar != 's':
                   self.score += self.temp_score['Cérebros']
                   print(f"Fim da rodada, {self.name}. Cérebros: {self.score}")
                   break
            else:
                print(f"Você levou 3 tiros na rodada, perdendo {self.temp_score['Cérebros']} cérebros")
                break

# criando os dados do jogo
class Dado(object):
    def __init__(self, color,sides):
        self.color = color
        self.sides = sides

def criar_dados():
    red = Dado('Vermelho',['tiro','tiro','tiro','cerebro','passo','passo'])
    green = Dado('Verde',['tiro','cerebro','cerebro','cerebro','passo','passo'])
    yellow = Dado('Amarelo',['passo','passo', 'tiro','tiro','cerebro', 'cerebro'])
    dados=[red,red,red,yellow,yellow,yellow,yellow,green,green,green,green,green,green]
    shuffle(dados)
    return dados

#criando jogadores a partir da classe definida
def criar_jogadores():
    players = []

    while True:
        try:
            total_players = int(input("-" * 40 + "\nZOMBIE DICE\nNúmero de Jogadores: "))
            if total_players > 1:
                break
            else:
                print("Você não pode jogar sozinho!")
        except ValueError:
            print("O número de jogadores precisa ser um número inteiro!")

    for i in range(0,total_players):
        name = input(f"Nome do Jogador {i+1}: ")
        this_player = Player(name, 0)
        players.append(this_player)
    shuffle(players)

    print("Ordem aleatória para jogar: ")
    for each_player in players:
        print(f"Jogador {each_player.name}. ")

        return players

if __name__ == '__main__':
    #cria jogadores com a função, armazenando na variável players
    players = criar_jogadores()
    game_over = False

    #Verificando se alguém fez 13 pontos, senão continua o jogo
    while game_over == False:
        for each_player in players:
            Player.rodada(each_player)
            if each_player.score >= 13:
                game_over = True
                jogador_vencedor = each_player.name

        print('-'*40 + "\nFim da rodada. Pontuação:")
        for each_player in players:
            print(f"Jogador {each_player.name}: {each_player.score} pontos")

    #Mostra resultado do jogo
    print("-" * 40 + f"\nFim de jogo. Pontuação final: ")
    print(f"Jogador vencedor: {jogador_vencedor}")
    for each_player in players:
        print(f"Jogador {each_player.name}: {each_player.score} pontos")