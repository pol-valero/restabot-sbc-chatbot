import random

locationResponses = ["The restaurant is in %s", "Go to %s and you will find the restaurant", "It is located in %s"]
dishesResponses = ["Some of the good dishes of the restaurant are: %s", "These are some of the dishes: %s", "Here is a list: %s"]
restaurantResponses = ["%s is one of the restaurants in %s", "%s is the one you might be looking for in %s"]
specialtyResponses = ["Their specialty is the %s ", "The %s is their specialty dish"]
ambienceResponses = ["Past customers described their ambience as %s ", "%s could be the best word to describe their ambience"]
specialtiesResponses = ["The star dishes in their top restaurants are: %s "]
nationalityResponses = ["This restaurant is know from its %s dishes", "You should go to this restaurant if you want to try some %s dishes", "This is the most autenthic %s restaurant"]
qualificationResponses = ["This restaurant has %s stars", "This restaurant has a %s stars rating.", "Customers have given this restaurant a %s stars rating."]

doNotUnderstandResponses = ["Sorry, I don't understand what you are asking", "Please, try to phrase the question in a different manner", "Reformulate the question using simple words, please"]

IND_REST = 0
IND_LOCAT = 1
IND_DISH = 2
IND_SPEC = 3
IND_AMBIENC = 4
IND_NATION = 5
IND_QUALIF = 6
IND_CITY = 7
IND_NAT = 8

class BotRestaurant:
    remember = [None] * 9

    def __init__(self, nlkt_utilities, data_loader):
        self.nlkt_utilities = nlkt_utilities
        self.data_loader = data_loader

    def isset(self, arr, index):
        return index < len(arr) and arr[index] is not None

    def updateRemember(self, arr, exception):
        #for i in range(len(arr)):
         #   if i != exception and i != 0:
          #      arr[i] = None
        return arr

    #Used to verify if the input string contain or does not contain any of the context tokens
    def noMoreContext(self, inputs):
        for token in inputs:
            if token in ["locat", "dish", "specialty", "specialti", "special", "ambienc", "nation", "qualif"]:
                return False
        return True

    def routine(self, message):
        filtered_input_tokens = self.nlkt_utilities.filter_input_tokens(message.content)

        for token in filtered_input_tokens:

            if token in self.data_loader.restaurant_names or (self.isset(self.remember, IND_REST) and token not in self.data_loader.city_names and token not in self.data_loader.nacionalities_names and token != "restaur"):
                print("Test1")

                if token in self.data_loader.restaurant_names:
                    self.remember[IND_REST] = token
                else:
                    token = self.remember[IND_REST]
                if "locat" in filtered_input_tokens: #Locat is the stem for "location"
                    self.remember[IND_LOCAT] = 1
                    self.remember = self.updateRemember(self.remember, IND_LOCAT)
                    location = self.data_loader.findLocation(token)
                    response = random.choice(locationResponses)
                    return response % location
                elif "dish" in filtered_input_tokens:
                    self.remember[IND_DISH] = 1
                    self.remember = self.updateRemember(self.remember, IND_DISH)
                    dishes = self.data_loader.findDishes(token)
                    response = random.choice(dishesResponses)
                    return response % dishes
                elif "specialti" in filtered_input_tokens or "specialty" in filtered_input_tokens or "special" in filtered_input_tokens:
                    self.remember[IND_SPEC] = 1
                    self.remember = self.updateRemember(self.remember, IND_SPEC)
                    specialty = self.data_loader.findSpecialty(token)
                    response = random.choice(specialtyResponses)
                    return response % specialty
                elif "ambienc" in filtered_input_tokens:
                    self.remember[IND_AMBIENC] = 1
                    self.remember = self.updateRemember(self.remember, IND_AMBIENC)
                    ambience = self.data_loader.findAmbience(token)
                    response = random.choice(ambienceResponses)
                    return response % ambience
                elif "nation" in filtered_input_tokens:
                    self.remember[IND_NATION] = 1
                    self.remember = self.updateRemember(self.remember, IND_NATION)
                    nationality = self.data_loader.findRestaurantNacionality(token)
                    response = random.choice(nationalityResponses)
                    return response % nationality
                elif "qualif" in filtered_input_tokens:
                    self.remember[IND_QUALIF] = 1
                    self.remember = self.updateRemember(self.remember, IND_QUALIF)
                    quali = self.data_loader.findRestaurantQualification(token)
                    response = random.choice(qualificationResponses)
                    return response % quali

            elif token in self.data_loader.city_names or (self.isset(self.remember, IND_CITY) and token not in self.data_loader.nacionalities_names and token != "restaur"):
                print("Entered")
                #or any(filtered_input_tokens) == any(self.data_loader.city_names)
                if token in self.data_loader.city_names:
                    print("Entered1")
                    self.remember[IND_CITY] = token
                else:
                    print("Entered2")

                    token = self.remember[IND_CITY]
                if "restaur" in filtered_input_tokens:
                    restaurant = self.data_loader.findRandomRestaurant(token)
                    self.remember[IND_REST] = restaurant
                    response = random.choice(restaurantResponses)
                    return response % (restaurant, token)
                elif "what" in message.content.lower():
                    specialties = self.data_loader.findSpecialties(token)
                    response = random.choice(specialtiesResponses)
                    return response % specialties

            elif token in self.data_loader.nacionalities_names:
                print("Test2")
                if token in self.data_loader.nacionalities_names:
                    self.remember[IND_NAT] = token
                else:
                    token = self.remember[IND_NAT]
                if "restaur" in filtered_input_tokens:
                    restaurant = self.data_loader.findNationalityRestaurant(token)
                    self.remember[IND_REST] = restaurant
                    response = random.choice(restaurantResponses)
                    print("Restaurant: " + restaurant)
                    return response % (restaurant, self.data_loader.findLocation(restaurant))

            #special case for when the user asks for "other restaurants" without specifying a location (so we use the last remembered location)
            elif token == "restaur" and self.isset(self.remember, IND_CITY):
                print("Test3")

                otherKnownTokenFound = 0
                for token in filtered_input_tokens:
                    if token in self.data_loader.city_names or token in self.data_loader.nacionalities_names or token in self.data_loader.restaurant_names:
                        otherKnownTokenFound = 1

                if otherKnownTokenFound == 0:
                    restaurant = self.data_loader.findRandomRestaurant(self.remember[IND_CITY])
                    self.remember[IND_REST] = restaurant
                    response = random.choice(restaurantResponses)
                    return response % (restaurant, self.remember[IND_CITY])

            #TODO: More if statements related to sentences containing "restaurant"

        return random.choice(doNotUnderstandResponses) #If we have not done any previous return, the message was not understood and we inform the user