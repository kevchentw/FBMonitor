open('fb.txt')
a = f.read()
l = a.split('\n')
for i in l:
    print('<li><a href="/monitor/?page='+ i.split(' ')[0]+'"'+ '>'+(" ").join(i.split(' ')[1: ])+'</a></li>')
