import pygame
import sys
import random
from personagem import Personagem
from consts import LARGURA, ALTURA, BAU_X, BAU_Y, PERSONAGEM_X, PERSONAGEM_Y

# Variáveis globais
experiencia = 0
quiz_resolvido = False
cenario_atual = 1  # Começa no cenário 1 (Primavera)
# Adicione as constantes para o número de corações
NUM_CORACOES = 3

# Função para exibir a tela de Game Over
def tela_game_over(tela):
    tela.fill((0, 0, 0))  # Limpa a tela com fundo preto
    fonte = pygame.font.Font(None, 74)
    texto_game_over = fonte.render("Game Over", True, (255, 0, 0))
    tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - 50))

    fonte = pygame.font.Font(None, 36)
    texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
    tela.blit(texto_reiniciar, (LARGURA // 2 - texto_reiniciar.get_width() // 2, ALTURA // 2 + 20))

    pygame.display.flip()

    # Espera até que o jogador pressione R
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reinicia o jogo
                    return

# Função para desenhar os corações
def desenhar_coracoes(tela, coracoes):
    for i in range(coracoes):
        coracao_img = pygame.transform.scale(pygame.image.load("assets/Recursos/coracao.png"), (30, 30))
        tela.blit(coracao_img, (LARGURA - 40, 10 + i * 35))


# Função para carregar recursos
def carregar_recursos():
    recursos = {}
    recursos['background_inicio'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/tela_inicial.jpg"), (LARGURA, ALTURA))

    # Cenário 1: Primavera
    recursos['background_primavera_nitido'] = pygame.image.load("assets/Backgrounds/cenario1(primavera-nitido).jpg")
    recursos['bau_primavera'] = pygame.image.load("assets/Recursos/baú fechado.png")
    recursos['ticket_primavera'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_primavera.png"), (44, 44))

    # Cenário 2: Verão
    recursos['background_verao_nitido'] = pygame.image.load("assets/Backgrounds/cenario2(verao-nitido).jpg")
    recursos['bau_verao'] = pygame.image.load("assets/Recursos/bau_verao.png")
    recursos['ticket_verao'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_verao.png"), (44, 44))

    # Cenário 3: Outono
    recursos['background_outono_nitido'] = pygame.image.load("assets/Backgrounds/cenario3(outono-nitido).jpg")
    recursos['bau_outono'] = pygame.image.load("assets/Recursos/bau_outono.png")
    recursos['ticket_outono'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_outono.png"), (44, 44))

    # Cenário 4: Inverno
    recursos['background_inverno_nitido'] = pygame.image.load("assets/Backgrounds/cenario4(inverno-nitido).jpg")
    recursos['bau_inverno'] = pygame.image.load("assets/Recursos/bau_inverno.png")
    recursos['ticket_inverno'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_inverno.png"), (44, 44))

    # Outros recursos
    recursos['barra_xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_comeco.png"), (200, 50))
    recursos['barra_xp_20'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_20%.png"), (200, 50))
    recursos['mapa'] = pygame.transform.scale(pygame.image.load("assets/Recursos/mapa.jpg"), (1280, 700))
    return recursos
# Função para mostrar o mapa
def mostrar_mapa(tela, recursos):
    clock = pygame.time.Clock()
    while True:
        tela.blit(recursos['mapa'], (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao jogo ao pressionar ESC
                    return

        clock.tick(60)

# Questões para cada cenário
questoes_primavera =  {
    1: {
        "pergunta": "Qual técnica de demonstração se utiliza para provar uma afirmação ao demonstrar que o contrário levaria a uma contradição?",
        "opcoes": ["A) Indução", "B) Contrapositivo", "C) Contradição", "D) Prova Direta"],
        "resposta": "C"
    },

    2: {
        "pergunta": "Em uma prova por contrapositivo, para provar P=>Q qual afirmação é provada?",
        "opcoes": ["A) Q=>P", "B) ¬P⇒¬Q", "C) ¬Q⇒¬P", "D) P^Q=>¬Q"],
        "resposta": "C"
    },

    3: {
        "pergunta": "Qual técnica de prova é mais apropriada para provar uma afirmação da forma “para todo n, se n é par, então n^2 é par”?",
        "opcoes": ["A) Contrapositiva", "B) Indução", "C) Contradição", "D) Prova Direta"],
        "resposta": "D"
    },

    4: {
        "pergunta": "A técnica de indução matemática é frequentemente usada para provar proposições sobre...",
        "opcoes": ["A) Números Racionais", "B) Números Naturais", "C) Números Complexos", "D) Números Irracionais"],
        "resposta": "B"
    },

    5: {
        "pergunta": "Para provar que 'se um número é ímpar, então seu quadrado também é ímpar', qual técnica seria mais adequada?",
        "opcoes": ["A) Contradição", "B) Prova Direta", "C) Contrapositivo", "D) Indução"],
        "resposta": "B"
    },

    6: {
        "pergunta": "Na indução matemática, qual é o primeiro passo?",
        "opcoes": ["A) Provar a afirmação para n+1", "B) Provar a afirmação para n=1", "C) Assumir a afirmação para n e n+1", "D) Refutar a afirmação para valores ímpares"],
        "resposta": "B"
    },

    7: {
        "pergunta": "Para provar uma proposição para todos os números naturais, qual método é mais eficiente?",
        "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
        "resposta": "B"
    },

    8: {
        "pergunta": "Ao provar uma afirmação por contradição, assumimos...",
        "opcoes": ["A) Que a afirmação é falsa", "B) Que a afirmação é verdadeira", "C) Que ambas são verdadeiras", "D) Que nenhuma delas é verdadeira"],
        "resposta": "A"
    },

    9: {
        "pergunta": "Para provar que a raiz quadrada de 2 é irracional, qual técnica é geralmente utilizada?",
        "opcoes": ["A) Contrapositivo", "B) Prova Direta", "C) Indução", "D) Contradição"],
        "resposta": "D"
    },

    10: {
        "pergunta": "Na prova por contrapositivo, qual proposição alternativa você assume para provar P=>Q?",
        "opcoes": ["A) P=>Q", "B) ¬P=>¬Q", "C) ¬Q⇒¬P", "D) Q=>P"],
        "resposta": "C"
    },

    11: {
        "pergunta": "Qual técnica de demonstração é mais útil para provar a fórmula da soma dos primeiros n números naturais?",
        "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositivo", "D) Redução ao absurdo"],
        "resposta": "B"
    },

    12: {
        "pergunta": "Para provar uma implicação “Se A, então B” usando contrapositivo, devemos provar...",
        "opcoes": ["A) Se B é falso, então A é falso", "B) Se B é verdadeiro, então A é falso", "C) Se A é verdadeiro, então B é falso", "D) Se A é falso, então B é falso"],
        "resposta": "A"
    },

    13: {
        "pergunta": "Qual técnica envolve assumir o oposto de uma afirmação e derivar uma contradição?",
        "opcoes": ["A) Indução", "B) Contradição", "C) Contrapositivo", "D) Prova Direta"],
        "resposta": "B"
    },

    14: {
        "pergunta": "Para provar que a soma de dois números ímpares é par, a técnica recomendada é...",
        "opcoes": ["A) Contradição", "B) Contrapositiva", "C) Prova Direta", "D) Indução"],
        "resposta": "C"
    },

    15: {
        "pergunta": "Uma prova que demonstra uma proposição ao verificar que a negação leva a uma conclusão impossível é chamada de...",
        "opcoes": ["A) Indução", "B) Contrapositivo", "C) Contradição", "D) Prova Direta"],
        "resposta": "C"
    },

    16: {
        "pergunta": "Para mostrar que uma proposição P implica Q em uma prova direta, qual suposição inicial fazemos?",
        "opcoes": ["A) Q é falso", "B) Q é verdadeiro", "C) P é verdadeiro", "D) P é falso"],
        "resposta": "C"
    },

    17: {
        "pergunta": "Qual dos seguintes é um exemplo de prova por contrapositivo?",
        "opcoes": ["A) Suponha que P e Q sejam verdadeiros", "B) Suponha que ¬Q e derive ¬P", "C) Suponha Q e prove P", "D) Suponha que ¬P é falso"],
        "resposta": "B"
    },

    18: {
        "pergunta": "Para provar que não existe número racional cuja raiz quadrada seja 3, utilizamos...",
        "opcoes": ["A) Indução", "B) Prova Direta", "C) Contradição", "D) Contrapositivo"],
        "resposta": "C"
    },

    19: {
        "pergunta": "Qual técnica é frequentemente utilizada em proposições do tipo 'para todo número natural n'?",
        "opcoes": ["A) Contrapositivo", "B) Indução", "C) Prova Direta", "D) Contradição"],
        "resposta": "B"
    },

    20: {
        "pergunta": "Qual técnica requer a demonstração de uma base e um passo de indução?",
        "opcoes": ["A) Contradição", "B) Contrapositivo", "C) Indução", "D) Prova Direta"],
        "resposta": "C"
    },

    21: {
        "pergunta": "Para provar que o produto de dois números racionais é racional, qual técnica é mais adequada?",
        "opcoes": ["A) Prova Direta", "B) Contrapositivo", "C) Contradição", "D) Indução"],
        "resposta": "A"
    },

    22: {
        "pergunta": "Qual técnica é utilizada para provar que se um número é divisível por 4, então seu quadrado é divisível por 16?",
        "opcoes": ["A) Prova Direta", "B) Indução", "C) Contrapositivo", "D) Contradição"],
        "resposta": "A"
    },

    23: {
        "pergunta": "A afirmação 'se um número é par, então seu sucessor é ímpar' pode ser provada usando...",
        "opcoes": ["A) Indução", "B) Prova Direta", "C) Contrapositivo", "D) Contradição"],
        "resposta": "B"
    },

    24: {
        "pergunta": "Para provar que n² − n é par para todo número natural n, a técnica sugerida é...",
        "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
        "resposta": "B"
    },

    25: {
        "pergunta": "Qual técnica de demonstração seria melhor para provar que a soma de um número par com um ímpar é ímpar?",
        "opcoes": ["A) Contradição", "B) Prova Direta", "C) Indução", "D) Contrapositivo"],
        "resposta": "B"
    },

    26: {
        "pergunta": "Para provar que o mínimo divisor de um número primo é ele mesmo, usamos...",
        "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositivo", "D) Prova Direta"],
        "resposta": "D"
    },

    27: {
        "pergunta": "Para provar que um número natural n é divisível por 3, assumimos que n≡0(mod3) e mostramos que...",
        "opcoes": ["A) n=3k+1", "B) n=3k", "C) n≡2(mod3)", "D) n=k+3"],
        "resposta": "B"
    },

    28: {
        "pergunta": "Para provar que um conjunto finito tem um número de subconjuntos que é uma potência de 2, usamos...",
        "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
        "resposta": "B"
    },

    29: {
        "pergunta": "Para mostrar que um número par multiplicado por outro número par é par, usamos...",
        "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositiva", "D) Prova Direta"],
        "resposta": "D"
    },

    30: {
        "pergunta": "Provar que a soma de dois múltiplos de um número é múltiplo desse número é um exemplo de...",
        "opcoes": ["A) Indução", "B) Contradição", "C) Contrapositivo", "D) Prova Direta"],
        "resposta": "D"
    }
}

questoes_verao = {
    1: {
        "pergunta": "Quantas maneiras diferentes há para escolher 2 pessoas de um grupo de 5?",
        "opcoes": ["A) 5", "B) 10", "C) 15", "D) 20"],
        "resposta": "B"
    },

    2: {
        "pergunta": "Quantos anagramas podem ser formados a partir da palavra 'COMBINAÇÃO'?",
        "opcoes": ["A) 10!", "B) 11!", "C) 11!/2!", "D) 10!/2!"],
        "resposta": "C"
    },

    3: {
        "pergunta": "Quantas formas existem para organizar 3 bolas vermelhas e 2 bolas azuis em uma linha?",
        "opcoes": ["A) 10", "B) 6", "C) 8", "D) 12"],
        "resposta": "A"
    },

    4: {
        "pergunta": "Em uma eleição com 3 candidatos, quantas maneiras diferentes existem para escolher uma ordem dos vencedores?",
        "opcoes": ["A) 6", "B) 8", "C) 9", "D) 12"],
        "resposta": "A"
    },

    5: {
        "pergunta": "Quantos subconjuntos com exatamente 3 elementos podem ser formados a partir de um conjunto de 6 elementos?",
        "opcoes": ["A) 15", "B) 18", "C) 20", "D) 10"],
        "resposta": "A"
    },

    6: {
        "pergunta": "Se você tem 5 livros e quer organizá-los em uma prateleira, quantas sequências diferentes são possíveis?",
        "opcoes": ["A) 60", "B) 120", "C) 80", "D) 100"],
        "resposta": "B"
    },

    7: {
        "pergunta": "Quantas maneiras há de escolher um presidente e um vice-presidente de um grupo de 7 pessoas?",
        "opcoes": ["A) 21", "B) 35", "C) 42", "D) 56"],
        "resposta": "C"
    },

    8: {
        "pergunta": "Quantas maneiras existem para escolher 2 pessoas de um grupo de 8?",
        "opcoes": ["A) 28", "B) 36", "C) 16", "D) 20"],
        "resposta": "A"
    },

    9: {
        "pergunta": "Quantas maneiras diferentes há de organizar as letras na palavra 'BANANA'?",
        "opcoes": ["A) 60", "B) 120", "C) 720", "D) 360"],
        "resposta": "D"
    },

    10: {
        "pergunta": "De quantas maneiras diferentes é possível escolher 3 frutas em uma caixa com 5 frutas diferentes?",
        "opcoes": ["A) 5", "B) 10", "C) 20", "D) 15"],
        "resposta": "D"
    },

    11: {
        "pergunta": "Qual é o valor de 7! (fatorial de 7)?",
        "opcoes": ["A) 5040", "B) 720", "C) 2520", "D) 40320"],
        "resposta": "A"
    },

    12: {
        "pergunta": "Quantas maneiras existem para organizar 4 pessoas em 4 cadeiras?",
        "opcoes": ["A) 16", "B) 64", "C) 24", "D) 36"],
        "resposta": "C"
    },

    13: {
        "pergunta": "De quantas maneiras podemos escolher 3 elementos de um conjunto com 8 elementos?",
        "opcoes": ["A) 28", "B) 56", "C) 16", "D) 35"],
        "resposta": "A"
    },

    14: {
        "pergunta": "Quantas maneiras diferentes existem para distribuir 5 bolas em 3 caixas, onde cada caixa pode receber qualquer número de bolas?",
        "opcoes": ["A) 125", "B) 243", "C) 15", "D) 45"],
        "resposta": "A"
    },

    15: {
        "pergunta": "Quantos subconjuntos de tamanho 2 podem ser formados a partir de um conjunto de 6 elementos?",
        "opcoes": ["A) 10", "B) 15", "C) 6", "D) 20"],
        "resposta": "B"
    },

    16: {
        "pergunta": "Quantas permutações diferentes das letras na palavra 'LIVRO' existem?",
        "opcoes": ["A) 60", "B) 120", "C) 24", "D) 36"],
        "resposta": "B"
    },

    17: {
        "pergunta": "Quantas maneiras existem para escolher uma equipe de 3 pessoas de um grupo de 9?",
        "opcoes": ["A) 84", "B) 120", "C) 36", "D) 28"],
        "resposta": "D"
    },

    18: {
        "pergunta": "Se você tem 10 opções e quer escolher 3 sem importar a ordem, quantas escolhas possíveis existem?",
        "opcoes": ["A) 120", "B) 720", "C) 30", "D) 36"],
        "resposta": "A"
    },

    19: {
        "pergunta": "Quantas maneiras diferentes existem para escolher 2 membros de um grupo de 7?",
        "opcoes": ["A) 21", "B) 42", "C) 35", "D) 14"],
        "resposta": "A"
    },

    20: {
        "pergunta": "Quantos subconjuntos podem ser formados a partir de um conjunto com 4 elementos?",
        "opcoes": ["A) 4", "B) 8", "C) 16", "D) 32"],
        "resposta": "C"
    },

    21: {
        "pergunta": "Quantas maneiras existem para distribuir 4 bolas em 2 caixas, onde cada caixa pode conter qualquer número de bolas?",
        "opcoes": ["A) 8", "B) 10", "C) 16", "D) 6"],
        "resposta": "A"
    },

    22: {
        "pergunta": "Quantas permutações podem ser feitas com as letras da palavra 'MELANCIA'?",
        "opcoes": ["A) 40,320", "B) 20,160", "C) 80,640", "D) 90,720"],
        "resposta": "B"
    },

    23: {
        "pergunta": "Qual é o número de maneiras de organizar as letras na palavra 'ELEFANTE'?",
        "opcoes": ["A) 40,320", "B) 20,160", "C) 80,640", "D) 60,480"],
        "resposta": "D"
    },

    24: {
        "pergunta": "Quantas formas existem de escolher uma equipe de 2 pessoas de um grupo de 8?",
        "opcoes": ["A) 28", "B) 16", "C) 36", "D) 21"],
        "resposta": "A"
    },

    25: {
        "pergunta": "Quantas maneiras existem para escolher 4 objetos de um conjunto de 6?",
        "opcoes": ["A) 15", "B) 20", "C) 30", "D) 12"],
        "resposta": "B"
    },

    26: {
        "pergunta": "Quantos subconjuntos de tamanho 3 podem ser escolhidos de um conjunto com 5 elementos?",
        "opcoes": ["A) 5", "B) 6", "C) 10", "D) 15"],
        "resposta": "B"
    },

    27: {
        "pergunta": "Quantas maneiras diferentes existem para arranjar as letras da palavra 'FATORIAL'?",
        "opcoes": ["A) 40,320", "B) 20,160", "C) 90,720", "D) 45,360"],
        "resposta": "C"
    },

    28: {
        "pergunta": "De quantas maneiras podem ser organizadas as letras da palavra 'ESCOLA'?",
        "opcoes": ["A) 720", "B) 1,080", "C) 2,520", "D) 840"],
        "resposta": "A"
    },

    29: {
        "pergunta": "Quantas combinações podem ser feitas escolhendo 3 pessoas de um grupo de 6?",
        "opcoes": ["A) 15", "B) 20", "C) 10", "D) 12"],
        "resposta": "A"
    },

    30: {
        "pergunta": "Quantas permutações podem ser feitas com as letras da palavra 'COMBINA'?",
        "opcoes": ["A) 40,320", "B) 20,160", "C) 5,040", "D) 10,080"],
        "resposta": "C"
    }
}

questoes_outono = {
    1: {
        "pergunta": "Qual é a definição básica de recursão em ciência da computação?",
        "opcoes": ["A) Uma função que chama a si mesma", "B) Uma função que nunca termina",
                   "C) Uma função que chama outra função", "D) Um loop infinito"],
        "resposta": "A"
    },

    2: {
        "pergunta": "Qual das seguintes é uma condição necessária para uma função recursiva?",
        "opcoes": ["A) Uma variável global", "B) Uma condição base", "C) Um loop", "D) Um contador"],
        "resposta": "B"
    },

    3: {
        "pergunta": "Qual função recursiva é frequentemente usada para calcular o valor de n! (fatorial de n)?",
        "opcoes": ["A) Soma", "B) Potência", "C) Multiplicação", "D) Fatorial"],
        "resposta": "D"
    },

    4: {
        "pergunta": "Qual é o resultado da função recursiva para fatorial de 0?",
        "opcoes": ["A) 0", "B) 1", "C) 2", "D) Indefinido"],
        "resposta": "B"
    },

    5: {
        "pergunta": "Qual é a principal vantagem do uso de recursão?",
        "opcoes": ["A) Menor uso de memória", "B) Código mais simples e legível", "C) Reduz o tempo de execução",
                   "D) Evita o uso de funções"],
        "resposta": "B"
    },

    6: {
        "pergunta": "O que é um caso base em uma função recursiva?",
        "opcoes": ["A) O caso que faz a função repetir", "B) O caso em que a função chama outra função",
                   "C) O caso que termina a recursão", "D) O caso que nunca é alcançado"],
        "resposta": "C"
    },

    7: {
        "pergunta": "Qual das seguintes estruturas é mais usada para implementar recursão?",
        "opcoes": ["A) Pilha", "B) Fila", "C) Lista", "D) Tabela Hash"],
        "resposta": "A"
    },

    8: {
        "pergunta": "O que é 'recursão direta'?",
        "opcoes": ["A) Quando uma função chama outra função", "B) Quando uma função chama a si mesma",
                   "C) Quando uma função chama duas outras funções", "D) Quando uma função nunca termina"],
        "resposta": "B"
    },

    9: {
        "pergunta": "O que ocorre se uma função recursiva não tiver um caso base?",
        "opcoes": ["A) A função termina normalmente", "B) A função entra em um loop infinito",
                   "C) A função retorna zero", "D) A função é ignorada pelo compilador"],
        "resposta": "B"
    },

    10: {
        "pergunta": "Qual é o papel de uma condição de parada em recursão?",
        "opcoes": ["A) Iniciar a recursão", "B) Reduzir o valor de uma variável", "C) Parar a recursão",
                   "D) Duplicar a função"],
        "resposta": "C"
    },

    11: {
        "pergunta": "Qual é o uso da recursão na resolução de problemas?",
        "opcoes": ["A) Para problemas que requerem repetição", "B) Para problemas lineares",
                   "C) Para problemas que podem ser divididos em subproblemas menores",
                   "D) Para problemas que não possuem solução base"],
        "resposta": "C"
    },

    12: {
        "pergunta": "Qual das seguintes é uma aplicação comum de recursão?",
        "opcoes": ["A) Calculadora", "B) Fatorial e sequência de Fibonacci", "C) Processador de texto",
                   "D) Planilha eletrônica"],
        "resposta": "B"
    },

    13: {
        "pergunta": "Qual das alternativas define 'recursão indireta'?",
        "opcoes": ["A) Uma função que chama outra função que eventualmente chama a função original",
                   "B) Uma função que nunca chama outra função", "C) Uma função que chama a si mesma",
                   "D) Uma função que retorna um valor fixo"],
        "resposta": "A"
    },

    14: {
        "pergunta": "Qual é a saída da função recursiva que calcula Fibonacci de 5?",
        "opcoes": ["A) 5", "B) 8", "C) 13", "D) 21"],
        "resposta": "B"
    },

    15: {
        "pergunta": "A recursão pode ser substituída por qual estrutura de controle?",
        "opcoes": ["A) Estrutura de seleção", "B) Estrutura de repetição (loops)", "C) Estrutura condicional",
                   "D) Estrutura de interrupção"],
        "resposta": "B"
    },

    16: {
        "pergunta": "Quantas chamadas recursivas são feitas para calcular o fatorial de 4?",
        "opcoes": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "resposta": "D"
    },

    17: {
        "pergunta": "Quais dos seguintes problemas podem ser resolvidos usando recursão?",
        "opcoes": ["A) Ordenação de listas", "B) Somar duas variáveis", "C) Multiplicação", "D) Filtragem de dados"],
        "resposta": "A"
    },

    18: {
        "pergunta": "Qual das seguintes não é uma característica da recursão?",
        "opcoes": ["A) Uso de chamadas de função", "B) Uso de caso base", "C) Uso de variáveis globais",
                   "D) Uso de pilha para armazenar chamadas"],
        "resposta": "C"
    },

    19: {
        "pergunta": "Recursão pode ser mais eficiente do que loops?",
        "opcoes": ["A) Sempre", "B) Em problemas que podem ser divididos em subproblemas", "C) Nunca",
                   "D) Em cálculos matemáticos simples"],
        "resposta": "B"
    },

    20: {
        "pergunta": "Qual das seguintes é uma vantagem da recursão?",
        "opcoes": ["A) Menor tempo de execução", "B) Menor uso de memória", "C) Simplificação de problemas complexos",
                   "D) Necessidade de mais código"],
        "resposta": "C"
    },

    21: {
        "pergunta": "Como a função recursiva fatorial de um número n é geralmente escrita?",
        "opcoes": ["A) f(n) = n + f(n-1)", "B) f(n) = n * f(n-1)", "C) f(n) = f(n-1)", "D) f(n) = n - f(n-1)"],
        "resposta": "B"
    },

    22: {
        "pergunta": "Recursão é uma abordagem natural para resolver problemas de qual natureza?",
        "opcoes": ["A) Iterativos", "B) Lineares", "C) Dividir para conquistar", "D) Aleatórios"],
        "resposta": "C"
    },

    23: {
        "pergunta": "Qual é uma desvantagem da recursão?",
        "opcoes": ["A) Aumenta a complexidade", "B) Consome mais memória devido à pilha de chamadas", "C) É mais lento",
                   "D) Não pode ser usado em problemas grandes"],
        "resposta": "B"
    },

    24: {
        "pergunta": "Qual das seguintes é uma aplicação prática da recursão?",
        "opcoes": ["A) Contar caracteres em uma string", "B) Multiplicação", "C) Processamento de árvores binárias",
                   "D) Processamento de matrizes"],
        "resposta": "C"
    },

    25: {
        "pergunta": "Na recursão, o que acontece com cada chamada recursiva?",
        "opcoes": ["A) É armazenada em uma fila", "B) É armazenada na pilha", "C) É descartada imediatamente",
                   "D) É processada em ordem reversa"],
        "resposta": "B"
    },

    26: {
        "pergunta": "Para qual estrutura de dados é mais adequada a recursão?",
        "opcoes": ["A) Fila", "B) Lista", "C) Pilha", "D) Dicionário"],
        "resposta": "C"
    },

    27: {
        "pergunta": "Quais são os casos mais comuns onde recursão é útil?",
        "opcoes": ["A) Jogos", "B) Algoritmos de busca e ordenação", "C) Processamento de dados",
                   "D) Edição de imagens"],
        "resposta": "B"
    },

    28: {
        "pergunta": "Qual é uma limitação da recursão em sistemas com pilha limitada?",
        "opcoes": ["A) Processamento lento", "B) Excesso de variáveis", "C) Estouro de pilha",
                   "D) Uso de função global"],
        "resposta": "C"
    },

    29: {
        "pergunta": "A profundidade de uma chamada recursiva refere-se a...",
        "opcoes": ["A) Número de vezes que a função é chamada", "B) A quantidade de memória usada",
                   "C) O número de parâmetros", "D) A estrutura de dados usada"],
        "resposta": "A"
    },

    30: {
        "pergunta": "A recursão de cauda é...",
        "opcoes": ["A) Uma função que termina em um loop",
                   "B) Uma recursão onde a chamada recursiva é a última operação", "C) Uma função sem caso base",
                   "D) Uma função que nunca termina"],
        "resposta": "B"
    }
}

questoes_inverno = { 1: {
    "pergunta": "Qual é a definição básica de recursão em ciência da computação?",
    "opcoes": ["A) Uma função que chama a si mesma", "B) Uma função que nunca termina",
               "C) Uma função que chama outra função", "D) Um loop infinito"],
    "resposta": "A"
},

2: {
    "pergunta": "Qual das seguintes é uma condição necessária para uma função recursiva?",
    "opcoes": ["A) Uma variável global", "B) Uma condição base", "C) Um loop", "D) Um contador"],
    "resposta": "B"
},

3: {
    "pergunta": "Qual função recursiva é frequentemente usada para calcular o valor de n! (fatorial de n)?",
    "opcoes": ["A) Soma", "B) Potência", "C) Multiplicação", "D) Fatorial"],
    "resposta": "D"
},

4: {
    "pergunta": "Qual é o resultado da função recursiva para fatorial de 0?",
    "opcoes": ["A) 0", "B) 1", "C) 2", "D) Indefinido"],
    "resposta": "B"
},

5: {
    "pergunta": "Qual é a principal vantagem do uso de recursão?",
    "opcoes": ["A) Menor uso de memória", "B) Código mais simples e legível", "C) Reduz o tempo de execução",
               "D) Evita o uso de funções"],
    "resposta": "B"
},

6: {
    "pergunta": "O que é um caso base em uma função recursiva?",
    "opcoes": ["A) O caso que faz a função repetir", "B) O caso em que a função chama outra função",
               "C) O caso que termina a recursão", "D) O caso que nunca é alcançado"],
    "resposta": "C"
},

7: {
    "pergunta": "Qual das seguintes estruturas é mais usada para implementar recursão?",
    "opcoes": ["A) Pilha", "B) Fila", "C) Lista", "D) Tabela Hash"],
    "resposta": "A"
},

8: {
    "pergunta": "O que é 'recursão direta'?",
    "opcoes": ["A) Quando uma função chama outra função", "B) Quando uma função chama a si mesma",
               "C) Quando uma função chama duas outras funções", "D) Quando uma função nunca termina"],
    "resposta": "B"
},

9: {
    "pergunta": "O que ocorre se uma função recursiva não tiver um caso base?",
    "opcoes": ["A) A função termina normalmente", "B) A função entra em um loop infinito", "C) A função retorna zero",
               "D) A função é ignorada pelo compilador"],
    "resposta": "B"
},

10: {
    "pergunta": "Qual é o papel de uma condição de parada em recursão?",
    "opcoes": ["A) Iniciar a recursão", "B) Reduzir o valor de uma variável", "C) Parar a recursão",
               "D) Duplicar a função"],
    "resposta": "C"
},

11: {
    "pergunta": "Qual é o uso da recursão na resolução de problemas?",
    "opcoes": ["A) Para problemas que requerem repetição", "B) Para problemas lineares",
               "C) Para problemas que podem ser divididos em subproblemas menores",
               "D) Para problemas que não possuem solução base"],
    "resposta": "C"
},

12: {
    "pergunta": "Qual das seguintes é uma aplicação comum de recursão?",
    "opcoes": ["A) Calculadora", "B) Fatorial e sequência de Fibonacci", "C) Processador de texto",
               "D) Planilha eletrônica"],
    "resposta": "B"
},

13: {
    "pergunta": "Qual das alternativas define 'recursão indireta'?",
    "opcoes": ["A) Uma função que chama outra função que eventualmente chama a função original",
               "B) Uma função que nunca chama outra função", "C) Uma função que chama a si mesma",
               "D) Uma função que retorna um valor fixo"],
    "resposta": "A"
},

14: {
    "pergunta": "Qual é a saída da função recursiva que calcula Fibonacci de 5?",
    "opcoes": ["A) 5", "B) 8", "C) 13", "D) 21"],
    "resposta": "B"
},

15: {
    "pergunta": "A recursão pode ser substituída por qual estrutura de controle?",
    "opcoes": ["A) Estrutura de seleção", "B) Estrutura de repetição (loops)", "C) Estrutura condicional",
               "D) Estrutura de interrupção"],
    "resposta": "B"
},

16: {
    "pergunta": "Quantas chamadas recursivas são feitas para calcular o fatorial de 4?",
    "opcoes": ["A) 2", "B) 3", "C) 4", "D) 5"],
    "resposta": "D"
},

17: {
    "pergunta": "Quais dos seguintes problemas podem ser resolvidos usando recursão?",
    "opcoes": ["A) Ordenação de listas", "B) Somar duas variáveis", "C) Multiplicação", "D) Filtragem de dados"],
    "resposta": "A"
},

18: {
    "pergunta": "Qual das seguintes não é uma característica da recursão?",
    "opcoes": ["A) Uso de chamadas de função", "B) Uso de caso base", "C) Uso de variáveis globais",
               "D) Uso de pilha para armazenar chamadas"],
    "resposta": "C"
},

19: {
    "pergunta": "Recursão pode ser mais eficiente do que loops?",
    "opcoes": ["A) Sempre", "B) Em problemas que podem ser divididos em subproblemas", "C) Nunca",
               "D) Em cálculos matemáticos simples"],
    "resposta": "B"
},

20: {
    "pergunta": "Qual das seguintes é uma vantagem da recursão?",
    "opcoes": ["A) Menor tempo de execução", "B) Menor uso de memória", "C) Simplificação de problemas complexos",
               "D) Necessidade de mais código"],
    "resposta": "C"
},

21: {
    "pergunta": "Como a função recursiva fatorial de um número n é geralmente escrita?",
    "opcoes": ["A) f(n) = n + f(n-1)", "B) f(n) = n * f(n-1)", "C) f(n) = f(n-1)", "D) f(n) = n - f(n-1)"],
    "resposta": "B"
},

22: {
    "pergunta": "Recursão é uma abordagem natural para resolver problemas de qual natureza?",
    "opcoes": ["A) Iterativos", "B) Lineares", "C) Dividir para conquistar", "D) Aleatórios"],
    "resposta": "C"
},

23: {
    "pergunta": "Qual é uma desvantagem da recursão?",
    "opcoes": ["A) Aumenta a complexidade", "B) Consome mais memória devido à pilha de chamadas", "C) É mais lento",
               "D) Não pode ser usado em problemas grandes"],
    "resposta": "B"
},

24: {
    "pergunta": "Qual das seguintes é uma aplicação prática da recursão?",
    "opcoes": ["A) Contar caracteres em uma string", "B) Multiplicação", "C) Processamento de árvores binárias",
               "D) Processamento de matrizes"],
    "resposta": "C"
},

25: {
    "pergunta": "Na recursão, o que acontece com cada chamada recursiva?",
    "opcoes": ["A) É armazenada em uma fila", "B) É armazenada na pilha", "C) É descartada imediatamente",
               "D) É processada em ordem reversa"],
    "resposta": "B"
},

26: {
    "pergunta": "Para qual estrutura de dados é mais adequada a recursão?",
    "opcoes": ["A) Fila", "B) Lista", "C) Pilha", "D) Dicionário"],
    "resposta": "C"
},

27: {
    "pergunta": "Quais são os casos mais comuns onde recursão é útil?",
    "opcoes": ["A) Jogos", "B) Algoritmos de busca e ordenação", "C) Processamento de dados", "D) Edição de imagens"],
    "resposta": "B"
},

28: {
    "pergunta": "Qual é uma limitação da recursão em sistemas com pilha limitada?",
    "opcoes": ["A) Processamento lento", "B) Excesso de variáveis", "C) Estouro de pilha", "D) Uso de função global"],
    "resposta": "C"
},

29: {
    "pergunta": "A profundidade de uma chamada recursiva refere-se a...",
    "opcoes": ["A) Número de vezes que a função é chamada", "B) A quantidade de memória usada",
               "C) O número de parâmetros", "D) A estrutura de dados usada"],
    "resposta": "A"
},

30: {
    "pergunta": "A recursão de cauda é...",
    "opcoes": ["A) Uma função que termina em um loop", "B) Uma recursão onde a chamada recursiva é a última operação",
               "C) Uma função sem caso base", "D) Uma função que nunca termina"],
    "resposta": "B"
}
}
questoes_inverno = {
    1: {
        "pergunta": "O que é um grafo em teoria dos grafos?",
        "opcoes": ["A) Um conjunto de pontos e linhas conectando pares de pontos", "B) Um conjunto de números",
                   "C) Uma sequência de passos", "D) Um tipo de matriz"],
        "resposta": "A"
    },

    2: {
        "pergunta": "O que significa dizer que um grafo é conexo?",
        "opcoes": ["A) Todos os vértices têm o mesmo grau", "B) Há um caminho entre qualquer par de vértices",
                   "C) O grafo contém um ciclo", "D) O grafo é completo"],
        "resposta": "B"
    },

    3: {
        "pergunta": "Qual é o número mínimo de arestas em um grafo conexo com n vértices?",
        "opcoes": ["A) n", "B) n - 1", "C) n + 1", "D) n * (n - 1) / 2"],
        "resposta": "B"
    },

    4: {
        "pergunta": "Qual dos seguintes é um exemplo de grafo não direcionado?",
        "opcoes": ["A) Grafo de rede de computadores", "B) Diagrama de fluxo de controle",
                   "C) Grafo de rede de estradas bidirecionais", "D) Arvore genealógica"],
        "resposta": "C"
    },

    5: {
        "pergunta": "Qual o nome dado a um grafo sem ciclos?",
        "opcoes": ["A) Conexo", "B) Ciclo", "C) Árvore", "D) Completo"],
        "resposta": "C"
    },

    6: {
        "pergunta": "Qual estrutura de dados é mais comumente usada para representar grafos em memória?",
        "opcoes": ["A) Pilha", "B) Lista de adjacência", "C) Fila", "D) Árvore binária"],
        "resposta": "B"
    },

    7: {
        "pergunta": "Qual algoritmo é frequentemente utilizado para encontrar o caminho mais curto em um grafo?",
        "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Kruskal", "C) Algoritmo de Prim",
                   "D) Algoritmo de Bellman-Ford"],
        "resposta": "A"
    },

    8: {
        "pergunta": "O que é um vértice de corte em um grafo?",
        "opcoes": ["A) Um vértice que aumenta o grau de outros vértices",
                   "B) Um vértice cuja remoção desconecta o grafo", "C) Um vértice sem arestas conectadas",
                   "D) Um vértice que forma um ciclo"],
        "resposta": "B"
    },

    9: {
        "pergunta": "Em um grafo ponderado, o que as arestas possuem além de vértices?",
        "opcoes": ["A) Peso", "B) Cor", "C) Número de ciclos", "D) Grafo completo"],
        "resposta": "A"
    },

    10: {
        "pergunta": "Qual dos seguintes grafos tem o maior número de arestas?",
        "opcoes": ["A) Grafo conexo", "B) Grafo completo", "C) Grafo ciclo", "D) Árvore"],
        "resposta": "B"
    },

    11: {
        "pergunta": "Um grafo direcionado é caracterizado por...",
        "opcoes": ["A) Arestas sem direção", "B) Arestas com direção específica", "C) Conexões que não formam ciclos",
                   "D) Nenhuma aresta"],
        "resposta": "B"
    },

    12: {
        "pergunta": "Em teoria dos grafos, o que é um circuito?",
        "opcoes": ["A) Um caminho que começa e termina no mesmo vértice", "B) Um caminho com vértices adjacentes",
                   "C) Um ciclo sem vértices repetidos", "D) Um grafo completo"],
        "resposta": "A"
    },

    13: {
        "pergunta": "Qual é a complexidade do algoritmo de busca em largura (BFS) em um grafo com V vértices e E arestas?",
        "opcoes": ["A) O(V)", "B) O(E)", "C) O(V + E)", "D) O(V * E)"],
        "resposta": "C"
    },

    14: {
        "pergunta": "Qual algoritmo é utilizado para encontrar uma árvore geradora mínima?",
        "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Prim", "C) Algoritmo de Bellman-Ford",
                   "D) Busca em profundidade"],
        "resposta": "B"
    },

    15: {
        "pergunta": "O que é um grafo completo?",
        "opcoes": ["A) Um grafo onde todos os vértices têm o mesmo grau",
                   "B) Um grafo em que todos os vértices estão conectados entre si", "C) Um grafo com um ciclo",
                   "D) Um grafo com número ímpar de arestas"],
        "resposta": "B"
    },

    16: {
        "pergunta": "Em um grafo, o grau de um vértice é...",
        "opcoes": ["A) O número de arestas conectadas ao vértice", "B) A soma dos pesos das arestas do grafo",
                   "C) O número de vértices", "D) O comprimento do maior caminho"],
        "resposta": "A"
    },

    17: {
        "pergunta": "Qual é a complexidade do algoritmo de Dijkstra usando uma fila de prioridade?",
        "opcoes": ["A) O(V^2)", "B) O(V + E)", "C) O(E log V)", "D) O(E^2)"],
        "resposta": "C"
    },

    18: {
        "pergunta": "O que é um grafo bipartido?",
        "opcoes": ["A) Um grafo com duas cores",
                   "B) Um grafo com vértices divididos em dois conjuntos onde arestas conectam apenas vértices de conjuntos diferentes",
                   "C) Um grafo completo", "D) Um grafo com dois ciclos"],
        "resposta": "B"
    },

    19: {
        "pergunta": "O que é um grafo planar?",
        "opcoes": ["A) Um grafo que pode ser desenhado no plano sem arestas cruzadas",
                   "B) Um grafo com apenas três vértices", "C) Um grafo que possui ciclos", "D) Um grafo completo"],
        "resposta": "A"
    },

    20: {
        "pergunta": "Qual é a diferença entre um caminho e um circuito em um grafo?",
        "opcoes": ["A) Caminho é fechado, circuito é aberto",
                   "B) Caminho não tem ciclos, circuito é um caminho fechado", "C) Caminho é maior que o circuito",
                   "D) Caminho é completo, circuito é bipartido"],
        "resposta": "B"
    },

    21: {
        "pergunta": "Qual algoritmo é usado para encontrar o caminho mínimo em grafos com arestas de pesos negativos?",
        "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Prim", "C) Algoritmo de Bellman-Ford",
                   "D) Algoritmo de Kruskal"],
        "resposta": "C"
    },

    22: {
        "pergunta": "Em qual estrutura de dados é baseada a busca em profundidade (DFS)?",
        "opcoes": ["A) Fila", "B) Pilha", "C) Lista", "D) Árvore binária"],
        "resposta": "B"
    },

    23: {
        "pergunta": "Qual é o número máximo de arestas em um grafo simples com n vértices?",
        "opcoes": ["A) n - 1", "B) n^2", "C) n * (n - 1) / 2", "D) 2^n"],
        "resposta": "C"
    },

    24: {
        "pergunta": "O que é um subgrafo?",
        "opcoes": ["A) Uma parte de um grafo", "B) Um grafo completo", "C) Um grafo desconexo", "D) Um ciclo no grafo"],
        "resposta": "A"
    },

    25: {
        "pergunta": "O algoritmo de Kruskal é usado para...",
        "opcoes": ["A) Encontrar o caminho mais curto", "B) Ordenar vértices", "C) Encontrar a árvore geradora mínima",
                   "D) Detectar ciclos"],
        "resposta": "C"
    },

    26: {
        "pergunta": "Como um grafo denso é definido?",
        "opcoes": ["A) Tem mais arestas que vértices", "B) Tem mais vértices que arestas", "C) É um grafo completo",
                   "D) Possui um único ciclo"],
        "resposta": "A"
    },

    27: {
        "pergunta": "Qual é o grau de um vértice isolado?",
        "opcoes": ["A) 0", "B) 1", "C) n", "D) 2"],
        "resposta": "A"
    },

    28: {
        "pergunta": "O que define um ciclo Hamiltoniano?",
        "opcoes": ["A) Um caminho que percorre todos os vértices uma vez e retorna ao inicial",
                   "B) Um caminho sem vértices repetidos", "C) Uma árvore geradora mínima", "D) Um grafo planar"],
        "resposta": "A"
    },

    29: {
        "pergunta": "Qual é a principal característica de um grafo direcionado acíclico?",
        "opcoes": ["A) Possui ciclos", "B) Não possui ciclos", "C) Todos os vértices têm o mesmo grau",
                   "D) É um grafo completo"],
        "resposta": "B"
    },

    30: {
        "pergunta": "Qual dos seguintes é um exemplo de aplicação de grafos?",
        "opcoes": ["A) Redes sociais", "B) Calendário", "C) Funções matemáticas", "D) Pilhas de execução"],
        "resposta": "A"
    }
}


# Função para verificar colisão com o baú
def colisao_bau(rect_personagem, recursos):
    if cenario_atual == 1:
        bau_rect = recursos['bau_primavera'].get_rect(topleft=(BAU_X, BAU_Y))
    elif cenario_atual == 2:
        bau_rect = recursos['bau_verao'].get_rect(topleft=(BAU_X, BAU_Y))
    elif cenario_atual == 3:
        bau_rect = recursos['bau_outono'].get_rect(topleft=(BAU_X, BAU_Y))
    elif cenario_atual == 4:
        bau_rect = recursos['bau_inverno'].get_rect(topleft=(BAU_X, BAU_Y))

    return rect_personagem.colliderect(bau_rect)

# Função do quiz para cada cenário
def quiz(tela, recursos):
    global quiz_resolvido, coracoes  # Adicione 'coracoes' como uma variável global
    tentativas_erradas = 0
    pontos = 0
    respostas_certas = []

    while True:  # Loop para repetir o quiz até que o jogador acerte mais de 2 perguntas
        # Seleciona questões com base no cenário atual
        if cenario_atual == 1:
            questoes_selecionadas = random.sample(list(questoes_primavera.items()), 5)
        elif cenario_atual == 2:
            questoes_selecionadas = random.sample(list(questoes_verao.items()), 5)
        elif cenario_atual == 3:
            questoes_selecionadas = random.sample(list(questoes_outono.items()), 5)
        elif cenario_atual == 4:
            questoes_selecionadas = random.sample(list(questoes_inverno.items()), 5)

        for numero, questao in questoes_selecionadas:
            tela.fill((255, 255, 255))
            mostrar_pergunta(tela, questao)
            pygame.display.flip()

            resposta_usuario = None
            while resposta_usuario is None:  # Fica no loop até o jogador responder
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            resposta_usuario = "A"
                        elif event.key == pygame.K_b:
                            resposta_usuario = "B"
                        elif event.key == pygame.K_c:
                            resposta_usuario = "C"
                        elif event.key == pygame.K_d:
                            resposta_usuario = "D"

                pygame.time.wait(100)  # Evita loop de alta CPU

            # Verificar resposta
            if resposta_usuario == questao["resposta"]:
                pontos += 1
                respostas_certas.append(numero)  # Armazenar o número da pergunta correta
                print(f"Resposta correta para pergunta {numero}!")
            else:
                tentativas_erradas += 1
                print(f"Resposta incorreta para pergunta {numero}!")

            # Verifica se o jogador atingiu 3 tentativas erradas
            if tentativas_erradas >= 3:
                tela_game_over(tela)  # Chama a tela de Game Over
                return coracoes  # Retorna o número de corações restantes

        # Exibir a pontuação final e as perguntas corretas
        exibir_resultado(tela, pontos, respostas_certas)

        # Se o jogador acertou 2 ou menos perguntas, perde um coração
        if pontos <= 2:
            coracoes -= 1  # Decrementa um coração
            print(f"Você acertou {pontos} perguntas. Você perdeu um coração! Corações restantes: {coracoes}")

            # Verifica se o jogador ficou sem corações
            if coracoes <= 0:
                tela_game_over(tela)  # Chama a tela de Game Over
                return coracoes  # Retorna 0 corações

        # Se o jogador acertou mais de 2 perguntas, marca o quiz como resolvido
        if pontos > 2:
            quiz_resolvido = True
            break  # Sai do loop do quiz

    return coracoes  # Retorna o número de corações restantes

# Função para exibir uma pergunta
def mostrar_pergunta(screen, questao):
    fonte = pygame.font.Font(None, 36)
    linhas_pergunta = quebrar_texto(questao["pergunta"], fonte, 700)

    # Exibe cada linha da pergunta
    for i, linha in enumerate(linhas_pergunta):
        texto_linha = fonte.render(linha, True, (0, 0, 0))
        screen.blit(texto_linha, (50, 100 + i * 40))

    # Exibir opções
    for i, opcao in enumerate(questao["opcoes"]):
        texto_opcao = fonte.render(opcao, True, (0, 0, 0))
        screen.blit(texto_opcao, (100, 200 + len(linhas_pergunta) * 40 + i * 40))

# Função para exibir o resultado do quiz
def exibir_resultado(tela, pontos, respostas_certas):
    tela.fill((255, 255, 255))
    fonte = pygame.font.Font(None, 48)
    fim_texto = fonte.render(f"Fim do Quiz! Pontuação Final: {pontos}/5", True, (0, 0, 0))
    tela.blit(fim_texto, (200, 300))

    if respostas_certas:
        perguntas_acertadas = ", ".join(map(str, respostas_certas))
        acertos_texto = fonte.render(f"Perguntas acertadas: {perguntas_acertadas}", True, (0, 0, 0))
        tela.blit(acertos_texto, (200, 350))

    pygame.display.flip()
    pygame.time.wait(3000)  # Espera 3 segundos antes de voltar ao jogo

# Função para quebrar texto longo em várias linhas
def quebrar_texto(texto, fonte, largura_maxima):
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        test_line = linha_atual + palavra + " "
        # Testa o tamanho da linha
        if fonte.size(test_line)[0] < largura_maxima:
            linha_atual = test_line
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)
    return linhas


def transicao(tela):
    clock = pygame.time.Clock()

    # Fade-out
    for alpha in range(255, -1, -5):  # De 255 a 0
        tela.fill((0, 0, 0))  # Preenche a tela com preto
        tela.set_alpha(alpha)  # Define a transparência
        pygame.display.update()
        clock.tick(60)

    # Fade-in
    for alpha in range(0, 256, 5):  # De 0 a 255
        tela.fill((0, 0, 0))  # Preenche a tela com preto
        tela.set_alpha(alpha)  # Define a transparência
        pygame.display.update()
        clock.tick(60)

# Função principal do jogo
def jogo(recursos):
    global experiencia, quiz_resolvido, cenario_atual
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    personagem = Personagem()  # Cria o personagem
    ticket_pego = False
    coracoes = NUM_CORACOES  # Inicializa o número de corações
    tentativas_quiz = 0  # Inicializa o contador de tentativas de quiz

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    mostrar_mapa(tela, recursos)

        teclas = pygame.key.get_pressed()
        personagem.atualizar(teclas)

        # Atualiza o fundo e o baú de acordo com o cenário atual
        if cenario_atual == 1:
            tela.blit(recursos['background_primavera_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                tela.blit(recursos['bau_primavera'], (BAU_X, BAU_Y))
                if colisao_bau(personagem.rect, recursos):
                    tentativas_quiz += 1  # Incrementa o contador de tentativas
                    quiz(tela, recursos)  # Inicia o quiz

        elif cenario_atual == 2:
            tela.blit(recursos['background_verao_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                tela.blit(recursos['bau_verao'], (BAU_X, BAU_Y))
                if colisao_bau(personagem.rect, recursos):
                    tentativas_quiz += 1  # Incrementa o contador de tentativas
                    quiz(tela, recursos)

        elif cenario_atual == 3:
            tela.blit(recursos['background_outono_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                tela.blit(recursos['bau_outono'], (BAU_X, BAU_Y))
                if colisao_bau(personagem.rect, recursos):
                    tentativas_quiz += 1  # Incrementa o contador de tentativas
                    quiz(tela, recursos)

        elif cenario_atual == 4:
            tela.blit(recursos['background_inverno_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                tela.blit(recursos['bau_inverno'], (BAU_X, BAU_Y))
                if colisao_bau(personagem.rect, recursos):
                    tentativas_quiz += 1  # Incrementa o contador de tentativas
                    quiz(tela, recursos)

        # Verifica se o jogador fez o quiz mais de 3 vezes
        if tentativas_quiz > 3:
            tela_game_over(tela)  # Chama a tela de Game Over
            return  # Sai da função jogo

        # Desenhar o personagem
        personagem.desenhar(tela)

        # Desenhar os corações na tela
        desenhar_coracoes(tela, coracoes)

        # Exibir o ticket se o quiz foi resolvido
        if quiz_resolvido and not ticket_pego:
            if cenario_atual == 1:
                tela.blit(recursos['ticket_primavera'], (BAU_X, BAU_Y))
            elif cenario_atual == 2:
                tela.blit(recursos['ticket_verao'], (BAU_X, BAU_Y))
            elif cenario_atual == 3:
                tela.blit(recursos['ticket_outono'], (BAU_X, BAU_Y))
            elif cenario_atual == 4:
                tela.blit(recursos['ticket_inverno'], (BAU_X, BAU_Y))

            fonte = pygame.font.SysFont(None, 15)
            texto1 = fonte.render("Aperte P para pegar", True, (255, 255, 255))
            tela.blit(texto1, (BAU_X, BAU_Y - 30))

            if teclas[ pygame.K_p]:  # Verifica se P foi pressionado
                ticket_pego = True
                experiencia += 10  # Adiciona experiência ao jogador
                print("Você pegou o ticket! +10 de experiência")

                # Chama a função de transição antes de mudar de cenário
                transicao(tela)

                # Avança para o próximo cenário
                if cenario_atual < 4:  # Verifica se ainda há cenários para avançar
                    cenario_atual += 1
                    quiz_resolvido = False  # Reseta o estado do quiz para o novo cenário
                    ticket_pego = False  # Reseta o estado do ticket
                    tentativas_quiz = 0  # Reseta o contador de tentativas
                    # Reseta a posição do personagem para a posição inicial
                    personagem.x = PERSONAGEM_X
                    personagem.y = PERSONAGEM_Y
                    personagem.rect.topleft = (personagem.x, personagem.y)

        pygame.display.flip()  # Atualiza a tela
        clock.tick(60)

# Função para exibir a tela inicial
def tela_inicio(recursos):
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    while True:
        tela.blit(recursos['background_inicio'], (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo(recursos)

# Inicialização do Pygame e execução do jogo
pygame.init()
recursos = carregar_recursos()
tela_inicio(recursos)