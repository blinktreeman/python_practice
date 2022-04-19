# 2. Найти максимальное из пяти чисел

nums = [1, 5 , 6 , 9, 0]
max = nums[0]
for i in nums:
    if i > max: max = i;
print('Максимальное число {}' .format(max))