from random import Random

from maubot import Plugin, MessageEvent
from maubot.handlers import command
from more_itertools import intersperse


class MockBot(Plugin):
    async def message_or_reply(self, evt, message):
        if evt.content.get_reply_to():
            reply_evt = await self.client.get_event(evt.room_id, evt.content.get_reply_to())
            return reply_evt.content.body
        else:
            return message

    @command.new("random")
    @command.argument("message", pass_raw=True)
    async def random(self, evt: MessageEvent, message: str) -> None:
        message = await self.message_or_reply(evt, message)
        rand = Random()
        rand.seed(message)
        result = "".join([rand.choice((c.upper(), c.lower())) for c in message])
        await evt.reply(result)

    @command.new("alternate")
    @command.argument("message", pass_raw=True)
    async def alternate(self, evt: MessageEvent, message: str) -> None:
        message = await self.message_or_reply(evt, message)
        result = "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(message)])
        await evt.reply(result)

    @command.new("strike")
    @command.argument("message", pass_raw=True)
    async def strike(self, evt: MessageEvent, message: str) -> None:
        message = await self.message_or_reply(evt, message)
        result = "\u0336".join(intersperse("\u0336", message)) + "\u0336"
        await evt.reply(result)

    @command.new("pray")
    @command.argument("message", pass_raw=True)
    async def pray(self, evt: MessageEvent, message: str) -> None:
        message = await self.message_or_reply(evt, message)
        result = "".join(intersperse(" 🙏 ", message.split(" ")))
        await evt.reply(result)

    @command.new("clap")
    @command.argument("message", pass_raw=True)
    async def clap(self, evt: MessageEvent, message: str) -> None:
        message = await self.message_or_reply(evt, message)
        result = "".join(intersperse(" 👏 ", message.split(" ")))
        await evt.reply(result)
