import json

import dicttoxml

rooms_path = input('Enter your full path to rooms.json: ')
rooms_path += "/rooms.json"
students_path = input('Enter your full path to students.json: ')
students_path += "/students.json"
doc_type = input('Enter formate of output file (json or xml): ')

with open(rooms_path, "r") as rooms_json:
    rooms = json.load(rooms_json)

with open(students_path, "r") as students_json:
    students = json.load(students_json)

stud_list = []

for room in rooms:
    for student in students:
        if int(student["room"]) == int(room["id"]):
            stud_list.append(student["name"])
    dict_stud = {
        'id': room['id'],
        'name': room['name'],
        'students': stud_list
    }
    if doc_type == 'json':
        with open("student_in_rooms.json", "a") as write_file:
            json.dump(dict_stud, write_file, sort_keys=True, indent=4)
    else:
        with open("student_in_rooms.xml", "a") as write_file:
            xml = dicttoxml.dicttoxml(dict_stud)
            write_file.write(str(xml))
    stud_list.clear()
