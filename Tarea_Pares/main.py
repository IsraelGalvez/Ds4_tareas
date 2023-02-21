import random
from collections import Counter
from art import logo

cards = { "espada": [11,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "diamante": [11,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "corazon": [11,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "trebol": [11,2,3,4,5,6,7,8,9,10,"J","Q","K"],
        }

def get_random_cards(all_cards, five_cards):
    list_espadas = []
    list_diamantes = []
    list_corazones = []
    list_treboles = [] 
    for num in range(0,5):
        # En la primera variable obtiene un tipo de carta de las cuatro -->
        # existentes, esto de manera aleatoria. El valor obtenido es el key del diccionario.
        type_of_card = random.choice(list(all_cards))
        # Se obtiene un valor de la lista de cartas de manera aleatoria. La lista se obtiene
        # de el del value del diccionario.
        value_of_card = random.choice(list(all_cards[type_of_card]))
        if type_of_card == "espada":
            list_espadas.append(value_of_card)
            five_cards[type_of_card] = list_espadas
        elif type_of_card == "diamante":
            list_diamantes.append(value_of_card)
            five_cards[type_of_card] = list_diamantes
        elif type_of_card == "corazon":
            list_corazones.append(value_of_card)
            five_cards[type_of_card] = list_corazones
        elif type_of_card == "trebol":
            list_treboles.append(value_of_card)
            five_cards[type_of_card] = list_treboles
        value_of_dictionary = all_cards[type_of_card]
        value_card_index = value_of_dictionary.index(value_of_card)
        value_of_dictionary.pop(value_card_index)
        # Como la lista disminuyó luego de elegir una carta, cambio el value del diccionario
        # de esta manera una carta no será elegida dos veces
        all_cards[type_of_card] = value_of_dictionary
    return five_cards

# El parámetro five_cards se refiere al diccionario con 5 cartas del usuario o computadora
def sum_cards(five_cards):
    list_of_type_of_cards = list(five_cards.keys())
    list_of_list = []
    score = 0
    list_of_cards_num = []

    for type in list_of_type_of_cards:
        list_of_list.append(five_cards[type])
    
    for sublist in list_of_list:
        for item in sublist:
            list_of_cards_num.append(item)

    score = even_third_full(list_of_cards_num)
    return score

def even_third_full(list_of_cards_num):
    score = 0
    # La clase Counter me entrega un diccionario con los items de una
    # lista y me dice cuantas veces se repitieron
    count = Counter(list_of_cards_num)
    result = {}

    for clave in count:  
        valor = count[clave]
        result[clave] = valor
    
    for key in result:
        if key == "J" or key == "Q" or key == "K":
            score += 10 * result[key] * result[key]
        else:
            score += key * result[key] * result[key]
    return score

def winner(user_score, computer_score):
    if user_score > computer_score:
        print(f"User wins!!!! The score was {user_score} and the computer score {computer_score}.")
    elif user_score == computer_score:
        print(f"The was result was a draw, score was {user_score}")
    else:
        print(f"Computer wins :( The score was {computer_score} and user score {user_score}")

def main():
    user_cards = get_random_cards(cards, {})
    computer_cards = get_random_cards(cards, {})
    print(f"{logo} \n")
    print(f"User cards \n{user_cards} \n")
    print(f"Computer cards \n{computer_cards} \n")
    score_user = sum_cards(user_cards)
    score_computer = sum_cards(computer_cards)
    winner(score_user, score_computer)

main()