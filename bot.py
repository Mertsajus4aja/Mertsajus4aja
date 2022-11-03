import telebot
import random
from telebot import types
from telebot import types
answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
PHOTO_PATH = '1.png'
bot = telebot.TeleBot('5796599612:AAGYa4GEcHcNEbPFWay4hD2mD-tc6jZf0Bo')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #bot.send_audio(message.from_user.id, audio=open('1.mp3', 'rb'))
    if message.text == "/start":
        bot.send_audio(message.from_user.id, audio=open('1.mp3', 'rb'))
        bot.send_photo(message.from_user.id, photo=open(PHOTO_PATH, 'rb'))
        bot.send_message(message.from_user.id,
                         'Привет я Чупакабра, твоя личная фигня, предсказывающая погоду, зарплату, падение метеорита, лежбища морских котиков и прочее. Спрашивай что знать хочешь, кстати если я тупить начала нажми /start')
        #.025bot.send_photo(message.from_user.id, photo=open('2.png', 'rb'))
    else:
        bot.send_message(message.from_user.id, random.choice(answers))
        bot.polling(none_stop=True, interval=0)


bot.polling(none_stop=True, interval=0)

