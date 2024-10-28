import os
import json


class PriceMachine():

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path='D:/test/'):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        # обрабатываем в цикле For список файлов в указанном каталоге
        for entry in os.listdir(file_path):
            # если в имени файла присутствует "price"
            if "price" in entry:
                # определяем путь к файлу
                full_path = os.path.join(file_path, entry)
                # проверяем является ли запись файлом
                if os.path.isfile(full_path):
                    # Если запись представляет собой файл, мы открываем его в режиме чтения.
                    with open(full_path, "r", encoding='UTF-8') as file:
                        # получаем индексы колонок по первой строке
                        for id, name in enumerate(file.readline().split(",")):
                            if "название" in name or "продукт" in name or "товар" in name or "наименование" in name:
                                name_id = id
                            elif "цена" in name or "розница" in name:
                                price_id = id
                            elif "фасовка" in name or "масса" in name or "вес" in name:
                                weight_id = id
                        # Продолжаем читать файл по строчно
                        for line in file:
                            lst = line.split(",")
                            lst2 = [
                                lst[name_id],
                                round(float(lst[price_id]), 2),
                                round(float(lst[weight_id].translate({ord('\n'): None})), 2),
                                entry,
                                round(float(lst[price_id]) / float(lst[weight_id].translate({ord('\n'): None})), 2)
                            ]
                            self.data.append(lst2)

        return self.data

    # def _search_product_price_weight(self, headers):
    #     '''
    #         Возвращает номера столбцов
    #     '''

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        file_html = open(fname, "w", encoding='UTF-8')
        file_html.write(result)

        data = sorted(self.data, key=lambda x: x[-1])

        for number, item in enumerate(data):
            result = ''
            product_name, price, weight, file_name, value = item
            result += '<tr>'
            result += f'<td>{number + 1}</td>'
            result += f'<td>{product_name}</td>'
            result += f'<td>{price}</td>'
            result += f'<td>{weight}</td>'
            result += f'<td>{file_name}</td>'
            result += f'<td>{value}</td>'
            result += '</tr>'
            file_html.write(result + '\n')

        result = ''
        result += '</tbody></table>'
        file_html.write(result + '\n')

        file_html.close()

    def find_text(self, text):
        number = 0
        search_list = []
        for i in self.data:
            if text.lower() in i[0].lower():
                search_list.append([i[0], i[1], i[2], i[3], i[4]])
        data = sorted(search_list, key=lambda x: x[-1])
        for items in data:
            number += 1
            print(number, items[0], items[1], items[2], items[3], items[4])


pm = PriceMachine()
print(pm.load_prices())

'''
    Логика работы программы
'''
while True:
    text = input("Введите строку для поиска: ")
    if text == "exit":
        break
    else:
        pm.find_text(text)

print('the end')
print(pm.export_to_html())
