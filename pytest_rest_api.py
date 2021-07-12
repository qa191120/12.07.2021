# do not forget to run the coupon project !!
import requests # need to install in settings
import json
import pytest

class RestObject:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

def test_rest_api_get_todos():
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.userId == 1
    assert t.title == 'delectus aut autem'
    assert t.completed == False

def test_rest_api_get_coupon():
    resp = requests.get("http://localhost:8080/coupon/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.title == 'Caffe'
    # [{"title":"Caffe","id":1},{"title":"Movie VIP","id":2},{"title":"Sky jump","id":3}]
