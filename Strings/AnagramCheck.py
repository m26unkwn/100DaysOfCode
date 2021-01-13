#Program to Check wheter a string is anagram or not

def anagramCheck( string1, string2):
    str1=sorted(string1)
    str2=sorted(string2)
    if len(string1) == len(string2):
        for i in range(len(string1)):
            if str1[i]!= str2[i]:
                return True
            else:
                return False
    else:
        return False
        


print(anagramCheck('1122', '1132'))