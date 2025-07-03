# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return
            
        nodes = {}
        res = Node(0)
        stack = [(node, res)]

        while stack:
            node, prev = stack.pop()
            if node.val in nodes:
                prev.neighbors.append(nodes[node.val])
                continue
            node_copy = Node(node.val)
            prev.neighbors.append(node_copy)
            nodes[node.val] = node_copy
            for nei in node.neighbors:
                stack.append((nei, node_copy))
        
        return res.neighbors[0]

    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None

        visited = {}

        def dfs(node: Node):
            val = node.val
            if val in visited:
                return visited[val]
            node_copy = Node(val)
            visited[val] = node_copy
            for nei in node.neighbors:
                node_copy.neighbors.append(dfs(nei))
            return node_copy
        
        return dfs(node)

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]
    sol = Solution()
    sol.cloneGraph(n1)