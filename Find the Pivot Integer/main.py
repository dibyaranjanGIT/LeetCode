class Solution:
    def pivotInteger(self, n: int) -> int:
        li = []
        for i in range(1, n+1):
            li.append(i)
        if len(li) == 1:
            return li[0]
        else:
            for i in range(n):
                a = sum(li[:i])
                b = sum(li[i-1:])
                if sum(li[:i]) == sum(li[i-1:]):
                    return li[i-1]
            else:
                return -1