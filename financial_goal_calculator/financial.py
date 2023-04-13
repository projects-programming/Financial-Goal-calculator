import sys
import random

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import ( QWidget, QApplication, QMainWindow, QLabel,
                             QPushButton, QVBoxLayout, QLineEdit, QGridLayout)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Financial Goal Calculator")

        # Adding app_title label widget
        app_title = QLabel("Financial Goal Calculator")
        font = app_title.font()
        font.setPointSize(18)
        app_title.setFont(font)


        # Adding wage_prompt line edit widgit
        wage_prompt = QLineEdit()
        wage_prompt.setMaxLength(50)
        wage_prompt.setPlaceholderText("Enter your hourly wage amount in digits")
        
        # Adding goal_prompt line edit widget
        goal_prompt = QLineEdit()
        goal_prompt.setMaxLength(100)
        goal_prompt.setPlaceholderText("Enter your goal amount you would like to reach in digits")

        # Adding calculate button
        calculate_button = QPushButton("Calculate")

        # Adding a way to present the data calculated
        present_data = QLabel("You will need to work ____ "  "hours to reach your goal.")
        font = present_data.font()
        font.setPointSize(14)
        present_data.setFont(font)
        #widget.setReadOnly(True) # uncomment this to make readonly

        wage_prompt.returnPressed.connect(self.return_pressed)
        wage_prompt.selectionChanged.connect(self.selection_changed)
        wage_prompt.textChanged.connect(self.text_changed)
        wage_prompt.textEdited.connect(self.text_edited)

        # Adding a Layout
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)

        layout.addWidget(app_title, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(wage_prompt, 1, 0)
        layout.addWidget(goal_prompt, 2, 0)
        layout.addWidget(calculate_button, 3, 0)
        layout.addWidget(present_data, 4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    
if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()