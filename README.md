# Food alert

## Prerequisite

- Python 3

## Installation

```shell
git clone https://github.com/hsiaoyi0504/food_alert
cd food_alert
python -m venv venv
source venv/bin/activate
pip install -r server/requirements.txt
python build.py  # build the data that will be used by server
```

## Start the server

`FLASK_APP=server/main.py flask run`

## Notes

### Server side

- Provide a api that can handle GET request from client in following format:
  `/food/<food_name>`