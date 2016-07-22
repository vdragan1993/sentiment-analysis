# coding=utf-8
__author__ = 'Dragan Vidakovic'
from src import scraper
from selenium import webdriver
from src import writer
import time

# browser driver
driver_location = "D:/chromedriver.exe"

# city list
srb = ['beograd', 'novisad', 'nis', 'subotica', 'pancevo', 'zrenjanin', 'kragujevac', 'krusevac', 'kraljevo', 'cacak']
bih = ['sarajevo', 'banjaluka', 'bijeljina', 'brcko', 'prijedor', 'zenica', 'tuzla', 'mostar']
cg = ['podgorica', 'bar', 'budva', 'kotor', 'tivat', 'hercegnovi', 'niksic', 'bijelopolje']

# max id of restaurant in each city
num_of_restaurants = 1001


def get_url(city, number):
    return "http://www.donesi.com/" + city + "/lat/review.php?objectID=" + str(number)


def get_file_name(folder, city, number, extension):
    return "../data/" + folder + "/" + city + "_" + str(number) + "." + extension


def get_restaurants_for_country(country, folder):
    country_count = 0
    for city in country:
        city_count = get_restaurants_for_city(city, folder)
        print("\t\t" + city + " reviews count: " + str(city_count))
        country_count += city_count

    return country_count


def get_restaurants_for_city(city, folder):
    city_count = 0
    for i in range(1, num_of_restaurants):
                file_name = get_file_name(folder, city, i, 'xlsx')
                restaurant_url = get_url(city, i)
                restaurant_count = get_restaurant_reviews(file_name, restaurant_url)
                print("\t" + restaurant_url + " reviews count: " + str(restaurant_count))
                city_count += restaurant_count

    return city_count


def get_restaurant_reviews(file, url):
    # connecting to website
    browser = webdriver.Chrome(driver_location)
    browser.get(url=url)

    all_reviews = []

    # check if existing
    if scraper.has_results(browser.page_source):
        # skip welcome form
        if browser.find_element_by_id("zone_form"):
            welcome_form = browser.find_element_by_id("zone_form")
            welcome_form.submit()

        # check if there is next page
        try:
            while browser.find_element_by_id("nav_next_page"):
                page_reviews = scraper.get_page_data(browser.page_source, browser.current_url)
                all_reviews = all_reviews + page_reviews
                next_page = browser.find_element_by_id("nav_next_page")
                next_page.click()
        # no next page
        except:
            page_reviews = scraper.get_page_data(browser.page_source, browser.current_url)
            all_reviews = all_reviews + page_reviews

        print("Collected reviews for restaurant: " + url + " , now writing file: " + file)
        writer.write_reviews(file, all_reviews)

    else:
        print("Restaurant: " + url + " does not exist!")

    browser.quit()
    time.sleep(1)
    return len(all_reviews)

if __name__ == "__main__":
    """
    serbia_reviews = get_restaurants_for_country(srb, 'srb')
    print("Total Serbia reviews: " + str(serbia_reviews))
    bih_reviews = get_restaurants_for_country(bih, 'bih')
    print("Total BiH reviews: " + str(bih_reviews))
    cg_reviews = get_restaurants_for_country(cg, 'cg')
    print("Total CG reviews: " + str(cg_reviews))
    """
    # temp test
    get_restaurant_reviews('../data/srb/beograd_100.xlsx', get_url('beograd', 100))
    get_restaurant_reviews('../data/srb/beograd_1.xlsx', get_url('beograd', 1))
    get_restaurant_reviews('../data/srb/beograd_200.xlsx', get_url('beograd', 200))