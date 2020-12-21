ingredients = {}
allergens = {}

for food in open("input").read().strip().splitlines():
    ingreds, allergs = food.split(" (contains ")
    ingreds = ingreds.split(" ")
    allergs = allergs[:-1].split(", ")
    for allerg in allergs:
        if allerg not in allergens:
            allergens[allerg] = set(ingreds)
        else:
            allergens[allerg] &= set(ingreds)
    for ingred in ingreds:
        if ingred not in ingredients:
            ingredients[ingred] = 1
        else:
            ingredients[ingred] += 1

for _ in range(100):
    for allerg in allergens:
        if len(allergens[allerg]) == 1:
            for other in allergens:
                if allerg != other:
                    allergens[other] -= allergens[allerg]

allergs = sorted(list(allergens.keys()))
ingred_with_allergens = [next(iter(allergens[allerg])) for allerg in allergs]

num = 0
for ingred, cnt in ingredients.items():
    if ingred not in ingred_with_allergens:
        num += cnt

print(num)
print(",".join(ingred_with_allergens))
