# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm


# import telebot
# import webbrowser
# bot = telebot.TeleBot('6031176695:AAHyJzqvedBKwxtHzL1SbWOqd71hhHNzA6A')
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Hello !, {message.from_user.first_name}')
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://itproger.com')
#
#
# if __name__ == '__main__':
#     bot.polling(none_stop=True)

# import telebot
# from telebot import types
#
# botTimeWeb = telebot.TeleBot('6499593666:AAHwVet3Hau60j1w0Kfu-eELftMaK_kCVLc')
#
#
# @botTimeWeb.message_handler(commands=['start'])
# def startBot(message):
#     first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь расскажу про present simple?"
#     markup = types.InlineKeyboardMarkup()
#     button_yes = types.InlineKeyboardButton(text='Давай', callback_data='yes')
#     markup.add(button_yes)
#     button_why = types.InlineKeyboardButton(text='потом', callback_data='why')
#     markup.add(button_why)
#     button_no = types.InlineKeyboardButton(text='нет не надо', callback_data='no')
#     markup.add(button_no)
#     botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
#
#
# @botTimeWeb.callback_query_handler(func=lambda call: True)
# def response(function_call):
#     if function_call.message:
#         if function_call.data == "yes":
#             second_mess = "круто !!!"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://youtu.be/6Qd1xAikoQc"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#         elif function_call.data == 'why':
#             second_mess = "чтож ок)"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Тормоз", url="https://avtokafe.ru/tormoza/"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#         elif function_call.data == 'no':
#             second_mess = "[хорошо!"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Можешь нажать", url="https://www.youtube.com/watch?v=G2huGX6z-RU"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#
#
# botTimeWeb.infinity_polling()


import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6499593666:AAHwVet3Hau60j1w0Kfu-eELftMaK_kCVLc')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = (f"<b>{message.from_user.first_name}</b>,  привет!\n  хочешь изучать иностранные языки?"
                  f"я Сама изучала с помошью них так что советую и тебе :) ")
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    button_why = types.InlineKeyboardButton(text='потом', callback_data='why')
    markup.add(button_why)

    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "круто !!!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Английский язык ", url="https://youtu.be/jMCOyUgKhqU"))
            markup.add(types.InlineKeyboardButton("Кыргызский язык", url="https://youtu.be/d0EYxU9G1Gg"))
            markup.add(types.InlineKeyboardButton("Арабский язык", url="https://youtu.be/f9dFflIP16c"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'why':
            second_mess = "чтож ок)"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Тормоз", url="https://avtokafe.ru/tormoza/"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)



botTimeWeb.infinity_polling()