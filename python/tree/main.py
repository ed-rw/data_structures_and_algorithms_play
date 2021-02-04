from tree import Tree

def main():
    t = Tree(1)
    t.add_node(t.root, 2)
    three_node = t.add_node(t.root, 3)
    four_node = t.add_node(t.root, 4)
    t.add_node(t.root, 5)
    t.add_node(three_node, 6)
    t.add_node(three_node, 7)
    t.add_node(three_node, 8)
    t.add_node(four_node, 9)
    t.add_node(four_node, 10)

    t.depth_first_traversal()
    print("")
    t.breadth_first_traversal()
    print("")


if __name__ == '__main__':
    main()
