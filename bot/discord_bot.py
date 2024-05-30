import discord

TOKEN = 'MTI0MzU5Mzg2MjI0MTQ1MjA1Mg.Grmwu1.ZmvpT_VVxLExGSefKWh4cesM0o3bOMzIb0DGZA'

init_message = 'Hello! I am RestaBot. Ask me any question you may have related to finding restaurants or knowing their food.'

class DiscordBot:
    def __init__(self, bot):
        intents = discord.Intents.default()
        intents.message_content = True
        self.client = discord.Client(intents=intents)
        self.bot = bot

        @self.client.event
        async def on_ready():
            await self.client.get_channel(1243594396495249483).send(init_message)
            await self.client.get_channel(1244011664789995561).send(init_message)

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            
            await message.channel.send(self.bot.routine(message))

    def run(self):
        self.client.run(TOKEN)