import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


app = QApplication(sys.argv)
img = QPixmap("test.png")
lab = QLabel()
lab.setPixmap(img)
lab.setScaledContents(True)
lab.show()
sys.exit(app.exec_())