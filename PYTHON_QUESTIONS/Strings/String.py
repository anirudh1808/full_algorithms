s=["first2000 the hello first2000first","it is 9000first where first is second and second is first."]

lst=[]
for i in s:
    s1=""
    i=i+" "
    finalStr = ""
    for j in i :
        if not j.isspace():
            s1=s1+j
        else:
            if s1.find("first")!=-1:
                finalStr=finalStr+" "
            else :
                finalStr=finalStr+" "+s1
            s1=""
    lst.append(finalStr.strip())

print(lst)






