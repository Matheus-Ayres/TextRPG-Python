import random

def intro():
    print("====================================\n Bem-vindo a Duskrealm, um mundo repleto de mistério e perigo.\n Você é o herói desta história, e sua jornada está prestes a começar.\n Em seu caminho, você encontrará dungeons sombrias, cheias de tesouros e perigos.\n Mas a escolha é sua: você se aventurará nestes lugares sinistros em busca de riquezas, ou seguirá um caminho mais seguro?\n Prepare-se para forjar sua própria lenda, onde suas escolhas moldam o destino do reino.\n====================================")

    print("Vocẽ deseja embarcar nessa jornada?\n-Sim, quero me aventurar (Digite 1)\n-Não, ficar em casa (Digite 2)")
    escolha = int(input())

    if escolha == 2:
        print("Você escolheu ficar em casa, pode ficar com seu medo guardado e não saia da sua zona de conforto.")
    elif escolha == 1:
        aventura ()


def aventura ():
    #protagonista
    class Personagem:
        def __init__(self, vida, arma):
            self.vida = vida
            self.arma = arma  #arma ao protagonista

        def atualizar_arma(self, nova_arma):
            self.arma = nova_arma
            print(f"|Você trocou sua arma atual para {self.arma.nome}.")

     #monstros
    class Monstro:
        def __init__(self, nome, vida, ataque): 
            self.nome = nome
            self.vida = vida
            self.ataque = ataque

        def receber_dano(self, dano):
            self.vida -= dano
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    # as armas
    class Arma:
        def __init__(self, nome, pericia, dano):
            self.nome = nome
            self.pericia = pericia
            self.dano = dano
        
        def atacar(self):
            resultado = random.randint(1, 20)
            print(f"Rolagem para ataque com {self.nome}: {resultado}")
            
            if resultado > self.pericia:
                dano = self.calcular_dano()
                print(f"Acertou o ataque com {self.nome}! Causou {dano} de dano.")
                return dano
            else:
                print(f"Errou o ataque com {self.nome}.")
                return 0

        def calcular_dano(self):
            total_dano = 0
                
            print("Rolagens de dados de dano:")
            for qtd_dados, faces_dados in self.dano:
                dados_rolados = []
                for _ in range(qtd_dados):
                    resultado_dado = random.randint(1, faces_dados)
                    dados_rolados.append(resultado_dado)
                print(f"    {qtd_dados}d{faces_dados}: {dados_rolados}")
                total_dano += sum(dados_rolados)
                
            return total_dano

    def combate(protagonista, monstro):
        while protagonista.vida > 0 and monstro.vida > 0:
            
            # Turno do jogador
            print("\nTurno do jogador:")
            dano_jogador = protagonista.arma.atacar()
            if dano_jogador > 0:
                monstro.receber_dano(dano_jogador)

            if monstro.vida <= 0:
                print(f"Parabéns! Você derrotou {monstro.nome}.")
                break

            # Turno do monstro
            print("\nTurno do monstro:")
            dano_monstro = random.randint(1, monstro.ataque)
            print(f"{monstro.nome} ataca e causa {dano_monstro} de dano.")
            protagonista.vida -= dano_monstro
            print(f"Sua vida restante: {protagonista.vida}")

            if protagonista.vida <= 0:
                print("Você foi derrotado...")
                break

    espada_de_metal =Arma("Espada De Metal", 8, [(1, 10), (2, 4)])
    graveto = Arma("Graveto", 5, [(1, 6), (1, 4)]) 
    protagonista = Personagem(200, 0)  
    aranha = Monstro("Aranha", 15, 3)  
    ciclop = Monstro("Ciclope", 46, 20)

    Nome = input("Escolha o nome do seu aventureiro: ")


    print(f''' VOCÊ COMEÇARÁ SUA, JORNADA!!! SEU PRIMEIRO OBJETIVO SERÁ IR ATÉ A UMA PEQUENA VILA: A Vila Verdejante. BOA SORTE {Nome}!!!
          

                                     ███████████                    
                                    █████████████                   
                                   ██████████████                   
                                   ███████████  █                   
                                   ██████  ██  █  █                 
                        ██████      ████                            
                   ██     █    ████  ██         █                   
                 █    ██████   █       █  █    █                    
                █   █        █          ███                         
                  █        ██              ███                      
                         ██         █          ██      ██           
                         █            ███       ██       █          
                       █                ███     █████████           
                     ██                ██  █████                    
                     ██                █                            
                       █              ██                            
                       █  ███        ██ ██                          
                      ██    █████   ███  █                          
                      █        ██████     █                         
                 █████        ███          ██                       
          ████   ██ ██      ██    █          █                      
          ████   ██ ██     █       ██        █                      
          ████     ███████          █    ███ ██                     
          ██                         █████ ██                       
                                       ██  ██                       
                                         █                          
                                          ███████                   
                                          ██████     ''')
    

    print('''==================================================================================
Enquanto explorava os recantos sombreados da densa floresta a caminho da Vila Verdejante,\nvocê se deparou com um baú solitário meio coberto por folhas caídas e musgo.
==================================================================================
Você deseja abrir o baú misterioso?
Sim (Digite 1)
Não (Digite 2)''')
    escolha = int(input())
    if escolha == 2:
            print('''Tem certeza?
Sim (Digite 1)
Não (Digite 2)''')
            escolha = int(input())
            if escolha == 1:
                print("Você seguirá sua jornada sem saber o que o aguardava no baú, pode ter evitado uma inconveniência ou perdido algo valioso.")
            elif escolha == 2:
                print("=================\nVocê abre o baú e acha um graveto!\n=================")
                print('''Deseja visualizar as informações do graveto?
        Sim (Digite 1)
        Não (Digite 2)''')
            protagonista.atualizar_arma(graveto)
            info_graveto = int(input())
            if info_graveto == 1:
                    print('''O Graveto tem uma pericia de 5 (Você vai ter que tirar mais de 5 no dado para conseguir realizar o ataque);
        O dano do Graveto é de: 1d4 + 1d6.''')
    elif escolha == 1:
            print("=================\nVocê abre o baú e acha um graveto!\n=================")
            print('''Deseja visualizar as informações do graveto?
        Sim (Digite 1)
        Não (Digite 2)''')
            protagonista.atualizar_arma(graveto)
            info_graveto = int(input())
            if info_graveto == 1:
                    print('''O Graveto tem uma pericia de 5 (Você vai ter que tirar mais de 5 no dado para conseguir realizar o ataque);
        O dano do Graveto é de: 1d4 + 1d6.''')
            

        
    print('''================================================\nPor entre as árvores ancestrais,\nvocê avistou uma criatura de oito patas tecendo sua teia.\nUma aranha, seus olhos brilhando com uma fome insaciável.\nEla decide que você será a comida dela.\n===============================================\n                                                              
                              █████                             
                            █████████     ██                    
                           ███      ███  █ ██                   
                   █████ ████         ███  █████                
                  █ ███████            ████   ███               
                █ ████ ██  ██         █████ █  ███              
              █████      ██ ███     █      ████ ██              
          ███████     ██   ██████████      █ ██  ███            
          ████       █  ███   █████ ██     █  ██                
                    █ ██  █ ███   ██  ████████ ██ ██            
                   ████  █  █       █  █ ██  █  ██ █            
                   █ ██  █ █        ██ █  ██     ██ █           
                 ██ ██  █ █         ██ █          ████          
                █████   █ █         ██ █                        
                       █ ██         ██ █                        
                      ████          █  █                        
                                    ██ ██                       
                                      ██        ''')
    
    print('''O que você deseja fazer?
    Usar seu graveto para se defender desta criatura. (Digite ATK)
    Fugir. Um graveto não será suficiente para enfrentar esta aranha. (Digite RUN)''')
    while True:
        decisao = input().upper()
        if decisao == "ATK":
            combate(protagonista, aranha)
            break
        elif decisao == "RUN":
            print("Ja é tarde demais e você se ve preso nas teias, sua única opção é lutar.")
            combate(protagonista, aranha)
            break
        else:
            print ("Opção inválida")
    print('''====================================================================================\nCom a aranha derrotada e as teias agora desfeitas pelo balançar do graveto,\n a vila emerge majestosamente no horizonte, como uma promessa de refúgio após a aflição da floresta sombria.\n====================================================================================
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▒▒▒▒▓▓▓▓▒▒▒▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▒▒▒▒▒▒▒▓▓
▓▓▓▓▓▓▒░░░░░░░░░░░░▒░▒▒▒▒▒▒▒░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▓▓▒▒▒▒▒▓▓▓▓▓▒▒▒▓▓▓▓
▓▓▓▓▓▓▒▒▒▒▒░░▒▒▒▒▒▒░▒░▒▒▒░▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓▒▒
▓▓▓▓▓▓▒▒░░░▒▒░▒▒▒░▒▒▒▒░▒░▒░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▒▓▒▒▓▒▒░░▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒
▓▓▓▓▒▒▒▒▒░▒▒▒▒▒▒░▒▒░▒▒▒▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▓▓▓▒▒▒▒▒▒▒░░▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▒▒▒▒░▒▒▒░▒▒▒▒░▒▒▒░▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▓▓▒▒▒▒▒░▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒
▓▓▒▒▒░░▒▒░▒▒▒▒▒░░▒▒▒░▒▒░░░▒░░▒░░░░░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▒▒░▒▒▒▒▒░░▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒
▓▒▒▒▒▒▒▒░▒░▒░▒▒▒▒▒▒▒▒▒░░░▒▒░░▒▒░░░░▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒░░▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓▓▒▒▒▒
▒░▒▒▒░▒▒▒░░▒▒▒░░▒░▒░▒░░░▒▒▒░░▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▓▒▒▓▓▒▒▒░▒▒▒░░▓▒░
▒▒▒▒░▒░▒░▒░▒░▒▒▒░▒▒▒░░░▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒░░░░▒░▒▒░░▒▒▒▒▒▒▓▒▒▒▒▒░░▓▓▒░░░░░░░
▒░░░▒░▒░▒░▒▒▒░▒░▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒░▒▒▒▒░░░░░░▒▒░░░░░░░░░░▓▓▒░▒▒▒░░░░░░░░▒
░▒░▒░░▒▒░▒▒░▒▒░░▒▒░░░▒▒▒░░▒▒▒▒░░▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒░░░░░░░░░░░░▓▓░░░░░░░░░░▒▒▒░░░░▒▓▒▒▒▒░▒▒
▒░▒▒░▒░▒▒▒░▒░▒░▒▒░░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░░▒▒▒▒▓▒░▒▒▒▒▒▒▒▒▒▒░░▒░░░░░░░░░░░░░▓▓░░░░░▒▒▓▒▓▓▒▓▒▒▒░░▒▒░░░░░░
░▒▒▒▒▒░▒▒▒▒░░░▒░▒░░░░▒▒▒░░▒▒▒▒░░▒▒▒░░░░░▒▒▒▓▒░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░▒░░░▒▒▓▒▒▓▓▒▒▒▒▒░░░░░░░░░░░
░▒▒▒▒▒▒▒░▒░▒▒▒░▒░░░▒░░▒▒░░░░░░░░▒▒░▒▒░░░▒▒▒▓▒░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░▒▒░▒░░░░░░░▒▒▒▓▒▒▒░▒▓▒▒▒░░░░░░░░░░░
▒▒▒▒░▒░░▒░░░▒▒▒░░░░▒▒▒░▒░▒▒░░▒▒░▒░▒▒▒░░░░▒▒▒░░▒▒▒▒▒▒▒▒▒░░░░░░░░░▒░▒▓▓▒░░░░░░▒▒▒▒▒▓▒▒░▒▒░░░░░░░▓▒░░░░
▒▒░▒░▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒░░░░▒▓▓▒▒▒░▒▒▒▒▒▒░░░░▒▒▒░▒▒░▒▓▓▒▒▒░░░░▒▓▒▒▒▒▒▒▒░░░░░░░░▒▒▒░░░░░
░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒░░▒▒░░░░▒▒▒▒▒▒▒░▓▒▒▒▓▓▒▒░░▒▒▓▒▒▒▒░░░░░░░░░░▒░░░░░░▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▓▒░▒░░░░░░▒▒▒▒▒▒▒▒▒░▓▓▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒░░░░░░▒░░░░░░░░░░░░░
░░░░░▒░░▒▒░▒▒▒░░░▒▒▒░░▒░░░░░░░░░▒▒░▒▒░▒░░░░▒▒░░░░░░░▒░░░░░░▒░▒▒▒▒▒▓▒▒░▒▒▒▒░░░▒▒▒░░░░░▒▒▒░░░░░░░░░░░░
░░░░░▒▒▒░▒░▒▒▒░░░▒▒▒▒▒░░░░░░░░░░░▒▒░▒░░░░░░░░░░░░░░░▒▒░░▒░▒░▓▓▒▒▓▓▓▓▓▓▒▒▓▒░░░▒▒▒░░░▒▒▒▒▒▒▒▒░░░░░░░░░
░░░░░▒▒▒▒░▒▒▒▒░▒░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒░▒▒▒▒░▒▒░▒▒░░░▒▓▓▓▓▓▒▓▓▓▒▒▒▓▒▓░░░░▒▒▒▒▒▒▒░░░░░░░░░
░░░░░▒▒▒▒▒▒▒▒▒▓▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒░▒░░▒▒▒░▒▓▓▒▒▒▒▒▒▒▒▒░░░▒░░▒▒▒▒▒▒▒░░░░░
░░░░░▒▓▓▓▓▒▓▓▓▓▒░▒▒▒▒▒░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▒▒▒▓▓▒▓▓▓▒▓▒▒░░░▒░░▒▒░▒▒▒▒▒▒▒▒░░░░░
░░░░░▒▒▓▓▓▒▓▓▓▓▒░▒▒░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░▓▒░▒▒▒▓▓▓▓▓▒▓▓▓▓▒▓▓▒▒▓▓▓▒▒░░▒▒▒▒▒▒▒▒░▒▒▒▒░░░░░
░░░░░▒▒▒▓▒▒▓▓▓▒▒░▒▒▒░▒░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▒▒▒▒▒░▒░▒▒▒▒▒▒░░▒░░░░░░░░
░░░░░▒▒▒▒▓▒▓▓▓▓▒░▒▒▒▒▒░░░░░░░░░▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒░▒▒▒▒▒▒▒▒░▒▒▒░░░░░░░
░░░░░░░░░▒▓▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▒▒▒▓▒▒▒▒▒▒▒▒▓░▒░▒▒▒▒▒▒░▒▒▒░░░░░░░
░░░░░░░░░▒▓▒▓▓▒▒░░░▒░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒░▒▒▒░░░░░░░
░▒░░░░▒▒░░▒▒▓▒▒▒░░░░▒░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░
▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒░░▒▓▒▒▒▒▓░░░░░░░░░░░░▒▒▒░░░▒░
▒▒▒▒▒▒▒░▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒░▒▒▒▒▓▒▒▒▒▒▓▒▒▒▒▒░▒▓▒░░░▒░▒▒▓▒▓░░░░░░░▒▒▒▒▒░░░░░░░░


''')
    

    print("================================================================================================\nVocê se depara com um jovem camponês,\n cujos olhos refletem a inocência da juventude e a coragem daqueles que enfrentam os perigos diários da vida na vila.\n Com uma voz trêmula, você se dirige ao jovem, implorando por sua ajuda desesperada.\n Campônes:\n Por favor, senhor(a), preciso da sua ajuda! Meu pai foi capturado por um monstro terrível, e estou desesperado para salvá-lo.\n Você parece ser uma pessoa corajosa, e tenho esperança de que você possa enfrentar esse desafio e trazer meu pai de volta são e salvo. Por favor, aceite me ajudar nessa jornada.\n================================================================================================")
    print(f'''Você, com pena, decide o ajudar:
        {Nome}
    Estou disposto a lhe ajudar, mas não possuo armamento o suficiente.

        Campones
    ah sim, claro que posso te ajudar com isso, mas antes como é o seu nome?

    Dizer o nome. (Digite 1)
    Não dizer o nome (Digite 2)
    ''')
    dizer_nome = int(input())
    while True:
        if dizer_nome == 1:
            print(f'''Campones:
    Certo! Sinto que posso confiar em você, {Nome} aceite esta espada de metal''')
            break
        elif dizer_nome == 2:
            print('''Campones:
    Não sei se posso confiar em você...''')
            print(f'''{Nome}:
    Tudo bem, se for por isso, meu nome é {Nome}.''')
            print(f'''Campones:
    Certo! Agora sinto que posso confiar em você, {Nome} aceite esta espada de metal''')
            break
        else:
            print("Digite um valor valido")
    protagonista.atualizar_arma(espada_de_metal)
    print('''Deseja visualizar as informações da espada?
        Sim (Digite 1)
        Não (Digite 2)''')
    info_espada = int(input())
    if info_espada == 1:
                    print('''A espada de metal tem uma pericia de 8 ;
O dano da espada de metal é de: 1d10 + 2d4.''')
    print(f'''Campones:
Meu pai esta na Caverna Do Olhar Único que fica ao oeste daqui, boa sorte, {Nome}''')
    
    print('''======================================================================================================================================================================================================================\nVocê prepara para sua jornada rumo à Caverna do Olhar Único. O vento sussurra segredos antigos enquanto ele avança pela trilha sinuosa que leva até a entrada escura da caverna.\nA cada passo, o ar parece mais denso, carregado com a aura de mistério e perigo que envolve aquele lugar.

Com o coração batendo forte no peito, ele se aventura pela escuridão, guiado apenas pela luz tênue de uma tocha.\nO eco de seus passos ressoa pelas paredes de pedra, como se a própria caverna estivesse sussurrando segredos ancestrais.\n Cada sombra parece esconder um perigo iminente, enquanto o herói se aproxima cada vez mais do coração das trevas.

Finalmente, ele avista uma luz fraca à distância, o brilho solitário que emana do olho único de um ciclope, guardião da caverna.\nSeu coração acelera ao enfrentar a imponente figura da criatura lendária,\n cujo olhar penetrante parece sondar a alma de quem ousa desafiá-la.\n======================================================================================================================================================================================================================\n
                                                                                           
 ░░▒░▒░ ░░░░░░▒░░░ ▒▒▒░ ░▒░░ ░ ░░░▒░░▒░░▒░░▒▒▒░▒░░░░░░░░░▒░░░░░░░░░░░░▒░░░░░░░░░░░▒░░░░░░  
 ░░ ░  ░░░░░░░   ▓▒▓▓██▓▒▒▒▒░░  ░░▒▒▒▒░░▒▒▒▒░░░▒░▒▒░▒▒▒▒░░░░░░░░░░░▒ ░▒▒▒▒▒░░░░░░░░░░░ ░░░ 
 ░░░░▒░░░░░ ▓ ▓▓▒▒▒▒░▓█▒▒░░▒▒▓██▓ ▒▒░░░░░░░ ▓▓▓▓▒▒▓░░░▒▒░░░░░▒░░▒▒▒▒ ░░  ░░░░ ░░ ░░ ░░░▒░░ 
 ░░░░░░░░░▒▒▒░▒░░▒░░░▒▓░░▒▒▒▒▓▒▒▒░░░░░░   ░ █▓▓▓▒▒▒▒▓░   ░░░░▒▓░▒░░▒░▒▒▒ ░░▒▒▒▒░░▒░ ░░░░░░ 
 ░░░░▒░░░▓▒░▒░░░░░░░░▓▓▓▒▒░▒░░░░░  ░  ▒░▒▒ ▒███▓▓▓▓▒▒▓█▒█▒ ▒░  ░▒░░▒░░▒▒░▒░░░░▒░░▒░░▒░░░░  
 ░░░░ ▒▒▒▒▒░░░░░░▒▒▒ ██▒░░░░▒▒▒ ▓███▓▓████ ██ ▓██▓▓▓▓▒  ░██░▒██░░░░░░░░░░░░░░░░▒░░░ ▒░░░░░ 
 ░░ ░▒▒▒░░▒░░▒░░█▒░ ▓▓▒░▒░▒░  ▒░░▒▒▒▓ ▒▒▓▒░▒▓ ▒█▓▓▓▒▓██░░▒██  ▒▒░▒▒░▒▓▒░▒▒▒▒░▒░░░░░ ▒░▒░░░ 
  ░▒░▒░░░░░░░ ▒░ ░░░▒▒░░░   ░▓▒░▒░  ░ ▒▒█▒▒▓▒▒▒▒▒▒▓▒▒▒███▓▒█  ▒░░░░▒░▒▒░░░ ▒▒▒▒░░░▒ ▒░░░░░ 
 ▒▓▓░░░█▓▒ ░▒▒▓▓░▒░░░▒▒░  ░█▒░     █▓█░    ▒▓▒▒▒▒▒░▒▒░░▒▒▒▓▓▒▒▒░░░░░▒▒▒░░▓░▒░░░░░░▒░░░░░░░ 
 ░░░ ▓▒░ ░▒▒▒▒░░▒░░▒▒▓▒▓██▓█░░░▓▒ ████▒▒█▓ ▓█░░░░▒▒▓▒▒▒▒▒▒▒▓░▓▓░░░░░░░▒▒▒▓░░░░▒░░░░░░░░░░▒ 
 ░░░▒   ░▓░░░░░░░ ░░░░▒███▓░▒████ ██▓█▓▓██▓██▓████▒▒    ▒▒▒▓▓▒▒░░▒░▒░░▒░░▓▓▒▒▒▒▒░░▒░▒░░░░░ 
 ░▒▒░░░▒░░░░▒░░  ░░ ▓▓▓█▒██░▒████▒█▓▓▓▓▓▓▓▒▒██▓▓▓▓▓█▓▓██▓░▒▒▓░▒▒ ░░█░▒░░░▒░▒▒▒░▒░▒▒░░░░░░░ 
 ▓▒ ░░░▒▒░░▒▒   ░██▓█▓█▓▒▒█▒▒▓▒▒▒▓█▓▓▓▓▓█▓▓█▓▓▓▓▓▓▓▓▓▒▒▒▓▓█▓▒█▓▓██░░▒▒░▒░▒░░▒▒▒▒░░░░░░░░░░ 
 ▓░ ░░░ ▒ ░▒░ ▓░▓▒░░▒▒▓█▓▓▓▒▒███▓█▓▓▓▓▓▓█▓▒█▓▒█▓▓▓▓▓▒▒▒▒▒░▓██▒▓░▓▓▓▒▓▒░▓▓▒░░▒▒░▒░░░░░░░░░░ 
 ▒░░░▓▓▒░ ▓▓▒▒▓▒▒▒▒▒▒▒▓▓▒▓▓░▓█▓██▓▓▓▓█████████████▓▓██▓▓▒▒▒▒█▓▓▒▒▒▓░▒░░░▓█ ░▒▒▒▒░░░░░░░░░░ 
 ░░░▓░ ░ ▓██▓ ░░▒▓▓▒▓░▒█▒▓█▓▓█▓▓█████████  █████████████████▓▒▒▓▒▒▒ ▓░░░▒▓▓ ░▒░░░░░░▒░░░░░ 
 ▒▓▒ ░▒▓█▓░▓▒ ▓▒▓▒▒░▓██▓▓▓▓▓▓████▒▓▒▓  ░        ▒░  █   █▒  ██▒▓▓▓▓▓█▓░░▒▒█ ░░▒▒░▒▒░░▒░░░░ 
 ▒░ ▒▓▒░░▒▒▒▒ ▒▒█▒▒▓▒▓▒▒▓▓▓████▓ ▒▒ ░█    ▒██▓▒  ▒      ▒░ ░ ███▓▓▒▓░▒░░░░▓█░▓▒▒▒▒░░▒▒░▒▒░ 
 ░░░▓█▒▒▓▓▒▒▒ ░▒░▓▓███████████░▒▒ ░ ███▓█▒░░ ▒▓▓░ ▓▓▓  ▒   ▓░▓ █▓▓▒▓▓▓▓█░▓██░░▒▒▒░ ░░▒░░▒░ 
 ░░▒▒  ▒▓░░▒▒░▒██▓ ░░░░▒▒███░ ▓▒▓ ██▓  ▓█████▓████░░▒▓█████░▒░▒▒▓▓▒█▓▒░░░▒░██▒▓▒░░█▓▒▒░▓░░ 
 ▒▓▓▓ ▒▒░▒▒▓▓ ▒▒ ░▓███████▓    ▒▒░▒ ░ ▒▒▒       ░░▒██░   ░█▓░░███▓▒▒▒▓▒▓▒▒▒ ░▒▒▒░█▓█   ▒▒░ 
 ▒▒▓▒▓▓ ▒▒▓▒▒ ▓▒▓███▓█▓░       ░█ ░░░░▓▒  ██████ ░░▒░█▓▒▓▒▒▓ ▒█ █▒██▓▓▓▒▒▒▒▓▓▒▒▒░▓█▒█░█▓▒▒ 
 ▒▒▒▒▒▒░▒▓▓░▒▓▓▒▓█▓▓█▓   ░▒▓▒░  ▓▒▒▓▒█▓▓ ▓█    █▒▒ ▓▓▓███░██ ░▓▓░  ░███▓▓▓▓▓▒█▓▒▒▓░▓▒▓▒ ▓░ 
 ░▒░▒▒▒▒▒▒▒▒▒░▒▓██░░   ░░▓░░░░░░░▒░▒▒▒ ░  ▒█████░ ▒▓█ █ ░▒ ▒▒▒█▓▒█░   ▒██▓▓▓▓░▓▒▓▒░▒▓▓▒░▓▒ 
 ▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓  ▓  ▒░░▒▓▒▒░░░░ ░░▒▒▓▓░░        ▒  ▒ ░▓▒ ░ ▓ ▒█▓▓██▓▒▒ ▓█▓▒▒▓▓▓▒▒▒▒░▓▓░▒▒ 
 ▒░░░▒▒▒▒▒▒▓▓▓███▒▒░░▒▒▓▓▒▒░░░░░  ░▒▓▓ ██▒██▓░▓█▒█▒ █░ █░▒▒░██▒▓██▓███▓▒░▓▓█▒▓▒▓▓░░▓▒░░░░░ 
 ▒░▒▓▒▒░▓▒▓▓█░▓▓░▒▓▒▒▓▓▒░░ ░  ░  ▒▒░▓▒█   ░███▓░ ▒  █░▒▒ ▓▓░    ░▒▒▓▓██░ ▓█▒▓▓▒▓█▓▒▓▓▒▓▒░▒ 
 ▒▒▒░▒▒▒▒▓▒▓▒▓▒░░░░        ▒▒▒░░ ▒▒░░░▓ ▒       ░█▓▒▓  ▓░▒▓████  ▒▒▓▒▓█▒ ▒█▓▒▓░░▒▒▒░▒▓▒▒ ▓ 
 ░░▒░▒▒▒▓▒▒▓█▒░   ▒▓▓▒▒▒▒▓▓▒   ░▒▒░▒▒ ░░░▒░░▒░░▒ ▒█▓  ▒███▓▓▓▓██░░▒▒░░▓▓░▒ █▓▓▓▒▒▓▒▒▒▒▒▒▒▓ 
 ░▒▒▒▒▒▓▓█▓ ░░ ░██▓▓▒▒▒░░   ░▒▒▒▒▒▒░░▒▒▒░░▒░▒░░░░▒  ░▓▓▒▓█▒▓███▓░▒▒▒▓▓▒▒█▓ ░█▓▓▓▒▒▒▓▒▒▒▓▓░ 
  ▒▒▒▓▓▒▒░ ░░ ░░▒▒░░▒░░░░  ░░ ▓▒░▒▒▒░░░░░░░      ░  ▒▒▒░▓▓██░        ▓▓▒▓█▓ ██▓▒▒▓▒▒▒▒▒▒░░ 
 ▓▓▓▓█░░░░░░░    ░░        ░  ░▒▒░░▒▒░▒░░░░▒▓▒ ░ ░▒████▓▓▓░      ░░   ▓▓▓██▒▒██▓▒▒▒▒░▒▒▒▒▒ 
 ▒▒▓▒█░▒▒░░░▒░       █████   ░ ░▒░▒▒░▒░░░░▒▓█░░▓▒░░░ ░▒▓   ▒▓ ▒    ░ ░▒▒▒▒░ ░ ▒█▓▒▒▒▒▒░▒▒▒ 
 ░▒▒▓█ ░░░░▒▓▓▓░ ░░░░█▓▒▒██ ░▒▒░░▒▒▒░░░░▒░▒▒█ ░▒▒▓▓▒▒▓▒▒▓▓██ ████▒  ░▒▒░   ▒█▒ ░█▓▓▒▒▒▒▒░▒ 
 ▒▓▒▒█ ▒▒▒▒▒▓███    ▒▓▒▓▓▓█ ░▒▒▒░▒░▒▒░░░░░░░▒▓░░░▒░▓▓▒▓▓▓▓▒▒ █▓▓█░ ░░░▒▒▒░▒▓█▒▒ █▒▒▒▒▒▒░░░ 
 ▓▓▒▒█ ░▒░  ░ ▒██▒  █▓▓▓▓▓█  ░░▒▒░▒▒░░░░░░░░▒▓▒▒▒▓▓▒▒▒█░░█▓▒▒█▓▓██    ░▒░░▓▓░▒▒ ██▓▒▒▒▒▒▒░ 
 ░▒▓██▓░▒▒░▒▓▒▒██░ ██▓▓▒▒▒▓█ ░░░░▒░▒▒▒░░░▒▒░░░ ░░ ░▒▓█▒ ▒▒▒░██▓▓▓█    ░░░▓▓▒░▓   █▒▒▒▒░░▒░ 
 ▒▒▒░█░ ▓▒░░▒▒▒░▓░██▓▒▒▒▒▒██ ▒░░░░▒░░░░░░░░░░▒ ▓█░░░░░░▓█▓ ░█▓▓▓▓▓█  ░░░▒▓▒░░░ ░ █▒▒▒▒▒▒▒▒ 
 ░▒░ ██ ░ ░▒░▒▒▓░ █▓▒▓▓████  ▒▒░░░░▒░░  ░░░░▒▓  ▓█▒ ░▒▓░   ██▓▓▒▒▓██░  ▒▒▒▓░▒░░▓  ▒▒▒▒▒░▒░ 
 ▒░▒▒▓ ░▒ ▒░░░▒▒██████▒▒░░░ ░ ░▒▒░░   ░▒░░▒░▒▒  ░▓▓▓ ░▒▒ ░ ▓█▓▓▒▓▓▒█▓  ░▒░▒▒▒ ░▒▒ ▒▓▒▒▒▒▒░ 
 ▒▒▓█▒░░  ▓░░ ▒▒░▓▒█░█▓▓░░▒░     ░░ ░░▒▒░░░ ░ ░░░░▒▓  ▓▒░ ░▒█▒▓▓▓▓▒▓▓▓  ░ ░░  ░▒▓ ▒▒▒▒▒░░░ 
 ░░▓░░  ▒▒  ▒▒        ▒░░░▒░▒▒░  ░░░░░░░░░▒░░▒░░▒░▒▓▒▒▒▒░░▒▒░▓▒░▒▓▒▓█▓▒  ░░ ░▓▓▒▒ ▓▒▒▒▒▒░░ 
 ▒░█    ░▒░▓░ ▓███░   ▒░▒▓░░▒▒▒▒░░░░░░░░ ░  ░░▒▒░ ░  ░░▒▒▒▒░░░▒▒░░░░▒██  ░▒▓▒▒▒░▒ ▓▒░░▒▒▒▒ 
 ░▒█    ░▒▓█░█▓▒▓██░█▓▓░▓▒ ▒░▒▒▒▒░ ░░░░▒░▒▒▒▒▒░ ▒░░░░░░░░░░░▒▒▓▓░░▒▒▓▒ ░▓▓░░▓▒ ░░░█▒░░░▒░░ 
 ▓██▒ ░█▒  ▒▒▓▒█░░░ ▓▒▒░▓ ░▒▒▒▒▒▒▒░░░▒░░░░░░░░░░░░░░ ░░░░▒▓▒▒▒▒█▓▓▒░░░▒▓▒▓▓▒   ▒ ░░░▒▒░░░░ 
   ░▒▓▓▓▓░  ░█  ░▒▒▒   ▒▒░░▒░░▒▒░░░  ▒░░░░░░░░░░░░░▒░░░░░▓░▒▒▒░░█▓▓▒█▓░░ ░ ░▒▒░░ ▒▒░░░░░░░ 
 ░    ░▒▒▒▓▓▓░    ░ ░░░█▒░▒░▒▒▒░▒░░░░▒░░░░░░░ ░░ ░░░░░░░▒░░░░░░ ▓▓█        ▒▒▒▒  ▒░▒▒█▓▒░░ 
 ▓███▒░░░░░ ░░▒█▒░▓▒░░░█  ░░ ░▒░░░   ▒░░░░░░▒░░░░▒▒░░░░░░░░░░░░ ▓░▒█▒▓██▓  ▒▒░  ▒▒░    ▒▓▓ 
  ▓░░ ░░ ░▓▒░  ░▒▓▒▒▓▒▒▒░░▒▒░░░░░ ░█ ▒░░░░░  ░░░░▒▒  ░░░▒░░░░░░  ▓▓▒█     ░░░  ▒█▒░▒▓██▒▓█ 
   ░ ░░░░░░ ░░░░░░░▒▒▓░░░▒░▒▒░░░  █▓ ░░▒░░░░░▒▒░░░ ▒░  ░▒▒░▒▒▓▒░░░▒▒▒ ░░░▒░   ▒▒           
 ▒░░░░░░░░░░░▒▒░░░   ░░░░░░░░▒░  ▓▓▓  ░    ░░░░░ ░░██▒  ▒▒▒▒▒░░░░ ▓▓▓▒░░    ▓▒░ ░  ░ ░░░░░ 
 ░▒▒░░░▒░░▒▒▒▒▒▒░▒▒▒▒░░░░░░░    ▒▓▒█░ ░ █░▒░░░░░ ▒▒░░▒▓  ░░░░░░░░ ▒▒░▒▒▒▓▓▓▓▓▓▒▒▓▓▒▓▓▒▒░░░ 
 ░▒▒▒▒▒▒▒▒░░░░░░░░▒▒ ░░░░░░   ▓█▓▒░▒░ ░ █ ░░░░  ░▒▒▒▒░░▓   ░░░░░░ ▓▓▒▓▓▒▒░ ░░ ░   ░░░░░░░░ 
 ▒▓▓▓▒▒▒░▒▒▒▒░░▓█▒▓▓▓░  ░░  ▓▓▒▒░░░▒▒     ░ ░  ░█▒▒▒▒▒▒▒█░ ░ ░░░░ ▓▒   ░▒▒▒░░▒░▒▒░░░░░░▒░░ 
 ░         ░░░▒░ ░░ ▒ ░░   ▒▒░░░░░░▒▒▓▓▒░░░░ ░▒▒░░░░░░▒▒▒▓ ░░░░░░  ▓▒▓▓▓▒░      ░░░░░░░░░░ 
 ░░░░▒▒▒▒▒▒▒▒░░▒░░░▒▒░░▒░▒ ▓▒░▒▒▒▒░▒░░░▒▒▒▒░ ░░  ░░░░░ ░ ▒  ░░░░░  ▓░░░    ▒██▒▒▒▒░░░░░░▒░ 
 ▒▒░░▒░ ░░▒░ ▒▒▒▒▒▒▒░▒▓▒░░░░░░░░░░░░░░░░   ▒ ▓▒▓▒▒▒▒▒░▒▒░░░ ░░░░░░ ▒   ░██▓█     ░░░░░░▒░░ 
 ░░░░▒▒░░  ░░░    ░░░░░░░░░▒░░         ░▒▒▒▓▒███▒░      ░█▒░░░▒░░▒ █▓░░      ░░░░░░░░░░▒░░ 
 ░░░░░░░░░░ ░ ░░░▒░░░░   ░░░░░░░▒▓▒▓▓▓▓▒▒█▓▒▒   ░█████████ ▒▒▒▒▒▒▒░ ██▓█▓▓▓▓████▓▓▒▒▒▒▒▒▒▒ 
 ░▒░▒░░░▒░▒░░▒▒░░  ░░ ░░░▒░░░░▓▓▓▒▒▒░▒▓░    ░▒▒░           ░ ░▒▒░░░ ▓███████▓█▓▓▓▓▓▒▒▒▒▒░▒ 
 ▒▒▒▒▒▓▒▒░▒░         ▒          ░░░░▒▒  ░░▓▒    ░                 ░        ░░░░░░░░▒▒░░░░░ 
   ░░░░▒█░▒▒███████▓█▓▓▓▓▓▓▓▒▓▒▒▓▓▒▒▒░▒▒▒▓▒ ▒███▓▓▓    ░▓███▓▒▒▒▒░        ░  ░          ░░ 
 ▒▒░░░ ░ ░░░    ▒▓▒▒░     ░▒▒▒▒░ ▒░░▒▒▓▒▓░▒▓▓░░░░▒▒▓▓█▓▓▓▒▒▒▓▒▒░░▒▒▒░░░░░░░     ░░░░░░░  ░ 
  ▒▒▒▒░▒░░░░░▒▒     ░░ ▒▓▒▒▓▒░▒▒░▒█▒▒▒▒░▒▒▓▒░░░▒▒▒█████▒▒▒▒▓▓▓▒▓█████▓▒▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒ 
 ░  ░░░▒░░▒░       ░░▒▒▒▒▒▓▒░▒▒▒░░░░░░▒▒░░  ░▓████▓▓▒▓▒▒░░░  ░░░░▒░░ ░░░░░▒░░░░▒▒▒░░░░░░░░ 
 ▒░░ ░░░▒░▒▒▓█▓▓▓███▓██▒░░░░░▒░▒▒░░░▒░░░░░░███████▓▒▒░▒▒▒▒▒░░░░░░░░▓▓▒▒▒▓▒░ ░  ░▒░░▒▒░░░░░ 
 ░░░▒░▒░▒▒▒▒░▒░░ ░ ░  ░  ░ ░░░▒▒░▒░▒░▒▒░▒██▓▓▓██▓▒▒▒▒▒▒▒░░░▒▒▒▒░░░░░▓▒ ░  ▓░▓█▒▒ ▒░▒ ░▒░░░ 
 ░▒▒░░░▒░░ ▒ ░  ░░░░░░░░░▒▒░▒▒▒░▒░░░▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░▒░░░▒░▒░░░░  ░░▒▓  ░▒▒▓  ░▒░▒░ ░░ 
 ░░░░  ░  ░▒▒▒▓▓▓▓▒▓▓▓▒▓ ░░░░░░░░░▒░░░░▒▒░░▒░▒░░░▒░░░░░░░▒▒░▒░░░░░░░░ ░▒░░░░░░ ░░░░░░░░░░░ 
 ░░░░░░░▒▒▒ ░░ ░      ░░░░░░░░░░░ ░░░░░░░░░░░░░░░░▒░░░░▒▒▒░░▒░▒▒▒▒▒▓▓▓▓░░░░░░▒░░  ░  ░░    
 ░░░░░░ ░  ░▒░░░░░░▒░░░▒░░░▒░░▒░░▒░░░░░▒▒░░▒░░░░ ░░░░░░░ ░▒▒▒▒▒░░░░░░░░░▒░░░░▒░░ ▒▒░░  ░▓░ 
 ░░░░░░░░░░░░░░░░▒░▒░░  ░▒░░░░ ░░░░▒▒▒░░▒░░░░░░▒▒▒░▒░░▒░░░ ░░░░░░░░░▒▒▒░ ░░░░░▒▒▒▒▒░▒░▒░   
                                                                                        
''')
    print("Ao fundo você observa o pai do campones, então sem exitar, você ataca o ciclope.")
    combate(protagonista, ciclop)
    print('''=======================================================\nApos derrotar o ciclope, você ajuda o pai do campones e...\n=======================================================
 ░▒▓██████▓▒░  ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓████████▓▒░░▒▓█▓▒░░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░  ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                         
    Sua Demo acabou                                                                                                    
          ''')

intro()





