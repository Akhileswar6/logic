def anagram(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower() 

    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for i in s1:
        freq[i] = freq.get(i, 0) + 1

    for i in s2:
        if i not in freq:
            return False
        freq[i] -= 1

    return all(value == 0 for value in freq.values())  

print(anagram("anagram", "nagaram"))
