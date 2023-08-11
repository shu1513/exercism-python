class Luhn:
    def __init__(self, card_num):
        card_num_new = "".join(card_num.split())
        self.card_num_new = card_num_new


    def valid(self):
        if  len(self.card_num_new) < 2 or not self.card_num_new.isdigit():
                return False
