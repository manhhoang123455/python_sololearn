# from itertools import count

# for i in count(5):
#     print(i)
#     if i >=11:
#         break

# from itertools import product
# a={1, 2}
# print(len(list(product(range(3), a))))

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))


a = (lambda x: x * (x+1)) (6)

print(a)