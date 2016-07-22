# coding=utf-8
__author__ = 'Dragan Vidakovic'


class Review:
    def __init__(self, username, user_url, title, published, rating, content, food_quality, food_choice,
                 prices, service, url, restaurant_name, restaurant_url):
        self.username = username
        self.user_url = user_url
        self.title = title
        self.published = published
        self.rating = rating
        self.content = content
        self.food_quality = food_quality
        self.food_choice = food_choice
        self.prices = prices
        self.service = service
        self.url = url
        self.restaurant_name = restaurant_name
        self.restaurant_url = restaurant_url