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
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Get FOREX data
        date = self.getdata()
        # Sort the rates by Currency name
        rates = sorted(self.rates.keys())

        # Create a label widget with the date
        dateLabel = QLabel(date)
        # Comboboxes are 'pull-down' menus
        self.fromComboBox = QComboBox()
        # The contents of the pull-down are the sorted currency names
        self.fromComboBox.addItems(rates)
        # Spinbox that handles float values
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)  # Spinbox range
        self.fromSpinBox.setValue(1.00)  # Spinbox initial value
        # Create combobox for the target currency
        self.toComboBox = QComboBox()
        # The contents of the pull-down are also the sorted currency names
        self.toComboBox.addItems(rates)
        # toLabel gets updated for every conversion but we initially set it to 1.00
        self.toLabel = QLabel("1.00")
        # Use grid layout for the widgets
        grid = QGridLayout()
        # add the widgets to the grid by specifying the row and column location
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        # Set the Form's main layout to grid
        self.setLayout(grid)
        # Signals and slots. We now define what happens when a widget emits an event
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)
        # Set the window title
        self.setWindowTitle("Currency")


    def updateUi(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()
        amount = ((self.rates[from_] / self.rates[to]) *
                  self.fromSpinBox.value())
        self.toLabel.setText("{0:.2f}".format(amount))

    # TODO: Find another way of getting csv data. Rates are not working
    def getdata(self):  # Idea taken from the Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            data = open(r".\FX_RATES_DAILY-sd-2017-01-03.csv", 'r').read()
            print(data)
            for line in data.split("\n"):
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception as e:
            return "Failed to download:\n{}".format(e)

# Create the application object
app = QApplication(sys.argv)
# Create a Form instance
form = Form()
# Paint the Form GUI
form.show()
# Run main application's event loop
app.exec_()

