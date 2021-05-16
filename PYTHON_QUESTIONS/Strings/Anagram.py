# https://practice.geeksforgeeks.org/problems/print-anagrams-together/1

'''
words[] = [act,god,cat,dog,tac]
Output
[[act,cat,tac],[god,dog]]
'''

def groupAnagram(s):
    dict={}
    for i in s:
        x=''.join(sorted(i))
        if x not in dict:
            dict[x]=[i]
        else:
            dict[x].append(i)
    lst=[]
    for i in dict:
        lst.append(dict[i])
    print(lst)

groupAnagram(['act','god','cat','dog','tac'])