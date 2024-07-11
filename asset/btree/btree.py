from typing import Union

class BTreeNode:
    def __init__(self, minimum_degree:int, is_leaf:bool = False):
        self.minimum_degree = minimum_degree  # キーの数を決定する度数
        self.is_leaf = is_leaf
        self.keys:list[int] = []
        self.children:list[BTreeNode] = []  # 子ノードのリスト
    def traverse(self, level:int = 0):
        # 全てのノードを出力する
        print("Level", level, ":", " ".join(str(k) for k in self.keys))
        for i in range(len(self.keys)):
            if not self.is_leaf:
                self.children[i].traverse(level + 1)
        if not self.is_leaf:
            self.children[-1].traverse(level + 1)
    def search(self, search_key:int)->Union["BTreeNode", None]:
        # B-Treeの検索アルゴリズム
        i = 0
        while i < len(self.keys) and search_key > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == search_key:
            return self
        if self.is_leaf:
            return None
        return self.children[i].search(search_key)
    def insert_non_full(self, insert_key:int):
        # ノードがいっぱいでない場合の挿入
        i = len(self.keys) - 1
        if self.is_leaf:
            self.keys.append(None)
            while i >= 0 and self.keys[i] > insert_key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = insert_key
        else:
            while i >= 0 and self.keys[i] > insert_key:
                i -= 1
            if len(self.children[i + 1].keys) == 2 * self.minimum_degree - 1:
                self.split_child(i + 1, self.children[i + 1])
                if self.keys[i + 1] < insert_key:
                    i += 1
            self.children[i + 1].insert_non_full(insert_key)
    def split_child(self, split_index:int, child_node:"BTreeNode"):
        another_child_node = BTreeNode(child_node.minimum_degree, child_node.is_leaf)
        self.children.insert(split_index + 1, another_child_node)
        self.keys.insert(split_index, child_node.keys[self.minimum_degree - 1])
        another_child_node.keys = child_node.keys[self.minimum_degree:(2 * self.minimum_degree - 1)]
        child_node.keys = child_node.keys[0:(self.minimum_degree - 1)]
        if not child_node.is_leaf:
            another_child_node.children = child_node.children[self.minimum_degree:(2 * self.minimum_degree)]
            child_node.children = child_node.children[0:self.minimum_degree]

class BTree:
    def __init__(self, t:int):
        self.root = BTreeNode(t, True)
        self.t = t
    def traverse(self):
        if self.root is not None:
            self.root.traverse()
    def search(self, k:int)->Union["BTreeNode", None]:
        if self.root is None:
            return None
        else:
            return self.root.search(k)
    def insert(self, k:int):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            temp = BTreeNode(self.t, False)
            self.root = temp
            temp.children.insert(0, root)
            temp.split_child(0, root)
            temp.insert_non_full(k)
        else:
            root.insert_non_full(k)

if __name__ == "__main__":
    # Example usage:
    btree = BTree(3)  # B-Tree with minimum degree 3
    insert_keys = [45, 3, 29, 18, 12, 23, 46, 37, 30, 6,
                   41, 27, 4, 17, 1, 16, 5, 44, 48, 24,
                   39, 19, 34, 13, 2, 32, 50, 8, 21, 9]
    for i in range(len(insert_keys)):
        btree.insert(insert_keys[i])
        if (i + 1) % 1 == 0:
            print("Traversal step", i + 1, ":")
            btree.traverse()
