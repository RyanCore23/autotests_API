import xml.etree.ElementTree as ET # Библиотека для работы с xml

# Задаем переменную с xml
xml_data = ''' 
<person>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <age>30</age>
    <address>
        <city>New York</city>
        <street>Main Street</street>
    </address>
</person>
'''

# Переводим в строку
root = ET.fromstring(xml_data)

# Получаем данные и выводим на печать
print(root.find("first_name").text)