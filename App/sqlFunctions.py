#================================================================
from asyncio.windows_events import NULL
from csv import writer

from importlib_metadata import SelectableGroups


def executeQuery(conn,query):
    try: 
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return 0
    except Exception as e:
        print(e)
        return 1
#================================================================

# 
#   CREATE/REFRESH THE DATABACE
#

delete_database = lambda conn: executeQuery(conn,"DROP DATABASE `paintings`;")

def create_database(conn):
    with open('mysite\static\SQL\create_painting_db.sql', 'r') as f:
        sqlcommands = f.read().split(';')
        for command in sqlcommands:
            status = executeQuery(conn,command)
            if status == 0: continue
            else: return 1
        return 0

def clear_database(conn):
    with open('mysite\static\SQL\clear_painting_db.sql', 'r') as f:
        sqlcommands = f.read().split(';')
        for command in sqlcommands:
            status = executeQuery(conn,command)
            if status == 0: continue
            else: return 1
        return 0
'''
import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
    )
print(delete_database(connection))
print(create_database(connection))
print(clear_database(connection))
addImage(connection,{'photo':'2222','name':'aa','size':'10x10'})
addUser(connection,{'firstname':'a','lastname':'s','email':'','photo':'NULL','region':'2','sity':'1','birthdate':'2-2-2'})
'''

#
#   INSERT DATA TO DATABASE
#

queryDict = {
'addUser':lambda data: f"INSERT INTO user(firstname,lastname,email,photo,region,sity,birthdate) VALUES ('{data['firstname']}','{data['lastname']}','{data['email']}',{data['photo']},'{data['region']}','{data['sity']}','{data['birthdate']}'); ",
'addFeedback':lambda data: f"INSERT INTO feedback(text,writer,seller,rating) VALUES ({data['id']},'{data['text']}',{data['writer']},{data['seller']},{data['rating']}); ",
'addMessage':lambda data: f"INSERT INTO message(sender,receiver,content,timestamp,about) VALUES ({data['sender']},{data['receiver']},'{data['content']}','{data['timestamp']}',{data['about']}); ",
'addPainting':lambda data: f"INSERT INTO painting(title,width,height,artist,description,type,location,yearmade,suportmaterial,methodcategory,owner,available,img) VALUES ('{data['title']}',{data['width']},{data['height']},'{data['artist']}','{data['description']}','{data['type']}','{data['location']}',{data['yearmade']},'{data['suportmaterial']}','{data['methodcategory']}',{data['owner']},{data['available']},{data['img']}); ",
'addOrder':lambda data: f"INSERT INTO order(painting,date,buyer,status) VALUES ({data['painting']},'{data['date']}',{data['buyer']},'{data['status']}'); ",
'addPayment':lambda data: f"INSERT INTO payment(amount,timestamp,order) VALUES ({data['amount']},'{data['timestamp']}',{data['order']}); ",
'addImage':lambda data: f"INSERT INTO image(photo,name,size) VALUES ('{data['photo']}','{data['name']}','{data['size']}'); ",
'addContains':lambda data: f"INSERT INTO contains(msg,img) VALUES ({data['msg']},{data['img']}); ",
'addForsale':lambda data: f"INSERT INTO forsale(painting,price,timestamp,added-description,active) VALUES ({data['painting']},{data['price']},'{data['timestamp']}','{data['added-description']}','{data['active']}'); "
}

addUser = lambda conn,data: executeQuery(conn,queryDict['addUser'](data))
addFeedback = lambda conn,data: executeQuery(conn,queryDict['addFeedback'](data))
addMessage = lambda conn,data: executeQuery(conn,queryDict['addMessage'](data))
addPainting = lambda conn,data: executeQuery(conn,queryDict['addPainting'](data))
addOrder = lambda conn,data: executeQuery(conn,queryDict['addOrder'](data))
addPayment = lambda conn,data: executeQuery(conn,queryDict['addPayment'](data))
addImage = lambda conn,data: executeQuery(conn,queryDict['addImage'](data))
addContains = lambda conn,data: executeQuery(conn,queryDict['addContains'](data))
addForsale = lambda conn,data: executeQuery(conn,queryDict['addForsale'](data))

