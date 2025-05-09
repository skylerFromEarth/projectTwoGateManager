import csv
import datetime
import os

class rgm:
    def __init__(self, date, track, raceNumber, numberOfHorses) -> None:
        """
        Method to set default instance for the creation of a race object
        :param date: The date of the race
        :param track: The track the race is hosted at
        :param raceNumber: The number of the current race
        :param numberOfHorses: the number of horses in current race
        """
        self.date = date
        self.track = track
        self.raceNumber = raceNumber
        self.numberOfHorses = numberOfHorses
        self.loadingGateStartTimer = None
        self.raceOffEndTimer = None
        self.loadTime = None
        self.avgLoadTimePerHorse = None


    def start_loading_gate(self) -> None:
        """
        Method to begin timer, as the loading of the starting gate begins
        :return:
        """
        self.loadingGateStartTimer = datetime.datetime.now()


    def end_loading_gate(self) -> None:
        """
        Method to end timer, as the gate opens and the race begins
        Method also calculated the complete loadtime
        Method also calculated average load time per horse
        """
        self.raceOffEndTimer = datetime.datetime.now()
        self.loadTime = self.raceOffEndTimer - self.loadingGateStartTimer
        self.avgLoadTimePerHorse = self.loadTime / int(self.numberOfHorses)


    def save_race(self) -> None:
        """
        Method to record race data in dataGateManager.csv
        """
        header = not os.path.isfile("dataGateManager.csv") or os.path.getsize("dataGateManager.csv") == 0

        with open("dataGateManager.csv", "a", newline='') as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(["Date", " Track", " Race Number", " Number of Horses", " Beginning Load Time", " Race Off Ending Load Time", " Duration of Load", " Average Time to Load Each Horse"])
            writer.writerow([f"Date: {self.date}", f" Track: {self.track}", f" Race Number: {self.raceNumber}", f" Number of Horses: {self.numberOfHorses}", f" Beginning Load Time: {self.loadingGateStartTimer.strftime("%H:%M:%S")}", f" Race Off Time: {self.raceOffEndTimer.strftime("%H:%M:%S")}", f" Duration of load: {self.loadTime}", f" Average Time to Load Each Horse: {self.avgLoadTimePerHorse}"])

