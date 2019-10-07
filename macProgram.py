from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Form(object):
    def setupUi(self, Form):

        connection = connectToDB('fecBase.sql')
        query = "select * from Errors"
        result = query_to_db(connection, query)
        number_of_rows = result.__len__()

        Form.setObjectName("NA61 Tool")
        Form.resize(1000, 700)
        Form.setMinimumSize(QtCore.QSize(970, 710))
        Form.setMaximumSize(QtCore.QSize(970, 710))
        Form.setSizeIncrement(QtCore.QSize(100, 200))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 356, 77))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(65)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(380, 10, 580, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(570, 80))
        self.graphicsView.setMaximumSize(QtCore.QSize(570, 120))
        self.graphicsView.setObjectName("graphicsView")


        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(650, 10,620,101))
        pixamp = QPixmap('NA61LOGO.jpg')
        self.pic.setPixmap(pixamp)
        self.pic.show()

        self.pic2 = QtWidgets.QLabel(Form)
        self.pic2.setGeometry(QtCore.QRect(390,11, 550, 99))
        pixamp2 =QPixmap('UJLOGO.jpg')
        self.pic2.setPixmap(pixamp2)
        self.pic2.show()


        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(9, 115, 350, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 300))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(40, 70, 81, 21))

        self.Qcheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.Qcheckbox.setGeometry(QtCore.QRect(125, 70, 81, 21))

        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(190, 70, 81, 21))

        self.Qcheckbox2 = QtWidgets.QCheckBox(self.groupBox)
        self.Qcheckbox2.setGeometry(QtCore.QRect(275, 70, 81, 21))

        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(40, 150, 81, 21))
        self.spinBox_3.setObjectName("spinBox_3")

        self.Qcheckbox3 = QtWidgets.QCheckBox(self.groupBox)
        self.Qcheckbox3.setGeometry(QtCore.QRect(125, 150, 81, 21))

        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setGeometry(QtCore.QRect(190, 150, 81, 21))

        self.Qcheckbox4 = QtWidgets.QCheckBox(self.groupBox)
        self.Qcheckbox4.setGeometry(QtCore.QRect(275, 150, 81, 21))


        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox)

        self.Qcheckbox5 = QtWidgets.QCheckBox(self.groupBox)
        self.Qcheckbox5.setGeometry(QtCore.QRect(125, 220, 81, 21))

        self.spinBox_5.setGeometry(QtCore.QRect(40, 220, 81, 21))
        self.spinBox_5.setObjectName("spinBox_5")







        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 81, 20))

        self.pushButton2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton2.setGeometry(QtCore.QRect(190, 250, 81, 20))


        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton2.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(190, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(190, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 420, 351, 271))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 13, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 160, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_15 = QtWidgets.QLabel(self.groupBox_3)

        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(20, 60, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(40, 100, 31, 31))

        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_16.setFont(font)

        self.label_15.setGeometry(QtCore.QRect(40, 200, 331, 31))

        self.label_15.setText(str(number_of_rows))
        QApplication.processEvents()

        if (number_of_rows == 0):
            self.label_15.setStyleSheet("color: green;")
            self.label_16.setStyleSheet("color: green;")
            self.label_16.setText("NO")
        else:
            self.label_16.setStyleSheet("color: red;")
            self.label_16.setText("-")
            self.label_15.setStyleSheet("color: red;")




        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(380, 160, 610, 532))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())


        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(570, 530))
        self.tableWidget.setMaximumSize(QtCore.QSize(570, 530))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 2000))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setRowCount(number_of_rows)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(102)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(102)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(380, 128, 103, 15))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.tableWidget.setHorizontalHeaderLabels(['Side', 'Sector', 'Partition', 'Branch', 'FEC Number'])
        self.tableWidget.setVerticalHeaderLabels([])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        for x in range (0,number_of_rows,1):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(result[x][1])))
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(result[x][2])))
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(result[x][3])))
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(result[x][4])))
            self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(str(result[x][5])))

        self.pushButton.clicked.connect(self.update_table)
        self.pushButton2.clicked.connect(self.clear)




    def clear(self):
        connection = connectToDB('fecBase.sql')
        query = "select * from Errors"
        result = query_to_db(connection, query)
        number_of_rows = result.__len__()
        self.tableWidget.setRowCount(number_of_rows)
        self.label_15.setText(str(number_of_rows))
        QApplication.processEvents()

        for x in range (0,number_of_rows,1):
            self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(result[x][1])))
            self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(result[x][2])))
            self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(result[x][3])))
            self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(result[x][4])))
            self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(str(result[x][5])))


        self.label_16.setStyleSheet("color: red;")
        self.label_16.setText("-")
        self.label_15.setStyleSheet("color: red;")

        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(0)

        self.Qcheckbox.setCheckState(0)
        self.Qcheckbox2.setCheckState(0)
        self.Qcheckbox3.setCheckState(0)
        self.Qcheckbox4.setCheckState(0)
        self.Qcheckbox5.setCheckState(0)



    def update_table(self):
        globalquery="select * from Errors "
        side = self.spinBox.value()
        sideCheck = self.Qcheckbox.isChecked()
        sideQuery=globalquery
        if sideCheck:
            sideQuery=globalquery + "where Side= " + str(side)

        sector = self.spinBox_2.value()
        sectorCheck = self.Qcheckbox2.isChecked()
        sectorQuery=globalquery
        if sectorCheck:
            sectorQuery=globalquery + "where Sector = " + str(sector)

        partition = self.spinBox_3.value()
        partitionCheck = self.Qcheckbox3.isChecked()
        partitionQuery=globalquery
        if partitionCheck:
            partitionQuery=globalquery + "where Partition = " + str(partition)


        branch = self.spinBox_4.value()
        branchCheck = self.Qcheckbox4.isChecked()
        branchQuery = globalquery
        if branchCheck:
            branchQuery=globalquery + "where Branch = " + str(branch)

        fec=self.spinBox_5.value()
        fecCheck = self.Qcheckbox5.isChecked()
        fecQuery= globalquery
        if fecCheck:
            fecQuery=globalquery + "where Fec = " + str(fec)



        connection = connectToDB('fecBase.sql')
        if(sideCheck or sectorCheck or partitionCheck or branchCheck or fecCheck):
            query = sideQuery + " INTERSECT " + sectorQuery + " INTERSECT " + partitionQuery + " INTERSECT " + \
            branchQuery + " INTERSECT " + fecQuery  + ";"
        else:
            query = "select * from Errors"


        result = query_to_db(connection, query)
        number_of_rows = result.__len__()
        QApplication.processEvents()


        self.label_15.setText(str(number_of_rows))

        if(number_of_rows==0):
            self.tableWidget.setRowCount(number_of_rows)
            self.label_15.setStyleSheet("color: green;")
            self.label_16.setStyleSheet("color: green;")
            self.label_16.setText("NO")

        if (number_of_rows != 0):
            self.tableWidget.setRowCount(number_of_rows)
            self.label_16.setStyleSheet("color: red;")
            self.label_16.setText("YES")
            self.label_15.setStyleSheet("color: red;")

            for x in range (0,number_of_rows,1):
                self.tableWidget.setItem(x, 0, QtWidgets.QTableWidgetItem(str(result[x][1])))
                self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(str(result[x][2])))
                self.tableWidget.setItem(x, 2, QtWidgets.QTableWidgetItem(str(result[x][3])))
                self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem(str(result[x][4])))
                self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem(str(result[x][5])))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NA61 Tool"))
        self.label.setText(_translate("Form", "NA61 TOOLBOX"))
        self.label_2.setText(_translate("Form", "SET PARAMETERS"))
        self.pushButton.setText(_translate("Form", "CHECK"))
        self.pushButton2.setText(_translate("Form", "CLEAR"))
        self.label_3.setText(_translate("Form", "SIDE"))
        self.label_4.setText(_translate("Form", "SECTOR"))
        self.label_5.setText(_translate("Form", "PARTTION"))
        self.label_6.setText(_translate("Form", "BRANCH"))
        self.label_7.setText(_translate("Form", "FEC NUMBER"))
        self.label_11.setText(_translate("Form", "STATISTICS"))
        self.label_12.setText(_translate("Form", "NUMBER OF RECORDS"))
        self.label_14.setText(_translate("Form", "DOES YOUR CARD IS IN THE DATABASE?"))
        self.label_10.setText(_translate("Form", "RESULTS"))


def connectToDB(db):
    try:
        connection = sqlite3.connect(db)
        return connection
    except Error as e:
        print(e)
    return None

def query_to_db(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
