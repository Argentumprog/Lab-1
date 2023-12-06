import telebot
from telebot import types

bot=telebot.TeleBot('6600805630:AAG2RRdEIcnsGJSDSNO8ixH9WPqXLZimo3k')

user_answers = {}
questions = [
    "Какого цвета должна быть шерсть котика?",
    "Какое имя лучше всего подходит для котика?",
    "Какое хобби у котика?",
    "Какой характер у котика?",
    "Какую игрушку предпочитает котик?",
]

options = [
    ["Серый", "Рыжий", "Черный"],
    ["Барсик", "Мурзик", "Леопольд"],
    ["Лазание по деревьям", "Чтение книг", "Лежание на солнышке"],
    ["Спокойный", "Игривый", "Независимый"],
    ["Мяч", "Мышь", "Веревочка"],
]

current_question = 0

@bot.message_handler(commands=['start'])
def start(message):
    global current_question
    current_question = 0
    user_answers.clear()
    bot.send_message(message.chat.id, "Привет! Давай поиграем в игру 'Какой ты котик?'")
    send_question(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    global current_question
    user_answers[current_question + 1] = call.data
    current_question += 1

    if current_question < len(questions):
        send_question(call.message.chat.id)
    else:
        show_results(call.message.chat.id)

def send_question(chat_id):
    question_text = questions[current_question]
    options_list = options[current_question]

    markup = types.InlineKeyboardMarkup()
    for option in options_list:
        markup.add(types.InlineKeyboardButton(text=option, callback_data=option))

    bot.send_message(chat_id, question_text, reply_markup=markup)

def show_results(chat_id):
    result_text = "Итоги опроса:\n"
    for question_number, answer in user_answers.items():
        result_text += f"{questions[question_number - 1]}\nОтвет: {answer}\n\n"

    cat_types = {
        "Серый": "Серый котик",
        "Рыжий": "Рыжий котик",
        "Черный": "Черный котик",
        "Барсик": "Котик по имени Барсик",
        "Мурзик": "Котик по имени Мурзик",
        "Леопольд": "Котик по имени Леопольд",
        "Лазание по деревьям": "Котик-лазающий",
        "Чтение книг": "Котик-книжник",
        "Лежание на солнышке": "Котик-лежачий",
        "Спокойный": "Спокойный котик",
        "Игривый": "Игривый котик",
        "Независимый": "Независимый котик",
        "Мяч": "Котик, любящий играть с мячом",
        "Мышь": "Котик, охотящийся на мышей",
        "Веревочка": "Котик с веревочкой",
    }

    cat_type = cat_types.get(user_answers[5], "Котик")

    result_text += f"Ваш котик: {cat_type}"

    bot.send_message(chat_id, result_text)

if __name__ == "__main__":
    bot.infinity_polling()
