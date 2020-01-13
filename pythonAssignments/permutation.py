from itertools import permutations



def stringPerm(word):
    c = 0
    permutated = permutations(word)
    for perm in list(permutated):
        c = c + 1
        print(''.join(perm))
    print("Total number of permutation of the string is ",c)

stringPerm("abcqa")
