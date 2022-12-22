from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket
import threading
import sys


class Ui_MainWindow(object):
    def setupUi(self, mainWindow, button_list_element):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(700, 825)
        mainWindow.setStyleSheet(");")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_grid = QtWidgets.QFrame(self.centralwidget)
        self.button_grid.setGeometry(QtCore.QRect(10, 120, 691, 701))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        font.setBold(True)
        self.button_grid.setFont(font)
        self.button_grid.setStyleSheet(");")
        self.button_grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_grid.setObjectName("button_grid")
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_1 = QtWidgets.QPushButton(self.button_grid)
        self.button_1.setGeometry(QtCore.QRect(10, 20, 150, 150))
        self.button_1.setMouseTracking(False)
        self.button_1.setStyleSheet(");")
        self.button_1.setText("")
        self.button_1.setCheckable(False)
        self.button_1.setChecked(False)
        self.button_1.setAutoDefault(False)
        self.button_1.setDefault(False)
        self.button_1.setFlat(False)
        self.button_1.setObjectName("button_1")
        self.button_1.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_2 = QtWidgets.QPushButton(self.button_grid)
        self.button_2.setGeometry(QtCore.QRect(180, 20, 150, 150))
        self.button_2.setStyleSheet(");")
        self.button_2.setText("")
        self.button_2.setCheckable(False)
        self.button_2.setAutoDefault(False)
        self.button_2.setDefault(False)
        self.button_2.setFlat(False)
        self.button_2.setObjectName("button_2")
        self.button_2.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_3 = QtWidgets.QPushButton(self.button_grid)
        self.button_3.setGeometry(QtCore.QRect(350, 20, 150, 150))
        self.button_3.setStyleSheet(");\n"
                                    "")
        self.button_3.setText("")
        self.button_3.setCheckable(False)
        self.button_3.setAutoDefault(False)
        self.button_3.setDefault(False)
        self.button_3.setFlat(False)
        self.button_3.setObjectName("button_3")
        self.button_3.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_6 = QtWidgets.QPushButton(self.button_grid)
        self.button_6.setGeometry(QtCore.QRect(180, 190, 150, 150))
        self.button_6.setStyleSheet(");")
        self.button_6.setText("")
        self.button_6.setCheckable(False)
        self.button_6.setAutoDefault(False)
        self.button_6.setDefault(False)
        self.button_6.setFlat(False)
        self.button_6.setObjectName("button_6")
        self.button_6.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_4 = QtWidgets.QPushButton(self.button_grid)
        self.button_4.setGeometry(QtCore.QRect(520, 20, 150, 150))
        self.button_4.setStyleSheet(");")
        self.button_4.setText("")
        self.button_4.setCheckable(False)
        self.button_4.setAutoDefault(False)
        self.button_4.setDefault(False)
        self.button_4.setFlat(False)
        self.button_4.setObjectName("button_4")
        self.button_4.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_5 = QtWidgets.QPushButton(self.button_grid)
        self.button_5.setGeometry(QtCore.QRect(10, 190, 150, 150))
        self.button_5.setStyleSheet(");")
        self.button_5.setText("")
        self.button_5.setCheckable(False)
        self.button_5.setAutoDefault(False)
        self.button_5.setDefault(False)
        self.button_5.setFlat(False)
        self.button_5.setObjectName("button_5")
        self.button_5.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_9 = QtWidgets.QPushButton(self.button_grid)
        self.button_9.setGeometry(QtCore.QRect(10, 360, 150, 150))
        self.button_9.setStyleSheet(");")
        self.button_9.setText("")
        self.button_9.setCheckable(False)
        self.button_9.setAutoDefault(False)
        self.button_9.setDefault(False)
        self.button_9.setFlat(False)
        self.button_9.setObjectName("button_9")
        self.button_9.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_7 = QtWidgets.QPushButton(self.button_grid)
        self.button_7.setGeometry(QtCore.QRect(350, 190, 150, 150))
        self.button_7.setStyleSheet(");")
        self.button_7.setText("")
        self.button_7.setCheckable(False)
        self.button_7.setAutoDefault(False)
        self.button_7.setDefault(False)
        self.button_7.setFlat(False)
        self.button_7.setObjectName("button_7")
        self.button_7.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_8 = QtWidgets.QPushButton(self.button_grid)
        self.button_8.setGeometry(QtCore.QRect(520, 190, 150, 150))
        self.button_8.setStyleSheet(");")
        self.button_8.setText("")
        self.button_8.setCheckable(False)
        self.button_8.setAutoDefault(False)
        self.button_8.setDefault(False)
        self.button_8.setFlat(False)
        self.button_8.setObjectName("button_8")
        self.button_8.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_10 = QtWidgets.QPushButton(self.button_grid)
        self.button_10.setGeometry(QtCore.QRect(180, 360, 150, 150))
        self.button_10.setStyleSheet(");")
        self.button_10.setText("")
        self.button_10.setCheckable(False)
        self.button_10.setAutoDefault(False)
        self.button_10.setDefault(False)
        self.button_10.setFlat(False)
        self.button_10.setObjectName("button_10")
        self.button_10.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_11 = QtWidgets.QPushButton(self.button_grid)
        self.button_11.setGeometry(QtCore.QRect(350, 360, 150, 150))
        self.button_11.setStyleSheet(");")
        self.button_11.setText("")
        self.button_11.setCheckable(False)
        self.button_11.setAutoDefault(False)
        self.button_11.setDefault(False)
        self.button_11.setFlat(False)
        self.button_11.setObjectName("button_11")
        self.button_11.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_12 = QtWidgets.QPushButton(self.button_grid)
        self.button_12.setGeometry(QtCore.QRect(520, 360, 150, 150))
        self.button_12.setStyleSheet(");")
        self.button_12.setText("")
        self.button_12.setCheckable(False)
        self.button_12.setAutoDefault(False)
        self.button_12.setDefault(False)
        self.button_12.setFlat(False)
        self.button_12.setObjectName("button_12")
        self.button_12.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_13 = QtWidgets.QPushButton(self.button_grid)
        self.button_13.setGeometry(QtCore.QRect(10, 530, 150, 150))
        self.button_13.setStyleSheet(");")
        self.button_13.setText("")
        self.button_13.setCheckable(False)
        self.button_13.setAutoDefault(False)
        self.button_13.setDefault(False)
        self.button_13.setFlat(False)
        self.button_13.setObjectName("button_13")
        self.button_13.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_14 = QtWidgets.QPushButton(self.button_grid)
        self.button_14.setGeometry(QtCore.QRect(180, 530, 150, 150))
        self.button_14.setStyleSheet(");")
        self.button_14.setText("")
        self.button_14.setCheckable(False)
        self.button_14.setAutoDefault(False)
        self.button_14.setDefault(False)
        self.button_14.setFlat(False)
        self.button_14.setObjectName("button_14")
        self.button_14.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_15 = QtWidgets.QPushButton(self.button_grid)
        self.button_15.setGeometry(QtCore.QRect(350, 530, 150, 150))
        self.button_15.setStyleSheet(");")
        self.button_15.setText("")
        self.button_15.setCheckable(False)
        self.button_15.setAutoDefault(False)
        self.button_15.setDefault(False)
        self.button_15.setFlat(False)
        self.button_15.setObjectName("button_15")
        self.button_15.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        self.button_16 = QtWidgets.QPushButton(self.button_grid)
        self.button_16.setGeometry(QtCore.QRect(520, 530, 150, 150))
        self.button_16.setStyleSheet(");")
        self.button_16.setText("")
        self.button_16.setCheckable(False)
        self.button_16.setAutoDefault(False)
        self.button_16.setDefault(False)
        self.button_16.setFlat(False)
        self.button_16.setObjectName("button_16")
        self.button_16.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 681, 51))
        font.setPointSize(24)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("\n"
                                 ");")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.my_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.my_wins_label.setGeometry(QtCore.QRect(20, 60, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.my_wins_label.setFont(font)
        self.my_wins_label.setStyleSheet(");")
        self.my_wins_label.setObjectName("my_wins_label")
        self.opp_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.opp_wins_label.setGeometry(QtCore.QRect(350, 60, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.opp_wins_label.setFont(font)
        self.opp_wins_label.setStyleSheet(");")
        self.opp_wins_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.opp_wins_label.setObjectName("opp_wins_label")
        self.name_frame = QtWidgets.QFrame(self.centralwidget)
        self.name_frame.setGeometry(QtCore.QRect(200, 70, 271, 51))
        self.name_frame.setStyleSheet(");")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setGeometry(QtCore.QRect(0, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setBold(False)
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")
        self.name_entry = QtWidgets.QLineEdit(self.name_frame)
        self.name_entry.setGeometry(QtCore.QRect(80, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_entry.setFont(font)
        self.name_entry.setStyleSheet("\n"
                                      ");")
        self.name_entry.setObjectName("name_entry")
        self.name_submit = QtWidgets.QPushButton(self.name_frame)
        self.name_submit.setGeometry(QtCore.QRect(190, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.name_submit.setFont(font)
        self.name_submit.setStyleSheet("\n"
                                       ");")
        self.name_submit.setObjectName("name_submit")
        mainWindow.setCentralWidget(self.centralwidget)

        button_list_element.append(self.button_1)
        button_list_element.append(self.button_2)
        button_list_element.append(self.button_3)
        button_list_element.append(self.button_4)
        button_list_element.append(self.button_5)
        button_list_element.append(self.button_6)
        button_list_element.append(self.button_7)
        button_list_element.append(self.button_8)
        button_list_element.append(self.button_9)
        button_list_element.append(self.button_10)
        button_list_element.append(self.button_11)
        button_list_element.append(self.button_12)
        button_list_element.append(self.button_13)
        button_list_element.append(self.button_14)
        button_list_element.append(self.button_15)
        button_list_element.append(self.button_16)
        self.button_1.clicked.connect(lambda: clicked(self.button_1, 0))
        self.button_2.clicked.connect(lambda: clicked(self.button_2, 1))
        self.button_3.clicked.connect(lambda: clicked(self.button_3, 2))
        self.button_4.clicked.connect(lambda: clicked(self.button_4, 3))
        self.button_5.clicked.connect(lambda: clicked(self.button_5, 4))
        self.button_6.clicked.connect(lambda: clicked(self.button_6, 5))
        self.button_7.clicked.connect(lambda: clicked(self.button_7, 6))
        self.button_8.clicked.connect(lambda: clicked(self.button_8, 7))
        self.button_9.clicked.connect(lambda: clicked(self.button_9, 8))
        self.button_10.clicked.connect(lambda: clicked(self.button_10, 9))
        self.button_11.clicked.connect(lambda: clicked(self.button_11, 10))
        self.button_12.clicked.connect(lambda: clicked(self.button_12, 11))
        self.button_13.clicked.connect(lambda: clicked(self.button_13, 12))
        self.button_14.clicked.connect(lambda: clicked(self.button_14, 13))
        self.button_15.clicked.connect(lambda: clicked(self.button_15, 14))
        self.button_16.clicked.connect(lambda: clicked(self.button_16, 15))
        self.name_submit.clicked.connect(connect)
        self.my_wins_label.setVisible(False)
        self.opp_wins_label.setVisible(False)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Крестики Нолики"))
        self.my_wins_label.setText(_translate("MainWindow", "Мои очки: 0"))
        self.opp_wins_label.setText(_translate("MainWindow", "Не мои очки: 0"))
        self.name_label.setText(_translate("MainWindow", "Игрок:"))
        self.name_submit.setText(_translate("MainWindow", "Ок"))


def connect():
    global your_details
    if len(ui.name_entry.text()) < 1:
        need_name = QMessageBox()
        need_name.setIcon(QMessageBox.Critical)
        need_name.setText("Сначала введите имя")
        need_name.setWindowTitle("Требуется имя")
        need_name.exec_()
    else:
        your_details["name"] = ui.name_entry.text()
        connect_to_server(ui.name_entry.text())


def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode('utf-8'))
        thread = threading.Thread(target=receive_message_from_server, args=(client, "m"))
        thread.start()

        MainWindow.setWindowTitle("Игрок - " + name)
    except socket.error:
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setText("Ошибка: Не удалось подключиться к серверу")
        error.setWindowTitle("Проблема подключения")
        error.exec_()


def receive_message_from_server(sck, m):
    global your_details, opponent_details, your_turn, you_started
    while True:
        from_server = sck.recv(4096).decode('utf-8')

        if not from_server:
            break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                ui.title.setText("Ждём 2го игрока")
            elif from_server == "welcome2":
                ui.title.setText("Соединение")

        elif from_server.startswith("Другой игрок:"):
            ui.title.setText("Крестики Нолики")
            temp = from_server.replace("Другой игрок:", "")
            temp = temp.replace("symbol:", "")
            opponent_details["name"] = temp[0:-1]
            your_details["symbol"] = temp[-1]

            ui.name_frame.setVisible(False)
            ui.my_wins_label.setVisible(True)
            ui.opp_wins_label.setVisible(True)

            # установка, кто за что играет
            if your_details["symbol"] == "O":
                opponent_details["symbol"] = "X"
            else:
                opponent_details["symbol"] = "O"

            # обновление побед
            ui.my_wins_label.setText(your_details["name"] + " (" + your_details["symbol"] + ") очки: " + str(your_details["score"]))
            ui.opp_wins_label.setText(opponent_details["name"] + " (" + opponent_details["symbol"] + ") очки: " + str(opponent_details["score"]))

            # O запускает игру
            if your_details["symbol"] == "O":
                ui.my_wins_label.setStyleSheet("")
                ui.opp_wins_label.setStyleSheet("")
                your_turn = True
                you_started = True
            else:
                ui.opp_wins_label.setStyleSheet("")
                ui.my_wins_label.setStyleSheet("")
                you_started = False
                your_turn = False
        elif from_server.startswith("index:"):
            label_index = int(from_server.replace("index:", ""))

            # обновление доски
            button_list[label_index].setText(opponent_details["symbol"])
            button_list[label_index].setEnabled(False)

            # проверка на победу или ничью
            if check_win(opponent_details["symbol"]):
                opponent_details["score"] += 1
                thread = threading.Thread(target=init)
                thread.start()
            elif check_tie():
                thread = threading.Thread(target=init)
                thread.start()
            else:
                your_turn = True
                ui.my_wins_label.setStyleSheet("")
                ui.opp_wins_label.setStyleSheet("")

    sck.close()


def init():
    global your_turn, your_details, opponent_details, you_started

    ui.my_wins_label.setText(your_details["name"] + " (" + your_details["symbol"] + ") очки: " + str(your_details["score"]))
    ui.opp_wins_label.setText(opponent_details["name"] + " (" + opponent_details["symbol"] + ") очки: " + str(opponent_details["score"]))

    for b in button_list:
        b.setText("")
        b.setEnabled(True)

    if you_started:
        you_started = False
        your_turn = False
        ui.my_wins_label.setStyleSheet("")
        ui.opp_wins_label.setStyleSheet("")
    else:
        you_started = True
        your_turn = True
        ui.my_wins_label.setStyleSheet("")
        ui.opp_wins_label.setStyleSheet("")


def clicked(button, label_index):
    global client, your_turn

    if your_turn:

        button.setText(your_details["symbol"])
        button.setEnabled(False)
        client.send(("index:" + str(label_index)).encode('utf-8'))
        your_turn = False

        # проверка на окончание игры
        if check_win(your_details["symbol"]):
            your_details["score"] += 1
            thread = threading.Thread(target=init)
            thread.start()
        elif check_tie():
            thread = threading.Thread(target=init)
            thread.start()
        else:
            ui.my_wins_label.setStyleSheet("")
            ui.opp_wins_label.setStyleSheet("")

    else:
        wait_turn = QMessageBox()
        wait_turn.setIcon(QMessageBox.Critical)
        wait_turn.setText("Нельзя ходить")
        wait_turn.setWindowTitle("Так")
        wait_turn.exec_()


# проверка на победу игрока
def check_win(player):
    if (button_list[0].text() == button_list[1].text() == button_list[2].text() == button_list[3].text() == player or
            button_list[4].text() == button_list[5].text() == button_list[6].text() == button_list[
                7].text() == player or
            button_list[8].text() == button_list[9].text() == button_list[10].text() == button_list[
                11].text() == player or
            button_list[12].text() == button_list[13].text() == button_list[14].text() == button_list[
                15].text() == player or
            button_list[0].text() == button_list[4].text() == button_list[8].text() == button_list[
                12].text() == player or
            button_list[1].text() == button_list[5].text() == button_list[9].text() == button_list[
                13].text() == player or
            button_list[2].text() == button_list[6].text() == button_list[10].text() == button_list[
                14].text() == player or
            button_list[3].text() == button_list[7].text() == button_list[11].text() == button_list[
                15].text() == player or
            button_list[0].text() == button_list[5].text() == button_list[10].text() == button_list[
                15].text() == player or
            button_list[3].text() == button_list[6].text() == button_list[9].text() == button_list[
                12].text() == player):
        return True
    return False


# если поле заполнено - ничья
def check_tie():
    for i, b in enumerate(button_list):
        if b.text() == "":
            return False
    return True


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
button_list = []
ui.setupUi(MainWindow, button_list)
MainWindow.setWindowTitle("Крестики Нолики")
MainWindow.show()

client = None
HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 5050

num_cols = 3
your_turn = False
you_started = False

your_details = {
    "name": " ",
    "symbol": "X",
    "score": 0
}

opponent_details = {
    "name": " ",
    "symbol": "O",
    "score": 0
}

sys.exit(app.exec_())
