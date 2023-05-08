from PyQt5.QtWidgets import *
from view import *
import math

# Code for display continuity between systems
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # Init method, submit buttons connect to methods
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.circleSubmitButton.clicked.connect(self.circle)
        self.squareSubmitButton.clicked.connect(self.square)
        self.rectangleSubmitButton.clicked.connect(self.rectangle)
        self.triangleSubmitButton.clicked.connect(self.triangle)

    def circle(self):
        # Circle area function, retrieve user input and validate
        measure = self.circleMeasurementInput.text()
        try:
            # If input is acceptable as float
            measure = float(measure)

            # Input must be greater than zero
            if measure > 0:
                # Calculate based on user selected diameter or radius measurement
                if self.circleDiamRadioButton.isChecked():
                    # After validations, if diameter button selected, calculate and display area
                    measure = measure / 2
                    area = (math.pi * (measure * measure))
                    self.outputLabel.clear()
                    self.outputLabel.setText(f'The area of your circle is {area:.4f}')
                elif self.circleRadiusRadioButton.isChecked():
                    # After validations, if radius button selected, calculate and display area
                    area = (math.pi * (measure * measure))
                    self.outputLabel.clear()
                    self.outputLabel.setText(f'The area of your circle is {area:.4f}')
                # Must select diameter or radius radio button
                else:
                    self.outputLabel.clear()
                    self.outputLabel.setText('Please select radius or diameter.')
            else:
                # If input less than zero, ask for positive value
                self.outputLabel.clear()
                self.outputLabel.setText('Please input a positive non-zero value.')
        except:
            # If input not acceptable as float, as for numeric value
            self.outputLabel.setText('Please enter a numeric value.')

    def square(self):
        # Square area function, one side measurement input
        side = self.squareMeasurementInput.text()
        try:
            # Validate input is acceptable as float
            side = float(side)
            # Validate input is positive and non zero
            if side > 0:
                # After vlidations, calculate and display area
                area = side * side
                self.outputLabel.clear()
                self.outputLabel.setText(f'The area of your square is {area:.4f}')
            else:
                # Ask for positive value if input less than or equal to 0
                self.outputLabel.clear()
                self.outputLabel.setText('Please input a positive non-zero value.')
        except:
            # Ask for numeric value if not accepted as float
            self.outputLabel.clear()
            self.outputLabel.setText('Please enter a numeric value.')

    def triangle(self):
        # Triangle area function, 2 inputs = base and height
        base = self.triangleBaseInput.text()
        height = self.triangleHeightInput.text()
        # Validate base is acceptable as float
        try:
            base = float(base)
            # Validate height is acceptable as float
            try:
                height = float(height)
                # Validate base is greater than zero
                if base > 0:
                    # Validate height is greater than zero
                    if height > 0:
                        # After validations, calculate and display area
                        area = (base * height) / 2
                        self.outputLabel.clear()
                        self.outputLabel.setText(f'The are of your triangle is {area:.4f}')

                    else:
                        # If height is less than or equal to zero, ask for positive non zero value
                        self.outputLabel.clear()
                        self.outputLabel.setText('Enter a positive non-zero value for height.')

                else:
                    # If base is less than or equal to zero, ask for positive non zero value
                    self.outputLabel.clear()
                    self.outputLabel.setText('Enter a positive non-zero value for the base.')
            except:
                # If height input is not acceptable as float, ask for numeric value
                self.outputLabel.clear()
                self.outputLabel.setText('Please enter numeric value for height.')
        except:
            # If base input is not acceptable as float, ask for numeric value
            self.outputLabel.clear()
            self.outputLabel.setText('Please enter numeric value for base.')

    def rectangle(self):
        # Rectangle area function, 2 inputs = length and width
        length = self.rectangleLengthInput.text()
        width = self.rectangleWidthInput.text()

        try:
            # Validate length input is acceptable as float
            length = float(length)
            try:
                # Validate width input is acceptable as float
                width = float(width)
                # Verify length is greater than zero
                if length > 0:
                    # Verify width is greater than zero
                    if width > 0:
                        # After all validation, calculate area and display
                        area = length * width
                        self.outputLabel.clear()
                        self.outputLabel.setText(f'The are of your rectangle is {area:.4f}')
                    else:
                        # If width is less than or equal to zero, ask for positive non zero value
                        self.outputLabel.clear()
                        self.outputLabel.setText('Enter a positive non-zero value for width.')
                else:
                    # If length is less than or equal to zero, ask for positive non zero value
                    self.outputLabel.clear()
                    self.outputLabel.setText('Enter a positive non-zero value for length.')
            except:
                # If width input not acceptable as float, ask for numeric value
                self.outputLabel.clear()
                self.outputLabel.setText('Please enter numeric value for width.')
        except:
            # If length input not acceptable as float, ask for numeric value
            self.outputLabel.clear()
            self.outputLabel.setText('Please enter numeric value for length.')










