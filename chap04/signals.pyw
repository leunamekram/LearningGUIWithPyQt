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

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    # An example of using each widgets predefined signals and slots
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()  # Create a 'knob' widget
        dial.setNotchesVisible(True)  # Show notches around the knob
        spinbox = QSpinBox()  # Create an integer spinbox widget

        # Define the layout to be each widget horizontally aligned
        layout = QHBoxLayout()
        # add the widgets to the layout
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        # Set the Form's layout
        self.setLayout(layout)

        # dial's signal is assigned to spinbox's slot
        dial.valueChanged.connect(spinbox.setValue)
        # spinbox's signal is assigned to dial's slot
        spinbox.valueChanged.connect(dial.setValue)
        # Window title
        self.setWindowTitle("Signals and Slots")


class Form2(QDialog):
    # The same as Form()
    def __init__(self, parent=None):
        super(Form2, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        self.setWindowTitle("Signals and Slots")


class ZeroSpinBox(QSpinBox):

    zeros = 0
    # Signals must be defined at the class level not at the instance level
    # Implementation should be reviewed based on the new PyQt5 doc
    # http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
    atzero = pyqtSignal(int, name='atzero')

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.valueChanged.connect(self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.atzero.emit(self.zeros)


class Form3(QDialog):
    # An example of how to define own signals and slots
    def __init__(self, parent=None):
        super(Form3, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        # Connect the dial signal to zerospinbox slot
        dial.valueChanged.connect(zerospinbox.setValue)
        # Connect the zerospinbox signal to dial slot
        zerospinbox.valueChanged.connect(dial.setValue)
        # Connect the zerospinbox userdefined signal to Form slot
        zerospinbox.atzero.connect(self.announce)

        self.setWindowTitle("Signals and Slots")

    def announce(self, zeros):
        print("ZeroSpinBox has been at zero {} times".format(zeros))


class Form4(QDialog):
    # An example of capturing text change signal from linedit
    def __init__(self, parent=None):
        super(Form4, self).__init__(parent)

        lineedit = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(lineedit)
        self.setLayout(layout)

        lineedit.textChanged.connect(self.consoleEcho)
        self.setWindowTitle("Signals and Slots")

    def consoleEcho(self, text):
        print(text)


class TaxRate(QObject):
    rateChanged = pyqtSignal(float, name='rateChanged')

    # An example of using the signals and slots on any QObject subclass
    def __init__(self):
        super(TaxRate, self).__init__()
        self.__rate = 17.5

    def rate(self):
        return self.__rate

    # A standard way of writing slots is to priorly check if the new value is
    # different with the current value
    def setRate(self, rate: float):
        if rate != self.__rate:
            self.__rate = rate
            self.rateChanged.emit(self.__rate)


def rateChanged(value):
    print("TaxRate changed to {0:.2f}%".format(value))


app = QApplication(sys.argv)
form = None
if len(sys.argv) == 1 or sys.argv[1] == "1":
    form = Form()
elif sys.argv[1] == "2":
    form = Form2()
elif sys.argv[1] == "3":
    form = Form3()
elif sys.argv[1] == "4":
    form = Form4()
if form is not None:
    form.show()
    app.exec_()
else:  # if sys.argv[1] == "5"
    vat = TaxRate()
    vat.rateChanged.connect(rateChanged)
    vat.setRate(17.5)    # No change will occur (new rate is the same)
    vat.setRate(8.5)     # A change will occur (new rate is different)
