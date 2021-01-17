from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/ranking')
def ranking():
    return None
    #  rank_json = hoge()
    #  return rank_json


@app.route('/total')
def total():
    return None
    #  total_score = hoge(player_id)
    #  return total_score


@app.route('/entry_player', methods=["POST"])
def entry_player():
    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_id = result_dict['id']
    player_name = result_dict['name']
    pref = result_dict['pref']

    #  check = hoge(player_id, player_name, pref)
    #  return check

    return f'{player_id}, {player_name}, {pref}\n'


@app.route('/result', methods=["POST"])
def result():
    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_id = result_dict['id']
    score = result_dict['score']

    #  check =hoge(player_id, score)
    #  return check

    return f'{player_id}, {score}\n'


if __name__ == '__main__':
    app.run(debug=True)
