import telebot
from telebot import types

BOT_TOKEN = '8762401039:AAGTNYhQBHgzIH8Dtr6POQ7VRlc3QE1G0SM'
ADMIN_ID = '193166316' 

bot = telebot.TeleBot(BOT_TOKEN)
user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    welcome_text = (
        "Приветствую! 🤝 Я — ИИ-консультант команды Владимира Ручкина, официального партнера платформы UDS.\n\n"
        "Мы помогаем селлерам маркетплейсов выстраивать легальные, прямые коммуникации "
        "с покупателями, увеличивать повторные продажи и защищать маржинальность бизнеса в рамках правил "
        "торговых платформ.\n\n"
        "Давайте за 1 минуту определим точки роста для вашего бренда. Какой у вас основной канал продаж?"
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Только Wildberries")
    btn2 = types.KeyboardButton("Только Ozon")
    btn3 = types.KeyboardButton("Wildberries + Ozon")
    btn4 = types.KeyboardButton("Свой интернет-магазин / Сайт")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(chat_id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Только Wildberries", "Свой интернет-магазин / Сайт"])
def handle_wb_or_site_sellers(message):
    chat_id = message.chat.id
    user_data[chat_id]['platform'] = message.text
    
    presentation_text = (
        "🎯 Отличный выбор. Работа на маркетплейсах сейчас требует жесткого контроля расходов, ведь комиссии и логистика постоянно растут.\n\n"
        "Посмотрите короткую видео-презентацию (около 20 минут), в которой подробно разобрана новая модель продаж, "
        "инструменты увеличения прибыли и механика создания собственной клиентской базы без риска блокировок:\n\n"
        "👉 Ссылка на видео: https://youtu.be/cujG178EMwg?is=IyFJw19m_I2__OBk\n\n"
        "После просмотра нажмите кнопку ниже, чтобы связаться со мной лично и обсудить потенциал для вашего магазина."
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_next = types.KeyboardButton("🚀 Хочу audit и разбор бизнеса")
    markup.add(btn_next)
    bot.send_message(chat_id, presentation_text, reply_markup=markup, disable_web_page_preview=False)

@bot.message_handler(func=lambda message: message.text == "Только Ozon")
def handle_ozon_seller(message):
    chat_id = message.chat.id
    user_data[chat_id]['platform'] = message.text
    
    presentation_text = (
        "🎯 Принято. Для селлеров Ozon сейчас открыты уникальные технологические возможности.\n\n"
        "Посмотрите эту специальную видео-презентацию. В ней детально показано, как работает официальная интеграция "
        "UDS x Ozon Доставка, как продавать товары напрямую клиентам через привычные ПВЗ и при этом полностью "
        "освободить свой бизнес от торговых комиссий маркетплейса:\n\n"
        "👉 Ссылка на видео: https://youtu.be/XRnaIY40t4Y?is=WTUrkOGxhUBrmtON\n\n"
        "После просмотра нажмите кнопку ниже, чтобы связаться со мной для детального разбора."
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_next = types.KeyboardButton("🚀 Хочу audit и разбор бизнеса")
    markup.add(btn_next)
    bot.send_message(chat_id, presentation_text, reply_markup=markup, disable_web_page_preview=False)

@bot.message_handler(func=lambda message: message.text == "Wildberries + Ozon")
def handle_multi_seller(message):
    chat_id = message.chat.id
    user_data[chat_id]['platform'] = message.text
    
    presentation_text = (
        "🎯 Сильное решение! Работа на двух крупнейших маркетплейсах одновременно дает огромный охват, "
        "но кратно увеличивает расходы на комиссии и удержание клиентов.\n\n"
        "Поскольку вы развиваете мультиплатформенные продажи, для вас актуальны сразу оба наших решения. "
        "Изучите эти материалы:\n\n"
        "1️⃣ Разбор модели продаж и создание базы для Wildberries:\n"
        "👉 Ссылка: https://youtu.be/cujG178EMwg?is=IyFJw19m_I2__OBk\n\n"
        "2️⃣ Работа с интеграцией UDS x Ozon Доставка без комиссий:\n"
        "👉 Ссылка: https://youtu.be/XRnaIY40t4Y?is=WTUrkOGxhUBrmtON\n\n"
        "После ознакомления нажмите кнопку ниже. Мы проведем комплексный аудит ваших каналов продаж."
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_next = types.KeyboardButton("🚀 Хочу audit и разбор бизнеса")
    markup.add(btn_next)
    bot.send_message(chat_id, presentation_text, reply_markup=markup, disable_web_page_preview=False)

@bot.message_handler(func=lambda message: message.text == "🚀 Хочу audit и разбор бизнеса")
def request_contact(message):
    chat_id = message.chat.id
    
    lead_text = (
        "Прекрасно! Самый эффективный способ примерить эту систему на ваш бизнес — короткий 15-минутный онлайн-разбор.\n\n"
        "Я лично подключусь к вам, покажу изнутри интерфейс системы, продемонстрирую инструменты и рассчитаю "
        "экономику сохранения маржи именно для вашего бренда.\n\n"
        "Нажмите кнопку ниже, чтобы поделиться контактом. Я свяжусь с вами для выбора удобного времени!"
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_phone = types.KeyboardButton("📱 Отправить контактные данные", request_contact=True)
    markup.add(btn_phone)
    bot.send_message(chat_id, lead_text, reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    chat_id = message.chat.id
    contact = message.contact
    
    user_info = user_data.get(chat_id, {})
    platform = user_info.get('platform', 'Не указана')
    
    thanks_text = (
        "Спасибо! Ваши данные успешно приняты. 👍\n\n"
        "Я уже получил уведомление и свяжусь с вами в ближайшее время здесь, в Telegram. Хорошего дня!"
    )
    bot.send_message(chat_id, thanks_text, reply_markup=types.ReplyKeyboardRemove())
    
    admin_notification = (
        "🔥 **У вас новый горячий лид на UDS!** 🔥\n\n"
        f"👤 **Имя:** {contact.first_name} {contact.last_name or ''}\n"
        f"📞 **Телефон:** +{contact.phone_number}\n"
        f"✈️ **Telegram:** @{message.from_user.username or 'скрыт'}\n"
        f"🏪 **Направление:** {platform}"
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_notification, parse_mode="Markdown")
    except Exception as e:
        print(f"Ошибка отправки уведомления админу: {e}")

if __name__ == '__main__':
    bot.infinity_polling()
