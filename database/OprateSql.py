import sqlite3
import json

dbname = 'scoreData.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()


def createTable():
    #  ユーザテーブル
    cur.execute("CREATE TABLE IF NOT EXISTS player(id, name, maxScore, area)")
    
    #  スコアのテーブル
    cur.execute('CREATE TABLE IF NOT EXISTS allJapan(date,id,name,score,pref)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hokkaido(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aomori(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Iwate(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyagi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Akita(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamagata(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukushima(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ibaraki(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tochigi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gunma(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saitama(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Chiba(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokyo(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kanagawa(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Niigata(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Toyama(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ishikawa(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukui(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamanashi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagano(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Gifu(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shizuoka(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Aichi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Mie(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shiga(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kyoto(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Osaka(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hyogo(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nara(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Wakayama(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tottori(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Shimane(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okayama(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Hiroshima(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Yamaguchi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Tokushima(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagawa(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Ehime(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kochi(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Fukuoka(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Saga(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Nagasaki(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kumamoto(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Oita(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Miyazaki(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Kagoshima(date,id,name,score)')
    cur.execute('CREATE TABLE IF NOT EXISTS Okinawa(date,id,name,score)')



def addUser(id: int, name: str, area: str):
    cur.execute("INSERT INTO player VALUES (?,?,?,?)", (id, name, 0, area)) # id重複時の処理はどうする
    


def insertData(playerId: int, name: str, score: int, pref: str):
    cur.execute("INSERT INTO allJapan VALUES (datetime('now', '+9 hours'),?,?,?,?)", (playerId, name, score, pref))
    cur.execute("INSERT INTO " + pref + " VALUES (datetime('now', '+9 hours'),?,?,?)", (playerId, name, score))
    conn.commit()


def addResult(id: int, score: int):
    cur.execute("")
    cur.execute("SELECT maxScore FROM player WHERE id = ?", (id,))
    hoge = cur.fetchone()
    if hoge[0] < score:
        cur.execute("UPDATE player SET maxScore = ? WHERE id = ?", (score, id))


# def showRank(pref):
#    rank = cur.execute("SELECT * FROM ? ORDER BY score DESC OFFSET 0 ROWS FETCH NEXT 50 ROWS ONLY", (pref,))


def showTotal(area: str = 'all'):
    with open('total.json', 'r') as f:
        total_dict = json.load(f)
        return total_dict[area]

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


if __name__ == '__main__':
    showTotal()
