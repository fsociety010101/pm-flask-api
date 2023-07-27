# Flask REST API
Technologies used:
* Python
* Flask
* Swagger UI
* OpenAPI
* SQLite
* SQLAlchemy


## API
#### /people:
* `GET` : Read the list of people
* `POST` : Create a person

#### /people/{lname}:
* `GET` : Read one person
* `PUT` : Update a person
* `DELETE` : Delete a person

#### /notes
* `POST` : Create a note associated with a person

#### /notes/{note_id}
* `GET` : Read one note
* `PUT` : Update a note
* `DELETE` : Delete a note
