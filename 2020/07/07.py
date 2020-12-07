rules = {}
containable = {}
with open("i") as file:
    for rule in file.readlines():
        words = rule.strip().split(" ")
        main_bag = " ".join(words[:2])
        rules[main_bag] = set()
        rest = " ".join(words[4:]).split(",")
        for sub in rest:
            if sub == "no other bags.":
                rules[main_bag].add(tuple((None, 0)))
                continue
            wrds = sub.strip().split(" ")
            cnt = int(wrds[0])
            bag = " ".join(wrds[1:3])
            rules[main_bag].add(tuple((bag, cnt)))
            try:
                containable[bag].add(main_bag)
            except:
                containable[bag] = set([main_bag])

def super_bags(bag, found=set()):
    try:
        for sup in list(containable[bag]):
            found.add(sup)
            found = super_bags(sup, found)
    except:
        pass
    finally:
        return found

def sub_bags(bag):
    if bag is None:
        return 0
    count = 0
    for sub, cnt in list(rules[bag]):
        count += (sub_bags(sub) + 1) * cnt
    return count

print(len(super_bags("shiny gold")))
print(sub_bags("shiny gold"))
