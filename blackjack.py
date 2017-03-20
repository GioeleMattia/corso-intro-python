from random import randint

class Blackjack:
    def __init__(self, mode = "40"):
        suites = ['clubs', 'spades', 'hearts','diamonds']
        values = range(2,12)

        cards = list()
        if mode == "40":
            for s in suites:
                for v in values:
                    cards.append((s, v))

        else:
            raise NotImplementedError    

        self.cards = cards

    def delta_cards(self, clist):
        sum = self.sum_cards(clist)    
        return 21 - sum        

    def pop_card(self):
        card = self.cards.pop(randint(0, len(self.cards)-1))
        return card

    def sum_cards(self, clist):
        sum = 0
        for c in clist:
            sum += c[1]
        return sum

    def ask_next(self, clist, courage): 
        #courage: 1,2,3 #increasing
        delta = self.delta_cards(clist)
        if delta < 6 and courage == 1:
            return True
        elif delta < 4 and courage == 2:
            return True
        elif  delta < 2 and courage == 3:
            return True
         

if __name__ == '__main__':
    b = Blackjack()

    print "Disponibili %s carte" % len(b.cards)
    
    again, again_ccounter = True, True
    user_cards = []
    while again:   
        c = b.pop_card()
        user_cards.append(c)
        print "Hai tirato su %s di %s" % (c[1], c[0])
        resp = raw_input("Vuoi continuare? [s/n]")
        if resp == "n" or b.sum_cards(user_cards) >= 21:
            again = False

    user_sum = b.sum_cards(user_cards)
    print "Hai ottenuto %s" % user_sum

    ccounter_cards = []

    while again_ccounter:
        c = b.pop_card()
        print c
        ccounter_cards.append(c)
        if b.ask_next(ccounter_cards,1) or b.sum_cards(ccounter_cards) >= 21:
            again_ccounter = False

    ccounter_sum = b.sum_cards(ccounter_cards)
    print "Il banco ha ottenuto %s" % ccounter_sum

    if user_sum > 21:
        print "Hai perso"
    elif ccounter_sum > 21:
        print  "Hai vinto"
    elif ccounter_sum > user_sum:
        print "Hai perso"
    else:
        print "Hai vinto"

