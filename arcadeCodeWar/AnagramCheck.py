def anagram_solution(s1,s2):
    if len(s1) == len(s2): 
        for i in range(len(s1)):
            if s1[i] in s2:
                return True
    else:
        return False

#complexity O(n)

print(anagram_solution('python','typhon'))