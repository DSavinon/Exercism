class BlackJack:

    def __init__(self) -> None:
        pass

    def value_of_card(self, card: str) -> int:
        """Le asignamos un valor a cada carta

        Args:
            card (str): [Valor str de la carta]

        Returns:
            int: [Valor int de la carta]
        """
        if card == 'K' or card == 'Q' or card == 'J' or card == '10':
            return 10
        elif card == '9':
            return 9
        elif card == '8':
            return 8
        elif card == '7':
            return 7
        elif card == '6':
            return 6
        elif card == '5':
            return 5
        elif card == '4':
            return 4
        elif card == '3':
            return 3
        elif card == '2':
            return 2
        elif card == '1' or card == 'A':
            return 1
    
    def higher_card(self, card_one: str, card_two: str) -> int or tuple:
        """Calculamos cual es la carta mayor entre dos cartas

        Args:
            card_one (str): [Valor str de la primera carta]
            card_two (str): [Valor str de la segunda carta]

        Returns:
            int or tuple: [Regresamos el valor Int de la carta mas alta o un Tuple con el valor de ambas cartas en caso de ser iguales]
        """
        x = self.value_of_card(card_one)
        y = self.value_of_card(card_two) 
        if x > y:
            return card_one
        elif x == y:
            return card_one, card_two
        return card_two

bj = BlackJack()
print(bj.higher_card('1', 'A'))