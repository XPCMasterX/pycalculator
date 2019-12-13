import tkinter
window = tkinter.Tk()
window.title("Calculator")



def getInput():
  global equation
  equation = textInput.get()
  global final 
  final = eval(equation)
  labelOne = tkinter.Label(window, text=final)
  labelOne.grid(row="1", column="0")

textInput = tkinter.Entry(window)
textInput.grid(row="0", column="0")

buttonOne = tkinter.Button(window, text="Evaluate!", bg="blue", fg="white", command=getInput)
buttonOne.grid(row="0", column="1")

window.geometry("900x300")
window.mainloop()