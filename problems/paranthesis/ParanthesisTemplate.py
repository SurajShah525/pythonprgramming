class Solution:
    """
        Valid paranthesis using python
    """
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            ?
        return stack == []

if __name__ == "__main__":
    input = "{{{[][]()()}}}"
    if Solution().isValid(input):
        print True
    else:
        print False

