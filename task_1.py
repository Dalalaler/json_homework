import json
import xmlify


rooms_path = input('Enter your path to rooms.json: ')
rooms_path += "/rooms.json"
students_path = input('Enter your path to students.json: ')
students_path += "/students.json"
students_in_rooms_path = input('Enter your path to save student_in_rooms file: ')
doc_type = input('Enter the type of file: ')
students_in_rooms_path += ("/students_in_rooms." + doc_type)


with open(rooms_path, "r") as rooms_json:
    rooms = json.load(rooms_json)

with open(students_path, "r") as students_json:
    students = json.load(students_json)

for room in rooms:
    room['students'] = []

for student in students:
    room_id = student['room']
    rooms[room_id]['students'].append(student)

if doc_type == ("json"):
    with open(students_in_rooms_path, 'w') as f:
        json.dump(rooms, f, indent=4)
else:
    with open(students_in_rooms_path, "w") as f:
        f.write(xmlify.dumps(rooms))
