import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.sicaklik = 3.6
        self.gaz = 40
        self.hacim = 144
        self.verimlilik = 100
        self.bilgiler = QtWidgets.QLabel("Erdal Emlik 1711012024   "
                                      "Melih Fırat Avcı 1711012034")
        self.temp = QtWidgets.QLabel("Sıcaklık")
        self.gas = QtWidgets.QLabel("Gaz")
        self.verim = QtWidgets.QLabel("Verimlilik")
        self.hcm = QtWidgets.QLabel("Hacim")
        self.temp1 = QtWidgets.QLineEdit(str(self.sicaklik))
        self.gas1 = QtWidgets.QLineEdit(str(self.gaz))
        self.verim1 = QtWidgets.QLineEdit(str(self.verimlilik))
        self.hcm1 = QtWidgets.QLineEdit(str(self.hacim))
        self.arttir = QtWidgets.QPushButton("Arttır")
        self.azalt = QtWidgets.QPushButton("Azalt")
        self.dengele = QtWidgets.QPushButton("Dengele")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.temp)
        v_box.addWidget(self.temp1)
        v_box.addWidget(self.gas)
        v_box.addWidget(self.gas1)
        v_box.addWidget(self.verim)
        v_box.addWidget(self.verim1)
        v_box.addWidget(self.hcm)
        v_box.addWidget(self.hcm1)
        v_box.addStretch()
        v_box.addWidget(self.arttir)
        v_box.addWidget(self.azalt)
        v_box.addWidget(self.dengele)
        v_box.addWidget(self.bilgiler)
        v_box.addStretch()
        self.setLayout(v_box)
        self.arttir.clicked.connect(self.art)
        self.azalt.clicked.connect(self.azal)
        self.dengele.clicked.connect(self.denge)
        self.show()
    def art(self):
        self.sicaklik +=1
        round(self.sicaklik,1)
        if self.sicaklik>3.6:
            self.hacim+=1
            self.verimlilik-=1

            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
        elif self.sicaklik<3.6:
            self.hacim -=1
            self.verimlilik -=1

            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
        else:
            self.sicaklik = 3.6
            self.hacim = 100
            self.verimlilik = 100
            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
    def azal(self):
        self.sicaklik -=1
        if self.sicaklik == 3.5999999999999996:
            self.sicaklik = 3.6
        if self.sicaklik>3.6:
            self.hacim +=1
            self.verimlilik -=1
            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
        elif self.sicaklik<3.6:
            self.hacim -=1
            self.verimlilik -=1
            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
        else:
            self.sicaklik = 3.6
            self.hacim = 100
            self.verimlilik = 100
            self.temp1.setText(str(self.sicaklik))
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
    def denge(self):
        if self.sicaklik<3.6:
            self.temp1.setText(str(self.sicaklik))
            self.gaz = abs(self.hacim)/abs(self.sicaklik)
            self.hacim = 144
            self.verimlilik =100
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))
        elif self.sicaklik>3.6:
            self.temp1.setText(str(self.sicaklik))
            self.gaz = self.hacim/abs(self.sicaklik)
            self.hacim = 144
            self.verimlilik = 100
            self.gas1.setText(str(self.gaz))
            self.verim1.setText(str(self.verimlilik))
            self.hcm1.setText(str(self.hacim))

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
