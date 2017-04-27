f = open('add10.py', 'r')
print (f.read())
f.close()

r = open("writetest.txt", 'w')
r.write("This is where all the stuff from up there will go")
r.close()

fr = open('writetest.txt', 'r')
print (fr.read())
fr.close()
