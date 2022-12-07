class Dir:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        
        self.parent = parent
        if self.parent is None:
            Dir.home = self
        self.size = size
        self.children = {}
        self.contained = 0
    
    def add(self, child, direct=True):
        if direct:
            self.children[child.name] = child
        
        self.contained += child.size
        if self.parent is not None:
            self.parent.add(child, False)

    def Tree(self, depth=0):
        if self.contained == 0:
            print(f"{'  ' * depth}- {self.name} (file, size={self.size})")
        else: 
            print(f"{'  ' * depth}- {self.name} (dir, sum={self.contained})")
            for child in self.children.values():
                Dir.Tree(child, depth + 1)

def get_small_dirs(pwd, size):
    small_dirs = []
    for child in pwd.children.values():
        if child.contained <= size and child.contained != 0:
            small_dirs.append(child)
        small_dirs.extend(get_small_dirs(child, size))
    return small_dirs

def get_big_dirs(pwd, size):
    big_dirs = []
    for child in pwd.children.values():
        if child.contained > size and child.contained != 0:
            big_dirs.append(child)
        big_dirs.extend(get_big_dirs(child, size))
    return big_dirs


pwd = Dir("/")
with open("input") as history:
    for line in history.readlines()[1:]:
        words = line.split()
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    pwd = pwd.parent
                    continue
                if words[2] not in pwd.children:
                    pwd.add(Dir(words[2], pwd))
                pwd = pwd.children[words[2]]
                continue
            elif words[1] == "ls":
                ls = True
                continue
        else:
            if words[0] == "dir":
                pwd.add(Dir(words[1], pwd))
            else:
                pwd.add(Dir(words[1], pwd, int(words[0])))
            continue

Dir.home.Tree()
print(sum([dir.contained for dir in get_small_dirs(Dir.home, 100_000)]))

full_size = 70_000_000
needed_free = 30_000_000
taken = Dir.home.contained
unused = full_size - taken
to_free = needed_free - unused

print(min([dir.contained for dir in get_big_dirs(Dir.home, to_free)]))
