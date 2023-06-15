# todo-app

this is for practice django

## Feature

- [x] Create todo
- [x] Update todo
- [x] Delete todo
- [x] List todo
- [x] Detail todo
- [x] Mark todo as done
- [x] Mark todo as undone

## Model Task

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| title | string | Task title |
| description | string | Task description |
| done | boolean | Task status |
| created | datetime | Task created datetime |
| updated | datetime | Task updated datetime |

## Model User

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| username | string | User username |
| password | string | User password |

## API

| Method | Path | Description |
| --- | --- | --- |
| GET | /api/v1/tasks/ | List todo |
| POST | /api/v1/tasks/ | Create todo |
| GET | /api/v1/tasks/:id/ | Detail todo |
| PUT | /api/v1/tasks/:id/ | Update todo |
| DELETE | /api/v1/tasks/:id/ | Delete todo |
| POST | /api/v1/tasks/:id/done/ | Mark todo as done |
| POST | /api/v1/tasks/:id/undone/ | Mark todo as undone |
| POST | /api/v1/users/ | Create user |
| GET | /api/v1/users/ | List User |
| GET | /api/v1/users/:id/ | Detail user |

### List todo

```
GET /api/v1/tasks/
```

#### Response

```
Status: 200 OK
```

```json
[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Task 1 description",
        "done": false,
        "created": "2021-01-01T00:00:00Z",
        "updated": "2021-01-01T00:00:00Z"
    },
    {
        "id": 2,
        "title": "Task 2",
        "description": "Task 2 description",
        "done": false,
        "created": "2021-01-01T00:00:00Z",
        "updated": "2021-01-01T00:00:00Z"
    }
]
```

### Create todo

```
POST /api/v1/tasks/
```

#### Request

```json
{
    "title": "Task 1",
    "description": "Task 1 description"
}
```

#### Response

```
Status: 201 Created
```

```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Task 1 description",
    "done": false,
    "created": "2021-01-01T00:00:00Z",
    "updated": "2021-01-01T00:00:00Z"
}
```

### Detail todo

```
GET /api/v1/tasks/:id/
```

#### Response

```
Status: 200 OK
```

```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Task 1 description",
    "done": false,
    "created": "2021-01-01T00:00:00Z",
    "updated": "2021-01-01T00:00:00Z"
}
```

### Update todo

```
PUT /api/v1/tasks/:id/
```

#### Request

```json
{
    "title": "Task 1",
    "description": "Task 1 description"
}
```

#### Response

```
Status: 200 OK
```

```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Task 1 description",
    "done": false,
    "created": "2021-01-01T00:00:00Z",
    "updated": "2021-01-01T00:00:00Z"
}
```

### Delete todo

```
DELETE /api/v1/tasks/:id/
```

#### Response

```
Status: 204 No Content
```

### Mark todo as done

```
POST /api/v1/tasks/:id/done/
```

#### Response

```
Status: 200 OK
```

```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Task 1 description",
    "done": true,
    "created": "2021-01-01T00:00:00Z",
    "updated": "2021-01-01T00:00:00Z"
}
```

### Mark todo as undone

```
POST /api/v1/tasks/:id/undone/
```

#### Response

```
Status: 200 OK
```

```json
{
    "id": 1,
    "title": "Task 1",
    "description": "Task 1 description",
    "done": false,
    "created": "2021-01-01T00:00:00Z",
    "updated": "2021-01-01T00:00:00Z"
}
```

### Create user

```
POST /api/v1/users/
```

#### Request

```json
{
    "username": "user1",
    "password": "password1"
}
```

#### Response

```
Status: 201 Created
```

```json
{
    "id": 1,
    "username": "user1",
    "password": "password1"
}
```

### List user

```
GET /api/v1/users/
```

#### Response

```
Status: 200 OK
```

```json
[
    {
        "id": 1,
        "username": "user1",
        "password": "password1"
    },
    {
        "id": 2,
        "username": "user2",
        "password": "password2"
    }
]
```

### Detail user

```
GET /api/v1/users/:id/
```

#### Response

```
Status: 200 OK
```

```json
{
    "id": 1,
    "username": "user1",
    "password": "password1"
}
```
