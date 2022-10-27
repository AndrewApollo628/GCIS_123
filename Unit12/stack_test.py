#Author: Andrew Apollo 

import node_stack

def main():
    a_stack = node_stack.Stack()

    print(a_stack.is_empty())

    print(repr(a_stack))

    a_stack.push("a")
    a_stack.push("b")
    a_stack.push("c")
    print(repr(a_stack))

    print(a_stack.peak())
    a_stack.pop()
    a_stack.pop()
    print(repr(a_stack))

main()