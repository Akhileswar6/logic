n = list(map(int, input().split()))
largest = n[0]
for num in n:
    if num > largest:
        largest = num

print(largest)