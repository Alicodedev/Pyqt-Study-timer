import sys
from Timer_home import * # main UI.py File 
from Theme_final import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLCDNumber, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import * #QObject, QThread, pyqtSignal #! (import * previous code) new code 
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
import datetime


###? Home window ### 
class Homewin(QDialog): 
    
    ##? timer function setup ##
    def __init__(self):
        super(Homewin, self).__init__()
        super().__init__()
        self.ui = Ui_Dialog() #Ui_Dialogplay ## All ui objects and attriubutes contained in class Ui_Dialog##
        self.ui.setupUi(self) # setupUiplay
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.run_watch) 
        self.timer.setInterval(1)
        
        ###! try building logical to save process on lcd display instead of earasing ####################
        
        self.mscounter = 0
        self.isreset = True
        self.ui.Play.clicked.connect(self.start_watch) # creating slots for event handling (button press)
        self.ui.Theme.clicked.connect(self.theme_switch) # signal for entering theme settings 
        self.showLCD()
     
    ##? Timer function  ##    
    def showLCD(self):
        text = str(datetime.timedelta(milliseconds=self.mscounter))[:-5] # changes the digits of miliseconds 
        self.ui.Clock.setDigitCount(10)
        
        if not self.isreset:  # if "isreset" is False
            self.ui.Clock.display(text)
            
        else:
            self.ui.Clock.display('0:00:00.0')

    def run_watch(self):
        self.mscounter += 1
        print(self.mscounter)
        self.showLCD()
      
    def start_watch(self):
        print("reset 1 on")
        
        self.ui.Play.clicked.disconnect(self.start_watch) ## disconnects a signal of object being used in multiple functions 
        #self.ui.Reset.clicked.disconnect(self.reset)
 
        self.ui.Play.setText("Pause") # changes to Pause button
        self.ui.BreakTool.setText("Work") # shows current state in work session

        #! self.start_watch.running # condition checking if pause is shown on Ui ############################## rest error code ####################
        
        self.ui.Play.clicked.connect(self.paused) # activates running funcion after play is clicked.
        self.timer.start()
        self.isreset = False
       
        #self.ui.Reset.clicked.connect(self.reset)
        
        ##? allows background color to switch 
        self.ui.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(234, 108, 126, 255), stop:1 rgba(250, 150, 155, 255));\n"## background color ##
        "border-radius: 15;")
             
    def paused(self): #? pause timer FUNCTION
        self.ui.Play.clicked.disconnect(self.paused) ## disconnects a signal of object being used in multiple functions 
        self.ui.Play.setText("Continue") # set's play button after pause clicked
        self.timer.stop() # pauses timer 
        self.ui.Play.clicked.connect(self.start_watch) # Timer button activated to continue running
        self.ui.Reset.clicked.connect(self.reset)
        #### print flags to see if signals are in different functions at the same time ####
    
        '''#! condtion to check if timer is running and when to connect and disconnect a signal from
         if self.start_watch.running == True:############################## rest error code ####################
            self.ui.Reset.clicked.connect(self.reset)############################## rest error code ####################
        else:############################## rest error code ####################
            self.ui.Play.clicked.disconnect(self.reset) ## disconnects a signal of object being used in multiple functions         
        ''' 
     
    def reset(self):
        self.ui.Reset.clicked.disconnect(self.reset) ## disconnects a signal of object being used in multiple functions 
        self.ui.Play.setText("Play")
        self.ui.BreakTool.setText("Break")
        self.timer.stop()
        self.mscounter = 0 ## 0 resets timer back to zero
        self.isreset = True
        self.showLCD()
        self.ui.Play.clicked.connect(self.start_watch)
      
    def theme_switch(self): #? switches to theme window @@@ NEW CODE @@@
        Theme_app = Theme_Win()#! new code theme object
        widget.addWidget(Theme_app) #! new code Theme widget 
        widget.setCurrentIndex(widget.currentIndex()+1)
    
##? saved sessions ## 

#? Class for background color 
class Theme_Win(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_2 = Ui_Theme() #Ui_Dialogplay ## All ui objects and attriubutes contained in class Ui_Dialog##
        self.ui_2.setupUi(self) # setupUiplay
        
        self.ui_2.pushButton_2.clicked.connect(self.colors)
        self.ui_2.pushButton_3.clicked.connect(self.switch_home)
        
    #! LOGIC FOR EACH COLOR SWITCH SHOULD BE DONE SO THAT EACH SIGNAL AFTER IS DISCONNECTED AND ONLY ONE EVENT CAN BE TIGGER THE BACKGROUND AT A TIME###$$$$$$$$
    #!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    def colors(self):
        self.ui_2.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.057, y1:0.943182, x2:0.857955, y2:0.125, stop:0 rgba(255, 65, 55, 255), stop:1 rgba(255, 1, 63, 255));\n"
        "\n")
    #! store signals of the color(setstylesheet) in a variable which can be used in homewin class
            
    def switch_home(self):
        main_home = Homewin()
        widget.addWidget(main_home)
        widget.setCurrentIndex(widget.currentIndex()+1)
  
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome_1 = Homewin()
widget.addWidget(welcome_1)
widget.setFixedHeight(520)
widget.setFixedWidth(520)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")