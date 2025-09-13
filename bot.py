from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import config  # ← فایل تنظیمات

BOT_TOKEN = "8149206600:AAGtx-bzUoU_yqkGWuOv3cEYf6_RogkIVAw"

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(config.WELCOME_MESSAGE)

# دستور /whoami
async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    if username:
        await update.message.reply_text(config.WHOAMI_MESSAGE.format(username=username))
    else:
        await update.message.reply_text("شما یوزرنیم ندارید.")

if __name__ == "__main__":
    # ساخت اپلیکیشن
    app = Application.builder().token(BOT_TOKEN).build()

    # افزودن دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("whoami", whoami))

    print("ربات روشن شد ✅")
    app.run_polling()

