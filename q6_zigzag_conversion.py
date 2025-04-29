class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        d = None
        r = 0
        for c in s:
            rows[r] += c
            if r == 0:
                d = 1
            elif r == numRows - 1:
                d = -1
            r += d

        return "".join(rows)


class hashNode:
    def __init__(self, item=0, next=None):
        self.item = item
        self.next = next


class hashMap:
    def __init__(self, length):
        self.length = length
        self.nodes = [None] * length
        self.last = [None] * length

    def add(self, item, row):
        new_node = hashNode(item)
        if not self.nodes[row]:
            self.nodes[row] = new_node
            self.last[row] = new_node
        else:
            last_node = self.last[row]
            last_node.next = new_node
            self.last[row] = new_node

    def get(self, row):
        current_node = self.nodes[row]
        str_list = []
        while current_node:
            str_list.append(current_node.item)
            current_node = current_node.next
        return ''.join(str_list)


class Solution:
    @staticmethod
    def _hashValue(index, row):
        n = 2 * row - 2
        value = index % n
        if value < row:
            return value
        return n - value

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        hm = hashMap(numRows)
        for i in range(len(s)):
            hash_value = self._hashValue(i, numRows)
            hm.add(s[i], hash_value)

        return_s = ''
        for r in range(hm.length):
            return_s += hm.get(r)

        return return_s


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        d = None
        r = 0
        for c in s:
            rows[r] += c
            if r == 0:
                d = 1
            elif r == numRows - 1:
                d = -1
            r += d

        return "".join(rows)


if __name__ == '__main__':
    hm = hashMap(4)
    hm.add('1', 0)
    hm.add('2', 0)
    print(hm.get(0))

    so = Solution()
    print(so._hashValue(6, 5))

    print(so.convert("PAYPALISHIRING", 4))
