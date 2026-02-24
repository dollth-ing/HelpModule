from maubot import Plugin

class HelpInfo(Plugin):
    @command.new()
  async def hello_world(self, evt: MessageEvent) -> None:
    await evt.reply("Hello, World!")