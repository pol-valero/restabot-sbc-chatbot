RestaBot, created by: Alex Liu, Pol Valero, Carles Contreras, Victoria Ortiz

In order to build and execute the project, we have used the IDE "PyCharm" with the Python version 3.9 and the following libraries imported:
-requests
-random
-json
-discord
-nltk

Importing these libraries is as simple as opening the project with PyCharm, situating the cursor over each import with a library name and press "install".

The bot can be executed in two different modes: terminal mode and discord mode.

-Terminal mode: The input to interact with the bot is entered in the terminal that is shown at the bottom part of the Pycharm window.
-Discord mode: The input to interact with the bot is entered in the discord chat.

To choose between terminal mode and discord mode, go to the "main.py" file and follow the instructions in the comments in order to "comment" or "uncomment" the necessary lines of code.

To execute the project with PyCharm, you simply have to have the "main.py" file open and press the green play button in the top right corner of the screen.
Once executed, if the bot is in "terminal mode" you will see a welcoming message in the terminal, and you will be able to interact with the bot.
If the bot is in "discord mode", you will have to scan the QR code that is at the end of the PDF file created and delivered for the project.
This QR code will allow you to access the discord server where the welcoming message will also be displayed and where you will be able to interact with the bot.

The bot saves the context of the restaurant and location that were discussed before, so you can ask questions without specifying these two variables.
Example questions to ask the bot:

Tell me a restaurant in Barcelona
What is the specialty of mcdonalds?
What are the dishes of tagliatella?
What is the nationality of Fosters?
What qualifications does telepizza have? What qualification does the restaurant have?
What do you recommend to eat in Mataro?
Recommend me any Italian restaurant
Average price for Tagliatella?
What is the ambience of the restaurant?
Number of tagliatellas?
What is the environment of the restaurant? What is the environment of Tagliatella?
Is the restaurant full?
What is the capacity?
Reviews of la Tagliatella
Restaurants similar to Tagliatella
What is the dresscode?
What is the location of McDonalds?
Information of Mcdonalds?

*Instead of the provided city and restaurant names, you can use any other city or restaurant name that you want to ask about and exists in the .json file that has the main "base de coneixement"