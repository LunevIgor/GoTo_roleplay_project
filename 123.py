file=open('save.txt','r')
s=file.readline()
f=file.readline()
s=list(s)
c=0
name=''
h=''


for i in s:
    if i == ' ':
       break
    c=c+1
for i in range (0,c):
    name=name+str(s[i])
for i in range (c+1,len(s)):
    h=h+str(s[i])
h=int(h)


c=0
name1=''
h1=''
for i in f:
    if i == ' ':
       break
    c=c+1
for i in range (0,c):
    name1=name1+str(f[i])
for i in range (c+1,len(f)):
    h1=h1+str(f[i])
h1=int(h1)


print(name,h)
print(name1,h1)
