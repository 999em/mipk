import telebot;
bot = telebot.TeleBot('%токен%');
photo = open('Путь к фото', 'rb')
bot.send_message(call.message.chat.id, text=text1, photo=photo,reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def send_welcome(message):
if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
	bot.polling(none_stop=True, interval=0)


from telebot import types
name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши');

def get_name(message): #задаем вопрос о месте
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Куда бы ты хотел пойти?');
    bot.register_next_step_handler(message, get_surnme);
	
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Сколько мест тебе интересно?');
    bot.register_next_step_handler(message, get_age);
	def get_age(message):
    global age;
    while age == 0: #проверяем ответ
        try:
             age = int(message.text) #проверяем, что количество введено корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Напиши, пожалуйста, число');
      keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
      keyboard.add(key_no);
      question = 'Тебя зовут '+name+', тебе интересенно'+surname+'?' мест"';
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
	  @bot.callback_query_handler(func=lambda call: True)
	  
if message.text == "1":
    bot.send_message(message.from_user.id, "Я могу посоветовать тебе "Царицыно, с прекрасными видами!")
elif message.text == "Напиши цифру еще раз":
    if message.text == "2":
    bot.send_message(message.from_user.id, "Я могу посоветовать тебе "Царицыно и ВДНХ, с прекрасными видами, но в разных частях города!")
elif message.text == "Напиши цифру еще раз":
	
	
	
	def get_name_2(message): #задаем вопрос о месте
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'После прогулки надо поесть. Куда бы ты хотел пойти?');
    bot.register_next_step_handler(message, get_surnme);
	
def get_surname_2(message):
    global surname;
    surname = message.text;
    bot.send_message('Сколько мест тебе хочется посетить сегодня?');
    bot.register_next_step_handler(message, get_age_2);
	def get_age_2(message):
    global age;
    while age == 0: #проверяем ответ
        try:
             age = int(message.text) #проверяем, что количество введено корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Напиши, пожалуйста, число');
      keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
      keyboard.add(key_no);
      question = 'Тебя зовут '+name_2+', тебе интересенно'+surname_2+'?' мест"';
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
	  @bot.callback_query_handler(func=lambda call: True)
	  
	  
if message.text == "1":
    bot.send_message(message.from_user.id, "Я могу посоветовать тебе "Две палочки, с кухнями Азии!")
elif message.text == "Напиши цифру еще раз":
    if message.text == "2":
    bot.send_message(message.from_user.id, "Я могу посоветовать тебе "Две палочки и Hite, с кухнями Азии!")
elif message.text == "Напиши цифру еще раз":
	
	
	
	
	
	
	