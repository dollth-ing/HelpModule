from maubot import Plugin, MessageEvent
from maubot.handlers import command

class HelpInfo(Plugin):
  @command.new()
  async def help(self, evt: MessageEvent) -> None:
    await evt.reply("Faggot!")