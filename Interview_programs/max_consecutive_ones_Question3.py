list=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
n=len(list)
def myfun(list,n):
    count=0
    result=0
    for i in range(0, n):
        if list[i]==1:
            count+=1
        else:
            if(count>result):
                result=count
            count=0
    return result
print(myfun(list,n))
