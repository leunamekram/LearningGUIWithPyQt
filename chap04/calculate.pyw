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
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Top-level windows are usually sub-classed from QDialog, QMainWindow or (seldomly) QWidget
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Add the 2-widgets we need to reference within Form
        self.browser = QTextBrowser()
        # QLineEdit is init'd with some text with the text entirely selected
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        # Define the layout to be each widget vertically aligned
        layout = QVBoxLayout()
        # Add the two widgets to the layout
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        # Setting the layout of Form to 'layout' makes the 2 widgets of it to be a child of Form
        self.setLayout(layout)
        # Set the focus to lineedit
        self.lineedit.setFocus()
        # Connect the 'Enter' event to updateUI method
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("{} = <b>{}</b>".format(text,
                                eval(text)))
        except:
            self.browser.append("<font color=red>{} is invalid!</font>"
                                .format(text))

# Create the application object
app = QApplication(sys.argv)
# Instantiate the form object
form = Form()
# Paint the Form object to our screen
form.show()
# Start off the event loop
app.exec_()
