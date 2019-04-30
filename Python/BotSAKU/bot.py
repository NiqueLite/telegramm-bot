import telebot

bot = telebot.TeleBot("696784173:AAEL2r-0y_qaYAoYLq7bv6hVlJFZJ-pvKCA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Я бот который создан для\nСАКУ - Секты Анархо-Коммунистов Украины.\nТы можешь запросить у меня ссылку для подключения к САКУ, а так же правила.")

	bot.send_message(message.chat.id, "Команды:\n/rules (Просмотр правил)\n/chat (Получение ссылки на чат САКУ)")

@bot.message_handler(commands=['rules'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Правила:\n1. Всё добровольно.\nНикто не может Вами управлять.\n2. Администрация может давать советы,\nно это Ваше дело выполнять их или нет.\n3. Если кто-то решит пойти против системы, \nто группа админов может вынести вердикт.\nВсе нарушения - этические нормы)")

@bot.message_handler(commands=['chat'])
def send_welcome(message):
	bot.send_message(message.chat.id, "https://t.me/AnarchistSAKU")

bot.polling( none_stop = True)
