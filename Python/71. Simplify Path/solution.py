class Solution:
    def simplifyPath(self, path: str) -> str:

        # 1. single dot (".") : stay at the current dire
        # 2. double dot ("..") :
        #   2.1 stack is empty: stay at the current dire which shoudld be the root dire
        #   2.2 stack is not empty: go one level up -> pop the top item in stack out
        # 3. empty : stay at the current dire
        # 4. other : go to the deeper dire named by this string -> push the curr item on the top of stack
        file = path.split('/')
        stack = []
        for loc in file:
            if loc == '.' or loc == '':
                continue
            elif loc == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(loc)
        return '/' + "/".join(stack)

if __name__ == '__main__':
    s = Solution()
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/home//foo/") == "/home/foo"