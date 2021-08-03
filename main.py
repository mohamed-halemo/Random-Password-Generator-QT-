from PyQt5.QtCore import Qt
from Gui import Ui_MainWindow
from PyQt5 import QtWidgets 
import sys
import string
import random
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self): #constructor
        super(ApplicationWindow, self).__init__()# let you inherit methods from a parent class
        self.ui = Ui_MainWindow() # intializing ui to main window
        self.ui.setupUi(self) #setting the ui
        self.text=self.ui.label_2
        
        self.GenerateBtn=self.ui.pushButton
        self.SaveBtn=self.ui.pushButton_2
        self.GenerateBtn.clicked.connect(self.Generate)
        self.SaveBtn.clicked.connect(self.Save)
        self.password=[]
        self.passSave=0
    def Generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation #letters , digits ,symbols
        Password = ''.join(random.choice(characters) for i in range(14))      #select random character from things above
        self.text.setText(str(Password))     #changing text (str becuase if there is numbers conver it to string)
        self.text.setTextInteractionFlags(Qt.TextSelectableByMouse)   #to make text generated copyable
        self.passSave=Password    #saving password
    def Save(self):
        self.password.append(self.passSave) #appending password generated to the array on clicking save
        f= open("passwords.txt","w+")  #generating text file and w to indicate writing to it 
        for i in range(len(self.password)):  
             f.write(" password chosen "+self.password[i] )  #writing to the text file the generated passwords
             f.write("\n")
        f.close() #closing file
        for i in range (len(self.password)):
            self.ui.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(self.password[i]))) #setting saved items in the table
def main():
    app = QtWidgets.QApplication(sys.argv) #list of commandline arguments passed to the Python program
    application = ApplicationWindow()  
    application.show()
    app.exec_()  #execution


if __name__ == "__main__":
    main()  #calling main