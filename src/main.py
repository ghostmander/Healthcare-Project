from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QLineEdit
from PyQt5 import uic, QtGui
import sys


# =================================================================================================
#                               ANTHROPOMETRIC ASSESSMENT
# =================================================================================================
class AnthropometryPage(QMainWindow):
    def __init__(self):
        super(AnthropometryPage, self).__init__()
        uic.loadUi(r"ui\Anthropometric_Assessment.ui", self)

        inputs = {
            "Length": self.findChild(QLineEdit, "lineEdit"),
            "Height": self.findChild(QLineEdit, "lineEdit_4"),
            "Weight": self.findChild(QLineEdit, "lineEdit_7"),
            "Wt-Ht": self.findChild(QLineEdit, "lineEdit_3"),
            "BMI": self.findChild(QLineEdit, "lineEdit_2"),
            "Age": self.findChild(QLineEdit, "lineEdit_5"),
            "BMI-ZScore": self.findChild(QLineEdit, "lineEdit_8"),
            "MUAC": self.findChild(QLineEdit, "lineEdit_6"),

        }
        inputs["Length"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["Length"].setPlaceholderText("Enter Length in cm")

        inputs["Height"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["Height"].setPlaceholderText("Enter Height in cm")

        inputs["Weight"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["Weight"].setPlaceholderText("Enter Weight in kg")

        inputs["Wt-Ht"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["Wt-Ht"].setPlaceholderText("Enter Wt/Ht")

        inputs["BMI"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["BMI"].setPlaceholderText("Enter BMI")

        inputs["Age"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["Age"].setPlaceholderText("Enter Age in years")

        inputs["BMI-ZScore"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["BMI-ZScore"].setPlaceholderText("Enter BMI-ZScore")

        inputs["MUAC"].setValidator(QtGui.QDoubleValidator(
            0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation))
        inputs["MUAC"].setPlaceholderText("Enter MUAC in cm")


if __name__ == '__main__':
    # Initialize Program
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    # Main Window
    mainwindow = AnthropometryPage()
    widget.addWidget(mainwindow)

    # Config
    widget.setWindowTitle("Anthropometric Assessment")
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting...")
