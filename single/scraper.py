import os
f = open('adj_pos.txt')
s = f.read()
adj_pos = s.split('\n')

f = open('adj_neg.txt')
s = f.read()
adj_neg = s.split('\n')

f = open('article.txt')
s = f.read()
s = s.lower()
words = s.split()

good = 0
for adj in adj_pos:
    good += words.count(adj)

print 'There are ' + str(good) + ' positive adjectives'

bad = 0
for adj in adj_neg:
    bad += words.count(adj)

print 'There are ' + str(bad) + ' negative adjectives'
