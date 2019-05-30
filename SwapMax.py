#!/usr/bin/env python3

# # First version


class Solution:
    def maximum_swap(self, num: int) -> int:
        digit_list = list(str(num))
        mx_index = digit_list.index(max(digit_list))
        digit_list[0], digit_list[mx_index] = digit_list[mx_index], digit_list[0]

        result = ''
        for i in digit_list:
            result += i

        return result


solution = Solution()
print(solution.maximum_swap(234))  # 432
print(solution.maximum_swap(2736))  # 7632
print(solution.maximum_swap(9973))  # 9973
print(solution.maximum_swap(35995))  # 99553

# # Second Version - Best one

# class Solution:
#     def maximum_swap(self, num: int) -> int:
#         digit_list = list(str(num))
#         result = ''
#         while len(digit_list) > 0:
#             mx_index = digit_list.index(max(digit_list))
#             digit_list[0], digit_list[mx_index] = digit_list[mx_index], digit_list[0]
#             result += digit_list.pop(0)

#         return result


# solution = Solution()
# print(solution.maximum_swap(234))  # 432
# print(solution.maximum_swap(2736))  # 7632
# print(solution.maximum_swap(9973))  # 9973
# print(solution.maximum_swap(35995))  # 99553
