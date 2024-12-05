class Node:
    def __init__(self, value):
        self.value = value
        self.nodes_before = []
        self.nodes_after = []

    def add_before(self, node):
        self.nodes_before.append(node)

    def add_after(self, node):
        self.nodes_after.append(node)

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value


class Order:
    def __init__(self, rules):
        self.rules = rules
        self.nodes = {}
        self._generate_nodes()

    def _generate_nodes(self):
        for rule in self.rules:
            rule = rule.strip().split("|")
            first = rule[0]
            second = rule[1]

            if first not in self.nodes:
                self.nodes[first] = Node(first)
            if second not in self.nodes:
                self.nodes[second] = Node(second)

            self.nodes[first].add_after(self.nodes[second])
            self.nodes[second].add_before(self.nodes[first])


rules = []
with open("input") as f:
    lines = f.readlines()
    updates = []
    for line in lines:
        if line == "\n":
            continue
        if "|" in line:
            rules.append(line)
        else:
            updates.append(line)

order = Order(rules)

correct_updates = []
for update in updates:
    update = update.strip().split(",")

    in_order = True

    for i in range(len(update)):
        node = order.nodes.get(update[i])

        for n in range(i + 1, len(update)):
            node_after = order.nodes.get(update[n])
            if node_after not in node.nodes_after:
                in_order = False
                break

    if in_order:
        correct_updates.append(update)

sum = 0
for update in correct_updates:
    mid = len(update) // 2
    sum += int(update[mid])

print(sum)
