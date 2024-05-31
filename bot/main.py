from data_loader import DataLoader
from nltk_utilities import NltkUtilities
from discord_bot import DiscordBot 
from bot import BotRestaurant

utilities = NltkUtilities()

data = DataLoader(utilities)
data.loadData()

botRestaurant = BotRestaurant(utilities, data)

botRestaurantDiscord = DiscordBot(botRestaurant, data)
botRestaurantDiscord.run()

#TODO: Create function to use terminal for interaction, just in case disc is not working. Also can be used to correct the project without using discord.