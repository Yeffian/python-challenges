class Tree:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.value)
    

# traverse recursively
def total(tree):
    if tree is None:
        return 0
    
    return total(tree.left) + total(tree.right) + tree.value

def print_tree(tree):
    if tree is None:
        return 0

    print(tree.value, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    if tree is None:
        return 0
    
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.value, end=' ')

def print_tree_inorder(tree):
    if tree is None:
        return None
    
    print_tree_inorder(tree.left)
    print(tree.value, end=' ')
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree is None: 
        return
    
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.value))
    print_tree_indented(tree.left, level+1)

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False
    
def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)
        get_token(token_list, ")")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)

    if get_token(token_list, "*"):
        b = get_product(token_list)     
        return Tree("*", a, b)
    else:
        return a
    
def get_sum(token_list):
    a = get_product(token_list)

    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    else:
        return a
    
def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise ValueError("Missing closing parenthesis")
        else:
            return x
    else:
        # idk what goes here

# tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
# print_tree(tree)
# print('\n')
# print_tree_postorder(tree)
# print('\n')
# print_tree_inorder(tree)
# print('\n')
# print_tree_indented(tree)
