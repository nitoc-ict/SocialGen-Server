from flask import Flask, request
import json
from database import OprateSql as ops

ops.createTable()
ops.creatJson()

app = Flask(__name__)


@app.route('/ranking')
def ranking():
    rank_json = ops.showRank()
    return rank_json


@app.route('/total')
def total():
    total_score = ops.showTotal()
    return total_score


@app.route('/entry_player', methods=["POST"])
def entry_player():
    ops.createTable()

    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_name = result_dict['name']
    pref = result_dict['pref']

    player_id = ops.addUser(player_name, pref)

    return str(player_id)


@app.route('/result', methods=["POST"])
def result():
    ops.creatJson()

    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_id = result_dict['id']
    score = result_dict['score']

    ops.addResult(player_id, score)

    return 'OK'


if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.2')
    app.run(debug=True)
