# TODO Напишите функцию для поиска индекса товара
def index_itemses(func_items_list, tovar):
    loose = 0
    for i in range(0, len(func_items_list)):
        if func_items_list[i] == tovar:
            return i
        else:
            loose += 1
    if loose >= len(items_list):
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_itemses(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
