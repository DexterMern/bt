from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# توکن ربات خود را اینجا قرار دهید
TOKEN = "6787509715:AAH2M_RMj7Gj0Fd1tE8UuMXLoXktwV3wEtI"
# ایدی گروه تلگرام
GROUP_CHAT_ID = 5625040520  # عدد ایدی گروه خود را جایگزین کنید

# دیکشنری برای ذخیره پیام‌ها
user_messages = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("به ربات خوش آمدید! از دستور /help برای راهنما استفاده کنید.")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("راهنمای استفاده از ربات:\n"
                              "/start - دریافت خوش آمدگویی\n"
                              "/help - نمایش راهنما\n"
                              "/message - ارسال پیام به ادمین\n"
                              "/order - ثبت سفارش برنامه نویسی")

def message_or_order(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("لطفاً یک پیام بنویسید.")

def handle_user_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message = update.message.text

    if user_message:
        # ارسال پیام به گروه یا ادمین
        user_link = f"https://t.me/{update.message.from_user.username}"
        message_to_admin = f"پیام جدید از کاربر {user_link}:\n\n{user_message}"
        context.bot.send_message(chat_id=GROUP_CHAT_ID, text=message_to_admin)

        # ارسال پیام به کاربر
        update.message.reply_text("پیام شما ارسال شد و به زودی با شما تماس می‌گیریم.")
    else:
        update.message.reply_text("پیام شما خالی است. لطفاً یک پیام متنی ارسال کنید.")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    
    # اضافه کردن هندلر برای درخواست /message و /order
    dp.add_handler(CommandHandler("message", message_or_order))
    dp.add_handler(CommandHandler("order", message_or_order))

    # اضافه کردن هندلر برای پیام‌های متنی
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_user_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
