from datetime import datetime
from config import app, db
from models import Person, Note

PEOPLE_NOTES = [
    {
        "lname": "John",
        "fname": "Tester",
        "notes": [
            ("Eligendi alias reiciendis consequuntur sint et eveniet in.", "2022-01-06 17:10:24"),
            ("Alias corrupti culpa sed eos nisi sed adipisci illum distinctio.", "2022-03-05 22:17:54"),
            ("Et possimus occaecati sequi et eum praesentium.", "2022-03-05 22:18:10"),
        ],
    },
    {
        "lname": "Chris",
        "fname": "Developer",
        "notes": [
            ("Illo non minus consequatur aperiam nostrum et.", "2022-01-01 09:15:03"),
            ("Voluptatem sit veniam aliquam qui facere.", "2022-02-06 13:09:21"),
        ],
    },
    {
        "lname": "Steven",
        "fname": "Janitor",
        "notes": [
            ("Vitae sunt quis eaque.", "2022-01-07 22:47:54"),
            ("Ad est consectetur ipsam saepe illo qui.", "2022-04-06 13:03:17"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_person)
    db.session.commit()
