class Solution:
    """
        Valid paranthesis using python
    """
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

if __name__ == "__main__":
    input = "{{{[][]()()}}}"
    if Solution().isValid(input):
        print True
    else:
        print False
