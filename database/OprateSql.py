import sqlite3
import json
from collections import OrderedDict

dbname = 'database/scoreData.db'


def createTable():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #  スコアのテーブル
    cur.execute('CREATE TABLE IF NOT EXISTS allJapan(id,name,score,pref)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hokkaido(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aomori(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Iwate(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyagi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Akita(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamagata(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukushima(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ibaraki(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tochigi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gunma(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saitama(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Chiba(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokyo(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kanagawa(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Niigata(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Toyama(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ishikaw(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukui(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamanashi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagano(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gifu(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shizuoka(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aichi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Mie(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shiga(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kyoto(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Osaka(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hyogo(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nara(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Wakayama(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tottori(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shimane(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okayama(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hiroshima(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamaguchi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokushima(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagawa(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ehime(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kochi(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukuoka(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saga(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagasaki(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kumamoto(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Oita(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyazaki(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagoshima(id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okinawa(id,name,score)')

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


if __name__ == '__main__':
    creatJson()
