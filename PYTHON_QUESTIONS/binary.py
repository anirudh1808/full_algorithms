k=3
n=8

lst=[]
def binary(i):
    if i==0:
        return
    binary(i//2)
    lst.append(i%2)

def numbers():
    global n,k,lst
    for i in range(n):
        binary(i)
        l1=[0]*(k-len(lst))
        if len(lst)>=1:
            l1=l1+lst

        last_element=None
        for x in l1:
            if x==last_element and last_element==1:
                break
            last_element=x
        else :
            print(l1)
        lst=[]


numbers()