class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        result = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or i==k or j==k:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    number = digits[i]*100 + digits[j]*10 + digits[k]
                    result.add(number)
                    print(number)
        return len(result)

f = Solution()
a = f.totalNumbers([1,2,3,4])
print(a) 
