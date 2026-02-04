from typing import Any, Dict
from app.services.connectors.base import Connector

class TelegramConnector(Connector):
    """Telegram connector stub.

    Replace this with real API calls, rate limits, retries, logging, etc.
    """

    def meta(self) -> Dict[str, Any]:
        return {"network": "telegram", "implemented": False}

    def post(self, channel: str, content: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: implement real posting
        return {"ok": True, "stub": True, "network": "telegram", "channel": channel, "content": content}
