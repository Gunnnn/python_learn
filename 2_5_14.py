# put your python code here
import itertools
num = input()
l = [str(x) for x in str(num)] # создаем list из введенной строки
#print('l =', l)
l_permutated = list(itertools.permutations(l))
#print('l_permutated=', l_permutated)
for item in l_permutated:
    print(''.join(item))