```python
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
        "Мы помогаем B2C-предпринимателям и селлерам маркетплейсов выстраивать легальные, прямые коммуникации "
        "с покупателями, увеличивать повторные продажи и защищать маржинальность бизнеса в рамках правил "
        "торговых платформ.\n\n"
        "Давайте за 1 минуту определим точки роста для вашего бренда. Какой у вас основной канал продаж?"
    )
    
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Wildberries / Ozon")
    btn2 = types.KeyboardButton("Розничный магазин / Сеть")
    btn3 = types.KeyboardButton("Сфера услуг / Общепит")
    btn4 = types.KeyboardButton("Смешанный формат (Маркетплейс + Розница)")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(chat_id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [
    "Wildberries / Ozon", "Розничный магазин / Сеть", "Сфера услуг / Общепит", "Смешанный формат (Маркетплейс + Розница)"
])
def handle_channel(message):
    chat_id = message.chat.id
    user_data[chat_id]['channel'] = message.text
    
    ask_scale_text = "Принято! Чтобы подобрать релевантный кейс, укажите примерный масштаб вашего бизнеса:"
    
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if message.text in ["Wildberries / Ozon", "Смешанный формат (Маркетплейс + Розница)"]:
        btn1 = types.KeyboardButton("До 500 заказов в месяц")
        btn2 = types.KeyboardButton("500 - 2000 заказов в месяц")
        btn3 = types.KeyboardButton("Более 2000 заказов в месяц")
    else:
        btn1 = types.KeyboardButton("1-2 филиала (точки)")
        btn2 = types.KeyboardButton("3-5 филиалов")
        btn3 = types.KeyboardButton("Крупная сеть (от 5 точек)")
        
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, ask_scale_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [
    "До 500 заказов в месяц", "500 - 2000 заказов в месяц", "Более 2000 заказов в месяц",
    "1-2 филиала (точки)", "3-5 филиалов", "Крупная сеть (от 5 точек)"
])
def handle_scale(message):
    chat_id = message.chat.id
    user_data[chat_id]['scale'] = message.text
    channel = user_data[chat_id].get('channel', '')
    
    if channel in ["Wildberries / Ozon", "Смешанный формат (Маркетплейс + Розница)"]:
        presentation_text = (
            "🎯 Отличная ниша, но сейчас маркетплейсы диктуют жесткие условия по комиссиям.\n\n"
            "**Как работает интеграция UDS x Ozon Доставка для вашей защиты:**\n"
            "Вы создаете собственный брендированный интернет-магазин, используя официальные, "
            "разрешенные регламентами методы омниканального маркетинга. Покупатели заказывают "
            "напрямую у вас и получают товары через привычные пункты выдачи (ПВЗ Ozon), но вы при этом "
            "**НЕ платите комиссию за продажу маркетплейсу**, а клиентская база и контакты остаются у вас.\n\n"
            "Хотите получить расчет потенциала чистой прибыли и снижения зависимости от платформ для вашего магазина?"
        )
    else:
        presentation_text = (
            "🎯 Понятно. В рознице и услугах сейчас идет жесткая борьба за каждого клиента, а реклама дорожает.\n\n"
            "**Что дает внедрение UDS:**\n"
            "Оцифровка 100% входящего трафика, автоматический сбор клиентской базы, умная программа лояльности "
            "с кэшбэком вместо прямых скидок (которые режут прибыль) и встроенная реферальная система.\n\n"
            "Хотите посмотреть готовые кейсы окупаемости UDS в вашей нише за 2 месяца?"
        )
        
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_yes = types.KeyboardButton("🚀 Да, хочу получить аудит и кейсы")
    markup.add(btn_yes)
    bot.send_message(chat_id, presentation_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🚀 Да, хочу получить аудит и кейсы")
def request_contact(message):
    chat_id = message.chat.id
    
    lead_text = (
        "Прекрасно! Самый эффективный способ примерить эту систему на ваш бизнес — короткий 15-минутный онлайн-разбор.\n\n"
        "Владимир Ручкин (официальный партнер UDS и эксперт по автоматизации продаж) лично подключится "
        "к вам, покажет изнутри интерфейс CRM-системы, продемонстрирует инструменты и рассчитает экономику "
        "для вашего бренда.\n\n"
        "Нажмите кнопку ниже, чтобы поделиться контактом. Владимир свяжется с вами для выбора удобного времени!"
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
    channel = user_info.get('channel', 'Не указан')
    scale = user_info.get('scale', 'Не указан')
    
    thanks_text = (
        "Спасибо! Ваши данные успешно приняты. 👍\n\n"
        "Владимир уже получил уведомление и свяжется с вами в ближайшее время здесь, в Telegram. Хорошего дня!"
    )
    bot.send_message(chat_id, thanks_text, reply_markup=types.ReplyKeyboardRemove())
    
    admin_notification = (
        "🔥 **У вас новый горячий лид на UDS!** 🔥\n\n"
        f"👤 **Имя:** {contact.first_name} {contact.last_name or ''}\n"
        f"📞 **Телефон:** +{contact.phone_number}\n"
        f"✈️ **Telegram:** @{message.from_user.username or 'скрыт'}\n"
        f"🏪 **Канал продаж:** {channel}\n"
        f"📊 **Масштаб бизнеса:** {scale}"
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_notification, parse_mode="Markdown")
    except Exception as e:
        print(f"Ошибка отправки уведомления админу: {e}")

if __name__ == '__main__':
    bot.infinity_polling()
