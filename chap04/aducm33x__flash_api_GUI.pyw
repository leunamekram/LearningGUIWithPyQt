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

    # GUI class variables
    address_entry = 0
    address = None
    size_entry = 0
    size = None
    feedatah_entry = 0
    feedatah = None
    feedatal_entry = 0
    feedatal = None

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create the first group box
        groupbox1 = self.createFormGroupBox1()
        groupbox2 = self.createFormGroupBox2()
        self.status = QLabel("Status: Ready")
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(groupbox1)
        mainlayout.addWidget(groupbox2)
        mainlayout.addWidget(self.status)
        self.setLayout(mainlayout)
        self.setFixedSize(self.sizeHint())
        self.setWindowTitle("Flash Test Tool Raw API")
        self.getTextEntries()

    def createFormGroupBox1(self):
        # Add buttons
        button1 = QPushButton("Mass Erase Prog")
        button2 = QPushButton("Mass Erase Data (2kB)")
        button3 = QPushButton("Mass Erase Data (4kB)")
        button4 = QPushButton("Erase Page")
        button5 = QPushButton("Write")
        button6 = QPushButton("Write Word-Page")
        button7 = QPushButton("Write w/o ECC")
        button8 = QPushButton("Read")

        # Button properties
        button1.setFocusPolicy(Qt.NoFocus)
        button2.setFocusPolicy(Qt.NoFocus)
        button3.setFocusPolicy(Qt.NoFocus)
        button4.setFocusPolicy(Qt.NoFocus)
        button5.setFocusPolicy(Qt.NoFocus)
        button6.setFocusPolicy(Qt.NoFocus)
        button7.setFocusPolicy(Qt.NoFocus)
        button8.setFocusPolicy(Qt.NoFocus)

        # Connect button signals to slot(s)
        # TODO: Add proper button actions
        button1.clicked.connect(self.clicked)
        button2.clicked.connect(self.clicked)
        button3.clicked.connect(self.clicked)
        button4.clicked.connect(self.clicked)
        button5.clicked.connect(self.clicked)
        button6.clicked.connect(self.clicked)
        button7.clicked.connect(self.clicked)
        button8.clicked.connect(self.clicked)

        # Create the group box object
        groupbox = QGroupBox('FW API Commands')

        # Create the layout
        layout = QGridLayout()
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(button4, 0, 3)
        layout.addWidget(button5, 1, 0)
        layout.addWidget(button6, 1, 1)
        layout.addWidget(button7, 1, 2)
        layout.addWidget(button8, 1, 3)

        # Set groupbox layout
        groupbox.setLayout(layout)
        groupbox.clearFocus()
        return groupbox

    def createFormGroupBox2(self):
        # Create the groupbox
        groupbox = QGroupBox('FW API Entries')

        # Text entry widgets
        self.address = QLineEdit('0x0')
        self.size = QLineEdit('0x0')
        self.feedatah = QLineEdit('0x0')
        self.feedatal = QLineEdit('0x0')

        # Assign text entry widgets to slots
        self.address.returnPressed.connect(self.getTextEntries)
        self.size.returnPressed.connect(self.getTextEntries)
        self.feedatal.returnPressed.connect(self.getTextEntries)
        self.feedatah.returnPressed.connect(self.getTextEntries)

        # Create the layout
        layout = QFormLayout()
        layout.addRow(QLabel("Address:"), self.address)
        layout.addRow(QLabel("Read/Write Size:"), self.size)
        layout.addRow(QLabel("FEEDATAH:"), self.feedatah)
        layout.addRow(QLabel("FEEDATAL:"), self.feedatal)

        # Set groupbox layout
        groupbox.setLayout(layout)
        return groupbox

    def clicked(self):
        # sender() returns None if clicked was invoked by a simple function call
        sender = self.sender()

        # This should be called by a valid widget
        if sender is None or not isinstance(sender, QPushButton):
            return

        if self.getTextEntries():
            self.status.setText("Status: Command '{}'".format(sender.text()))
            # Call API command here via dictionary

    def getTextEntries(self):
        try:
            self.address_entry = int(self.address.text(), 16)
            self.size_entry = int(self.size.text(), 16)
            self.feedatah_entry = int(self.feedatah.text(), 16)
            self.feedatal_entry = int(self.feedatal.text(), 16)
            return True
        except ValueError as e:
            self.status.setText("Status: '{}'".format(e))
            return False


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
