# def count_letters(text):
#     dict_ = {}
#     text.lower()
#     for n in range(0, len(text)):
#         if text[n].isalpha():
#             dict_[text[n]] = 0
#     for n in range(0, len(text)):
#         dict_[text[n]] = dict_[text[n]] + 1
#         return dict_


# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_ = {}
    text = text.lower()
    uniq_words = str(set(text))
    for k in range(0, len(uniq_words)):
        if uniq_words[k].isalpha():
            dict_[uniq_words[k]] = 0
    for n in range(0, len(text)):
        for k in range(0, len(uniq_words)):
            if text[n] == uniq_words[k] and text[n].isalpha():
                dict_[uniq_words[k]] = dict_[uniq_words[k]] + 1
    return dict_


def calculate_frequency(dict0_, text):
    count = 0
    for n in range(0, len(text)):
        if text[n].isalpha:
            count += 1
    for value in dict0_.keys():
        dict0_[value] = format(round(dict0_[value] / count, 2), '.2f')
    return dict0_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dict1_ = count_letters(main_str)
dict2_ = calculate_frequency(dict1_, main_str)
for i in dict2_.keys():
    print(i + ": " + dict2_[i])

# TODO Распечатайте в столбик букву и её частоту в тексте
