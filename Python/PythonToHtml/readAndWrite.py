import sys

i = 0
f = open('NamesTest.csv', 'r')
c = open('NamesTestHtml.html', 'wt')
line = f.readline()
for line in f:
    c.write(line)
    
f.close()
c.close()

print('File Read and Writting!')

