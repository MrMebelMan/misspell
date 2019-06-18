#!/usr/bin/env python3

from random import choice as random_choice, randint

NEIGHBORS = {
    'a': 'qwszx',
    'b': 'vghn',
    'c': 'xdfv',
    'd': 'wersfxcv',
    'e': '34wrsdf',
    'f': 'ertdgcvb',
    'g': 'rtyfhvbn',
    'h': 'tyugjbnm',
    'i': '789uojkl',
    'j': 'yuihknm',
    'k': 'uiojlm,',
    'l': 'iopk,.',
    'm': 'jkn,',
    'n': 'bhjm',
    'o': '90ipkl',
    'p': "0-o[l'",
    'q': '12was',
    'r': '345etdfg',
    's': 'qweadzxc',
    't': '456ryfgh',
    'u': '78yihjk',
    'v': 'cfgb',
    'w': '23qeasd',
    'x': 'zasdc',
    'y': '67tughj',
    'z': 'asx',
    '-': '0=p[',
    '.': 'l',
}

NEIGHBORS_UNICODE = {
    'a': 'á',
    'c': 'č',
    'd': 'ď',
    'e': 'ěé',
    'i': 'íǐ',
    'n': 'ňń',
    'o': 'óǒ',
    'r': 'řŕ',
    's': 'šś',
    't': 'ť',
    'u': 'ǔú',
    'v': 'ǘǚ',
    'y': 'ý',
    'z': 'žź',
    'ě': 'qwe',
    'š': 'wer',
    'č': 'ert',
    'ř': 'rty',
    'ž': 'tyu',
    'ź': 'tyu',
    'ý': 'yzui',
    'ž': 'tyzu',
    'á': 'uio',
    'í': 'iop',
}

ALL_NEIGHBORS = dict(NEIGHBORS)
for key in NEIGHBORS_UNICODE:
    if key in ALL_NEIGHBORS:
        ALL_NEIGHBORS[key] += NEIGHBORS_UNICODE.get(key, '')
    else:
        ALL_NEIGHBORS[key] = NEIGHBORS_UNICODE.get(key, '')

def make_typo(string: str, unicode: bool=False) -> str:
    if string is None or string == '':
        return ''
    replace_choices = ALL_NEIGHBORS if unicode else NEIGHBORS
    string = str(string)

    chance = randint(0, 100)
    index = randint(0, max(0, len(string) - 1))
    if chance >= 85 and chance < 95:
        return string[:index] + string[index+1:]  # erase character
    elif chance >= 95:
        return string[:index] + string[index] + string[index:]  # repeat character
    else:
        pass  # replace character
        
    # check that there are replaceable characters
    found = False
    for c in set(string.lower()):
        if c in replace_choices:
            found = True
            break
    if not found:
        return string

    while True:
        index = randint(0, max(0, len(string) - 1))
        random_char = string[index]
        char_lower = random_char.lower()

        if char_lower in replace_choices:
            break

    ret = list(string)

    ret[index] = random_choice(replace_choices[random_char.lower()])

    # preserve case
    if random_char != char_lower:
        ret[index] = ret[index].upper()

    return ''.join(ret)

def make_typos(string: str, percent: (int, float)=5, unicode=False):
    if percent < 1 or percent >= 100:
        raise ValueError("'percent' should be between 1 and 99")

    num_of_typos = int(len(string.replace(' ', '')) / 100 * percent)

    for num in range(0, num_of_typos):
        string = make_typo(string, unicode=unicode)

    return string

