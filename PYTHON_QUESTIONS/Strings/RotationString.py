# Theory -> https://www.codesdope.com/blog/article/checking-if-strings-are-rotations-of-each-other/
# Practice -> https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

def areRotations(str1, str2):

    if len(str1)!=len(str2):
        print('Not rotation')

    temp=str1+str1

    if temp.count(str2)>0:
        print('Rotated')
    else:
        print('Not rotated')

areRotations("ABACD","CDABA")