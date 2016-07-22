# coding=utf-8
__author__ = 'Dragan Vidakovic'
from bs4 import BeautifulSoup
from src.model import Review


def has_results(html):
    return "Nije dostupno!" not in html


def get_page_data(html, review_url):
    soup = BeautifulSoup(html, 'html.parser')
    # restaurant info
    restaurant = soup.findAll("a", attrs={"class": "btn btn-primary btn-large"})[0]
    restaurant_name = restaurant.get_text().strip()[9:]
    restaurant_link = restaurant['href']

    ret_val = []
    reviews = soup.findAll("div", attrs={"itemprop": "review"})
    for review in reviews:
        ret_val.append(get_review_data(str(review), review_url, restaurant_name, restaurant_link))

    return ret_val


def get_review_data(review, review_url, restaurant_name, restaurant_link):
    soup = BeautifulSoup(review, 'html.parser')

    # extracting user info
    user = soup.findAll("a", attrs={"itemprop": "author"})[0]
    username = user.get_text().strip()
    user_url = user['href'].strip()

    # extracting review info
    review_title = soup.findAll("meta", attrs={"itemprop": "name"})[0]
    title = review_title['content'].strip()

    date_published = soup.findAll("meta", attrs={"itemprop": "datePublished"})[0]
    published = date_published['content'].strip()

    rating_value = soup.findAll("meta", attrs={"itemprop": "reviewRating"})[0]
    rating = rating_value['content'].strip()

    review_content = soup.findAll("span", attrs={"itemprop": "reviewBody"})[0]
    content = review_content.get_text().strip()

    # other ratings
    food_quality = None
    food_choice = None
    prices = None
    service = None
    all_ratings = soup.findAll("td", attrs={"width": "110"})
    if len(all_ratings) == 4:
        for all_rating in all_ratings:
            rating_string = all_rating.get_text().strip()
            rating_description = rating_string[1:]
            if rating_description.startswith("Kvalitet hrane"):
                food_quality = rating_string[0]
            elif rating_description.startswith("Izbor"):
                food_choice = rating_string[0]
            elif rating_description.startswith("Cene"):
                prices = rating_string[0]
            elif rating_description.startswith("Usluga"):
                service = rating_string[0]

    ret_val = Review(username, user_url, title, published, rating, content, food_quality, food_choice, prices, service,
                     review_url, restaurant_name, restaurant_link)
    return ret_val