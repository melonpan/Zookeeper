group_1, group_2, group_3 = int(input()), int(input()), int(input())

group_1 = group_1 // 2 + group_1 % 2
group_2 = group_2 // 2 + group_2 % 2
group_3 = group_3 // 2 + group_3 % 2

total_desks = group_1 + group_2 + group_3

print(total_desks)

# old, ugly code (that works)
# if group_1 % 2 != 0:
#     group_1 = group_1 // 2 + 1
# else:
#     group_1 = group_1 // 2
#
# if group_2 % 2 != 0:
#     group_2 = group_2 // 2 + 1
# else:
#     group_2 = group_2 // 2
#
# if group_3 % 2 != 0:
#     group_3 = group_3 // 2 + 1
# else:
#     group_3 = group_3 // 2
