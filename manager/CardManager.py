import pickle

class CardManager:
    def __init__(self, card_list):
        self.card_list = card_list

    # should be done with db
    def check_card_number(self, card_number):
        for card in self.card_list:
            if card_number == card.number:
                return card

        return None