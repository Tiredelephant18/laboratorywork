# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sigh_=','):
    list1 = str1.split(sigh_)
    list2 = str2.split(sigh_)
    list3 = []
    for x in list1:
        for y in list2:
            if x == y:
                list3.append(x)
    list3.sort()
    return list3


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
