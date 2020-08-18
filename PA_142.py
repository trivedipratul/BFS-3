#Time Complexity - O(n * 2^n)
#Space Complexity - O(n)
from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        flag = False
        def isValid(s):
            count = 0
            for i in s:
                if i == '(':
                    count = count + 1
                elif i == ')':
                    count = count - 1
                if count == -1:
                    return False
            return count == 0
        
        ans = []
        vis = set()
        q = deque()
        #vis.add(s)
        q.append(s)
        while q:
            temp = q.popleft()
            #print(temp)
            if isValid(temp):
                flag = True
                ans.append(temp)
            if flag == False:
                for i in range(len(temp)):
                    if temp[i] in '()':
                        t1 = temp[0:i] + temp[i+1:]
                        if t1 not in vis:
                            vis.add(t1)
                            q.append(t1)
        return(ans)