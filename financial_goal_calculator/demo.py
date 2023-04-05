import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, 
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QWidget
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Create our layouts
        main_layout = QVBoxLayout()

        # QLabel example
        title_label = QLabel("Title for my app")

        # Set the font
        font = title_label.font()
        font.setPointSize(30)
        title_label.setFont(font)

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                  Qt.AlignmentFlag.AlignTop)

        # Add label to main_layout
        main_layout.addWidget(title_label)

        # Checkboxes
        this_checkbox = QCheckBox()
        this_label = QLabel("This")
        that_checkbox = QCheckBox()
        that_label = QLabel("That")

        # Add checkboxes to horizontal layouts
        check_box_row = QHBoxLayout()
        check_box_row.setAlignment(Qt.AlignmentFlag.AlignLeft)
        check_box_row.addWidget(this_checkbox)
        check_box_row.addWidget(this_label)
        check_box_row.addWidget(that_checkbox)
        check_box_row.addWidget(that_label)

        # Add row to vertical layout
        main_layout.addLayout(check_box_row)

        # Set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()