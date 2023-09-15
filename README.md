# Lab: Banjo - Fortune

## API Overview
This API hosts fortunes. You can "like" fortunes, change them, and assign categories. 

Potential uses include a fortune teller, a magic 8 ball, or a daily astrology reading.

### Endpoints

| Route                   | HTTP Method | Payload                                                                    |
|-------------------------|-------------|----------------------------------------------------------------------------|
| `fortune_teller/new`    | `POST`      | `fortune_statement`: `str`  <br> `category_happy`: `bool`  <br>   `category_sad`: `bool`  |
| `fortune_teller/all`    | `GET`       | None                                                                       |
| `fortune_teller/edit`   | `POST`      | `id`: `int`                                                                |
| `fortune_teller/like`   | `POST`      | `id`: `int`                                                                |
| `fortune_teller/random` | `GET`       | `category_happy`: `bool`  <br>  `category_sad`: `bool`                            |


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



