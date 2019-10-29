# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import platform
from solver import Solve
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
import numpy as np
import cv2
import os

lista= ["rubiks-side-F","rubiks-side-R","rubiks-side-B","rubiks-side-L","rubiks-side-U","rubiks-side-D"]
count1=0
count=0
sides=True
Solution=""
counter=0
begin=-1

class Camara(Screen):
	
	def callback(self):
		global count1
		if count1 >= 6:
			self.ids['label1'].text="SCAN COMPLETE"
			presentation.get_screen('galeria').ids.g1.source = "fotos/rubiks-side-F.png"
			presentation.get_screen('galeria').ids.g2.source = "fotos/rubiks-side-R.png"
			presentation.get_screen('galeria').ids.g3.source = "fotos/rubiks-side-B.png"
			presentation.get_screen('galeria').ids.g4.source = "fotos/rubiks-side-L.png"
			presentation.get_screen('galeria').ids.g5.source = "fotos/rubiks-side-U.png"
			presentation.get_screen('galeria').ids.g6.source = "fotos/rubiks-side-B.png"
		else:
			cv2.imwrite(("fotos/{0}.png".format(lista[count1])),frame)
			self.ids['label1'].text="{0}.png was scanned".format(lista[count1])
			count1+=1
			
			
	def reset(self):
		global count1
		count1 = 0
		presentation.get_screen('camara').ids.label1.text = "Cube Face Scanner"
		
	
class Solution(Screen):
	def solver(self):
		global scramble
		global count
		global counter
		self.ids['bum'].text="LOADING SOLUTION WAIT..."
		scramble=Solve()
		self.ids['bum'].text=scramble
		scramble=scramble.split(" ")
		count=len(scramble)

class Galeria(Screen):
	pass
	
class AnimatedSolution(Screen):
	power = StringProperty('solve.png')
	texto = StringProperty('')
	def change_state(self):		
		global counter
		
		try:
			if counter==count :
				self.ids['display'].text=""
				self.power="solve.png"
			elif counter == ((count+1) * -1):
				counter=0
			elif scramble[counter] =="R":
				self.ids['display'].text="Movimento R\nLado direito (right)\nno sentido horário"
				self.power = 'r.jpg'
				counter+= 1
			elif scramble[counter] =="R'":
				self.ids['display'].text="Movimento R'\nLado direito (right)\nno sentido anti-horário"
				self.power="r'.jpg"
				counter+= 1
			elif scramble[counter] =="U":
				self.ids['display'].text="Movimento U\nLado de cima (up)\nno sentido horário"
				self.power="u.jpg"
				counter+= 1
			elif scramble[counter] =="U'":
				self.ids['display'].text="Movimento U'\nLado de cima (up)\nno sentido anti-horário"
				self.power="u'.jpg"
				counter+= 1
			elif scramble[counter] =="L":
				self.ids['display'].text="Movimento L\nLado esquerdo (left)\nno sentido horário"
				self.power="l.jpg"
				counter+= 1
			elif scramble[counter] =="L'":
				self.ids['display'].text="Movimento L'\nLado esquerdo (left)\nno sentido anti-horário"
				self.power="l'.jpg"
				counter+= 1
			elif scramble[counter] =="D":
				self.ids['display'].text="Movimento D\nLado de baixo (down)\n\nno sentido horário"
				self.power="d.jpg"
				counter+= 1
			elif scramble[counter] =="D'":
				self.ids['display'].text="Movimento D'\nLado de baixo (down)\nno sentido anti-horário"
				self.power="d'.jpg"
				counter+= 1
			elif scramble[counter] =="B":
				self.ids['display'].text="Movimento B\nLado de trás (back)\nno sentido horário"
				self.power="b.jpg"
				counter+= 1
			elif scramble[counter] =="B'":
				self.ids['display'].text="Movimento B'\nLado de trás (back)\nno sentido anti-horário"
				self.power="b'.jpg"
				counter+= 1
			elif scramble[counter] =="F":
				self.ids['display'].text="Movimento F\nLado da frente (front)\nno sentido horário"
				self.power="f.jpg"
				counter+= 1
			elif scramble[counter] =="F'":
				self.ids['display'].text="Movimento F'\nLado da frente (front)\nno sentido anti-horário"
				self.power="f'.jpg"
				counter+= 1
			elif scramble[counter] =="R2":
				self.ids['display'].text="Movimento R2\nLado direito (right)\ncom giro duplo"
				self.power="r2.jpg"
				counter+= 1
			elif scramble[counter] =="U2":
				self.ids['display'].text="Movimento U2\nLado de cima (up)\ncom giro duplo"
				self.power="u2.jpg"
				counter+= 1
			elif scramble[counter] =="L2":
				self.ids['display'].text="Movimento L2\nLado esquerdo (left)\ncom giro duplo"
				self.power="l2.jpg"
				counter+= 1
			elif scramble[counter] =="D2":
				self.ids['display'].text="Movimento D2\nLado de baixo (down)\ncom giro duplo"
				self.power="d2.jpg"
				counter+= 1
			elif scramble[counter] =="B2":
				self.ids['display'].text="Movimento B2\nLado de trás (back)\ncom giro duplo"
				self.power="b2.jpg"
				counter+= 1
			elif scramble[counter] =="F2":
				self.ids['display'].text="Movimento F2\nLado da frente (front)\ncom giro duplo"
				self.power="f2.jpg"
				counter+= 1
			else:
				pass
		except:
			pass
			
	def change_state1(self):		
		global counter
		
		try:
			if counter==count:
				counter=begin	
			elif counter == ((count+1) * -1):
				self.ids['display'].text=""
				self.power="solve.png"
			elif scramble[counter] =="R":
				self.ids['display'].text="Movimento R'\nLado direito (right)\nno sentido anti-horário"
				self.power = "r'.jpg"
				counter-= 1
			elif scramble[counter] =="R'":
				self.ids['display'].text="Movimento R\nLado direito (right)\nno sentido horário"
				self.power="r.jpg"
				counter-= 1
			elif scramble[counter] =="U":
				self.ids['display'].text="Movimento U'\nLado de cima (up)\nno sentido anti-horário"
				self.power="u'.jpg"
				counter-= 1
			elif scramble[counter] =="U'":
				self.ids['display'].text="Movimento U\nLado de cima (up)\nno sentido horário"
				self.power="u.jpg"
				counter-= 1
			elif scramble[counter] =="L":
				self.ids['display'].text="Movimento L'\nLado esquerdo (left)\nno sentido anti-horário"
				self.power="l'.jpg"
				counter-= 1
			elif scramble[counter] =="L'":
				self.ids['display'].text="Movimento L\nLado esquerdo (left)\nno sentido horário"
				self.power="l.jpg"
				counter-= 1
			elif scramble[counter] =="D":
				self.ids['display'].text="Movimento D'\nLado de baixo (down)\nno sentido anti-horário"
				counter-= 1
			elif scramble[counter] =="D'":
				self.ids['display'].text="Movimento D\nLado de baixo (down)\n\nno sentido horário"
				self.power="d'.jpg"
				self.power="d.jpg"
				counter-= 1
			elif scramble[counter] =="B":
				self.ids['display'].text="Movimento B'\nLado de trás (back)\nno sentido anti-horário"
				self.power="b'.jpg"
				counter-= 1
			elif scramble[counter] =="B'":
				self.ids['display'].text="Movimento B\nLado de trás (back)\nno sentido horário"
				self.power="b.jpg"
				counter-= 1
			elif scramble[counter] =="F":
				self.ids['display'].text="Movimento F'\nLado da frente (front)\nno sentido anti-horário"
				self.power="f'.jpg"
				counter-= 1
			elif scramble[counter] =="F'":
				self.ids['display'].text="Movimento F\nLado da frente (front)\nno sentido horário"
				self.power="f.jpg"
				counter-= 1
			elif scramble[counter] =="R2":
				self.ids['display'].text="Movimento R2\nLado direito (right)\ncom giro duplo"
				self.power="r2.jpg"
				counter-= 1
			elif scramble[counter] =="U2":
				self.ids['display'].text="Movimento U2\nLado de cima (up)\ncom giro duplo"
				self.power="u2.jpg"
				counter-= 1
			elif scramble[counter] =="L2":
				self.ids['display'].text="Movimento L2\nLado esquerdo (left)\ncom giro duplo"
				self.power="l2.jpg"
				counter-= 1
			elif scramble[counter] =="D2":
				self.ids['display'].text="Movimento D2\nLado de baixo (down)\ncom giro duplo"
				self.power="d2.jpg"
				counter-= 1
			elif scramble[counter] =="B2":
				self.ids['display'].text="Movimento B2\nLado de trás (back)\ncom giro duplo"
				self.power="b2.jpg"
				counter-= 1
			elif scramble[counter] =="F2":
				self.ids['display'].text="Movimento F2\nLado da frente (front)\ncom giro duplo"
				self.power="f2.jpg"
				counter-= 1
			else:
				pass
		except:
			pass
		
