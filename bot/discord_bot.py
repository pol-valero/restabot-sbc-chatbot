import discord

TOKEN = 'MTI0MzU5Mzg2MjI0MTQ1MjA1Mg.Grmwu1.ZmvpT_VVxLExGSefKWh4cesM0o3bOMzIb0DGZA'

class DiscordBot:
    def __init__(self, bot, dataLoader):
        intents = discord.Intents.default()
        intents.message_content = True
        self.client = discord.Client(intents=intents)
        self.bot = bot
        self.dataLoader = dataLoader
        self.listOfCities = dataLoader.getOriginalUniqueCityNames()

        auxString = ("\n\nHello! I am RestaBot. Ask me any question you may have related to finding restaurants or knowing their food.\n\nCities where I have knowledge: %s"
                     "\n\nExample questions: I want to go to a restaurant in X city. What is the specialty of X restaurant? Restaurants similar to X chain. Is X restaurant in X place full? Show relevant information of X restaurant in X city..."
                     "\nOther restaurant knowledge: nationality, specialty, dishes, ambience, qualification, review, capacity, dresscode, environment...")
        self.init_message = auxString % self.listOfCities

        @self.client.event
        async def on_ready():
            await self.client.get_channel(1243594396495249483).send(self.init_message)
            await self.client.get_channel(1244011664789995561).send(self.init_message)

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            await message.channel.send(self.bot.routine(message))

    def run(self):
        self.client.run(TOKEN)