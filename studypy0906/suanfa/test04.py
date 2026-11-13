"""
栈的应用
给定一个只包括“（”“）”的字符串s，判断字符串是否有效
有效字符串需满足
左括号必须用相同类型的右括号闭合
左括号必须以正确的顺序闭合
每个右括号都有一个对应的相同类型的左括号
"""

class Solution:
    def isValid(self, s:str) -> bool:
        #定义一个栈
        stack = []
        for char in s:
            match char:
                case '(' | '[' | '{':
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
        return True if not stack else False


print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))