import sys
import random

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import ( QWidget, QApplication, QMainWindow, QLabel,
                             QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QSpinBox)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Financial Goal Calculator")

        # Adding app_title label widget
        app_title = QLabel("Financial Goal Calculator")
        font = app_title.font()
        font.setPointSize(18)
        app_title.setFont(font)
        app_title.setStyleSheet("QLabel { background-color : #27374D; color : #DDE6ED; }");

        # Adding wage_prompt line edit widgit
        self.wage_prompt = QLineEdit()
        self.wage_prompt.setMaxLength(50)
        self.wage_prompt.setPlaceholderText("Enter your hourly wage amount in digits")
        self.wage_prompt.setStyleSheet("QLineEdit { background-color : #27374D; color : #DDE6ED; }");
    
        # Adding goal_prompt line edit widget
        self.goal_prompt = QLineEdit()
        self.goal_prompt.setMaxLength(100)
        self.goal_prompt.setPlaceholderText("Enter your goal amount you would like to reach in digits")
        self.goal_prompt.setStyleSheet("QLineEdit { background-color : #27374D; color : #DDE6ED; }");
        self.setStyleSheet("background-color: #27374D;")

        # Adding calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setStyleSheet("QPushButton { background-color : #526D82; color : #DDE6ED; }");
        # add a calculate function
        self.calculate_button.clicked.connect(self.calculate_financial_goal)

        # Adding a way to present the data calculated
        self.present_data = QLabel("You will need to work ____ "  "hours to reach your goal.")
        font = self.present_data.font()
        font.setPointSize(14)
        self.present_data.setFont(font)
        self.present_data.setStyleSheet("QLabel { background-color : #27374D; color : #DDE6ED; }");
        #widget.setReadOnly(True) # uncomment this to make readonly

        # Adding a Layout
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)

        layout.addWidget(app_title, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.wage_prompt, 1, 0)
        layout.addWidget(self.goal_prompt, 2, 0)
        layout.addWidget(self.calculate_button, 3, 0)
        layout.addWidget(self.present_data, 4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.setCentralWidget(widget)
    
    def calculate_financial_goal(self):
        """Calculate hours to reach users goal"""

        # Get hourly wage, converted the string to a floating number
        hourly_wage = self.wage_prompt.displayText()
        print(hourly_wage)
        wage_entered = self.wage_prompt.text()
        wage = float(wage_entered)

        # Get goal amount, converted the string to a floating number
        goal_amount = self.goal_prompt.displayText()
        print(goal_amount)
        amount_entered = self.goal_prompt.text()
        amount = float(amount_entered)

        # Calculate the hours needed to work to reach the goal amount
        data_calculation = amount/wage
        print(data_calculation)
        
        # Display results
        self.present_data.setText("You will need to work " + str(data_calculation) + " hours to reach your goal.")
    
if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()