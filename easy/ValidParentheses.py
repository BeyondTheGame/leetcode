class Solution:
    def isValid(self, s):
        """
        没有考虑(大，中，小)括号的等级大小，例如({})这样的是否为非法
        :type s: str
        :rtype: bool
        """
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in pairs:
                if len(stack) != 0 and pairs[char] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:  # stack is not null
            return False
        else:
            return True

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                if pairs[stack.pop()] != char:
                    return False
        return len(stack) == 0
    def isValid3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if stack == []:
                    return False
                elif char == ')':
                    if stack.pop() != '(':
                        return False
                elif char == ']':
                    if stack.pop() != '[':
                        return False
                elif char == '}':
                    if stack.pop() != '{':
                        return False

        return stack == []
