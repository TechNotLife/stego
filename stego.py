from PIL import Image, ImageDraw 
from random import randint		
from re import findall
from tkinter import *
from tkinter.filedialog import askopenfilename
import PIL.Image

def encrypt():
	keys = [] 					#сюда будут помещены ключи
	print("Выберете картинку для стеганографии")
	root = Tk()
	root.withdraw()
	root.update()
	file_path = askopenfilename()
	root.destroy()
	img = PIL.Image.open(file_path)	#создаём объект изображения
	draw = ImageDraw.Draw(img)	   		#объект рисования
	width = img.size[0]  		   		#ширина
	height = img.size[1]		   		#высота	
	pix = img.load()				#все пиксели тут
	f = open('keys.txt','w')			#текстовый файл для ключей
	for elem in ([ord(elem) for elem in input("text: ")]):
		key = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print('Ключи записаны в keys.txt')
	img.save("STEGO_picture.png", "PNG")
	f.close()

def decrypt():
	a = []
	keys = []
	print("Выберете картинку в которой стеганография")
	root = Tk()
	root.withdraw()
	root.update()
	file_path = askopenfilename()
	root.destroy()
	img = PIL.Image.open(file_path)
	pix = img.load()
	print("Выберете файл с ключами")
	root = Tk()
	root.withdraw()
	root.update()
	key_path = askopenfilename()
	root.destroy()
	f = open(key_path, 'r')
	y = str([line.strip() for line in f])
	for i in range(len(findall(r'\((\d+)\,', y))):
		keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
	for key in keys:
		a.append(pix[tuple(key)][0])
	print(''.join([chr(elem) for elem in a]))


def main():
	if (int(input('0. Дешифрование\n1. Шифрование\n'))):
		encrypt()
	else:
		decrypt()

main()
