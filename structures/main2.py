#Для целого числа k от 1 до 99 напечатать фразу «Мне k лет»,
# учитывая при этом, что при некоторых значениях k слово «лет» надо заменить на слово «год» или «года». Например, 11 лет, 22 года, 51 год.

for i in range(1, 100):
    if i == 1 or i == 21 or i == 31 or i == 41 or i == 51 or i == 61 or i == 71 or i == 81 or i == 91:
        print(f"Мне {i} год.")
    elif (i % 10 == 2 and i != 12) or (i % 10 == 3 and i != 13) or (i % 10 == 4 and i != 14):
        print(f"Мне {i} годa.")
    elif (i % 10 == 5) or (i % 10 == 6) or (i % 10 == 7) or (i % 10 == 8) or (i % 10 == 9) or (i % 10 == 0) or (i % 10 == 1) or (i % 10 == 2) or (i % 10 == 3) or (i % 10 == 4)\
            or (i == 12) or (i == 13) or (i == 14):
        print(f"Мне {i} лет.")