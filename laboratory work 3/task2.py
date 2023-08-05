# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, razdel=","):
    first_group_split = group1.split(razdel)
    second_group_split = group2.split(razdel)
    list_both = []
    for i in first_group_split:
        for j in second_group_split:
            if i == j:
                list_both.append(i)
    list_both.sort()
    return list_both

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
