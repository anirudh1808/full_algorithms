
import heartrate
import snoop
nestedList = ['comfort', 'balloon', ['grind', 'trampl', ['music', 'consign'], [['crate', 'unusual'], 'press', 'heal'], 'majestic'], 'string', 'study', ['trampl', 'far', ['forgetful', [1, 'dispose'], 'jar', 'absorbing'], 'shatter', ['voracious'], ['scissors', ['disastrous'], ['banana'], 'implicate'], 'tangy', 'tangy', ['toothpaste', ['way', 'weary'], [400, ['resemble', 'leather', 'impose'], 'impose']], 'blue-eyed', [[['coast']]] ,45]]

# Requirement: Find a way to bring in all the nested list values to one single list.


heartrate.trace(browser=True)
@snoop
def recursiveList(nestedList ,lst):

    if lst is None :
        lst =[]

    if len(nestedList )==0:
        return lst

    for l in nestedList :
        if isinstance(l ,list):
            recursiveList(l ,lst)
        else :
            lst.append(l)
    return lst

l=recursiveList(nestedList,None)

print(l)
# for l in nestedList :
#   print(l,type(l))