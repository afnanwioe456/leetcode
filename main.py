# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur = {(0, 0): 1}
    cur[(0, 0)] = min(cur[(0, 0)], 0)
    print(cur)
    l = [0, 0, 0, 0, 0, 0, 0, 0]
    l[2: 5] = [1] * 3
    print(l)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
