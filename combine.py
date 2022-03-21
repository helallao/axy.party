import itertools

c = [x if x.endswith('/') else (x + '/') for x in '''anahtar/
paspas/
kaynak/
dosya/
KAPI/
duvar/
desen/
dag/
tepe/
kule/
057/
plan/
034/
wonderland/
saat/
masal/'''.split('\n')]

new_list = []


min, max = 1, 5
for n in range(min, max+1):
	for xs in itertools.combinations(c, r=n):
		word = ''.join(xs)
		
		new_list.append(f'https://axy.party/{word}')


with open('wordlist.txt', 'w') as fp:
    fp.write('\n'.join(new_list))