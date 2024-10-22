from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator
import sys
from aws.connection_utils import *


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
                "Checkbox": self.findChild(QCheckBox, "checkBox_length"),
            },
            "Height": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "Placeholder": "Height (cm)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_height"),
            },
            "Weight": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "Placeholder": "Weight (kg)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_weight"),
            },
            "Wt-Ht": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "Placeholder": "Weight for Height",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_wfh"),
            },
            "BMI": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "Placeholder": "BMI",
                "Validator": QDoubleValidator(0.0, 99.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bmi"),
            },
            "Age": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_5"),
                "Placeholder": "Age (years)",
                "Validator": QRegExpValidator(QtCore.QRegExp("[1-9]\d?")),
                "Checkbox": self.findChild(QCheckBox, "checkBox_age"),
            },
            "BMI-ZScore": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "Placeholder": "BMI for age Z-Score",
                "Validator": QDoubleValidator(0.0, 3000.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bmifazs"),
            },
            "MUAC": {
                "LineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "Placeholder": "MUAC (cm)",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_muac"),
            }
        }

        for k, v in inputs.items():
            v["LineEdit"].setValidator(v["Validator"])
            v["LineEdit"].setPlaceholderText(v["Placeholder"])
            v["Checkbox"].setChecked(True)
            v["Checkbox"].setText('')
            v["Checkbox"].toggled.connect(v["LineEdit"].setEnabled)
            v["Checkbox"].setStyleSheet('''
                                        QCheckBox::indicator { width: 18px; height: 18px; }
                                        QCheckBox::indicator:checked { image: url(ui/Media/Radio_checked.png); }
                                        QCheckBox::indicator:unchecked { image: url(ui/Media/Radio_unchecked.png); }''')
            v["LineEdit"].setStyleSheet(
                "QLineEdit { background-color: rgb(255, 255, 255); } QLineEdit:disabled { background-color: rgb(200, 200, 200); }")

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

    def checkbox_handler(self, checkbox, linedit, name="Test"):
        print(f"Clicked {name}")
        linedit.setEnabled(checkbox.isChecked())

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
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_glucose"),
            },
            "BUN": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_7"),
                "PlaceHolder": "BUN",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bun"),
            },
            "Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_6"),
                "PlaceHolder": "Creatinine",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_creatinine"),
            },
            "BUN/Creatinine": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "BUN/Creatinine",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bunc"),
            },
            "Calcium": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Calcium",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox"),
            },
            "Protein": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "Protein",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_protein"),
            },
            "ALP": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_8"),
                "PlaceHolder": "ALP",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_alp"),
            },
            "ALT": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_11"),
                "PlaceHolder": "ALT",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_aat"),
            },
            "RBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_10"),
                "PlaceHolder": "RBC_Count",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_rbc"),
            },
            "Hemaglobin": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_16"),
                "PlaceHolder": "Hemaglobin",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_hb"),
            },
            "Hematrocrit": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_9"),
                "PlaceHolder": "Hematrocrit",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_hematocrit"),
            },
            "MCV": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_15"),
                "PlaceHolder": "MCV",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_mcv"),
            },
            "MCH": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_13"),
                "PlaceHolder": "MCH",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_mch"),
            },
            "Platelets": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_12"),
                "PlaceHolder": "Platelets",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_pc"),
            },
            "WBC_Count": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_14"),
                "PlaceHolder": "WBC_Count",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_wbcc"),
            },
        }
        self.stoolInputs = {
            "Helminth": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_17"),
                "PlaceHolder": "Helminth",
                "Validator": QRegExpValidator(QtCore.QRegExp(".{0,50}"))
            }
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])
            v["Checkbox"].setChecked(True)
            v["Checkbox"].setText('')
            v["Checkbox"].toggled.connect(v["lineEdit"].setEnabled)
            v["Checkbox"].setStyleSheet('''
                                        QCheckBox::indicator { width: 18px; height: 18px; }
                                        QCheckBox::indicator:checked { image: url(ui/Media/Radio_checked.png); }
                                        QCheckBox::indicator:unchecked { image: url(ui/Media/Radio_unchecked.png); }''')
            v["lineEdit"].setStyleSheet(
                "QLineEdit { background-color: rgb(255, 255, 255); } QLineEdit:disabled { background-color: rgb(200, 200, 200); }")

        self.stoolInputs["Helminth"]["lineEdit"].setValidator(
            self.stoolInputs["Helminth"]["Validator"])
        self.stoolInputs["Helminth"]["lineEdit"].setPlaceholderText(
            self.stoolInputs["Helminth"]["PlaceHolder"])
        self.bioInputs = inputfields

        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.clinicalButton = self.findChild(QPushButton, "pushButton_8")
        self.dietaryButton = self.findChild(QPushButton, "pushButton_9")
        self.submit_button = self.findChild(QPushButton, "Submit_button")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.clinicalButton.clicked.connect(self.go_to_clinical)
        self.dietaryButton.clicked.connect(self.go_to_dietary)
        self.submit_button.clicked.connect(self.submit)

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

    def submit(self):
        proceedable = True
        for v in [*self.bioInputs.values(), *self.stoolInputs.values()]:
            if v["lineEdit"].text() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please fill all the fields")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                proceedable = False
                break
        if proceedable:
            data = []
            for v in self.bioInputs.values():
                data.append(v["lineEdit"].text())
                # data.append(v["Datatype"](v["LineEdit"].text()))
                v["lineEdit"].setText("")

            insert_metabolic(f"'p1', {', '.join(data)}")
            insert_stool_sample(
                f"'p1', \"{self.stoolInputs['Helminth']['lineEdit'].text()}\"")
            self.stoolInputs['Helminth']['lineEdit'].setText("")
            print("Submitting the data: ", data)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Data Submitted Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

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
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bpe"),
            },
            "Bitot": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "Bitot Spot",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_bs"),
            },
            "Emaciation": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "Emaciation",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_e"),
            },
            "HairLoss": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_5"),
                "PlaceHolder": "Hair Loss",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_hl"),
            },
            "Changes_Hairloss": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Changes in Hair Loss",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_cihc"),
            },
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])
            v["Checkbox"].setChecked(True)
            v["Checkbox"].setText('')
            v["Checkbox"].toggled.connect(v["lineEdit"].setEnabled)
            v["Checkbox"].setStyleSheet('''
                                        QCheckBox::indicator { width: 18px; height: 18px; }
                                        QCheckBox::indicator:checked { image: url(ui/Media/Radio_checked.png); }
                                        QCheckBox::indicator:unchecked { image: url(ui/Media/Radio_unchecked.png); }''')
            v["lineEdit"].setStyleSheet(
                "QLineEdit { background-color: rgb(255, 255, 255); } QLineEdit:disabled { background-color: rgb(200, 200, 200); }")

        self.inputs = inputfields
        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.dietaryButton = self.findChild(QPushButton, "pushButton_9")
        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.submitButton = self.findChild(QPushButton, "Submit_button")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)
        self.dietaryButton.clicked.connect(self.go_to_dietary)
        self.submitButton.clicked.connect(self.submit)

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

    def submit(self):
        proceedable = True
        for k, v in self.inputs.items():
            if v["lineEdit"].text() == "":
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
                data.append(v["lineEdit"].text())
                v["lineEdit"].setText("")

            insert_clinical(f"'p1', 'pat1', 21, 'M', {', '.join(data)}")
            print("Submitting the data: ", data)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Data Submitted Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()


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
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_dds"),

            },
            "24hR": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_4"),
                "PlaceHolder": "24 Hour Recall",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_24hr"),
            },
            "FFQ": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_2"),
                "PlaceHolder": "Food Frequency Questionnaire",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_ffq"),
            },
            "FGQ": {
                "lineEdit": self.findChild(QLineEdit, "lineEdit_3"),
                "PlaceHolder": "Food Group Questionnaire",
                "Validator": QDoubleValidator(0.0, 300.0, 2, notation=QDoubleValidator.StandardNotation),
                "Checkbox": self.findChild(QCheckBox, "checkBox_fgq"),
            },
        }
        for k, v in inputfields.items():
            v["lineEdit"].setValidator(v["Validator"])
            v["lineEdit"].setPlaceholderText(v["PlaceHolder"])
            v["Checkbox"].setChecked(True)
            v["Checkbox"].setText('')
            v["Checkbox"].toggled.connect(v["lineEdit"].setEnabled)
            v["Checkbox"].setStyleSheet('''
                                        QCheckBox::indicator { width: 18px; height: 18px; }
                                        QCheckBox::indicator:checked { image: url(ui/Media/Radio_checked.png); }
                                        QCheckBox::indicator:unchecked { image: url(ui/Media/Radio_unchecked.png); }''')
            v["lineEdit"].setStyleSheet(
                "QLineEdit { background-color: rgb(255, 255, 255); } QLineEdit:disabled { background-color: rgb(200, 200, 200); }")

        self.inputs = inputfields
        self.anthropometryButton = self.findChild(QPushButton, "pushButton_6")
        self.clinicalButton = self.findChild(QPushButton, "pushButton_8")
        self.biochemicalButton = self.findChild(QPushButton, "pushButton_7")
        self.submitButton = self.findChild(QPushButton, "Submit_button")
        self.anthropometryButton.clicked.connect(self.go_to_anthropometric)
        self.biochemicalButton.clicked.connect(self.go_to_biochemical)
        self.clinicalButton.clicked.connect(self.go_to_clinical)
        self.submitButton.clicked.connect(self.submit)

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

    def submit(self):
        proceedable = True
        for k, v in self.inputs.items():
            if v["lineEdit"].text() == "":
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
                data.append(v["lineEdit"].text())
                v["lineEdit"].setText("")

            insert_dietary(f"'p1', {', '.join(data)}")
            print("Submitting the data: ", data)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Data Submitted Successfully")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()


if __name__ == '__main__':
    # Initialize Program
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    # Main Window
    mainwindow = AnthropometryPage()
    # os.system('cls|clear')
    widget.addWidget(mainwindow)

    # Config
    widget.setWindowTitle("Anthropometric Assessment")
    widget.resize(1250, 950)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting...")
