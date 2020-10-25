from parseFunc import *
import tkinter as tk

def graph_arsenic():
    box_plot('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'Arsenic', 'ug/l')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
graphButton = tk.Button(frame, text='Graph', command=graph_arsenic)
graphButton.pack()

root.mainloop()


# if __name__ == '__main__':
#     graph_value_over_time('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'Temperature, water')
#     graph_value_over_time('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'pH')

#     box_plot('C:\\Dev\\WaterQualityDataVisualizer\\src\\csv\\result.csv', 'Arsenic', 'ug/l')


    
