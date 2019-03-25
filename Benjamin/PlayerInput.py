#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key, Controller

class PlayerInput:
        
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    
        #Player
        #JOYSTICK
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)      
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        #BUTTONS
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        #BUTTON LIGHTS
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

        #JOYSTICK INTERUPTS
        GPIO.add_event_detect(4, GPIO.BOTH, callback=self.setPlayer1Up)       
        GPIO.add_event_detect(22, GPIO.BOTH, callback=self.setPlayer1Down)
        GPIO.add_event_detect(27, GPIO.BOTH, callback=self.setPlayer1Right)
        GPIO.add_event_detect(17, GPIO.BOTH, callback=self.setPlayer1Left)

        #BUTTON INTERUPTS
        GPIO.add_event_detect(5, GPIO.BOTH, callback=self.setPlayer1Button1)
        GPIO.add_event_detect(12, GPIO.BOTH, callback=self.setPlayer1Button2)
        

        #BUFFER AND LITERAL VALUES FOR JOYSTICK
        self.p1Up_Literal = False
        self.p1Up_Buffer = False
    
        self.p1Down_Literal = False
        self.p1Down_Buffer = False

        self.p1Right_Literal = False
        self.p1Right_Buffer = False
        
        self.p1Left_Literal = False
        self.p1Left_Buffer = False

        #BUFFER AND LITERAL VALUES FOR BUTTONS
        self.p1Button1_Literal = False
        self.p1Button1_Buffer = False

        self.p1Button2_Literal = False
        self.p1Button2_Buffer = False

    #SETS JOYSTICK DIRECTIONS AND BUTTON ONOFF, IS CALLED FROM INTERUPT
    def setPlayer1Up(self, channel):
        if GPIO.input(4):
            self.p1Up_Literal = True
            self.p1Up_Buffer = True
        else:
            self.p1Up_Literal = False
        
    def setPlayer1Down(self, channel):
        if GPIO.input(22):
            self.p1Down_Literal = True
            self.p1Down_Buffer = True
        else:
            self.p1Down_Literal = False
        
    def setPlayer1Right(self, channel):
        if GPIO.input(27):
            self.p1Right_Literal = True
            self.p1Right_Buffer = True
        else:
            self.p1Right_Literal = False
        
    def setPlayer1Left(self, channel):
        if GPIO.input(17):
            self.p1Left_Literal = True
            self.p1Left_Buffer = True
        else:
            self.p1Left_Literal = False

    def setPlayer1Button1(self, channel):
        if GPIO.input(5):
            self.p1Button1_Literal = True
            self.p1Button1_Buffer = True
        else:
            self.p1Button1_Literal = False

    def setPlayer1Button2(self, channel):
        if GPIO.input(12):
            self.p1Button2_Literal = True
            self.p1Button2_Buffer = True
        else:
            self.p1Button2_Literal = False
    
    
    #RETURNS TRUE FALSE IS A DIRECTION IS BEING HELD DOWN
    def getPlayer1Up(self):
        temp = self.p1Up_Buffer
        self.p1Up_Buffer = False
        return self.p1Up_Literal or temp

    def getPlayer1Down(self):
        temp = self.p1Down_Buffer
        self.p1Down_Buffer = False
        return self.p1Down_Literal or temp

    def getPlayer1Right(self):
        temp = self.p1Right_Buffer
        self.p1Right_Buffer = False
        return self.p1Right_Literal or temp

    def getPlayer1Left(self):
        temp = self.p1Left_Buffer
        self.p1Left_Buffer = False
        return  self.p1Left_Literal or temp

    def getPlayer1Button1(self):
        temp = self.p1Button1_Buffer
        self.p1Button1_Buffer = False
        return self.p1Button1_Literal or temp
   
    def getPlayer1Button2(self):
        temp = self.p1Button2_Buffer
        self.p1Button2_Buffer = False
        return self.p1Button2_Literal or temp
    
    #SETS THE LIGHT ON OR OFF
    def setLightButton1(self, isOn):
            if isOn:
                GPIO.output(6, GPIO.HIGH)
            else:
                GPIO.output(6, GPIO.LOW)
    def setLightButton2(self, isOn):
            if isOn:
                GPIO.output(16, GPIO.HIGH)
            else:
                GPIO.output(16, GPIO.LOW)    


#MAIN FOR TESTING
if __name__ == "__main__":
    print ("Testing GPIO inputs")

    buttonInput = PlayerInput()
    keyboard = Controller()

    while(True):
        if(buttonInput.getPlayer1Up()):
            keyboard.press("w")
        else:
            keyboard.release("w")
            
        if(buttonInput.getPlayer1Down()):
            keyboard.press("s")
        else:
            keyboard.release("s")
            
        if(buttonInput.getPlayer1Right()):
            keyboard.press("d")
        else:
            keyboard.release("d")
            
        if(buttonInput.getPlayer1Left()):
            keyboard.press("a")
        else:
            keyboard.release("a")

        if(buttonInput.getPlayer1Button1()):
            keyboard.press(Key.space)
        else:
            keyboard.release(Key.space)

        if(buttonInput.getPlayer1Button2()):
            keyboard.press("q")
        else:
            keyboard.release("q")

        buttonInput.setLightButton1(True)
        buttonInput.setLightButton2(False)
        time.sleep(2)
        buttonInput.setLightButton1(False)
        buttonInput.setLightButton2(True)
        time.sleep(1)


