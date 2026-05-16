import json

json_data = '''
{
  "name": "Сергей",
  "age": 42,
  "is_student": false,
  "couses": ["python", "QA Automation", "API Testing"],
  "address": {
    "city": "Ейск",
    "zip": "353680"
  }
}
'''

# Превралили json объект в словарь
# С S json.loads - работа со строкой
parse_data = json.loads(json_data)

print(parse_data)

# словарь
data = {
    "name": "Юлия",
    "age": 41,
    "is_student": True,
}

# Преобразование в json
# С S - json.dumps работа со строками
json_string = json.dumps(data, indent=2, ensure_ascii=False) # indent - количество отступов слева, ensure_ascii - декод киррилицы
print(json_string)

# Читаем из файла json_example.json, в папке с проектом
# Без S работа с фалами json.load
with open("json_example.json", "r", encoding="UTF-8") as file:
    data_from_file = json.load(file)
    print(data_from_file)

# Запись в файл for_file.json (если НЕТ - то создаст)
with open("for_file.json", "w", encoding="UTF-8")as write_file:
    json.dump(data, write_file, ensure_ascii=False, indent=2)

