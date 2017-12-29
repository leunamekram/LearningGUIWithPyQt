#!/usr/bin/env python3
# Copyright (c) 2008-10 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import functools
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        button1 = QPushButton("COMMAND_ERASEPAGE")
        button2 = QPushButton("COMMAND_MASSERASEPROG")
        button3 = QPushButton("COMMAND_MASSERASEDATA")
        button4 = QPushButton("COMMAND_MASSERASEALLDATA")
        button5 = QPushButton("COMMAND_WRITE")
        button6 = QPushButton("COMMAND_READ")
        button7 = QPushButton("COMMAND_WRITEPAGEWORD")
        button8 = QPushButton("COMMAND_WRITE_ECC_DISABLED")
        self.label = QLabel("Click a button...")

        grid = QGridLayout()
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 0, 2)
        grid.addWidget(button4, 0, 3)
        grid.addWidget(button5, 1, 0)
        grid.addWidget(button6, 1, 1)
        grid.addWidget(button7, 1, 2)
        grid.addWidget(button8, 1, 3)
        grid.addWidget(self.label, 2, 0)
        self.setLayout(grid)

        button1.clicked.connect(self.clicked)
        button2.clicked.connect(self.clicked)
        button3.clicked.connect(self.clicked)
        button4.clicked.connect(self.clicked)
        button5.clicked.connect(self.clicked)
        button6.clicked.connect(self.clicked)
        button7.clicked.connect(self.clicked)
        button8.clicked.connect(self.clicked)

        self.setWindowTitle("FLash Tool Tester")

    def clicked(self):
        # sender() returns None if clicked was involved by a simple function call
        button = self.sender()
        print(button)
        if button is None or not isinstance(button, QPushButton):
            return
        self.label.setText("You clicked button '{}'".format(
                           button.__name__()))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
