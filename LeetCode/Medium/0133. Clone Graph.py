"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        idea:
         - create new nodes using dfs
         - dfs takes an original node & copy it
        """

        # key = old, val = new
        nodeMap = {}

        def dfs(orig_node):
            if orig_node in nodeMap:
                return nodeMap[orig_node]
            elif orig_node == None: 
                return None
            
            new_node = Node(orig_node.val)
            nodeMap[orig_node] = new_node

            for neighbor in orig_node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)

            return new_node
        
        return dfs(node)

        
