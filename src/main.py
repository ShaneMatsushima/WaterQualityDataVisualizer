from parseFunc import *
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

filename = ""
  
def open_file(): 
    global filename
    file = askopenfile(initialdir='/', filetypes =[('CSV Files', '*.csv')]) 
    filename = file.name
  
root = Tk() 
root.geometry('1000x600') 
root.title('Water Quality Data Visualizer 1.0')

btn = Button(root, text ='Select CSV File', command = lambda:open_file()) 
btn.place(relx=0.5, rely=0.5, anchor=CENTER) 

graph = Button(root, text='Plot data by time', command = lambda:box_plot(filename, 'Arsenic', 'ug/l'))
graph.place(relx=0.5, rely=1.0, anchor=S)
  
mainloop() 


# if __name__ == '__main__':
#     graph_value_over_time('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'Temperature, water')
#     graph_value_over_time('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'pH')

#     box_plot('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'Arsenic', 'ug/l')