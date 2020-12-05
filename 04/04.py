fields = {
    "byr": lambda s: 1920 <= int(s) <= 2002,
    "iyr": lambda s: 2010 <= int(s) <= 2020,
    "eyr": lambda s: 2020 <= int(s) <= 2030,
    "hgt": lambda s: hgt(s),
    "hcl": lambda s: hcl(s),
    "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda s: pid(s),
    "cid": lambda s: True,
}


def hgt(s):
    try:
        end = s[-2:]
        num = int(s[:-2])
    except:
        return False
    if end == "cm":
        return 150 <= num <= 193
    elif end == "in":
        return 59 <= num <= 76
    else:
        return False


def hcl(s):
    if s[0] != "#":
        return False
    for l in s[1:]:
        valid = False
        if 48 <= ord(l) <= 57:
            valid = True
        if 97 <= ord(l) <= 102:
            valid = True
        if not valid:
            return False
    return True


def pid(s):
    for l in s:
        if 48 <= ord(l) <= 57:
            continue
        return False
    return len(s) == 9


count = 0
passport = {i: False for i in list(fields.keys())[:-1]}
def validate(passport, count):
    if all(i == True for i in list(passport.values())):
        count += 1
    return count


with open("data.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        if line == "":
            count = validate(passport, count)
            passport = {i: False for i in list(fields.keys())[:-1]}
            continue
        for field in line.strip().split(" "):
            cat, val = field.split(":")
            passport[cat] = True  # first part
            # passport[cat] = fields[cat](val)  # second part
    count = validate(passport, count)
print(count)
