import json

# დავალება 1

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f'Name: {self.name} - Price: {self.price} - Quantity: {self.quantity}'
#
# def customized_serializer(obj: Product):
#     if isinstance(obj, Product):
#         return {'name': obj.name, 'price': obj.price, 'quantity': obj.quantity}
#
# def customized_deserializer(json_data):
#     return Product(json_data['name'], json_data['price'], json_data['quantity'])
#
# product1 = Product('Bagels', 5.99, 6)
# product2 = Product('English Muffins', 4.99, 4)
# product3 = Product('Sourdough', 6.99, 1)
# product4 = Product('Emmy\'s Cookies', 7, 12)
# product5 = Product('Rosemary Crackers', 12.99, 30)
#
# products = [product1, product2, product3, product4, product5]
#
#
# with open('products2.json', 'w') as new_json_file:
#     json.dump(products, new_json_file, default=customized_serializer, indent=4)
#
#
# with open('products2.json') as read_json_file:
#     try:
#         products2 = json.load(read_json_file, object_hook=customized_deserializer)
#         for product in products2:
#             print(product)
#     except json.decoder.JSONDecodeError as e:
#         print(e)

######################################################


# დავალება 2
class Movie:
    def __init__(self, adult, backdrop_path, genre_ids, id, original_language, original_title, overview, popularity, poster_path, release_date, title, video, vote_average, vote_count, genres):
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.genre_ids = genre_ids
        self.id = id
        self.original_language = original_language
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.genres = genres

    # def __str__(self):
    #     return f'{self.original_title} - {self.release_date} - {self.genres}'


movies_list = []

with open('movies.json', 'r') as json_file:
    try:
        movies = json.load(json_file)
        # print(type(movies))

        for movie in movies:
            for key, value in movie.items():
                if key == 'results':
                    for i in value:
                        if 'Crime' in i['genres'] and int(i['release_date'][:4]) > 2000:
                            for j in i['genres']:
                                if j == 'Crime':

                                movies_list.append(i)
                        # print(type(i['release_date']))
    except json.decoder.JSONDecodeError as e:
        print(e)


# for movie in movies:
    # print(movie["results"][1]["original_title"])
# counter = 0
# for movie in movies:
#     for i in range(len(movies)):

        # counter += 1
        # print(movie['results'][i]['title'], counter)

print(movies_list)

