
class Node:
    def __init__(self):
        self.left_kid = None
        self.right_kid = None
        self.key = 0
        self.value = 0
        self.parent = None


def add(v: Node, x: int):
    assert v != None, 'v == None in add'
    ## changes root
    if v.key == x:
        return
    elif v.key > x:
        if v.left_kid == None:
            v.left_kid = Node()
            v.left_kid.key = x
            v.left_kid.value = x
            v.left_kid.parent = v
        else:
            add(v.left_kid, x)
    else:
        if v.right_kid == None:
            v.right_kid = Node()
            v.right_kid.key = x
            v.right_kid.value = x
            v.right_kid.parent = v
        else:
            add(v.right_kid, x)


def get_min(v: Node) -> Node:

    assert v != None, 'v == None in get min'

    start = v

    while True:
        if start.left_kid != None:
            start = start.left_kid
        else:
            break

    return start


def remove(v: Node, x: int):

    def change_parents_link(new_v):
        if not x_is_root:
            if x_Node.parent.left_kid != None:
                if x_Node.key == x_Node.parent.left_kid.key:  # ===========
                    x_Node.parent.left_kid = new_v
            else:  # => right_kid != None
                if x_Node.key == x_Node.parent.right_kid.key:
                    x_Node.parent.right_kid = new_v  # ===========
                else:
                    print("assert")

    x_Node = find(v, x)

    if x_Node != None:

        x_is_root = True
        if x_Node.parent != None:
            x_is_root = False

        if x_Node.left_kid != None and x_Node.right_kid != None:
            min_Node = get_min(x_Node.right_kid)

            remove(min_Node, min_Node.key)

            min_Node.parent.left_kid = min_Node.right_kid
            min_Node.right_kid.parent = min_Node.parent

            min_Node.parent = x_Node.parent
            min_Node.right_kid = x_Node.right_kid
            min_Node.left_kid = x_Node.left_kid

            change_parents_link(min_Node)

            x_Node.right_kid.parent = min_Node
            x_Node.left_kid.parent = min_Node

        elif x_Node.left_kid != None:
            x_Node.left_kid.parent = x_Node.parent
            change_parents_link(x_Node.left_kid)

        elif x_Node.right_kid != None:
            x_Node.right_kid.parent = x_Node.parent
            change_parents_link(x_Node.right_kid)

        else:
            if x_is_root: # x_Node это корень и у нее нет ниодного ребенка
                v = None
            else:
                change_parents_link(None)


def find(v: Node, x: int) -> Node:
    start = v

    while start != None:
        if start.key == x:
            break
        elif start.key > x:
            start = start.left_kid
        else:
            start = start.right_kid

    return start

def next_of(v: Node, x: int) -> Node: # min y > x
    assert v != None, 'v == None in next_of'

    start = v
    ans = None

    while start != None:
        if start.key > x:
            ans = start
            start = start.left_kid
        else:
            start = start.right_kid

    return ans

def prev_of(v: Node, x: int) -> Node: # max y < x
    assert v != None, 'v == None in next_of'

    start = v
    ans = None

    while start != None:
        if start.key < x:
            ans = start
            start = start.right_kid
        else:
            start = start.left_kid

    return ans

root = None

import sys

f_in = sys.stdin

with f_in:
    lines = f_in.readlines()
    for line in lines:
        line = line.strip()
        [oper, x] = line.split()

        if oper == 'insert':
            if root == None:
                root = Node()
                root.key = int(x)
                root.value = int(x)
            else:
                add(root, int(x))

        elif oper == 'delete':
            remove(root, int(x))

        elif oper == 'exists':
            x_Node = find(root, int(x))
            if x_Node == None:
                print('false')
            else:
                print('true')

        elif oper == 'next':
            next = next_of(root, int(x))
            if next == None:
                print('none')
            else:
                print(next.key)

        elif oper == 'prev':
            prev = prev_of(root, int(x))
            if prev == None:
                print('none')
            else:
                print(prev.key)

