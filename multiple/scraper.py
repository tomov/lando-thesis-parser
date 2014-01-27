import os
f = open('adj_pos2.txt')
s = f.read()
adj_pos = s.split('\n')

f = open('adj_neg2.txt')
s = f.read()
adj_neg = s.split('\n')

f = open('list.csv') ## exported from Excel as Macintosh CSV
s = f.read()
rows = s.split('\r')
rows.pop(0)

for row in rows:
    num = row.split(',')[0]
    name = num + '.txt'

    f = open(name)
    s = f.read()
    s = s.lower()
    words = s.split()

    good = 0
    for adj in adj_pos:
        good += words.count(adj)

    bad = 0
    for adj in adj_neg:
        bad += words.count(adj)

    print 'For ' + num + ': ' + str(good) + ' good and ' + str(bad) + ' bad, score = ' + str(good - bad) + ' or ' + str(good / bad if bad > 0 else good )
