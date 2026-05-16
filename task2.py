class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self._update_height(node)
        balance = self._balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, root, key):
        return self._insert(root, key)

    def find_sum(self, node):
        if node is None:
            return 0
        return node.key + self.find_sum(node.left) + self.find_sum(node.right)


def run():
    tree = AVLTree()
    root = None
    values = [20, 10, 30, 5, 15, 25, 35, 2, 7]

    for v in values:
        root = tree.insert(root, v)

    total_sum = tree.find_sum(root)

    print("=== Завдання 2 ===")
    print(f"Вузли дерева: {sorted(values)}")
    print(f"Сума всіх значень: {total_sum}")
    print(f"Перевірка (sum()): {sum(values)}")
