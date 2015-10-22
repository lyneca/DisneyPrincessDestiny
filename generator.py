__author__ = 'wing2048'
import hashlib

princesses = [
    'Cinderella',
    'Rapunzel',
    'Ariel',
    'Aurora',
    'Snow White',
    'Fa Mulan',
    'Pocahontas',
    'Belle',
    'Tiana',
    'Jasmine',
    'Merida',
    'Anna',
    'Elsa',
    'Moana'
]
while True:
    print('Birthday (dd/mm/yyyy)')
    birthday = input('> ')
    print('Name:')
    name = input('> ')
    r_hash = hashlib.sha512((birthday + name).encode()).hexdigest()
    char_id = 0
    for c in r_hash:
        if eval('0x'+c) <= 13:
            char_id = eval('0x'+c)
    print('Your Disney Destiny Princess is', princesses[char_id] + '!')