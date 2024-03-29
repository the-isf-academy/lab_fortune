# Lab: Banjo - Fortune

## API Overview
This API hosts fortunes. You can "like" fortunes, change them, and assign categories. 

Potential uses include a fortune teller, a magic 8 ball, or a daily astrology reading.

### Endpoints

| Endpoint                   | HTTP Method | Payload                                                                    |
|-------------------------|-------------|----------------------------------------------------------------------------|
| `fortune/new`    | `POST`      | `fortune_statement`: `str`  <br> `category_happy`: `bool`  <br>   `category_sad`: `bool`  |
| `fortune/all`    | `GET`       | None                                                                       |
| `fortune/edit`   | `POST`      | `id`: `int`                                                                |
| `fortune/like`   | `POST`      | `id`: `int`                                                                |
| `fortune/random` | `GET`       | `category_happy`: `bool`  <br>  `category_sad`: `bool`                            |


---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a [Banjo](https://pypi.org/project/django-banjo/) server:** `banjo` 
> *Optionally can start in debug mode with: `banjo --debug`*



