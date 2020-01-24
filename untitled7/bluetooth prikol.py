from kivy.uix.widget import Widget
from kivy.graphics import  Color,Line,Rectangle,Ellipse
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

import time
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import serial.tools.list_ports
import serial

from pygame import mixer

mixer.init()
mixer.music.load("signalka2.mp3")



ser=0

Config.set("graphics", "resizable", "0")  # resizable- змінюємий
Config.set("graphics", "width", "562")
Config.set("graphics", "height", "1000")
BLmod=0

prikol=0
acum=0



class Back(Widget):
	def __init__(self, **kwargs):
		super(Back, self).__init__(**kwargs)

		with self.canvas:
			Rectangle(source="Wollet.gif", pos=self.pos , size=(562,1000))

class SomeItem(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SomeItem, self).__init__(**kwargs)
        with self.canvas:
            if (BLmod == 1):
                print(ser.readline())
                Color(1, 1, 1)
                Rectangle(source="5.png", pos=(30, 910), size=(86 * 0.52, 125 * 0.52))
            else:
                self.canvas.clear()
                print("OFF")
                Color(1, 0.1, 0)
                Rectangle(source="5.png", pos=(30, 910), size=(86 * 0.52, 125 * 0.52))

    def on_touch_down(self, touch):
        global BLmod
        global ser
        with self.canvas:
            if touch.x<90 and touch.x>16 and touch.y<980 and touch.y>920:
                    try:
                        print(BLmod)
                        self.canvas.clear()
                        if BLmod==1:
                            ser = serial.Serial("COM8", 9600)
                        else:
                            ser = serial.Serial("COM8", 9600)
                        Color(1, 1, 1)
                        Rectangle(source="5.png", pos=(30, 910), size=(86 * 0.52, 125 * 0.52))
                        BLmod = 1
                    except:
                        with self.canvas:
                            self.canvas.clear()
                            BLmod = 0
                            Color(1, 0.1, 0)
                            Rectangle(source="5.png", pos=(30, 910), size=(86 * 0.52, 125 * 0.52))
                            print("0")

class MyButton1(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton1, self).__init__(**kwargs)
        self.source = '1.png'
        with self.canvas:
            Color(1, 1, 1)
            Ellipse(pos=(281 - 20, 585), size=(40, 40))
            Color(1, 0.1, 0)
            Ellipse(pos=(281 - 10, 585 + 10), size=(20, 20))
    def on_press(self):
        global prikol
        with self.canvas:
            if prikol==1:
                if BLmod==1:
                    ser.write(str.encode("N"))
                prikol=0
                Color(1, 1, 1)
                Ellipse(pos=(281 - 20, 585), size=(40, 40))
                Color(1, 0.1, 0)
                Ellipse(pos=(281 - 10, 585+10), size=(20, 20))
            else:
                if BLmod==1:
                    ser.write(str.encode("S"))
                prikol=1
                Color(1, .1, 0)
                Ellipse(pos=(281 - 20, 585), size=(40, 40))
                Color(1, 1, 1)
                Ellipse(pos=(281 - 10, 585 + 10), size=(20, 20))
    def my_callback(dt):
        if(prikol==1):
            ser.write(str.encode("E"))
            #    mixer.music.play()
             #   print("don`t conection")

    Clock.schedule_interval(my_callback, 8)




class MyButton2(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton2, self).__init__(**kwargs)
        self.source = '8.png'

    def on_press(self):
        print("PREKOL!")
        if(BLmod==1):
            ser.write(str.encode("1"))

        self.source="9.png"

    def on_release(self):
        if (BLmod == 1):
            ser.write(str.encode("0"))

        self.source = "8.png"

valume=8
sosu=0
class MyButton3(ButtonBehavior, Image,object):
    acum_variant=("11.png","12.png","13.png","14.png","15.png","16.png","17.png","18.png")

    def __init__(self, **kwargs):
        super(MyButton3, self).__init__(**kwargs)
        self.source = '20.png'
        Clock.schedule_interval(self.my_callback, 1)
    def my_callback(self,dt):
        global acum
        global BLmod
        global sosu
        sosu += 1
        if sosu > 7:
            sosu = 0


        acum_variant = ("11.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png")
        if BLmod==1:
            self.source = acum_variant[7-sosu]









class MyButton4(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton4, self).__init__(**kwargs)
        self.source = '4.png'
        with self.canvas:
            Color(1, .1, 0)
            Line(points=[94,230,462,230],width=6)

    def on_touch_down(self, touch):
        with self.canvas:
            if touch.y>185 and touch.y <259 and touch.x>94 and touch.x <462:
                global valume
                some=3+int(8*(touch.x-94)/368)
                if BLmod == 1:
                    ser.write(str.encode(str(some)))
                Color(1, 1, 1)
                Line(points=[touch.x, 230, 462, 230], width=6)
                Color(1, 0.1, 0)
                Line(points=[94, 230, touch.x, 230], width=6)



class WalletApp(App):
    def build(self):
        all_item=BoxLayout(orientation="vertical",padding=10)

        all_item.add_widget(Back())
        all_item.add_widget(Widget())
        all_item.add_widget(MyButton1())
        all_item.add_widget(MyButton2())
        all_item.add_widget(MyButton3())
        all_item.add_widget(MyButton4())
        all_item.add_widget(SomeItem())

        return all_item

WalletApp().run()

