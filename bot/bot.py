#!/usr/bin/env python
from django.core.management.utils import get_random_secret_key
import requests
import logging
from data.config import BOT_TOKEN, ADDRES
from telegram import ForceReply, Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ApplicationBuilder, AIORateLimiter
from telegram.constants import ParseMode, ChatAction

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def save_user(message) -> int(): # type: ignore
    post_data = {"username": str(message.from_user.id),
                 "first_name": str(message.from_user.first_name),
                 "last_name": str(message.from_user.last_name),
                 "password": str(get_random_secret_key())}
    url = f"{ADDRES}api/register/"
    response = requests.post(url, data=post_data)
    return response


def activate_user(id):
    post_data = {"username": str(id)}
    url = f"{ADDRES}api/register/activate-user/"
    response = requests.post(url, data=post_data)
    return response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usr = save_user(update.message)
    if usr.status_code == 201:
        user = update.effective_user
        await update.message.reply_html(
            rf"Salom NoxonFx Botiga Xush Kelibsiz {user.mention_html()}!")
    else:
        await update.message.reply_html(
            rf"Ushbu Hisob Oldin yaratilgan!")


async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usr = activate_user(update.message.from_user.id)
    if usr.status_code == 200:
        await update.message.reply_text(f"<b>Kod:</b> {usr.text}", parse_mode=ParseMode.HTML)
    elif usr.status_code == 400:
        await update.message.reply_text(f"<b>Xatolik:</b> Serverda So'rovlar Soni Oshib Ketti", parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text("<b>Xolat:</b> siz to'lov qilmagansiz!", parse_mode=ParseMode.HTML)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Kirish kodini olish uchun /login ni bosing!")


async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/start", "Boshlash"),
        BotCommand("/login", "Kirish"),
        BotCommand("/help", "Yordam xabarini ko'rsatish"),
    ])


def main() -> None:
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .concurrent_updates(True)
        .rate_limiter(AIORateLimiter(max_retries=10))
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("login", login_command))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
