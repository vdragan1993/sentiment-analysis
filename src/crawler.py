# coding=utf-8
__author__ = 'Dragan Vidakovic'
from src import scraper
from selenium import webdriver

# browser driver
driver_location = "D:/chromedriver.exe"

# city list
srb = ['beograd', 'novisad', 'nis', 'subotica', 'pancevo', 'zrenjanin', 'kragujevac', 'krusevac', 'kraljevo', 'cacak']
bih = ['sarajevo', 'banjaluka', 'bijeljina', 'brcko', 'prijedor', 'zenica', 'tuzla', 'mostar']
cg = ['podgorica', 'bar', 'budva', 'kotor', 'tivat', 'hercegnovi', 'niksic', 'bijelopolje']

# max id of restaurant in each city
num_of_restaurants = 1001


def get_url(city, number):
    return "http://www.donesi.com/" + city + "/review.php?objectID=" + str(number)


def get_file_name(folder, city, number, extension):
    return folder + "/" + city + "_" + str(number) + "." + extension


def get_restaurants_for_country(country, folder):
    for city in country:
        get_restaurants_for_city(city, folder)


def get_restaurants_for_city(city, folder):
    for i in range(1, num_of_restaurants):
                file_name = get_file_name(folder, city, i, 'txt')
                restaurant_url = get_url(city, i)
                get_restaurant_reviews(file_name, restaurant_url)


def get_restaurant_reviews(file, url):
    print("Collecting reviews for restaurant: " + url + " , and writing file: " + file)
    # connecting to website
    browser = webdriver.Chrome(driver_location)
    browser.get(url=url)
    # check if existing
    if scraper.has_results(browser.page_source):
        # skip welcome form
        if browser.find_element_by_id("zone_form"):
            welcome_form = browser.find_element_by_id("zone_form")
            welcome_form.submit()

        # check if there is next page
        try:
            while browser.find_element_by_id("nav_next_page"):
                print(browser.current_url)
                # TODO: magic for scraping
                next_page = browser.find_element_by_id("nav_next_page")
                next_page.click()
        # no next page
        except:
            # TODO: magic for scraping
            print(browser.current_url)

    else:
        print("Restaurant: " + url + " does not exist!")

    browser.quit()

if __name__ == "__main__":
    #get_restaurants_for_country(srb, 'srb')
    #get_restaurants_for_country(bih, 'bih')
    #get_restaurants_for_country(cg, 'cg')

    # temp test
    get_restaurant_reviews('a.txt', get_url('beograd', 100))
    get_restaurant_reviews('b.txt', get_url('beograd', 1))
    get_restaurant_reviews('c.txt', get_url('beograd', 200))