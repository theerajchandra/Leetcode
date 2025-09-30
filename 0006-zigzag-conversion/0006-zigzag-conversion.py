class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #Base case
        if numRows == 1:
            return s

        #For first and last row
        result = ""
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row, len(s), increment):
                result += s[i]
                #middle row
                if (row > 0 and row < numRows - 1 and 
                    i + increment - 2 * row < len(s)):
                    result += s[i + increment - 2 * row]
                
        return result

