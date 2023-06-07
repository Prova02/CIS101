#problem-1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
X = 12
Y = 18
print(gcd(X, Y))


#problem-2

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
def insert_node(root, value):
        if root is None:
            return Node(value)
        else:
            if root.value < value:
                root.right = insert_node(root.right, value)
            else:
                root.left = insert_node(root.left, value)
        return root
def is_leaf(node):
    return node.left is None and node.right is None
def check_leaf_nodes(root):
    if root is None:
            return []
    elif is_leaf(root):
        if root.value % 2 == 0:
            return ['Even']
        else:
            return ['Odd']
    else:
        return check_leaf_nodes(root.left) + check_leaf_nodes(root.right)

root = Node(10)
insert_node(root, 5)
insert_node(root, 13)
insert_node(root, 3)
insert_node(root, 7)
insert_node(root, 14)

leaf_nodes = check_leaf_nodes(root)
print(leaf_nodes)


#

#problem-3

class GraphMatrix:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
def printSinkNodes(self):
    sink_nodes = []
    for i in range(self.V):
        is_sink = True
    for j in range(self.V):
        if self.graph[i][j] == 1:
            is_sink = False
        break
    if is_sink:
        sink_nodes.append(i)
    return sink_nodes
graph_matrix = [
[0, 1, 1, 0],
[0, 0, 1, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
]
graph_obj = GraphMatrix(graph_matrix)
sink_nodes = graph_obj.printSinkNodes()
print("Sink nodes: ", sink_nodes)

