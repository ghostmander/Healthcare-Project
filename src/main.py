from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QDoubleValidator, QIntValidator
import sys
from aws.connection_utils import insert_anthropometric


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
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "Height": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "Placeholder": "Height (cm)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "Weight": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "Placeholder": "Weight (kg)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "Wt-Ht": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "Placeholder": "Weight for Height",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "BMI": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "Placeholder": "BMI",
                "Validator": QDoubleValidator(0.0, 99.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "Age": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_5"),
                "Placeholder": "Age (years)",
                "Validator": QIntValidator(0, 199),
                "Datatype": int
            },
            "BMI-ZScore": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "Placeholder": "BMI for age Z-Score",
                "Validator": QDoubleValidator(0.0, 3000.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            },
            "MUAC": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "Placeholder": "MUAC (cm)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Datatype": float
            }
        }

        for k, v in inputs.items():
            v["LineEdit"].setValidator(v["Validator"])
            v["LineEdit"].setPlaceholderText(v["Placeholder"])

        self.inputs = inputs
        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.clinicalButton = self.findChild(QPushButton, "pushButton_8")
        self.dietaryButton = self.findChild(QPushButton, "pushButton_9")
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)
        self.clinicalButton.clicked.connect(self.go_to_clinical)
        self.dietaryButton.clicked.connect(self.go_to_dietary)
        self.submitButton = self.findChild(QPushButton, "pushButton_10")
        self.submitButton.clicked.connect(self.submit)

    def go_to_biochemical(self):
        biochem = BiochemicalPage()
        widget.addWidget(biochem)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_clinical(self):
        clinical = ClinicalPage()
        widget.addWidget(clinical)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_dietary(self):
        diatery = DietaryPage()
        widget.addWidget(diatery)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submit(self):
        proceedable = True
        for k, v in self.inputs.items():
            if v["LineEdit"].text() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please fill all the fields")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                proceedable = False
                break
        if proceedable:
            data = []
            for v in self.inputs.values():
                data.append(v["LineEdit"].text())
                # data.append(v["Datatype"](v["LineEdit"].text()))
                v["LineEdit"].setText("")

            insert_anthropometric(f"'p1', {', '.join(data)}")
            print("Submitting the data: ", data)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Data Submitted Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()


# =================================================================================================
#                               BIOCHEMICAL ASSESSMENT
# =================================================================================================


class BiochemicalPage(QMainWindow):
    def __init__(self):
        super(BiochemicalPage, self).__init__()
        uic.loadUi(r"ui\Biochemical_Assessment.ui", self)

        inputfields = {
            "Glucose": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit"),
                "PlaceHolder": "Glucose",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "BUN": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "PlaceHolder": "BUN",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "PlaceHolder": "Creatinine",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "BUN/Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "BUN/Creatinine",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Calcium": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Calcium",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Protein": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "Protein",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "ALP": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "PlaceHolder": "ALP",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "ALT": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_11"),
                "PlaceHolder": "ALT",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "RBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_10"),
                "PlaceHolder": "RBC_Count",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Hemaglobin": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_16"),
                "PlaceHolder": "Hemaglobin",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Hematrocrit": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_9"),
                "PlaceHolder": "Hematrocrit",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "MCV": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_15"),
                "PlaceHolder": "MCV",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "MCH": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_13"),
                "PlaceHolder": "MCH",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Platelets": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_12"),
                "PlaceHolder": "Platelets",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "WBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_14"),
                "PlaceHolder": "WBC_Count",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Helminth": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_17"),
                "PlaceHolder": "Helminth",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            }
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])

        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.clinicalButton = self.findChild(QPushButton, "pushButton_8")
        self.dietaryButton = self.findChild(QPushButton, "pushButton_9")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.clinicalButton.clicked.connect(self.go_to_clinical)
        self.dietaryButton.clicked.connect(self.go_to_dietary)

    def go_to_anthropometric(self):
        anthro = AnthropometryPage()
        widget.addWidget(anthro)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_clinical(self):
        clinical = ClinicalPage()
        widget.addWidget(clinical)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_dietary(self):
        diatery = DietaryPage()
        widget.addWidget(diatery)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# =================================================================================================
#                               CLINICAL ASSESSMENT
# =================================================================================================
class ClinicalPage(QMainWindow):
    def __init__(self):
        super(ClinicalPage, self).__init__()
        uic.loadUi(r"ui\Clinical_Assessment.ui", self)

        inputfields = {
            "BLE": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit"),
                "PlaceHolder": "Bilateral Pitting Edema",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Bitot": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "Bitot Spot",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Emaciation": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "Emaciation",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "HairLoss": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_5"),
                "PlaceHolder": "Hair Loss",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "Changes_Hairloss": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Changes in Hair Loss",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])

        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.dietaryButton = self.findChild(QPushButton, "pushButton_9")
        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)
        self.dietaryButton.clicked.connect(self.go_to_dietary)

    def go_to_biochemical(self):
        biochem = BiochemicalPage()
        widget.addWidget(biochem)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_anthropometric(self):
        anthro = AnthropometryPage()
        widget.addWidget(anthro)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_dietary(self):
        diatery = DietaryPage()
        widget.addWidget(diatery)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# =================================================================================================
#                               DIETARY ASSESSMENT
# =================================================================================================
class DietaryPage(QMainWindow):
    def __init__(self):
        super(DietaryPage, self).__init__()
        uic.loadUi(r"ui\Dietary_Assessment.ui", self)

        inputfields = {
            "DDS": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit"),
                "PlaceHolder": "Dietary Diversity Score",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "24hR": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "24 Hour Recall",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "FFQ": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "Food Frequency Questionnaire",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
            "FGQ": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Food Group Questionnaire",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation)
            },
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])

        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.clinicalButton = self.findChild(QPushButton, "pushButton_8")
        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)
        self.clinicalButton.clicked.connect(self.go_to_clinical)

    def go_to_anthropometric(self):
        anthro = AnthropometryPage()
        widget.addWidget(anthro)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_biochemical(self):
        biochem = BiochemicalPage()
        widget.addWidget(biochem)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_clinical(self):
        clinical = ClinicalPage()
        widget.addWidget(clinical)
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
