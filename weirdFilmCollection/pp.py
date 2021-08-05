import pymysql


def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        db='test',
        user='root',
        passwd='sa',
        charset='utf8',
        use_unicode=False
    )
    return conn

dbObject = dbHandle()
cursor = dbObject.cursor()
sql = "insert into movie(ID,TITLE,RATE,URL,DIRECTORS,CASTS,NUMBER,IMDBURL,IMDBRATE,IMDBRATENUMBER) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
params = (1,1,1,1,1,1,1,1,1,1)

try:
    cursor.execute(sql,params)
    dbObject.commit()
except Exception as e:
    print(e)
    dbObject.rollback()

