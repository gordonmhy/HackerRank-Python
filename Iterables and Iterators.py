# Iterables and Iterators

import itertools

n = int(input())
letters = str(input()).split(' ')

permutations = iter(itertools.permutations(letters, int(input())))

nominator = 0
denominator = 0
i = next(permutations, None)
while i is not None:
    if 'a' in i:
        nominator += 1
    denominator += 1
    i = next(permutations, None)

print('{:.3f}'.format(nominator/denominator))