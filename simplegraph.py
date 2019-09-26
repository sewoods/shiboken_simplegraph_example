import sys, os
import numpy as np
from scipy import optimize
from PySide2.QtCore import QUrl, QObject, Slot, QPointF, QTimer, Signal, Property
from PySide2.QtWidgets import QApplication # Need this for QtCharts
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCharts import *
from Datafit import DataGenerator as LibDataGenerator
from Datafit import DataFitter

class ScipyFit(QObject):
	def __init__(self):
		QObject.__init__(self)
		self.__pts=[]

	@Slot(QObject,QObject)
	def createFit(self,xy_series,fit_xy_series):
		#Remove previous data
	    del self.__pts[:]
	    num_pts = xy_series.count()
	    x_data = np.zeros(num_pts)
	    y_data = np.zeros(num_pts)
	    def test_func(x,a,b):
		    return a*np.sin(b*x)
	    for n in range(num_pts):
		    x_data[n] = xy_series.at(n).x()
		    y_data[n] = xy_series.at(n).y()
	    params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[1,1])
	    for n in range(num_pts):
		    y_data[n] = test_func(x_data[n],params[0],params[1])
		    point=QPointF(x_data[n],y_data[n])
		    self.__pts.append(point)
	    fit_xy_series.replace(self.__pts)

class LibraryFit(QObject):
	def __init__(self):
		QObject.__init__(self)
		self.__pts=[]

	@Slot(QObject,QObject)
	def createFit(self,xy_series,fit_xy_series):
		#Remove previous data
	    del self.__pts[:]
	    num_pts = xy_series.count()
	    x_data = np.zeros(num_pts)
	    y_data = np.zeros(num_pts)
	    m_b = np.zeros(2)
	    for n in range(num_pts):
		    x_data[n] = xy_series.at(n).x()
		    y_data[n] = xy_series.at(n).y()
	    fitter = DataFitter()
	    m_b = fitter.linearRegression(x_data,y_data)
	    for n in range(num_pts):
	        y = m_b[0]*x_data[n] + m_b[1]
	        point = QPointF(x_data[n],y)
	        self.__pts.append(point)
	    fit_xy_series.replace(self.__pts)


class DataGenerator(QObject):
	def __init__(self):
		QObject.__init__(self)
		self.__pts=[] # an array of QPointF
		self.__num_pts=200
		self.__x_data=[]
		self.__b=0
		x_increment = 2*np.pi/float(self.__num_pts)
		for n in range(self.__num_pts):
			x = -np.pi + n*x_increment
			self.__x_data.append(x)

	def generateWithNumpy(self):
		# Remove previous data
		del self.__pts[:]
		noise = np.random.normal(0,0.17,self.__num_pts)
		for n in range(self.__num_pts):
			y = np.sin(self.__x_data[n]) + noise[n]
			point=QPointF(self.__x_data[n],y)
			self.__pts.append(point)

	def generateWithLibrary(self):
		# Remove previous data
		del self.__pts[:]
		datagen=LibDataGenerator()
		y_data=[]
		y_data=datagen.getData(self.__x_data)
		self.__b=y_data[99]
		for n in range(self.__num_pts):
			point=QPointF(self.__x_data[n],y_data[n])
			self.__pts.append(point)
		
	@Slot(QObject)
	def generatePlotData(self,xy_series):
		self.generateWithNumpy()
		xy_series.replace(self.__pts)

	@Slot(QObject)
	def generateLibPlotData(self,xy_series):
		self.generateWithLibrary()
		xy_series.replace(self.__pts)

if __name__ == "__main__":
	# Set Default Style 
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"

    # Data Generator
    data_generator=DataGenerator()

	# SciPy Fit
    scipy_fit=ScipyFit()

	# Library Fit
    library_fit=LibraryFit()

    # Application window and QML engine
    # Qt Charts uses Qt Graphics View Framework for drawing, therefore QApplication must be used.
    # Expected to change (perhaps as early as 5.14)
    app=QApplication(sys.argv)
    engine=QQmlApplicationEngine()

    # Set Context Property
    engine.rootContext().setContextProperty("dataGenerator",data_generator)
    engine.rootContext().setContextProperty("scipyFit",scipy_fit)
    engine.rootContext().setContextProperty("libraryFit",library_fit)

    # Load start point into QML Engine
    engine.load(QUrl('./graphdisplay.qml'))

    # Execute application
    sys.exit(app.exec_())

