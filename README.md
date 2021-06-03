# WaterQualityDataVisualizer
This project was based around parsing and visualizing large water quality data (csv) based around data from 
[this link](https://www.waterqualitydata.us/). The visualizer implements a easy to use UI that allows users to select specific 
data points in the large data set to visualize. Data visualize does not take into affect outliers which may scew the outcome of the data presented. 

## Description
This project was produced in one semesters worth of class time as a replacement for in class curriculum. This project allows users to implement large data sets that are formatted as a csv and visualize, through various graphs, the data collected. The data being collected is based around the csv formatting the [National Water Quality Council](https://www.waterqualitydata.us/), NWQC, data sets that are made public on their website. 

The goal of this project is not only to help users visualize large data sets but to gain a better understanding on what is happening to bodies of water around specific areas. This project is a part of a larger project that revolves around utilizing machine learning in order to predict which bodies of water need to be tested for different criterias that maybe harmful to the enviornment around it. 

## Getting Started

### Dependencies
The following list are libraries or dependencies needed in order to utilize the program:

* Python 2.0+
* datetime
* Pandas 
* Numpy 
* MatPlotLib
* tkinter

### Installing

To install the project, in your terminal, clone the repository. From there place any csv files being utilized in to the csv folder and run main.py under the src file. The UI will then pop up asking for infomration on the data you would like to visualize. 

## Help

For any issues or inqueries about the program, please open an issues tab and the issue will be addressed as soon as possible. 

## Author

Mentor: Dr. Jordan Wolfand

Developer: [Shane Matsushima](https://github.com/ShaneMatsushima)


## Version History
* 0.2
    * Implementation of UI aspect
    * Code condenced to incorporate any csv file from the NWQC
* 0.1
    * Initial Release

 
