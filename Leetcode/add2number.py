
class Solution:

    def add2numbers(self, l1, l2):

        result = []
        carry = 0

        i = 0

        while i < len(l1) or i < len(l2) or carry:

            val1 = l1[i] if i < len(l1) else 0
            val2 = l2[i] if i < len(l2) else 0

            val = val1 + val2 + carry

            carry = val // 10
            digit = val % 10

            result.append(digit)

            i += 1

        return result


f = Solution()
a = f.add2numbers([2, 4, 3], [5, 6, 4])

print(a)

