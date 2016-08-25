from PIL import Image
imgname="static_qr_code_without_logo.jpg"
img=Image.open(imgname)
s=''
f=[]
c=0
v=0
b=[8,9,10,11,12]
for i in range(40,249,10):
    for j in range (40,249,10):
        a=img.getpixel((i,j))
        if c == 8:
            f.append(a)
        a=str(a)
        s=s+a

        v=v+1
    print(s)
    s=''
    c=c+1
print(f)
d=[1,0,1,0,1]
m=[]
print(f[0],f[1],f[2],f[3],f[4])
for i in range (0,5):
    if d[i]==f[i]:
        m.append(0)
    else:
        m.append(1)
    print(i)
print(m)
l=[0,0,0]
r=0
t=0
y=0
u=0
i=''
r=str(img.getpixel((289,289)))
t=str(img.getpixel((288,289)))
if int(t) == 1:
    t='0'
else:
    t='1'
y=str(img.getpixel((289,288)))
if int(y) == 1:
    y='0'
else:
    y='1'
u=str(img.getpixel((288,288)))
if int(u) == 1:
    u='0'
else:
    u='1'
i=r+t+y+u
print(i)
r=str(img.getpixel((289,287)))
t=str(img.getpixel((288,287)))
y=str(img.getpixel((289,286)))
if int(y) == 1:
    y='0'
else:
    y='1'
u=str(img.getpixel((288,286)))
if int(u) == 1:
    u='0'
else:
    u='1'
i=i+r+t+y+u

print(i)
i=chr(int(i,2))
print(i)


