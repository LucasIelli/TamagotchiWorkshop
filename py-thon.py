# This is a training of the basics of Python, not really working anymore, go on pet.py.

import random

# Bibliothèque snake = {} NOT object in Python
pets = [
    {
        'photo': '~<:<<<<<<<<<<<x--',
        'name': 'Snaky',
        'age': 2,
        'weight': 220.54,
        'hungry': True,
        'phrases': ['*Kssss*', '*Snnnnakkky*', '*Sssss*', '*Sssssank youuu'],
    },
    {
        'photo': '=^..^=',
        'name': 'CutyCat',
        'age': 5,
        'weight': 6.2,
        'hungry': True,
        'phrases': ['*Miaou*', '*Rrrrrou*', '*Purrrrrr*', '*Pfffff*'],
    }
]


def startup_pets():
    print('Welcome')
    print('Wish pet do you choose?')
    for pet in pets:
        print(pet['name'])
    pets_choice = input()

    for pet in pets:
        if pet['name'] == pets_choice:
            print(pet['name'] + ' already loves you')
            return pet
    print('No pet with this name 😒')
    return startup_pets()


def chat_pets(pet):
    print(pet['name'] + ' says ' + random.choice(pet['phrases']))


def pets_stats(pet):
    print('Say hello to your new pet, ' + pet['name'] + ' !')
    print(pet['photo'])
    # You need to transform integral into string with str()
    print(pet['name'] + ' weights ' + str(pet['weight']) + ' pounds')

    if pet['hungry']:
        print(pet['name'] + ' is hungry !')
    else:
        print(pet['name'] + ' burps loudly')

    if pet['weight'] > 250:
        print(pet['name'] + ' is massive !')


pet = startup_pets()
pets_stats(pet)

terminate = False
while not terminate:
    print('#############')
    user_input = input()
    if user_input == 'quit':
        terminate = True
    elif user_input == 'chat':
        chat_pets(pet)
    elif user_input == 'feed':
        print('*mmmmmhhh...*')
        snake['weight'] = weight + 1
        snake['hungry'] = False
    else:
        print('command not found, please use quit or feed')

print('You have quit your pets')
