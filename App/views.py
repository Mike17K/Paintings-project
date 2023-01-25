from django.shortcuts import render
from .sqlFunctions import addUser
import mysql.connector

# Create your views here.
def home(request):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='paintings'
        )

    status = 1#addUser(connection,{'firstname':'aaaa','lastname':'s','email':'','photo':'NULL','region':'2','sity':'1','birthdate':'2-2-2'})
    if status == 0: print("Success")
    elif status == 1: print("Failed")

    return render(request,"./App/index.html")