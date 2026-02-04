from app.services.connectors.telegram.connector import TelegramConnector
from app.services.connectors.discord.connector import DiscordConnector
from app.services.connectors.reddit.connector import RedditConnector
from app.services.connectors.x.connector import XConnector

connector_registry = {
    "telegram": TelegramConnector,
    "discord": DiscordConnector,
    "reddit": RedditConnector,
    "x": XConnector,
}
