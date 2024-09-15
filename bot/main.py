from data_loader import DataLoader
from nltk_utilities import NltkUtilities
from discord_bot import DiscordBot 
from bot import BotRestaurant

utilities = NltkUtilities()

data = DataLoader(utilities)
data.loadData()

botRestaurant = BotRestaurant(utilities, data)

#----------UNCOMMENT TO RUN BOT IN COMPUTER TERMINAL. COMMENT TO RUN BOT IN DISCORD---------

botRestaurant.executeInTerminal()

#-------------------------------------------------------------------------------------------


#----------UNCOMMENT TO RUN BOT IN DISCORD. COMMENT TO RUN BOT IN COMPUTER TERMINAL---------

#botRestaurantDiscord = DiscordBot(botRestaurant, data)
#botRestaurantDiscord.run()

#-------------------------------------------------------------------------------------------

