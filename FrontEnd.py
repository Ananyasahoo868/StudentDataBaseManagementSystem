from tkinter import *
import tkinter.messagebox

import BackEnd

class Student :

	def __init__(self,root) :
		self.root = root
		self.root.title("Student Database Management System")
		self.root.geometry("1350x7500+0+0")
		self.root.configure(background = "cadet blue")

		stdID = StringVar()
		FirstName = StringVar()
		SurName = StringVar()
		DoB = StringVar()
		Age = StringVar()
		Gender = StringVar()
		Address = StringVar()
		MobileNo = StringVar()




		def iExit() :

			iExit = tkinter.messagebox.askyesno("Student Database System", "Confirm if you want to exit")
			if iExit > 0 :
				root.destroy()
				return


		def clearData() :
			self.txtStdID.delete(0,END)
			self.txtfna.delete(0,END)
			self.txtSna.delete(0,END)
			self.txtDoB.delete(0,END)
			self.txtAge.delete(0,END)
			self.txtGender.delete(0,END)
			self.txtAdr.delete(0,END)
			self.txtMobile.delete(0,END)




		MainFrame = Frame(self.root,background = "cadet blue")
		MainFrame.grid()

		TitFrame = Frame(MainFrame,bd = 2,width = 1350,height = 70,padx = 18,pady = 10, background = "ghost white",relief = RIDGE)
		TitFrame.pack(side = TOP)

		self.lblTit = Label(TitFrame,font = ('arial',47,'bold'),text = "Student Database System",background = "Ghost White")
		self.lblTit.grid()

		ButtonFrame = Frame(MainFrame,bd =  2,width = 1350,height = 70,padx = 18,pady = 10,background = "Ghost White",relief = RIDGE)
		ButtonFrame.pack(side = BOTTOM)

		DataFrame = Frame(MainFrame, width = 1350, height = 600, padx = 20,pady = 20,relief=RIDGE,background='cadet blue')
		DataFrame.pack(side=BOTTOM)

		DataFrameLEFT = LabelFrame(DataFrame, bd = 1,width = 800,height = 600,padx = 20,relief = RIDGE,background = "ghost white",font = ('arial',20,'bold'),text="Student Info\n")
		DataFrameLEFT.pack(side = LEFT)

		DataFrameRIGHT = LabelFrame(DataFrame, bd = 1,width = 500,height = 600,padx = 20,relief = RIDGE,background = "Ghost White",font=('arial',20,'bold'),text = 'Student details\n')
		DataFrameRIGHT.pack(side = RIGHT)


		self.lblStdID = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Student ID",padx = 18,pady = 10,background = "Ghost White")
		self.lblStdID.grid(row=0,column = 0,sticky = W)

		self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = stdID,width = 35)
		self.txtStdID.grid(row=0,column = 1)

		self.lblfna = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "First Name",padx = 18,pady = 10,background = "Ghost White")
		self.lblfna.grid(row=1,column = 0,sticky = W)
		self.txtfna = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = FirstName,width = 35)
		self.txtfna.grid(row=1,column = 1)


		self.lblSna = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Last Name",padx = 18,pady = 10,background = "Ghost White")
		self.lblSna.grid(row=2,column = 0,sticky = W)

		self.txtSna = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = SurName,width = 35)
		self.txtSna.grid(row=2,column = 1)

		self.lblDoB = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "DoB",padx = 18,pady = 10,background = "Ghost White")
		self.lblDoB.grid(row=3,column = 0,sticky = W)
		self.txtDoB = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = DoB,width = 35)
		self.txtDoB.grid(row=3,column = 1)

		self.lblAge = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Age",padx = 18,pady = 10,background = "Ghost White")
		self.lblAge.grid(row=4,column = 0,sticky = W)
		self.txtAge = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = Age,width = 35)
		self.txtAge.grid(row=4,column = 1)

		self.lblAdr = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Address",padx = 18,pady = 10,background = "Ghost White")
		self.lblAdr.grid(row=5,column = 0,sticky = W)
		self.txtAdr = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = Address,width = 35)
		self.txtAdr.grid(row=5,column = 1)

		self.lblGender = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Gender",padx =18,pady = 10,background = "Ghost White")
		self.lblGender.grid(row=6,column = 0,sticky = W)
		self.txtGender = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = Gender,width = 35)
		self.txtGender.grid(row=6,column = 1)

		self.lblMobile = Label(DataFrameLEFT,font=('arial',20,'bold'),text = "Mobile No",padx = 18,pady = 10,background = "Ghost White")
		self.lblMobile.grid(row=7,column = 0,sticky = W)
		self.txtMobile = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable = MobileNo,width = 35)
		self.txtMobile.grid(row=7,column = 1)


		scrollbar = Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0, column=1, sticky='ns')

		studentlist = Listbox(DataFrameRIGHT, width = 41, height = 16, font = ('arial',12,'bold'),yscrollcommand = scrollbar.set)
		studentlist.grid(row=0,column=0,padx=8)
		scrollbar.config(command = studentlist.yview)


		self.btnAddDate = Button(ButtonFrame, text="Add New",font=('arial',20,'bold'),height = 1,width = 10,bd = 4)
		self.btnAddDate.grid(row = 0,column = 0)
		self.btnAddDate = Button(ButtonFrame, text="Display",font=('arial',20,'bold'),height = 1,width = 10,bd = 4)
		self.btnAddDate.grid(row = 0,column = 1)
		self.btnAddDate = Button(ButtonFrame, text="Clear",font=('arial',20,'bold'),height = 1,width = 10,bd = 4,command = clearData)
		self.btnAddDate.grid(row = 0,column = 2)
		self.btnAddDate = Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),height = 1,width = 10,bd = 4)
		self.btnAddDate.grid(row = 0,column = 3)
		self.btnAddDate = Button(ButtonFrame, text="Search",font=('arial',20,'bold'),height = 1,width = 10,bd = 4)
		self.btnAddDate.grid(row = 0,column = 4)
		self.btnAddDate = Button(ButtonFrame, text="Update",font=('arial',20,'bold'),height = 1,width = 10,bd = 4)
		self.btnAddDate.grid(row = 0,column = 5)
		self.btnAddDate = Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),height = 1,width = 10,bd = 4, command = iExit)
		self.btnAddDate.grid(row = 0,column = 6)








		

if __name__ == '__main__' :
	root = Tk()
	application = Student(root)
	root.mainloop()