import zipfile
import glob
import sqlite3
from sqlite3 import Error


def readData(data):


    sideNumber = []
    sectorNumber = []
    partitionNumber = []
    branch = []
    FEC = []
    allParameters = []


    file = open(data, 'r')
    a = file.read()
    a = a.split()


    for x in range(0, len(a), 5):
        sideNumber.append(a[x])
        sectorNumber.append(a[x+1])
        partitionNumber.append(a[x+2])
        branch.append(a[x+3])
        FEC.append(a[x+4])


    for x in range(0, len(sideNumber), 1):
        temp = (
        x+1, sideNumber[x], sectorNumber[x], partitionNumber[x], branch[x], FEC[x])
        allParameters.append(temp)
    return allParameters, sideNumber, sectorNumber, partitionNumber, branch, FEC


def connectToDB(db):
    try:
        connection = sqlite3.connect(db)
        return connection
    except Error as e:
        print(e)
    return None


def create_table(connection, sql_create):
    try:
        c = connection.cursor()
        c.execute(sql_create)
    except Error as e:
        print(e)


def creatingDB(connection, sqlSyntax,sqlSyntax1):
    if connection is not None:
        create_table(connection, sqlSyntax)
        create_table(connection, sqlSyntax1)

    else:
        print("Error! cannot create the database connection.")


def fillDB(connection, allParameters):
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO Errors VALUES (?,?,?,?,?,?)', allParameters)
    cursor.execute("select * from Errors")
    connection.commit()




data='preparedBase.txt'



allParameters, sideNumber, sectorNumber, partitionNumber, branch, FEC = readData(data)

connection = connectToDB("fecBase.sql")
sql_create = (
    'CREATE TABLE IF NOT EXISTS Errors(ErrorID integer PRIMARY KEY AUTOINCREMENT, Side integer, Sector integer, Partition integer, Branch integer, Fec integer)')
sqldrop = (
    'DROP TABLE IF EXISTS Errors')

creatingDB(connection,sqldrop, sql_create)
fillDB(connection, allParameters)

