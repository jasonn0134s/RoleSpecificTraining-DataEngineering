numbers = [10,20,10,30,20,10,40]

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print(freq) 