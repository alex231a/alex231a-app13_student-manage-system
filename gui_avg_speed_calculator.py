from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')

        grid = QGridLayout()

        # Create Widgets
        name_label = QLabel("Distance")
        self.distance_value = QLineEdit()
        self.combobox = QComboBox()
        self.combobox.addItem("km")
        self.combobox.addItem("miles")

        time_label = QLabel("Time(hours)")
        self.time_value = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_avg_speed)
        self.output_label = QLabel("")

        # Add Widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.distance_value, 0, 1)
        grid.addWidget(self.combobox, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_value, 1, 1)

        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

        self.setLayout(grid)

    def calculate_avg_speed(self):
        distance = int(self.distance_value.text())
        metrics = self.combobox.currentText()
        time = int(self.time_value.text())
        print(distance, metrics, time)
        result = distance / time
        self.output_label.setText(f"{result} {metrics} per hour.")
        return "Good"


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
