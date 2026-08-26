dicionario_gamer = {
    "buffar": "Aumentar o poder, força ou atributos de um personagem ou item.",
    "nerfar": "Enfraquecer ou diminuir os atributos de um personagem ou item.",
    "noob": "Jogador novato ou que joga mal.",
    "grindar": "Jogar repetidas vezes para conseguir itens, dinheiro ou experiência.",
    "respawn": "O reaparecimento de um personagem ou item após morrer ou ser coletado.",
    "lag": "Atraso na resposta do jogo devido à conexão lenta.",
    "gg": "Good Game (Bom jogo), dito no fim da partida.",
    "tryhard": "Jogador que se esforça ao máximo para vencer.",
    "tankar": "Aguentar muito dano ou resistir a um ataque forte no lugar de outros.",
    "loot": "Itens, armas ou tesouros coletados durante o jogo."
}
if word in dicionario_gamer.keys():
    # O que devemos fazer se a palavra for encontrada?
    print(dicionario_gamer[word])
else:
    # O que devemos fazer se a palavra não for encontrada?
    print('esta palavra não está disponível.')
