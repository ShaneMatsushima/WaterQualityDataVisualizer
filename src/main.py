# GUI Creation for Data Visualization of csv Files
# Created by: Shane Matsushima
# Date: 10/25/2020

#TODO: create note that data visualizer is meant for csv files from https://www.waterqualitydata.us/

from parseFunc import *
from tkinter import * 
from tkinter.filedialog import askopenfile 
from tkinter import messagebox

root = Tk() 
root.geometry('800x300') 
root.title('Water Quality Data Visualizer 1.0')

filename = ""

# Defined relative coord for widgets
ROW_ONE = 0.25
ROW_TWO = 0.4
ROW_THREE = 0.55
ROW_FOUR = 0.7
LEFT_MARGIN = 0.025

# entry for unit
unitEntry = Entry(root, width=25, borderwidth=2)

elements = [
    'Mercury',
    'Manganese',
    'BOD, Ultimate',
    'Caffeine',
    'Carbonate',
    'Chloride',
    'Copper',
    'Enterococcus',
    'E. Coli',
    'Fipronil',
    'Iron',
    'Lead',
    'Nitrate',
    'Nitrite',
    'Phosphate-Phosphorus',
    'Nitrogen',
    'Oil and Gas',
    'Oxygen',
    'Sulfate',
    'Total Suspended Solids / SSC',
    'Total Coliform',
    'Total Dissolved Solids',
    'Zinc',
    'Arsenic',
    'Fecal Coliform', 
    'Temperature, water',
    'pH'
]

graphs = [
    'Line graph',
    'Box-Plot'
]

optionVariable = StringVar()
optionVariable.set(elements[0]) # default value

graphVariable = StringVar()
graphVariable.set(graphs[0]) # default value

# Define functions
def open_file(): 
    global filename
    file = askopenfile(initialdir='/', filetypes =[('CSV Files', '*.csv')]) 
    filename = file.name
    print(filename)

def show_data():
    if filename == "":
        messagebox.showwarning(title=None, message='Please select a csv file')
    unit = unitEntry.get()
    if graphVariable.get() == 'Line graph':
        graph_value_over_time(filename, optionVariable.get())
    if graphVariable.get() == 'Box-Plot':
        box_plot(filename, optionVariable.get(), unit)
 

# UI Element Create
selectCsvButton = Button(root, text='Select CSV File', padx=25, pady=10, command=open_file)
label1 = Label(root, text='Please select the type of data: ', pady=10) 
dropDownElement = OptionMenu(root, optionVariable, *elements)
label2 = Label(root, text='Please select the type of graph: ', pady=10)
dropDownGraph = OptionMenu(root, graphVariable, *graphs)
label3 = Label(root, text='Please input a unit the data: ', pady=10)
applyButton = Button(root, text='Show Data', pady=10, command=show_data)


# UI Element Placement
selectCsvButton.place(relx=0.5, rely=0.1, anchor=CENTER)
label1.place(relx=LEFT_MARGIN, rely=ROW_ONE, anchor=W)
dropDownElement.place(relx=0.3, rely=ROW_ONE, anchor=W)
label2.place(relx=LEFT_MARGIN, rely=ROW_TWO, anchor=W)
dropDownGraph.place(relx=0.3125, rely=ROW_TWO, anchor=W)
label3.place(relx=LEFT_MARGIN, rely=ROW_THREE, anchor=W)
unitEntry.place(relx=0.305, rely=ROW_THREE, anchor=W)
applyButton.place(relx=LEFT_MARGIN, rely=ROW_FOUR, anchor=W)


mainloop() 
