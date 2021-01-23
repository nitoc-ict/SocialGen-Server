import sqlite3
import json
from collections import OrderedDict

dbname = 'database/scoreData.db'


def createTable():
    with open(dbname, 'a'):
        pass

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #  スコアのテーブル
    cur.execute('CREATE TABLE IF NOT EXISTS allJapan(id integer,name,score,pref)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hokkaido(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aomori(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Iwate(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyagi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Akita(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamagata(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukushima(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ibaraki(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tochigi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gunma(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saitama(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Chiba(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokyo(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kanagawa(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Niigata(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Toyama(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ishikaw(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukui(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamanashi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagano(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gifu(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shizuoka(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aichi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Mie(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shiga(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kyoto(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Osaka(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hyogo(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nara(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Wakayama(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tottori(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shimane(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okayama(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hiroshima(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamaguchi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokushima(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagawa(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ehime(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kochi(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukuoka(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saga(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagasaki(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kumamoto(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Oita(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyazaki(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagoshima(id integer,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okinawa(id integer,name,score)')
    conn.commit()
    conn.close()


def creatJson():
    try:
        with open('database/totalScore.json', mode='x') as f:
            totalDict = {
                "allJapan": 0,
                "Hokkaido": 0,
                "Aomori": 0,
                "Iwate": 0,
                "Miyagi": 0,
                "Akita": 0,
                "Yamagata": 0,
                "Fukushima": 0,
                "Ibaraki": 0,
                "Tochigi": 0,
                "Gunma": 0,
                "Saitama": 0,
                "Chiba": 0,
                "Tokyo": 0,
                "Kanagawa": 0,
                "Niigata": 0,
                "Toyama": 0,
                "Ishikawa": 0,
                "Fukui": 0,
                "Yamanashi": 0,
                "Nagano": 0,
                "Gifu": 0,
                "Shizuoka": 0,
                "Aichi": 0,
                "Mie": 0,
                "Shiga": 0,
                "Kyoto": 0,
                "Osaka": 0,
                "Hyogo": 0,
                "Nara": 0,
                "Wakayama": 0,
                "Tottori": 0,
                "Shimane": 0,
                "Okayama": 0,
                "Hiroshima": 0,
                "Yamaguchi": 0,
                "Tokushima": 0,
                "Kagawa": 0,
                "Ehime": 0,
                "Kochi": 0,
                "Fukuoka": 0,
                "Saga": 0,
                "Nagasaki": 0,
                "Kumamoto": 0,
                "Oita": 0,
                "Miyazaki": 0,
                "Kagoshima": 0,
                "Okinawa": 0
            }
            json.dump(totalDict, f, indent=4)
    except FileExistsError:
        pass


def addUser(name: str, pref: str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #  idの作成
    sqlCount = cur.execute("SELECT COUNT(*) FROM allJapan")
    player_id = sqlCount.fetchone()[0] + 1

    #  allJapanへの追加
    cur.execute("INSERT INTO allJapan VALUES (?,?,?,?)", (player_id, name, 0, pref))
    #  areaへの追加
    cur.execute(f"INSERT INTO {pref} VALUES (?, ?, ?)", (player_id, name, 0))

    conn.commit()
    conn.close()

    return player_id


def addResult(player_id: int, score: int):
    #  db側の処理
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("SELECT pref FROM allJapan WHERE id = ?", (player_id,))
    pref = cur.fetchone()[0]

    cur.execute("UPDATE allJapan SET score = ? WHERE id = ? AND score < ?", (score, player_id, score))
    cur.execute(f"UPDATE {pref} SET score = ? WHERE id = ? AND score < ?", (score, player_id, score))

    conn.commit()
    conn.close()

    #  json側の処理
    with open('database/totalScore.json', 'r') as f:
        total_dict = json.load(f, object_pairs_hook=OrderedDict)

    total_dict[pref] += score
    total_dict['allJapan'] += score

    with open('database/totalScore.json', 'w') as f:
        json.dump(total_dict, f, indent=4)


def showTotal(area: str = 'allJapan'):
    with open('database/totalScore.json', 'r') as f:
        total_dict = json.load(f)
        return str(total_dict[area])


def showRank(pref: str = 'allJapan'):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute(f"SELECT id, name, score FROM {pref} ORDER BY CAST(score AS integer) DESC LIMIT 50 OFFSET 0")
    scoreList = cur.fetchall()

    for i, scoreTuple in enumerate(scoreList):
        scoreList[i] = {'rank': i + 1, 'id': scoreTuple[0], 'userName': scoreTuple[1], 'score': scoreTuple[2]}
    conn.commit()
    conn.close()

    return json.dumps(scoreList)
