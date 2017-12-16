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

import sys  # for accessing command line arugments
import time  # for sleep function where execution is halted
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # Contains QApplication

# Create QApplication object. We are not yet creating the GUI application here
# Command-line argument(sys.argv) is passed in the class init for the QApplication
# to process supported arguments, if any (see initialiser's docs)
app = QApplication(sys.argv)

try:
    due = QTime.currentTime()  # Default time
    message = "Alert!"  # Default message

    # If there are no command-line arguments passed
    if len(sys.argv) < 2:
        # a ValueError exception is raised
        raise ValueError

    # Get command-line argument for hours and minutes (should be colon(:) separated)
    hours, mins = sys.argv[1].split(":")

    # The passed time should be valid integer values
    due = QTime(int(hours), int(mins))

    if not due.isValid():
        # If QTime returns the due time to be out of range, we raise ValueError exception
        raise ValueError

    # Treat the remaining CL args as part of the message
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

except ValueError:
    # Any caught exception will make the default message to be the usage example
    message = "Usage: alert.pyw HH:MM [optional message]"  # 24hr clock

# Wait till we reached/passed the due time
while QTime.currentTime() < due:
    # Suspend for a while to let other running programs have the chance to execute
    time.sleep(20)  # 20 seconds

# ================================================================================
# Here, we begin creating our GUI app
# ================================================================================

# Our GUI's widget is simply a label. This will be the window
label = QLabel("<font color=red size=72><b>{}</b></font>"
               .format(message))

# Set the window's flag to disable the title bar
label.setWindowFlags(Qt.SplashScreen)

# This doesn't show the window we just created but schedules/adds it to the Qapp's
# object event queue
label.show()

# Set-up the single-shot timer to call QApp's quit method after 60 seconds time-out
QTimer.singleShot(60000, app.quit)  # 1 minute

# At this point, 2 events are scheduled: one it the event to display our widget and the
# other is the event to terminate it after 1-minute

# Call now QApp's exec_ method to process the scheduled events inside EVENT LOOPS
app.exec_()
