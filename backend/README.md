# Backend Installation

<br>

Backend requires [Python](https://www.python.org/downloads/) 3.10.2 to run.

<br>

Install the dependencies.

```sh
cd backend
python -m venv env
.\env\Scripts\activate
cd scripts
pip install -r requirements.txt
```

<br>

If you need to upgrade pip version

```sh
python -m pip install --upgrade pip
```

<br>

Start the server.

```sh
cd backend\source
uvicorn main:app --reload
```

Run unit tests

```sh
cd backend
pytest
```
