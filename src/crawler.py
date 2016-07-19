# coding=utf-8
__author__ = 'Dragan Vidakovic'

# browser driver
driver_location = "D:/chromedriver.exe"

# city list
srb = ['beograd', 'novisad', 'nis', 'subotica', 'pancevo', 'zrenjanin', 'kragujevac', 'krusevac', 'kraljevo', 'cacak']
bih = ['sarajevo', 'banjaluka', 'bijeljina', 'brcko', 'prijedor', 'zenica', 'tuzla', 'mostar']
cg = ['podgorica', 'bar', 'budva', 'kotor', 'tivat', 'hercegnovi', 'niksic', 'bijelopolje']

# max id of restaurant in each city
num_of_restaurants = 1000


def get_url(city, number):
    return "www.donesi.com/" + city + "/review.php?objectID=" + str(number)


def get_restaurants_for_country(country):
    return None


def get_restaurants_for_city(city):
    return None


def get_restaurant_reviews(url):
    return None


if __name__ == "__main__":
    print("Hello World!")