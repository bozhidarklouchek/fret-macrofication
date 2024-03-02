class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def calculate_coordinates(root, x, y, level, spacing):
    if root is None:
        return
    
    # Assign coordinates to the current node
    root.x = x
    root.y = y
    y -= spacing  # Adjust y for next level
    
    # Recursively calculate coordinates for children
    child_count = len(root.children)
    if child_count > 0:
        # Calculate total width required by children
        total_width = (child_count - 1) * spacing
        # Calculate starting x-coordinate for children
        start_x = x - total_width / 2
        for child in root.children:
            calculate_coordinates(child, start_x, y, level + 1, spacing)
            start_x += spacing

def draw_tree(root):
    if root is None:
        return
    # Calculate coordinates with initial values
    calculate_coordinates(root, 0, 0, 0, 50)
    # Print coordinates of each node
    print("Node\tX\tY")
    print("Root\t{}\t{}".format(root.x, root.y))
    print_tree(root)

def print_tree(node):
    for child in node.children:
        print("{}\t{}\t{}".format(child.value, child.x, child.y))
        print_tree(child)

# Example usage:
root = TreeNode("A")
root.children = [TreeNode("B"), TreeNode("C"), TreeNode("D")]
root.children[0].children = [TreeNode("E"), TreeNode("F")]
root.children[2].children = [TreeNode("G")]
draw_tree(root)
