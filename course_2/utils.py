import requests
import random
from basicword import BasicWord

def load_random_word():
  response = requests.get('https://www.jsonkeeper.com/b/2HJL')
  response = response.json()
  random_word = random.choice(response)
  object_1 = BasicWord(random_word['word'], random_word['subwords'])
  return object_1