import re
from collections import Counter


def vogais(string):
    return Counter(re.sub('[^aeiouAEIOU]', '', string))

print(vogais('heyyy psiu beijo me liga'))

