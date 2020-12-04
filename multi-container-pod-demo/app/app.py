import redis
import pymysql
from flask import Flask, request

DEBUG=True
app=Flask(__name__)

DATABASE='mysqldb'
app.config.from_object(__name__)

class MysqlDB:
    def __init__(self):
        self.conn=pymysql.connect(host='mysql',
                user='root', 
                password='password', 
                charset='utf8mb4',
                port=3306,
                db='blog')

@app.route("/get/<user_name>")
def get_user_post(user_name):
    """Returns a user post for a given username
       Returns 404 for non-existent users."""

    r=redis.Redis(host='localhost', port=6379)
    user_post=r.get(user_name)
    app.logger.info(user_post)
    if user_post:
        user_post=user_post.decode("utf-8") 
        return f"{user_name}'s post: {user_post}(SERVING FROM CACHE!!)\n", 200
    cur=MysqlDB().conn.cursor()
    cur.execute("SELECT * FROM posts")
    for row in cur.fetchall():
        app.logger.info(row)
        if user_name == row[1]:
            r.set(row[1], row[2])
            r.expire(row[1], 10)
            return f"{row[1]}'s post: {row[2]}\n", 200
    # Zsh identifies o/p as partial line without \n
    return "User not Found!\n", 404
    r.set('foo', 'bar')
    status=200
    headers={}
    return response, status, headers
    pass

@app.route("/add", methods=["POST"])
def add_user_post():
    if 'username' not in request.json or 'userpost' not in request.json:
        return request.json
        return "Invalid details\n", 400
    else:
        connection=MysqlDB().conn
        with connection.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS \
                     posts(Sno integer primary key AUTO_INCREMENT, \
                     UserName varchar(10), Post varchar(100))")
            payload=(request.json['username'], request.json['userpost'])
            app.logger.info(payload)
            cur.execu   te("INSERT INTO posts(UserName, Post) VALUES(%s, %s)", payload)
        connection.commit()
        return f"{request.json['username']}'s post Added successfully!\n", 200

if __name__ == "__main__":
    app.run(port=5000)