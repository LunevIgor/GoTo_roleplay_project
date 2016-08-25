file =open('names.txt','r')
players_name_list=list(file.readline())
players_name_list.pop(0)
players_name_list.pop(1)
players_name_list.pop(0)
a=players_name_list[0]
b=''
while a!=' ':
    b=b=a
    players_name_list.pop(0)
    a=players_name_list[0]
players_name_list.pop(0)
s=int(b)
print(s)
f=''
c=1

print(players_name_list)
for i in range(0,s):
    f=''
    c=0
    if len(players_name_list)!=0:
        a=players_name_list[0]
    while a!=' ':
        f=f+a
        c=c+1
        if len(players_name_list)>0:
            players_name_list.pop(0)
            if len(players_name_list)>0:
                a=players_name_list[0]
        if len(players_name_list)==0:
            break
    if len(players_name_list)>0:
        players_name_list.pop(0)
    print(f)

