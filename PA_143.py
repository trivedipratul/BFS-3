#Time Complexity - O(n)
#Space Complexity - O(n)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        d = dict()
        q = deque()
        q.append(node)
        while q:
            temp = q.popleft()
            if temp not in d:
                d[temp] = Node(temp.val)
            #node = d[temp]
            for nei in temp.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    q.append(nei)
                d[temp].neighbors.append(d[nei])
        
        return(d[node])