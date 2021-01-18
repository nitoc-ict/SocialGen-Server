from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/ranking')
def ranking():
    player_id = int(request.args.get('id'))
    #  rank_json = hoge()
    #  return rank_json

    rank_dict = {1: {'id': player_id, 'name': 'hoge', 'score': 100},
                 2: {'id': player_id+1, 'name': 'fuge', 'score': 90},
                 3: {'id': player_id+2, 'name': 'fuga', 'score': 80}
                }
    rank_json = json.dumps(rank_dict)
    return rank_json


@app.route('/total')
def total():
    #  total_score = hoge(player_id)
    #  return total_score
    return '10000'


@app.route('/entry_player', methods=["POST"])
def entry_player():
    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_id = result_dict['id']
    player_name = result_dict['name']
    pref = result_dict['pref']

    #  check = hoge(player_id, player_name, pref)
    #  return check

    return '1'


@app.route('/result', methods=["POST"])
def result():
    result_json = request.get_data()
    result_dict = json.loads(result_json)

    player_id = result_dict['id']
    score = result_dict['score']

    #  check =hoge(player_id, score)
    #  return check

    return '1'


if __name__ == '__main__':
    app.run(debug=True)
