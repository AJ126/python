bob=(0,1,0,6,8,9)
alice=(1,0,5,7,2,0,9)
count=0
for i in bob:
    if i in alice:
        print(i)
