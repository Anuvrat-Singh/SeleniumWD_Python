class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a = sorted(input_arr)
        len_a = len(a)
        ideal_list = list(range(min(a), max(a)+1))
        # print (ideal_list)
        if a == ideal_list:
            return "1"
        else:
            return "0"


input_arr = [1,2,3,4,5]

sol = Solution()
s = sol.solve(input_arr)
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a = sorted(input_arr)
        len_a = len(a)
        ideal_list = list(range(min(a), max(a)+1))
        # print (ideal_list)
        if a == ideal_list:
            return "1"
        else:
            return "0"


input_arr = [1,2,3,4,5]

sol = Solution()
s = sol.solve(input_arr)

print(s)