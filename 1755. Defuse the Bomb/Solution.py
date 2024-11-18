class Solution(object):
    def decrypt(self, code, k):
        
        def next(c, l):
            if l < len(c) - 1:
                l = l + 1
            else:
                l = 0
            return l
        def prev(c, l):
            if l == 0:
                l = len(c) - 1
            else:
                l = l - 1
            return l
        if k == 0:
            result = [0]*len(code)
            return result
        result = []
        if k > 0:
            for i in range(len(code)):
                curr = i
                val = 0
                for j in range(k):
                    curr = next(code, curr)
                    val += code[curr]
                result.append(val)
            return result
        if k < 0:
            for i in range(len(code)):
                curr = i
                val = 0
                for j in range(abs(k)):
                    curr = prev(code, curr)
                    val += code[curr]
                result.append(val)
            return result

        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        