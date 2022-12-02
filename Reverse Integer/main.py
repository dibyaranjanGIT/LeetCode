class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            string_x = str(x)
            result = int(string_x[::-1])
            if -2 ** 31 < result < (2**31)-1:
                return result
            else:
                return 0
        else:
            num = x * -1
            string_x = str(num)
            result = int(string_x[::-1]) * -1
            if -2 ** 31 < result < (2*31)-1:
                return result
            else:
                return 0
       