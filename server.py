from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/ranking')
def ranking():
    player_id = request.args.get('id')
    return player_id
    #  rank_json = hoge(player_id)
    #  return rank_json


@app.route('/total')
def total():
    player_id = request.args.get('id')
    return player_id
    #  total_json = hoge(player_id)
    #  return rank_json


@app.route('/result', methods=["POST"])
def result():
    result_json = request.get_data()
    result_dict = json.loads(result_json)
    user_dict = result_dict.values[0]

    player_id = user_dict['id']
    player_name = user_dict['name']
    score = user_dict['score']
    pref = user_dict['pref']

    print(result_dict)
    #  hoge(player_id, player_name, score, pref)
    return result_json


if __name__ == '__main__':
    app.run(debug=True)
