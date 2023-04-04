import PySimpleGUI as sg
from Display import display as s

sg.theme("LightBlue3")

layout = [[sg.Text("Calculator:")],
          [sg.Text(size=(30,4), background_color= "LightBlue4",key='-OUTPUT-')],
          [sg.Text("Results:"), sg.Text(size=(15,1), key = '-RESULT-')],
          [sg.Cancel("Close")],
          [sg.Button("^", size = (4,2))],
          [sg.Button("7", size =(4,2)),sg.Button("8", size =(4,2)), sg.Button("9", size =(4,2)), sg.Button("DEL", size =(4,2)), sg.Button("AC", size =(4,2))],
          [sg.Button("4", size =(4,2)),sg.Button("5", size =(4,2)),sg.Button("6", size =(4,2)), sg.Button("*", size =(4,2)), sg.Button("/", size =(4,2))],
          [sg.Button("1", size =(4,2)),sg.Button("2", size =(4,2)),sg.Button("3", size =(4,2)), sg.Button("+", size =(4,2)), sg.Button("-", size =(4,2))],
          [sg.Button("0", size =(4,2)),sg.Button(".", size =(4,2)),sg.Button("x10", size =(4,2)), sg.Button("ANS", size =(4,2)), sg.Button("=", size =(4,2))]]


text = []
main = sg.Window("Calculator ver0.1 pretest",layout)

#Displaying the interface.
while True:
    event, value = main.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    elif event == "DEL":
        text.pop()
        main["-OUTPUT-"].update("".join(text))
    elif event == "AC":
        text.clear()
        main["-OUTPUT-"].update("".join(text))
    #special event for "=" sign, initialize the calculating algorithm.
    elif event == "=":
        try:
            rpn = s.RPN(s.whole(text))
            main["-RESULT-"].update(s.doMath(rpn))
        except:
            main["-RESULT-"].update("Syntax error")
    else:
        text.append(event)        
        main["-OUTPUT-"].update("".join(text))
main.close()


