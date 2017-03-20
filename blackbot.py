from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from blackjack import Blackjack

TOKEN = "371081553:AAHPGVIQ7bzRB7A-0DSrzkE4gqErSYLNczk"

messages = []

def start(bot, update):    
    update.message.reply_text("Iniziamo a giocare! /nuova per iniziare")

def start_game(bot, update):
    global bjack
    bjack = Blackjack()
    c = bjack.pop_card()
    global user_cards
    user_cards = [c]
    update.message.reply_text("Hai tirato su %s" % str(c))
    update.message.reply_text("Vuoi contuinuare?")

def controller(bot, update):
    msg = update.message.text
    messages.append(dict(user=update.message.from_user.id,
                         chat=update.message.chat_id ,                   
                         msg=update.message.text))

    if msg not in ["s", "n"]:
        update.message.reply_text("Puoi rispondermi solo s o n")

    elif msg == "s":
        c = bjack.pop_card()
        global user_cards
        user_cards.append(c)
        update.message.reply_text("Hai tirato su %s" % str(c))
        update.message.reply_text("Disponibili %s carte" % len(bjack.cards))
        update.message.reply_text("Vuoi contuinuare?")

    else:
        user_sum = bjack.sum_cards(user_cards)
        update.message.reply_text("Hai ottenuto %s" % user_sum)
        ccounter_cards = []
        again_ccounter = True
        while again_ccounter:
            import pdb; pdb.set_trace()
            c = bjack.pop_card()
            update.message.reply_text("Il banco ha tirato su %s" % str(c))
            ccounter_cards.append(c)
            ccounter_sum = bjack.sum_cards(ccounter_cards)
            if not bjack.ask_next(ccounter_cards,randint(1,4)) or ccounter_sum >= 21:
                again_ccounter = False


        update.message.reply_text("Il banco ha ottenuto %s" % ccounter_sum)

        winner = bjack.get_winner(user_sum, ccounter_sum)
        update.message.reply_text("Vince %s (1: giocatore, 2:banco)" % winner)
        
        print messages
    

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("nuova", start_game))

    dp.add_handler(MessageHandler(Filters.text, controller))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
