from tkinter import *
import math

number = 0
operator = '+'

class Button_grid():
	def __init__(self, x, y, text, func):
		self.button = Button(text = text, bg = button_bg, fg = button_fg, command = func)
		self.button.place(x = x * 50, y = y * 50 + 50, width = 50, height = 50)

def exponentiation_pressed():
	entry['text'] = str(float(entry['text']) ** 2)

def root_pressed():
	entry['text'] = str(math.sqrt(float(entry['text'])))

def delete_all_pressed():
	entry['text'] = ''
	number = 0

def delete_pressed():
	entry['text'] = entry['text'][0:len(entry['text'])-1]

def number_pressed(number):
	entry['text'] += number

def operation_pressed(operation):
	global number, operator
	number = entry['text']
	entry['text'] = ''
	operator = operation

def is_oper_pressed():
	try:
		if operator == '/' and float(entry['text']) == 0.0:
			entry['text'] = "Division by zero"
		else:
			exec("entry['text'] = str(float(number) " + operator + " float(entry['text']))")
	except:
		entry['text'] = 'Неправильный ввод'



screen_width = 200
screen_height = 300

button_bg = 'black'
button_fg = 'white'

window = Tk()
window.geometry(f'{screen_width}x{screen_height}')
window.resizable(False, False)
window['bg'] = 'black'
window.title("Calc")

entry = Label(text = "", bg = 'white', fg = 'black')
entry.place(x = 0, y = 0, width = screen_width, height = 50)

exponentiation = Button_grid(0, 0, '^2', exponentiation_pressed)
root = Button_grid(1, 0, 'root', root_pressed)
delete_all = Button_grid(2, 0, 'C', delete_all_pressed)
delete = Button_grid(3, 0, '<==', delete_pressed)
seven = Button_grid(0, 1, '7', lambda: number_pressed('7'))
eight = Button_grid(1, 1, '8', lambda: number_pressed('8'))
nine = Button_grid(2, 1, '9', lambda: number_pressed('9'))
division = Button_grid(3, 1, '/', lambda: operation_pressed('/'))
four = Button_grid(0, 2, '4', lambda: number_pressed('4'))
five = Button_grid(1, 2, '5', lambda: number_pressed('5'))
six = Button_grid(2, 2, '6', lambda: number_pressed('6'))
multiplication = Button_grid(3, 2, '*', lambda: operation_pressed('*'))
one = Button_grid(0, 3, '1', lambda: number_pressed('1'))
two = Button_grid(1, 3, '2', lambda: number_pressed('2'))
three = Button_grid(2, 3, '3', lambda: number_pressed('3'))
minus = Button_grid(3, 3, '-', lambda: operation_pressed('-'))
zero = Button_grid(0, 4, '0', lambda: number_pressed('0'))
tochka = Button_grid(1, 4, ',', lambda: number_pressed('.'))
plus = Button_grid(2, 4, '+', lambda: operation_pressed('+'))
is_oper = Button_grid(3, 4, '=', is_oper_pressed)

window.mainloop()