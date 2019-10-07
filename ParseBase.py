import zipfile
import glob
import sqlite3
from sqlite3 import Error

def readData(data):
    zip_ref = zipfile.ZipFile(data+'.zip', 'r')
    zip_ref.extractall()
    zip_ref.close()

    list_of_files = glob.glob(data+'/*.data')

    sideNumber=[]
    sectorNumber=[]
    partitionNumber=[]
    branch=[]
    FEC=[]
    ALTROchip=[]
    ALTROchannel=[]

    for x in list_of_files:
        file = open(x, 'r')
        a = file.read()
        a=a.split()
        a[0]=""
        for x in range (1, len(a), 6):
            sideNumber.append(a[x+1])
            sectorNumber.append(a[x+2])
            partitionNumber.append(a[x+3])
            binaryInfo=(bin(int(a[x+4])))
            binaryInfo='{:012d}'.format(int(binaryInfo[2:]))
            branch.append(binaryInfo[0])
            FEC.append(int('{:04d}'.format(int(binaryInfo[1:5])),2))
            ALTROchip.append(int('{:03d}'.format(int(binaryInfo[5:8])),2))
            ALTROchannel.append(int('{:04d}'.format(int(binaryInfo[8:12])),2))

    compFEC=FEC[0]
    compBranch=branch[0]
    compPartition = partitionNumber[0]
    compSector = sectorNumber[0]
    compSide=sideNumber[0]
    i=0
    output = open("preparedBase.txt", "w")

    output.write(str(sideNumber[0])+ " "+str(sectorNumber[0])+" "+str(partitionNumber[0])+" "+str(branch[0])+" " +str(FEC[0]) +'\n')
    i = i + 1


    for x in range(1,len(FEC),1):
        if FEC[x]!=compFEC:
            output.write(str(sideNumber[x])+ " " + str(sectorNumber[x])+ " " +str(partitionNumber[x])+" "+str(branch[x])+" "+ str(FEC[x]) +'\n')
            i = i + 1

        if FEC[x]==compFEC and branch[x]!=compBranch:
            output.write(str(sideNumber[x]) + " " + str(sectorNumber[x]) + " " + str(partitionNumber[x]) + " " + str(
                branch[x]) + " " + str(FEC[x]) + '\n')
            i = i + 1

        if FEC[x]==compFEC and branch[x]==compBranch and partitionNumber[x]!=compPartition:
            output.write(str(sideNumber[x]) + " " + str(sectorNumber[x]) + " " + str(partitionNumber[x]) + " " + str(
                branch[x]) + " " + str(FEC[x]) + '\n')
            i = i + 1

        if FEC[x] == compFEC and branch[x] == compBranch and partitionNumber[x] == compPartition and sectorNumber[x]!= compSector:
            output.write(str(sideNumber[x]) + " " + str(sectorNumber[x]) + " " + str(partitionNumber[x]) + " " + str(
                branch[x]) + " " + str(FEC[x]) + '\n')
            i = i + 1

        if FEC[x] == compFEC and branch[x] == compBranch and partitionNumber[x] == compPartition and sectorNumber[
                x] == compSector and sideNumber[x]!=compSide:
            output.write(str(sideNumber[x]) + " " + str(sectorNumber[x]) + " " + str(partitionNumber[x]) + " " + str(
                branch[x]) + " " + str(FEC[x]) + '\n')
            i = i + 1

        compBranch=branch[x]
        compFEC=FEC[x]
        compPartition=partitionNumber[x]
        compSector=sectorNumber[x]
        compSide=sideNumber[x]
    print(str(i))



data='20181203'
readData(data)