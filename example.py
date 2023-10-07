from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Age Calculator')

        grid = QGridLayout()

        # Create Widgets
        name_label = QLabel("Name")
        self.name_edit = QLineEdit()
        date_birth_label = QLabel("Date of birth: mm/dd/yyyy")
        self.date_birth_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add Widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        year = datetime.now().year
        date_of_birth = self.date_birth_edit.text()
        list_birth = date_of_birth.split("/")
        year_of_birth = list_birth[2]
        result = int(year) - int(year_of_birth)

        self.output_label.setText(f"{self.name_edit.text()} is {result} years old.")
        return int(year) - int(year_of_birth)


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
