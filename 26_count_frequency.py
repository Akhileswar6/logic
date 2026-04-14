n = input().split()
freq = {}
max_count = 0
most_repeated_word = " "
for i in n:
    freq[i] = freq.get(i,0) + 1

for j in freq:
    if freq[j] > max_count:
        max_count = freq[j]
        most_repeated_word = j

print(most_repeated_word)
print(max_count)


    

    
    