class ScreenManagement(ScreenManager):
	pass
	
presentation = Builder.load_file("scam.kv")
	
class MainApp(App):
	def build(self):
		self.title = 'Face Scanner'
		self.capture = cv2.VideoCapture(0)  #criamos um objeto de capture de vídeo. Associamos à primeira camera
		ret, frame = self.capture.read() #criamos um frame com esta imagem
		#cv2.namedWindow("CV2 Image")     #nome da janela
		#cv2.imshow("CV2 Image", frame)
		Clock.schedule_interval(self.atualizaImagem, 1.0/30.0)
		return presentation
		
	def atualizaImagem(self, dt):
		global frame
		ret, frame = self.capture.read()   #captura uma imagem da camera
				#line
		cv2.line(frame, (100, 100), (100, 100*4), color=(0, 0, 0), thickness=25)
		cv2.line(frame, (100*2, 100), (100*2,100*4), color=(0, 0, 0), thickness=25)
		cv2.line(frame, (100*3, 100), (100*3,100*4), color=(0, 0, 0), thickness=25)
		cv2.line(frame, (100*4, 100), (100*4,100*4), color=(0, 0, 0), thickness=25)
		# devide
		cv2.line(frame, (100, 100), (100*4, 100), color=(0, 0, 0),thickness=25)
		cv2.line(frame, (100, 100*2), (100*4, 100*2), color=(0, 0, 0),thickness=25)
		cv2.line(frame, (100, 100*3), (100*4, 100*3), color=(0, 0, 0),thickness=25)
		cv2.line(frame, (100, 100*4), (100*4, 100*4), color=(0, 0, 0),thickness=25)
		#line
		#cv2.rectangle(frame,(90,90),(410,410),(0,255,0),3)
		frame=frame[90:410, 90:410]
		
		buf1 = cv2.flip(frame, 0)   #inverte para não ficar de cabeça para baixo
		buf = buf1.tostring() # converte em textura
		
		texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
		texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

		presentation.get_screen('camara').ids.frame1.texture = texture1
	
if __name__ == "__main__":
    MainApp().run()