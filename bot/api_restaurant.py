import requests


class BusinessApiInfo:
    def __init__(self, business_alias, image_url, is_closed, yelp_url, address, phone):
        self.business_alias = business_alias
        self.image_url = image_url
        self.is_closed = is_closed
        self.yelp_url = yelp_url
        self.address = address
        self.phone = phone


class ApiRestaurant:

    API_KEY = 'pOzWWzqjDvSKN1csYN8EyexXORPtKmGJEcjeUC9EpPU9uKvtyBGRHHdQc_M_gpa3ZsJ3o6LZtZ3mI0S7yKZaNnmHcDp54umxg891z900V8q0z6_-Apph7764muxZZnYx'

    business_id = None
    business_alias = None
    image_url = None
    is_closed = None
    yelp_url = None
    address = None
    phone = None

    business_api_info = None


    def get_business_info_implementation(self, api_key, restaurant_name, location):
        url = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization': f'Bearer {api_key}'}
        params = {
            'term': restaurant_name,
            'location': location,
            'limit': 1
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        print(response.json())
        businesses = data.get('businesses')
        if businesses:
            self.business_id = businesses[0]['id']
            self.business_alias = businesses[0]['alias']
            self.image_url = businesses[0]['image_url']
            self.is_closed = businesses[0]['is_closed']
            self.yelp_url = businesses[0]['url']
            self.address = businesses[0]['location']['address1']
            self.phone = businesses[0]['phone']

            self.business_api_info = BusinessApiInfo(self.business_alias, self.image_url, self.is_closed, self.yelp_url, self.address, self.phone)
        else:
            return None

    def get_business_info(self, restaurant_name, location):

        self.get_business_info_implementation(self.API_KEY, restaurant_name, location)

        if self.business_id:
            return self.business_api_info
        else:
            print('Not found in API.')
            return None
