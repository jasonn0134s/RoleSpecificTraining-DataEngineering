with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

print(nums)

print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))

count = 0
for n in nums:
    if n > 50:
        count += 1

print("Greater than 50:", count)