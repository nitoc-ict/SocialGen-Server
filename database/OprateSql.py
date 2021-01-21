import sqlite3
import re

dbname = 'scoreData.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS player(id, name, maxScore, area)")
    cur.execute("CREATE TABLE IF NOT EXISTS totalScore(area, totalScore)")
    '''
    cur.executescript("""
        INSERT INTO totalScore VALUES (allJapan,0)
        INSERT INTO totalScore VALUES (Hokkaido,0)
        INSERT INTO totalScore VALUES (Aomori,0)
        INSERT INTO totalScore VALUES (Iwate,0)
        INSERT INTO totalScore VALUES (Miyagi,0)
        INSERT INTO totalScore VALUES (Akita,0)
        INSERT INTO totalScore VALUES (Yamagata,0)
        INSERT INTO totalScore VALUES (Fukushima,0)
        INSERT INTO totalScore VALUES (Ibaraki,0)
        INSERT INTO totalScore VALUES (Tochigi,0)
        INSERT INTO totalScore VALUES (Gumma,0)
        INSERT INTO totalScore VALUES (Saitama,0)
        INSERT INTO totalScore VALUES (Chiba,0)
        INSERT INTO totalScore VALUES (Tokyo,0)
        INSERT INTO totalScore VALUES (Kanagawa,0)
        INSERT INTO totalScore VALUES (Nigata,0)
        INSERT INTO totalScore VALUES (Toyama,0)
        INSERT INTO totalScore VALUES (Ishikawa,0)
        INSERT INTO totalScore VALUES (Fukui,0)
        INSERT INTO totalScore VALUES (Yamanashi,0)
        INSERT INTO totalScore VALUES (Nagano,0)
        INSERT INTO totalScore VALUES (Gifu,0)
        INSERT INTO totalScore VALUES (Shizuoka,0)
        INSERT INTO totalScore VALUES (Aichi,0)
        INSERT INTO totalScore VALUES (Mie,0)
        INSERT INTO totalScore VALUES (Shiga,0)
        INSERT INTO totalScore VALUES (Kyoto,0)
        INSERT INTO totalScore VALUES (Osaka,0)
        INSERT INTO totalScore VALUES (Hyogo,0)
        INSERT INTO totalScore VALUES (Nara,0)
        INSERT INTO totalScore VALUES (Wakayama,0)
        INSERT INTO totalScore VALUES (Tottori,0)
        INSERT INTO totalScore VALUES (Shimane,0)
        INSERT INTO totalScore VALUES (Okayama,0)
        INSERT INTO totalScore VALUES (Hiroshima,0)
        INSERT INTO totalScore VALUES (Yamaguchi,0)
        INSERT INTO totalScore VALUES (Tokushima,0)
        INSERT INTO totalScore VALUES (Kagawa,0)
        INSERT INTO totalScore VALUES (Ehime,0)
        INSERT INTO totalScore VALUES (Kochi,0)
        INSERT INTO totalScore VALUES (Fukuoka,0)
        INSERT INTO totalScore VALUES (Saga,0)
        INSERT INTO totalScore VALUES (Nagasaki,0)
        INSERT INTO totalScore VALUES (Kumamoto,0)
        INSERT INTO totalScore VALUES (Oita,0)
        INSERT INTO totalScore VALUES (Miyazaki,0)
        INSERT INTO totalScore VALUES (Kagoshima,0)
        INSERT INTO totalScore VALUES (Okinawa,0)
    """)
    '''


def addUser(id: int, name: str, area: str):
    cur.execute("INSERT INTO player VALUES (?,?,?,?)", (id, name, 0, area)) # id重複時の処理はどうする
    conn.commit()
    # check =
    # return(check)

def addResult(id: int, score: int):
    cur.execute("")
    cur.execute("SELECT maxScore FROM player WHERE id = ?", (id,))
    hoge = cur.fetchone()
    if hoge[0] < score:
        cur.execute("UPDATE player SET maxScore = ? WHERE id = ?", (score, id))

    conn.commit()
    # check =
    # return(check)

''' Un Completed
def getRank(id: int):
    return(json,rank,score)

def getTotalScore(area: str):
    totalJP
    totalarea
    totalScore[] = {totalJP,totalarea}
    return(totalScore[])
'''

''' test
createTable()
addUser(1, 'hundo', 'Okinawa')
addResult(1, 60000)
'''
conn.close()