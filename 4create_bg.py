import os

for img in os.listdir('neg/rawdata-remote'):
    line = 'neg/rawdata-remote/' + img + '\n'
    with open('bg-remote.txt', 'a') as f:
        f.write(line)

for img in os.listdir('neg/rawdata-ii'):
    line = 'neg/rawdata-ii/' + img + '\n'
    with open('bg-ii.txt', 'a') as f:
        f.write(line)
