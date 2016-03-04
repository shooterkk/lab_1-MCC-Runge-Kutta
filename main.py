#coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from custom_canvas import StaticCanvas

app = QApplication(sys.argv)
app.setApplicationName('Lab 1')
form_class, base_class = loadUiType('main_form.ui')


class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.x_t = StaticCanvas(self.x_t_tab,'$x(t)$')
        self.x_dx = StaticCanvas(self.x_dx_tab,'$\dot{x}(x)$')
        self.afc = StaticCanvas(self.afc_tab)
        self.x_t_layout.addWidget(self.x_t)
        self.x_dx_layout.addWidget(self.x_dx)
        self.afc_layout.addWidget(self.afc)

    @pyqtSlot()
    def build_graph(self):
        pass

    @pyqtSlot()
    def template_selected(self):
        pass

    @pyqtSlot('QString')
    def coef_changed(self, value):
        pass

    @pyqtSlot(int)
    def limit_change(self, velue):
        pass

    @pyqtSlot('double')
    def step_change(self, value):
        pass

    @pyqtSlot('QString')
    def initval_change(self, value):
        pass



#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('Лабораторна робота №1 - МСС')
form.show()
sys.exit(app.exec_())