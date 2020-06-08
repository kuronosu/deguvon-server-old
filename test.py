import os, json
import django
from scrape.main import get_anime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deguvon.settings")
django.setup()


if __name__ == '__main__':
    # from api.utils import cache_directory_soft
    # # from api.models import Anime
    # # from django.db import transaction
# from api.models import Episode, Relation, State, Type, Genre
# from api.serializers import StateSerializer, TypeSerializer, GenreSerializer
# state_list = StateSerializer(State.objects.all().order_by('id'), many=True, context={'request': None}).data
# type_list = TypeSerializer(Type.objects.all().order_by('id'), many=True, context={'request': None}).data
# genre_list = GenreSerializer(Genre.objects.all().order_by('id'), many=True, context={'request': None}).data
# print(state_list, type_list, genre_list, sep="\n")
# json.dumps({'states': state_list, 'types': type_list, 'genres': genre_list})
    # print("Scrape")
    anime = get_anime('/anime/997/aiura')
    print(anime)
    # print("Save")
    # with transaction.atomic():
    #     Anime.create_or_update(anime)
    # print("End")
    # with open('directory.json', 'r') as f:
    #     text = f.read()
    #     print(text[:300].encode().decode('unicode-escape'))
    # print('cache')
    # cache_directory_soft()


# import codecs
# myString = "spam\\neggs"
# print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
# myString = "naïve \\t test"
# print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))

# import re
# import codecs
# ESCAPE_SEQUENCE_RE = re.compile(
#     r''' ( \\U........ # 8-digit hex escapes 
#     | \\u.... # 4-digit hex escapes
#     | \\x.. # 2-digit hex escapes
#     | \\[0-7]{1,3} # Octal escapes
#     | \\N\{[^}]+\} # Unicode characters by name
#     | \\[\\'"abfnrtv] # Single-character escapes 
# )''', re.UNICODE | re.VERBOSE)
# def decode_escapes(s):
#     def decode_match(match):
#         return codecs.decode(match.group(0), 'unicode-escape')
#     return ESCAPE_SEQUENCE_RE.sub(decode_match, s) 


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'deguvon',
#         'USER': 'deguvon',
#         'PASSWORD': 'deguvon',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }