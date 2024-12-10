class Node:
    def __init__(self, value):
        self.value = value
        self.summ = None
        self.multiplie = None
        self.concat = None

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

        # summ node keeps + operation and multiplie node keeps * operation
        if node.value + self.numbers[index] <= self.test_value:
            node.summ = Node(self.numbers[index]+node.value)
            self.build_tree(node.summ, index + 1)

        if node.value * self.numbers[index] <= self.test_value:
            node.multiplie = Node(self.numbers[index]*node.value)
            self.build_tree(node.multiplie, index + 1)

        if int(f"{node.value}{self.numbers[index]}") <= self.test_value:
            node.concat = Node(int(f"{node.value}{self.numbers[index]}"))
            self.build_tree(node.concat, index + 1)

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


