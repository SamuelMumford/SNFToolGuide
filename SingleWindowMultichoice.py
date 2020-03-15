# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:04:46 2020

@author: Sam
"""

import tkinter as tk
import difflib
import webbrowser
from functools import partial
import ToolGuideInfo

class HyperlinkManager:

    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="blue", underline=1)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(tk.CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return

root = tk.Tk()
root.withdraw()

current_window = None

def  replace_window(root):
    """Destroy current window, create new window"""
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = tk.Toplevel(root)

    # if the user kills the window via the window manager,
    # exit the application. 
    current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)

    return current_window

#Pull up a window with a help text script
def help_text(helpers, index):
    new_window = tk.Toplevel(root)
    textHelp = tk.Text(new_window, wrap=tk.WORD)
    textHelp.insert(tk.INSERT, str(helpers[index]))
    textHelp.pack()
    return new_window

#The main window for inputting tool specifications and displaying tool information
def new_window(Qs, Titles, starter, guide, names, helpers):
    #Make the window and the global ans variable with tool info
    window = replace_window(root)
    global ans
    ans = [-1]*len(Titles)
    ans[0] = starter
    buttons = dict()
    questions = dict()
    maxC = 0
    window.title("Tool Selection Helper")
    #Find out how many columns are needed to store all buttons to follow
    for i in range(1, len(Titles)-1):
        if(len(Qs[i][:]) > maxC):
            maxC = len(Qs[i][:])
    #Display instructions on using the tool
    startBoxSize = 12
    textStart = tk.Text(window, height = startBoxSize, bd=10, wrap=tk.WORD)
    textStart.config(state="normal")
    textStart.insert(tk.INSERT, ToolGuideInfo.startScript)
    textStart.config(state = "disabled")
    textStart.grid(row = 0, column = 0, columnspan = maxC+2, rowspan = startBoxSize)
    #Display the list of tools which meet the initial specifications (i.e. any metal or dielectric tool)
    textOut = tk.Text(window, height = 5, bd = 10)
    textOut.config(state="normal")
    textOut.insert(tk.INSERT, "Viable Tools: ")
    textOut.insert(tk.INSERT, viable_tools(guide))
    textOut.config(state="disabled")
    textOut.grid(row=3*len(Titles)+1 + startBoxSize, column=0, columnspan=maxC+2, rowspan=5)
    #Declare the prompts and the buttons which change tool requirements
    for i in range(1, len(Titles)-1):
        questions[i] = tk.Text(window, height = 1, bd = 4)
        questions[i].grid(row=3*i + startBoxSize, column=0, columnspan=maxC, rowspan=1)
        questions[i].insert(tk.INSERT, str(Titles[i]) + ':')
        questions[i].config(state="disabled")
        for k in range(len(Qs[i][:])):
            #Clear specification buttons
            if(k +1 == len(Qs[i][:])):
                buttons[str(i) + str(k)] = tk.Button(window, bg = "yellow", text=Qs[i][k], command=lambda a=[i, -1, questions[i], Titles[i], Qs[i][k], textOut, guide]: change_answers(a))
                buttons[str(i) + str(k)].grid(row = 3*i + startBoxSize, column = maxC)
            #Tool specification buttons
            else:
                buttons[str(i) + str(k)] = tk.Button(window, text=Qs[i][k], command=lambda a=[i, k, questions[i], Titles[i], Qs[i][k], textOut, guide]: change_answers(a))
                buttons[str(i) + str(k)].grid(row = 3*i + 1 + startBoxSize, column = k)
        #Help buttons for each prompt
        buttons[str(i)] = tk.Button(window, bg = "light blue", text='Help', command=lambda a=i: help_text(helpers, a))
        buttons[str(i)].grid(row = 3*i + startBoxSize, column = maxC+1)
    #Buttons to quit the program, display more detailed tool info, and clear all tool requirements
    Quit_button = tk.Button(window, text="QUIT", bg='red', command=root.destroy)
    Quit_button.grid(row = len(3*Titles) + startBoxSize, column = 1, pady = 5)
    Eval_button = tk.Button(window, text="Get Tool Info", bg= "light green", command=lambda: eval_answers(textOut, names, guide))
    Eval_button.grid(row = len(3*Titles) + startBoxSize, column = 0, pady = 5)
    Clear_All_button = tk.Button(window, text="Clear All", bg = "yellow", command=lambda: clear_all(questions, Titles, textOut, guide))
    Clear_All_button.grid(row = len(3*Titles) + startBoxSize, column = maxC, pady = 5)

#Reset the global ans variable to accept all answers, keeping only the classification
#of metal or dielectric
def clear_all(BoxList, tit, textOut, guide):
    for i in range(1, len(ans)):
        ans[i] = -1
    for i in range(1, len(BoxList)+1):
        BoxList[i].config(state = "normal")
        BoxList[i].delete('1.0', tk.END)
        BoxList[i].insert(tk.INSERT, str(tit[i]) + ':')
        BoxList[i].config(state="disabled")
    textOut.config(state="normal")
    textOut.delete('1.0', tk.END)
    textOut.insert(tk.INSERT, "Viable Tools: ")
    textOut.insert(tk.INSERT, viable_tools(guide))
    textOut.config(state="disabled")

#Change the global ans variable storing tool specifications based on a button press.
#Then write the names of all viable tools remaining.
def change_answers(x):
    ans[x[0]] = x[1]
    x[2].config(state="normal")
    x[2].delete('1.0', tk.END)
    if(x[1] != -1):
        x[2].insert(tk.INSERT, str(x[3]) + ': ' + str(x[4]))
    else:
        x[2].insert(tk.INSERT, str(x[3]) + ': ')
    x[2].config(state="disabled")
    text = x[5]
    text.config(state="normal")
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Viable Tools: ")
    text.insert(tk.END, str(viable_tools(x[6])))
    text.config(state="disabled")

#return a string of all the acceptable tool names using the accept_ans
#function to determine if each tool works with the current requirements
def viable_tools(guide):
    baseS = ""
    for key in guide:
        if(accept_ans(guide[key])):
            baseS = baseS + key + ', '
    baseS = baseS[:-2]
    return baseS

#Check your current answers/button press values against the acceptable
#button press values for each tool
def accept_ans(arr2D):
    toolWorks = True
    for i in range(len(arr2D)):
        if(ans[i] not in arr2D[i][:]):
            toolWorks = False
    return toolWorks

#Use accept_ans to find tool names that work, then use the search function on the 
#dictionary of tool information to display tool information
def eval_answers(text, names, guide):
    text.config(state="normal")
    text.delete('1.0', tk.END)
    text.insert(tk.END, 'Result:')
    for key in guide:
        if(accept_ans(guide[key])):
            matches = sequence_matcher(names, 3, .5, key)
            hyperlink = HyperlinkManager(text)
            text.config(state="normal")
            text.insert(tk.END, '\n')
            text.insert(tk.END, 'Displaying info for: ' + str(matches[0]))
            text.insert(tk.END, '\n')
            text.insert(tk.END, 'Training by ' + names[matches[0]][0])
            text.insert(tk.END, '\n')
            text.insert(tk.END, 'Repairs by ' + names[matches[0]][1])
            text.insert(tk.END, '\n')
            text.insert(tk.END, 'New SNF tool site ')
            text.insert(tk.INSERT, 'here', hyperlink.add(partial(webbrowser.open, names[matches[0]][2])))
            text.insert(tk.END, '\n')
            text.insert(tk.END, 'Old Wiki entry ')
            text.insert(tk.INSERT, 'here', hyperlink.add(partial(webbrowser.open, names[matches[0]][3])))
            text.insert(tk.END, '\n')
    text.config(state="disabled")

#Decide if you are using the metal or dielectric deposition prompt questions
def start_window(counter, Qs1, Qs2, Titles1, Titles2, MKey, DKey, MHelpers, DHelpers):
    counter += 1

    window = replace_window(root)
    label = tk.Label(window, text=Titles1[counter-1])
    button = tk.Button(window, text=Qs1[counter-1][0], command= lambda: new_window(Qs1, Titles1, 0, MKey, names, MHelpers))
    button2 = tk.Button(window, text=Qs1[counter-1][1], command= lambda: new_window(Qs2, Titles2, 1, DKey, names, DHelpers))
    #button3 = tk.Button(window, text=Qs1[counter-1][2], command= lambda: new_window(Qs3, Titles3, 2, MDKey, names))
    Quit_button = tk.Button(window, text="QUIT", command=root.destroy)
    label.pack(fill="both", expand=True, padx=20, pady=20)
    button.pack(padx=10, pady=10)
    button2.pack(padx=10, pady=10)
    #button3.pack(padx=10, pady=10)
    Quit_button.pack(padx=10, pady=10)
    
#Window for deciding on how to look for tool information
def base_start_window(counter, Qs1, Qs2, Titles1, Titles2, names, MKey, DKey, MHelpers, DHelpers):
    window = replace_window(root)
    label = tk.Label(window, text="Help Picking Tool or Getting Info?")
    button = tk.Button(window, text="Help Me Get Tool Info", command= lambda: search_window(names))
    button2 = tk.Button(window, text="Help Me Pick a Tool", command= lambda: start_window(counter, QsM, QsD, TitM, TitD, MKey, DKey, MHelpers, DHelpers))
    label.pack(fill="both", expand=True, padx=20, pady=20)
    button.pack(padx=10, pady=10)
    button2.pack(padx=10, pady=10)

#Main Tkinter window for searching for tool info based on a name
def search_window(names):
    #Setup window
    window = replace_window(root)
    label = tk.Label(window, text='Search for Tool')
    text0 = tk.Text(window, height = 1)
    text0.insert(tk.INSERT, "Type Tool Name Below:")
    text0.config(state="disabled")
    text0.pack(expand=True, padx=20, pady=0)
    text = tk.Text(window, height = 1)
    text.pack(padx=20, pady=10)
    textOut = tk.Text(window, height = 10)
    textOut.insert(tk.INSERT, "Result:")
    textOut.config(state="disabled")
    textOut.pack()
    #Search button calls a search on input text
    Search_button = tk.Button(window, text="SEARCH", command=lambda: search_input(text, textOut, names))
    Search_button.pack(side = tk.LEFT, padx=10, pady=10)
    #Reset your search
    clear_button = tk.Button(window, text="CLEAR", command=lambda: clear_text(text, textOut))
    clear_button.pack(side = tk.LEFT, padx=10, pady=10)
    Quit_button = tk.Button(window, text="QUIT", command=root.destroy)
    Quit_button.pack(side = tk.LEFT, padx=10, pady=10)

#Use the sequence matcher to search for the right tool, then display the tool information
#In an output textbox
def search_input(textBox, textOutput, names):
    inputValue=textBox.get("1.0","end-1c")
    matches = sequence_matcher(names, 3, .5, inputValue)
    if(len(matches) > 0):
        hyperlink = HyperlinkManager(textOutput)
        textOutput.config(state="normal")
        textOutput.delete('1.0', tk.END)
        textOutput.insert(tk.END, 'Result:')
        textOutput.insert(tk.END, '\n')
        textOutput.insert(tk.END, 'Displaying info for: ' + str(matches[0]))
        textOutput.insert(tk.END, '\n')
        textOutput.insert(tk.END, 'Training by ' + names[matches[0]][0])
        textOutput.insert(tk.END, '\n')
        textOutput.insert(tk.END, 'Repairs by ' + names[matches[0]][1])
        textOutput.insert(tk.END, '\n')
        textOutput.insert(tk.END, 'New SNF tool site ')
        textOutput.insert(tk.INSERT, 'here', hyperlink.add(partial(webbrowser.open, names[matches[0]][2])))
        textOutput.insert(tk.END, '\n')
        textOutput.insert(tk.END, 'Old Wiki entry ')
        textOutput.insert(tk.INSERT, 'here', hyperlink.add(partial(webbrowser.open, names[matches[0]][3])))
        textOutput.insert(tk.END, '\n')
        textOutput.config(state="disabled")
    else:
        textOutput.config(state="normal")
        textOutput.insert("Did not find that tool")
        textOutput.config(state="disabled")
        
#Reset the output text box after displaying tool information
def clear_text(textBox, textOutput):
    textOutput.config(state="normal")
    textOutput.delete('1.0', tk.END)
    textOutput.insert(tk.INSERT, "Result:")
    textOutput.config(state="disabled")
    textBox.delete('1.0', tk.END)

#Look through the library of tool names and see which is closest to the input
def sequence_matcher(input_dict, n, cutoff, word):
    #input_list = input_dict.items()
    matches = list()
    bmatch = 0
    word = word.lower()
    for key, value in input_dict.items():
        tmatch = difflib.SequenceMatcher(None, word, key).ratio()
        if len(matches) > n:
            break
        if difflib.SequenceMatcher(None, word, key).ratio() >= cutoff:
            if(tmatch > bmatch):
                bmatch = tmatch
                if(len(value) == 1):
                    matches = ([value[0], input_dict[value[0]]])
                else:
                    matches = ([key, value])
    return matches


#Read in the questions and button options
TitM = ToolGuideInfo.TitM
TitD = ToolGuideInfo.TitD
QsM = ToolGuideInfo.QsM
QsD = ToolGuideInfo.QsD

#An index that keeps track of TKinter windows
counter = 0
#A dictionary pointing from tool names (and common other names for tools) to tool info
names = ToolGuideInfo.names
#A dictionary pointing from tool names to acceptable answers/button presses
metalKey = ToolGuideInfo.metalKey
DiKey = ToolGuideInfo.DiKey
#Help information for each prompt
DHelp = ToolGuideInfo.DHelp
MHelp = ToolGuideInfo.MHelp
#Run the main program
base_start_window(counter, QsM, QsD, TitM, TitD, names, metalKey, DiKey, MHelp, DHelp)
root.mainloop()