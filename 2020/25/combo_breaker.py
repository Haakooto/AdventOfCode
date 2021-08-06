card_pk = 15628416
door_pk = 11161639
# card_pk = 5764801
# door_pk = 17807724

card_loop = 0
door_loop = 0
moder = 20201227

i = 0
n = 1
subj_0 = 7
while True:
    n *= subj_0
    n %= moder
    i += 1
    if n == card_pk:
        card_loop = i
        if door_loop:
            break
    if n == door_pk:
        door_loop = i
        if card_loop:
            break

enc_key_door = 1
for _ in range(door_loop):
    enc_key_door *= card_pk
    enc_key_door %= moder
print(enc_key_door)

# enc_key_card = 1
# for _ in range(card_loop):
#     enc_key_card *= door_pk
#     enc_key_card %= moder
# print(enc_key_card)


