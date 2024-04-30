# Import the tkinter module
from tkinter import *

# Creating the GUI window.
root = Tk()
root.title("Tkarami_Calculator")
root.geometry("312x400")
root.resizable(0, 0)





# Creating our text widget.
input_text = StringVar()


def btn_click(item):
  global expression
  global flag_dot
  if(item=="." and flag_dot==0):
      flag_dot=1
      expression = expression + str(item)
      input_text.set(expression)
  elif(item!="."):
      if(item=="+" or item=="-" or item=="*" or item=="/" ):

          if(expression[-1]!="+" and expression[-1]!="-"
                  and expression[-1]!="*" and expression[-1]!="/"):
              flag_dot = 0
              expression = expression + str(item)
              input_text.set(expression)
          else:

              expression = (str(expression)[:-1]) + str(item)
              input_text.set(expression)

      else:
              expression = expression + str(item)
              input_text.set(expression)


def btn_clear():
 global expression
 global flag_dot
 flag_dot=0
 expression = ""
 input_text.set("")


def btn_equal():
 global expression
 global flag_dot
 if(expression==""):
  expression=input_text.get()
 result = str(eval(expression))
 input_text.set(result)
 expression = ""
 flag_dot=0


expression = ""
flag_dot=0



input_frame = Frame(root, width = 312, height = 50, bd = 0,
                    highlightbackground = "gray", highlightcolor = "gray", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), foreground="black",
                    textvariable = input_text, width = 50, bd = 0, justify = LEFT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(root, width = 312, height = 290)
btns_frame.pack()

clear_img = PhotoImage(file ="clear.png")
divide_img = PhotoImage(file ="dive.png")
#divide_img=divide_img.subsample(1,1) change size of image

clear= Button(btns_frame,image=clear_img,borderwidth=0,command=lambda :btn_clear()).grid(row = 0, column = 0)
divide= Button(btns_frame,image=divide_img,borderwidth=0,command=lambda :btn_click("/")).grid(row = 4, column = 3)


#clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
#divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven_img = PhotoImage(file ="seven.png")
eight_img = PhotoImage(file ="eight.png")
nine_img = PhotoImage(file ="nine.png")
multiply_img = PhotoImage(file ="mul.png")

seven= Button(btns_frame,image=seven_img,borderwidth=0,command=lambda :btn_click(7)).grid(row = 1, column = 0)
eight= Button(btns_frame,image=eight_img,borderwidth=0,command=lambda :btn_click(8)).grid(row = 1, column = 1)
nine= Button(btns_frame,image=nine_img,borderwidth=0,command=lambda :btn_click(9)).grid(row = 1, column = 2)
multiply= Button(btns_frame,image=multiply_img,borderwidth=0,command=lambda :btn_click("*")).grid(row = 1, column = 3)


#seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
#eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
#nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
#multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)



four_img = PhotoImage(file ="four.png")
five_img = PhotoImage(file ="five.png")
six_img = PhotoImage(file ="six.png")
minus_img = PhotoImage(file ="minus.png")

four= Button(btns_frame,image=four_img,borderwidth=0,command=lambda :btn_click(4)).grid(row = 2, column = 0)
five= Button(btns_frame,image=five_img,borderwidth=0,command=lambda :btn_click(5)).grid(row = 2, column = 1)
six= Button(btns_frame,image=six_img,borderwidth=0,command=lambda :btn_click(6)).grid(row = 2, column = 2)
minus= Button(btns_frame,image=minus_img,borderwidth=0,command=lambda :btn_click("-")).grid(row = 2, column = 3,sticky="nsew")


#four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
#five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
#six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
#minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


one_img = PhotoImage(file ="one.png")
two_img = PhotoImage(file ="two.png")
three_img = PhotoImage(file ="three.png")
plus_img = PhotoImage(file ="plus.png")

one= Button(btns_frame,image=one_img,borderwidth=0,command=lambda :btn_click(1)).grid(row = 3, column = 0)
two= Button(btns_frame,image=two_img,borderwidth=0,command=lambda :btn_click(2)).grid(row = 3, column = 1)
three= Button(btns_frame,image=three_img,borderwidth=0,command=lambda :btn_click(3)).grid(row = 3, column = 2)
plus= Button(btns_frame,image=plus_img,borderwidth=0,command=lambda :btn_click("+")).grid(row = 3, column = 3)


#one = Button(btns_frame, text = "1",image=one_img, width = 10, height = 3, cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
#two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
#three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
#plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero_img = PhotoImage(file ="zero.png")
dot_img = PhotoImage(file ="dot.png")
equal_img = PhotoImage(file ="equal.png")

zero= Button(btns_frame,image=zero_img,borderwidth=0,command=lambda :btn_click(0)).grid(row = 4, column = 0)
point= Button(btns_frame,image=dot_img,borderwidth=0,command=lambda :btn_click(".")).grid(row = 4, column = 1)
equals= Button(btns_frame,image=equal_img,borderwidth=0,command=lambda :btn_equal()).grid(row = 4, column = 2)


#zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              #command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
#point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               #command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
#equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          #      command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()