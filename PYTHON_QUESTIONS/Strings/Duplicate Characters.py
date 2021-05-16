# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
def printCountDuplicates(s):
    dict={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    for i in dict:
        if dict[i]>1:
            print("{}, count={}".format(i,dict[i]))

printCountDuplicates("geeksforgeeks")




