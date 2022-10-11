from Tkinter import *
import math

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.instruction = Label(self, text = "Ingresa el numero de burpees que realizaste hoy: ")
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		
		self.burpees = Entry(self)
		self.burpees.grid(row = 1, column = 0, sticky = W)

		self.submit_button = Button(self, text = "Calcular", command = self.reveal)
		self.submit_button.grid(row = 1, column = 1, sticky = W)
		
		self.result = Label(self, text = "El numero de burpees que ha realizado es: ")
		self.result.grid(row = 3, column = 0, columnspan = 2, sticky = W)

		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row = 4, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		content = float(self.burpees.get())
		message = ( content + 1 ) * ( content / 2 )
		self.text.delete(0.0, END)
		self.text.insert(0.0, message)


root = Tk()
root.title("Password")
root.geometry("350x200")

app = Application(root)

root.mainloop()