# TODO  Напишите функцию count_letters
def count_letters(string_): # словарь из букв и их количества
    str_ = string_.lower()
    slovar_kolich = {}
    for let in list(str_):
        kolvo = 0
        if let.isalpha():
            for letpovtor in list(str_):
                if let == letpovtor:
                    kolvo += 1
                    slovar_kolich[let] = kolvo
    return slovar_kolich

# TODO Напишите функцию calculate_frequency
def calculate_frequency(slovar_):
    kol_bukv = 0                        # Будет содержать общее количество букв в словаре
    for chislo, in slovar_:
         kol_bukv += slovar_[chislo]

    slov_chast = {}                     # Словарь с частотами букв
    for bukv in slovar_:
        slov_chast[bukv] = slovar_[bukv] / kol_bukv
    return slov_chast


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

# TODO Распечатайте в столбик букву и её частоту в тексте

for letter, stat in calculate_frequency(count_letters(main_str)).items():
    print(f"{letter}: {float(stat):.2f}")