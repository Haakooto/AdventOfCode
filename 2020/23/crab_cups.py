class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{self.prev.val} -> {self.val} -> {self.next.val}"

    def __add__(self, cnt):
        this = self
        for _ in range(cnt):
            this = this.next
        return this


class Linked_list:
    def __init__(self, vals):
        self.nodes = {}
        self.nodes[vals[0]] = (prev := Node(vals[0]))
        for val in vals[1:]:
            self.nodes[val] = (this := Node(val, prev))
            prev.next = this
            prev = this
        this.next = (first := self.nodes[vals[0]])
        first.prev = this

    def __getitem__(self, key):
        return self.nodes[key]

    def move(self, key, dest):
        subj = self[key]
        subj.prev.next = subj.next
        subj.next.prev = subj.prev

        obj = self[dest]
        subj.next = obj.next
        subj.prev = obj
        obj.next.prev = subj
        obj.next = subj


def sim(cups, iterations):
    LL = Linked_list(cups)
    current = LL[cups[0]]
    for _ in range(iterations):
        picked = [(current + i).val for i in (1, 2, 3)]
        dest = len(cups) if current.val == 1 else current.val - 1
        while dest in picked:
            dest = len(cups) if dest == 1 else dest - 1
        while picked != []:
            LL.move(picked.pop(), dest)
        current = current.next
    return LL[1]


cups = "158937462"
# cups = "389125467"
cups = [int(i) for i in cups]

one = sim(cups, 100)
res = ""
while (this := one + len(res) + 1) != one:
    res += str(this.val)
print(res)

one = sim(cups + list(range(10, 10 ** 6 + 1)), 10 ** 7)
print((one + 1).val * (one + 2).val)