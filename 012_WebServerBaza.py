from flask import Flask
import pymysql.cursors
app = Flask(__name__)

@app.route("/")
def index():

    """
    create database ESSIS2019 character set utf8 collate utf8_general_ci;
    use ESSIS2019;
    create table example(id int not null primary key auto_increment,name varchar(50));
    insert into example(name) values ('Dora');
    """

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='ESSIS2019',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select name from example where sifra=%s"
            cursor.execute(sql, (1))
            result_from_database = cursor.fetchone()
    finally:
        connection.close()
    
    return "<h1>" + result_from_database["name"] +  "</h1>"

if __name__ == "__main__":
    app.run()
