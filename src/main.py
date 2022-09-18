from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QLineEdit, QPushButton
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QDoubleValidator
import sys


# =================================================================================================
#                               ANTHROPOMETRIC ASSESSMENT
# =================================================================================================
class AnthropometryPage(QMainWindow):
    def __init__(self):
        super(AnthropometryPage, self).__init__()
        uic.loadUi(r"ui\Anthropometric_Assessment.ui", self)

        inputs = {
            "Length": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit"),
                "Placeholder": "Length (cm)",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Height": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "Placeholder": "Height (cm)",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Weight": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "Placeholder": "Weight (kg)",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Wt-Ht": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "Placeholder": "Weight for Height",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "BMI": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "Placeholder": "BMI",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Age": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_5"),
                "Placeholder": "Age (years)",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "BMI-ZScore": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "Placeholder": "BMI for age Z-Score",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "MUAC": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "Placeholder": "MUAC (cm)",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            }
        }

        for k, v in inputs.items():
            v["LineEdit"].setValidator(v["Validator"])
            v["LineEdit"].setPlaceholderText(v["Placeholder"])

        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)

    def go_to_biochemical(self):
        biochem = BiochemicalPage()
        widget.addWidget(biochem)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# =================================================================================================
#                               BIOCHEMICAL ASSESSMENT
# =================================================================================================
class BiochemicalPage(QMainWindow):
    def __init__(self):
        super(BiochemicalPage, self).__init__()
        uic.loadUi(r"ui\Biochemical_Assessment.ui", self)

        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        inputfields = {
            "Glucose": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit"),
                "PlaceHolder": "Glucose",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "BUN": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "PlaceHolder": "BUN",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "PlaceHolder": "Creatinine",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "BUN/Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "BUN/Creatinine",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Calcium": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Calcium",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Protein": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "Protein",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "ALP": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "PlaceHolder": "ALP",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            # "Glucose2": {
            #     "lineEdit": self.findChild(QLineEdit, "lineEdit_5"),
            #     "PlaceHolder": "Glucose2",
            #     "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            # },
            "ALT": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_11"),
                "PlaceHolder": "ALT",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "RBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_10"),
                "PlaceHolder": "RBC_Count",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Hemaglobin": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_16"),
                "PlaceHolder": "Hemaglobin",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Hematrocrit": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_9"),
                "PlaceHolder": "Hematrocrit",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "MCV": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_15"),
                "PlaceHolder": "MCV",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "MCH": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_13"),
                "PlaceHolder": "MCH",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Platelets": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_12"),
                "PlaceHolder": "Platelets",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "WBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_14"),
                "PlaceHolder": "WBC_Count",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            },
            "Helminth": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_17"),
                "PlaceHolder": "Helminth",
                "Validator": QtGui.QDoubleValidator(0.0, 300.0, 2, notation=QtGui.QDoubleValidator.StandardNotation)
            }
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])

    def go_to_anthropometric(self):
        anthro = AnthropometryPage()
        widget.addWidget(anthro)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == '__main__':
    # Initialize Program
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    # Main Window
    mainwindow = AnthropometryPage()
    widget.addWidget(mainwindow)

    # Config
    widget.setWindowTitle("Anthropometric Assessment")
    widget.resize(1200, 750)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting...")