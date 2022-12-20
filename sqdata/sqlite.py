import sqlite3 as sqlite

connection = sqlite.connect("new-db") # If it doesn't exist.. create it


local_cursor = connection.cursor() 
admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE orders (order_id integer PRIMARY KEY AUTOINCREMENT, drink VARCHAR(20), name VARCHAR(30), size VARCHAR(10))"

def runQuery(query):
    data = local_cursor.execute(query) 
    return data

def getallrecords():
    query = "SELECT * FROM orders"
    data = runQuery(query) 
    return data.fetchall()
def insertdata(order):
    query = f"insert into orders (drink, name, size) values('{order[0]}','{order[1]}','{order[2]}')"
    runQuery(query)

insert_query = "INSERT INTO orders (drink, name, size) "
select_query = "SELECT * FROM Orders"
# runQuery(create_query)
# print(runQuery(select_query).fetchall())
def commitdata():
    connection.commit()
