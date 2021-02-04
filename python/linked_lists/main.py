from stack import Stack
from deque import Deque

def test_stack():

    stack_no_items = Stack()
    print(stack_no_items)
    try:
        print(stack_no_items.index(1))
    except Exception as e:
        print(repr(e))
    print(f"find non-existant value: {stack_no_items.find('a')}")

    try:
        stack_no_items.pop()
    except Exception as e:
        print(repr(e))

    print("")

    stack_one_item = Stack()
    stack_one_item.push('a')
    print(stack_one_item)
    print(stack_one_item.index(0))
    try:
        print(stack_one_item.index(1))
    except Exception as e:
        print(repr(e))
    print(f"find non-existant value: {stack_one_item.find('b')}")
    print(f"find existing value: {stack_one_item.find('a')}")
    print(f"pop: {stack_one_item.pop()}")
    print(stack_one_item)

    print("")

    stack_three_items = Stack()
    stack_three_items.push('b')
    stack_three_items.push(1)
    stack_three_items.push(2)
    print(stack_three_items)
    print(f"index 1: {stack_three_items.index(1)}")
    print(f"index 2: {stack_three_items.index(2)}")
    try:
        print(stack_three_items.index(3))
    except Exception as e:
        print(repr(e))
    print(f"find non-existant value: {stack_three_items.find('a')}")
    print(f"find existing value: {stack_three_items.find(2)}")
    print(f"peek: {stack_three_items.peek()}")
    print(f"pop: {stack_three_items.pop()}")
    print(stack_three_items)
    print(f"pop: {stack_three_items.pop()}")
    print(stack_three_items)
    print(f"peek: {stack_three_items.peek()}")

def test_deque():

    d = Deque()

    d.insert_head(1)
    print(d)
    d.insert_tail(2)
    print(d)
    print(f"pop tail: {d.pop_tail()}")
    print(d)
    print(f"pop head: {d.pop_head()}")
    print(f"should be empty: {d}")
    d.insert_tail(1)
    print(d)
    d.insert_head(2)
    print(d)
    print(f"pop head: {d.pop_head()}")
    print(d)
    print(f"pop tail: {d.pop_tail()}")
    print(f"should be empty: {d}")
    d.insert_tail('a')
    d.insert_head('b')
    d.insert_head('c')
    d.insert_head('d')
    print(d)
    print(f"new deque reverse: {d.reverse()}")
    print(d)
    print("reverse in place:")
    d.reverse_in_place()
    print(d)



def main():
    # test_stack()
    test_deque()


if __name__ == '__main__':
    main()
