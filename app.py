# -*- coding:utf-8 -*-
import json
from flask import Flask, render_template, request

app = Flask(__name__)


class Good:
    def __init__(self, name, price, stock, place, store_time, expire_time):
        self.name = name
        self.price = price
        self.stock = stock
        self.place = place
        self.store_time = store_time
        self.expire_time = expire_time
class LogGood:
    def __init__(self, cls_, name, price, stock, place, store_time, expire_time):
        self.cls_ = cls_
        self.name = name
        self.price = price
        self.stock = stock
        self.place = place
        self.store_time = store_time
        self.expire_time = expire_time


good_list = {
    1: Good("good1", 100, 10, "place1", "2024-5-10", "2025-10-20"),
    2: Good("good2", 200, 20, "place2", "2024-5-10", "2025-10-20"),
    3: Good("good3", 300, 30, "place3", "2024-5-10", "2025-10-20"),
    4: Good("good4", 400, 40, "place4", "2024-5-10", "2025-10-20"),
    5: Good("good5", 500, 50, "place5", "2024-5-10", "2025-10-20"),
}

log_list = []

@app.route("/")
def hello_world():
    return render_template("home.html", good_list=good_list)


@app.route('/goodInfo/<good_id>')
def goodInfo(good_id):
    return render_template("goodInfo.html", good=good_list[int(good_id)])


@app.route('/addGood')
def addGood():
    return render_template("addGood.html")


@app.route('/addGoodData', methods=['POST'])
def addGoodData():
    data = request.data
    data = json.loads(data)
    good_list[list(good_list.keys())[-1] + 1] = Good(data['name'], data['price'], data['stock'], data['place'], data['store_time'],
                                      data['expire_time'])
    log_list.append(LogGood('add', list(good_list.keys())[-1] + 1, data['price'], data['stock'],
                                                     data['place'], data['store_time'],
                                                     data['expire_time']))
    return {
        "code": 0,
        "msg": 'add successly',
        'data': []
    }


@app.route('/updateInfo/<good_id>')
def updateInfo(good_id):
    return render_template("updateInfo.html", good=good_list[int(good_id)], good_id=good_id)


@app.route('/update', methods=['POST'])
def updateData():
    data = request.data
    data = json.loads(data)
    good_list[data['good_id']] = Good(data['name'], data['price'], data['stock'], data['place'], data['store_time'],
                                      data['expire_time'])
    return {
        "code": 0,
        "msg": 'update successly',
        'data': []
    }


@app.route('/deletGood/<good_id>')
def deletGood(good_id):
    data = good_list[int(good_id)]
    del good_list[int(good_id)]
    print(data.price)

    log_list.append(LogGood('delete', data.name, data.price,
                                                       data.stock,
                                                       data.place, data.store_time,
                                                       data.expire_time))
    print(log_list)
    return {
        "code": 0,
        "msg": 'delete successly',
        'data': []
    }

@app.route("/log")
def log():
    return render_template("log.html", log_list=log_list)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
