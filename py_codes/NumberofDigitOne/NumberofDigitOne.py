class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n < 0:
            return 0
        ones, x = [0], 0
        while 10 ** x <= 0x7FFFFFFF:
            ones.append(ones[x] * 10 + 10 ** x)
            x += 1
        # print ones
        cnt, size = 0, len(str(n))
        for digit in str(n):
            digit = int(digit)
            size -= 1
            n -= digit * 10 ** size
            if digit > 1:
                cnt += digit * ones[size] + 10 ** size
            elif digit == 1:
                cnt += n + ones[size] + 1
        return cnt

test = Solution()
print test.countDigitOne(123)
