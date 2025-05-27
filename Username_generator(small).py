# RANDOM USERNAME GENERATOR
import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']


def capitalize_suffix(name):
    return name.capitalize()


capitalize_suffixes = list(map(capitalize_suffix, suffixes))
print('Capitalized suffixes:', capitalize_suffixes)


def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)


random_names = [create_fantasy_name(prefixes, capitalize_suffixes) for i in range(10)]

print('Fantasy names:', random_names)



