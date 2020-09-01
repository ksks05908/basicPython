# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
rating = [7, 5, 3, 3, 2]
print(f'Рейтинг: {rating}')
new_el = int(input('Введите новый элемент рейтинга: '))
for i in range(len(rating)):
    if new_el < rating[-1]:
        rating.append(new_el)
        break
    elif new_el > rating[0]:
        rating.insert(1, new_el)
        break
    elif (rating[i] > new_el or rating[i] == new_el) and rating[i + 1] < new_el:
        rating.insert(i + 1, new_el)
        break
print(rating)

