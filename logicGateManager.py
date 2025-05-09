from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from gateManager1 import *
from raceGateManager import rgm

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Method to manage Gate Manager GUI and an instance of a race
        """
        super().__init__()
        self.setupUi(self)

        self.dropboxes()


        self.btnLoadingGate.clicked.connect(self.loading_gate)
        self.btnRaceOff.clicked.connect(self.race_off)






    def dropboxes(self) -> None:
        """
        Method to organize GUI, populate dropdowns and organize the date dropdown for todays date
        """
        self.dropdownRacetrack.addItems(["Atokad Downs", "Fonner Park", "Harrah's Columbus", "Horseman's Park", "Legacy Downs"])
        self.dropdownNumberOfHorses.addItems(str(i) for i in range(1,21))
        self.dateEdit.setDate(QDate.currentDate())

    def loading_gate(self) -> None:
        """
        Mathod to organize information when user starts timer
        """
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        track = self.dropdownRacetrack.currentText()
        raceNumber = self.inputRaceNumber.text().strip()
        numberOfHorses = self.dropdownNumberOfHorses.currentText()

        try:
            raceNumber = int(raceNumber)
            if raceNumber < 1:
                self.labelMessage.setText("Race number must be above 0")
                return
        except ValueError:
            self.labelMessage.setText("Enter a valid race number, numbers only")
            return



        self.raceGateManager = rgm(date, track, str(raceNumber), numberOfHorses)
        self.raceGateManager.start_loading_gate()
        self.labelMessage.setText("Horses are entering the starting gate (timer has begun)")

    def race_off(self) -> None:
        """
        Method to organize info when user stops timer
        :return:
        """
        self.raceGateManager.end_loading_gate()
        self.raceGateManager.save_race()
        self.labelMessage.setText("Race off, data has been recorded in dataGateManager.csv\nTo record another race, enter values and continue as usual")


        self.dropdownRacetrack.clear()
        self.dropdownNumberOfHorses.clear()
        self.inputRaceNumber.clear()
        self.dropboxes()



    