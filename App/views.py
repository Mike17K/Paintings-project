from django.shortcuts import render
from .sqlFunctions import addUser,addForsale,addPainting,addImage
import mysql.connector
from datetime import datetime

# Create your views here.
def home(request):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='paintings'
        )
    mycursor = connection.cursor()

    status = 1 #addUser(connection,{'firstname':'aaaa','lastname':'s','email':'','photo':'NULL','region':'2','sity':'1','birthdate':'2-2-2'})
    if status == 0: print("Success")
    elif status == 1: print("Failed")

    '''
    addPainting(connection,{
    'title':'mona lisa',
    'width': 10.5,
    'height': 20.3,
    'artist': 'me',
    'description': 'looking strange',
    'type': 'oilpainting',
    'location': 'athens',
    'yearmade': 1800,
    'suportmaterial': 'wood',
    'methodcategory': 'facepaint',
    'owner': 1,
    'available': 1,
    'img': 1
    })

    addImage(connection,{
    'photo':1,
    'name':"mona lisa",
    'size': "10x20"    
    })

    addForsale(connection,{
    'painting':1,
    'price':50.0,
    'timestamp': datetime.now(),
    'added_description': "pay meee",
    'active': 1
    })
    '''

    mycursor.execute("SELECT title,image.photo,price,description,artist,user.firstname,user.lastname,user.photo FROM ((forsale join painting on forsale.id=painting.id) join image on painting.img=image.id) join user on owner=user.id;")
    result = mycursor.fetchall()
    
    cards = []
    for row in result:
        print(row)

        cardObj = {
            'title':row[0], 
            'image':row[1],
            'price':row[2],
            'description':row[3],
            'artist':row[4],
            'seller':row[5]+" "+row[6],
        }
        cards.append(cardObj)

    return render(request,"./App/index.html",{'cards':cards})