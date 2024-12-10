class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, numbers, test_value):
        self.root = Node(numbers[0])
        self.test_value = test_value
        self.numbers = numbers
        self.is_valid = False

        self.build_tree(self.root, 1)

    def build_tree(self, node, index):
        if index == len(self.numbers):
            if node.value == self.test_value:
                self.is_valid = True
            return

        # Left node keeps + operation and right node keeps * operation
        if node.value + self.numbers[index] <= self.test_value:
            node.left = Node(self.numbers[index]+node.value)
            self.build_tree(node.left, index + 1)

        if node.value * self.numbers[index] <= self.test_value:
            node.right = Node(self.numbers[index]*node.value)
            self.build_tree(node.right, index + 1)


with open("input") as f:
    lines = f.readlines()

    valid_count = 0
    for line in lines:
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split(' ')))

        tree = Tree(numbers, test_value)
        if tree.is_valid:
            valid_count += test_value

    print(valid_count)


