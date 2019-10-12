import json

with open("rooms.json", "r") as rooms_json:
    rooms = json.load(rooms_json)

with open("students.json", "r") as students_json:
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
    with open("data_file.json", "a") as write_file:
        json.dump(dict_stud, write_file,  sort_keys=True, indent=4)
    stud_list.clear()

