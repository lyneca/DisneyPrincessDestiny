__author__ = 'wing2048'
import hashlib


class Princess():
    def __init__(self, name, hair, eyes, other):
        self.name = name
        self.hair = hair
        self.eyes = eyes
        self.other = other


princesses = [
    Princess('Cinderella', 'white', 'blue', 'feet of a very unique size'),
    Princess('Rapunzel', 'kilometre-long, golden', 'green', 'you pose a choking hazard to small children'),
    Princess('Ariel', 'red', 'blue', 'a mermaid tail'),
    Princess('Aurora', 'golden', 'purple', 'chronic fatigue'),
    Princess('Snow White', 'black', 'brown', 'you live with seven tiny men'),
    Princess('Fa Mulan', 'black', 'brown', 'you have a gender identity crisis'),
    Princess('Pocahontas', 'brown', 'brown', 'the uncanny ability to speak English'),
    Princess('Belle', 'brown', 'brown', 'bestiality'),
    Princess('Tiana', 'brown', 'brown', 'you work two jobs to support your sugar mill business'),
    Princess('Jasmine', 'black', 'brown', 'you will marry whomever you want'),
    Princess('Merida', 'red', 'blue', 'you can weave tapestries, apparently'),
    Princess('Anna', 'red', 'green', 'you have no magical powers'),
    Princess('Elsa', 'white', 'blue', 'you can control ice'),
]

while True:
    print('Birthday (dd/mm/yyyy)')
    birthday = input('> ')
    print('Name:')
    name = input('> ')
    c_hash = hashlib.sha512((birthday + name).encode()).hexdigest()
    n_hash = hashlib.sha512(''.join(sorted(list(birthday + name))).encode()).hexdigest()
    b_hash = hashlib.sha512(''.join(sorted(list(birthday + name), reverse=True)).encode()).hexdigest()
    y_hash = hashlib.sha512((name + birthday).encode()).hexdigest()
    name = hair = eyes = other = ''
    for c in c_hash:
        if eval('0x' + c) <= len(princesses) - 1:
            name = princesses[eval('0x' + c)].name
    for c in n_hash:
        if eval('0x' + c) <= len(princesses) - 1:
            hair = princesses[eval('0x' + c)].hair
    for c in b_hash:
        if eval('0x' + c) <= len(princesses) - 1:
            eyes = princesses[eval('0x' + c)].eyes
    for c in n_hash:
        if eval('0x' + c) <= len(princesses) - 1:
            other = princesses[eval('0x' + c)].other
    print('You are %s. You have %s hair, %s eyes and %s!' % (name, hair, eyes, other))