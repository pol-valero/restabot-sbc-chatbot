import json
import random
from model import Restaurant, Location

class DataLoader:
    knowledge = []
    
    restaurant_names = []
    city_names = []
    dish_names = []
    nacionalities_names = []

    def __init__(self, Nltk_Utilities):
        self.nlkt_utilities = Nltk_Utilities
    
    def loadData(self):
        with open("restaurants.json", 'r') as f:
            data = json.load(f)

        restaurants = []
        for item in data:
            location_data = item['location']
            location = Location(location_data['city'], location_data['country'], location_data['environment'])

            restaurant = Restaurant(
                name=item['name'],
                location=location,
                dishes=item['dishes'],
                specialty=item['specialty'],
                ambience=item['ambience'],
                nationality=item['nationality'],
                qualification=item['qualification'],
                criticReview=item['criticReview'],
                peopleCapacity=item['peopleCapacity'],
                peopleInside=item['peopleInside'],
                averagePrice=item['averagePrice']

            )
            restaurants.append(restaurant)

        self.knowledge = restaurants

        self.getUniqueRestaurantNames()
        self.getUniqueCityNames()
        self.getUniqueDishNames()
        self.getUniqueNationalityName()

        if len(self.knowledge) == 0:
            print("No data loaded")

        if len(self.restaurant_names) == 0:
            print("No restaurant names loaded")

        if len(self.city_names) == 0:
            print("No city names loaded")

        if len(self.dish_names) == 0:
            print("No dish names loaded")

    def getUniqueRestaurantNames(self):
        unique_names = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.name.lower()) not in unique_names: #We avoid having duplicates in the list
                unique_names.append(self.nlkt_utilities.stem_word(restaurant.name.lower()))

        self.restaurant_names = unique_names

    def getUniqueDishNames(self):
        unique_names = []
        for restaurant in self.knowledge:
            for dish in restaurant.getDishes():
                if self.nlkt_utilities.stem_word(dish.lower()) not in unique_names: #We avoid having duplicates in the list
                    unique_names.append(self.nlkt_utilities.stem_word((dish.lower())))
        self.dish_names = unique_names

    def getUniqueNationalityName(self):
        unique_names = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.nationality.lower()) not in unique_names: #We avoid having duplicates in the list
                unique_names.append(self.nlkt_utilities.stem_word(restaurant.nationality.lower()))
        self.nacionalities_names = unique_names

    def getUniqueCityNames(self):
        unique_names = []
        for restaurant in self.knowledge:
            if  self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) not in unique_names: #We avoid having duplicates in the list
                unique_names.append(self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()))
        self.city_names = unique_names

    def findLocation(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getLocation().getCity()
        return "noLocationFound"

    def findDishes(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getDishes()
        return "noDishesFound"

    def findSpecialty(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getSpecialty()
        return "noSpecialityFound"

    def findSpecialties(self, location_name):
        found = 0
        specialties = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name) or self.nlkt_utilities.stem_word(restaurant.getLocation().getCountry().lower()) == self.nlkt_utilities.stem_word(location_name):
                specialties.append(restaurant.getSpecialty())
                found = 1

        if (found == 0):
            return "noSpecialityFound"
        else:
            return specialties

    def findAmbience(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getAmbience()
        return "noAmbienceFound"

    def findRestaurantNacionality(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getNationality()
        return "noNationalityFound"

    def findRandomRestaurant(self, location_name):
        restaurants = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name) or self.nlkt_utilities.stem_word(restaurant.getLocation().getCountry().lower()) == self.nlkt_utilities.stem_word(location_name):
                restaurants.append(restaurant.getName())

        if len(restaurants) == 0:
            return "noRestaurantFound"

        return random.choice(restaurants)

    def findNationalityRestaurant(self, nationality):
        restaurants = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getNationality().lower()) == self.nlkt_utilities.stem_word(nationality):
                restaurants.append(restaurant.getName())

        if len(restaurants) == 0:
            return "noNationalityFound"
        
        return random.choice(restaurants)

    def findRestaurantQualification(self, rest_name, location_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(rest_name.lower()) and self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name):
                return restaurant.getQualification()
        return "noQualityFound"

    def findNationalityPlaces(self, nationality, location_name):

        restaurants = []
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getNationality().lower()) == self.nlkt_utilities.stem_word(nationality):
                restaurants.append(restaurant.getName())

        if len(restaurants) == 0:
            return "noNationalityFound"

        return random.choice(restaurants)

    def findRestaurantEnvironment(self, restaurant_name, location_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()) and self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name):
                return restaurant.getLocation().getEnvironment()
        return "noEnvironmentFound"

    def findPrice(self, restaurant_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                return restaurant.getAveragePrice()
        return "noPriceFound"

    def findNumberOfSameChainRestaurants(self, restaurant_name):
        chain = 0
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()):
                chain += 1
        return chain

    def findCapacity(self, restaurant_name, location_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()) and self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name):
                return restaurant.getPeopleCapacity()
        return "noCapacityFound"

    def findReview(self, restaurant_name, location_name):
        for restaurant in self.knowledge:
            if self.nlkt_utilities.stem_word(restaurant.getName().lower()) == self.nlkt_utilities.stem_word(restaurant_name.lower()) and self.nlkt_utilities.stem_word(restaurant.getLocation().getCity().lower()) == self.nlkt_utilities.stem_word(location_name):
                return restaurant.getCriticReview()
        return "noReviewFound"