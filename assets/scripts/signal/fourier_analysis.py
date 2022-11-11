import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, rfft

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class FunctionSelector(QGroupBox):
    def __init__(self):
        super().__init__("Fourier transform function")
        self.functions = {
            "fft": fft,
            "rfft": rfft,
        }

        # buttons
        fft_button = QRadioButton("fft")
        rfft_button = QRadioButton("rfft")

        # layout 
        self.button_group = QButtonGroup()
        layout = layout = QVBoxLayout()
        for button in (fft_button, rfft_button, ):
            self.button_group.addButton(button)
            layout.addWidget(button)

        self.setLayout(layout)
        fft_button.setChecked(True)

    def get_checked_function(self):
        function_name = self.button_group.checkedButton().text()
        return self.functions[function_name]


class ModeSelector(QGroupBox):
    def __init__(self):
        super().__init__("To depict")
        self.mode = {
            "Real and imaginary parts": "part",
            "Magnitude and phase": "polar",
        }
        
        # buttons
        imagreal_button = QRadioButton("Real and imaginary parts")
        absphase_button = QRadioButton("Magnitude and phase")

        # layout 
        self.button_group = QButtonGroup()
        
        layout = QVBoxLayout()
        for button in (imagreal_button, absphase_button, ):
            self.button_group.addButton(button)
            layout.addWidget(button)

        self.setLayout(layout)
        imagreal_button.setChecked(True)

    def get_checked_mode(self):
        full_text = self.button_group.checkedButton().text() 
        return self.mode[full_text]


class Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.fig, self.axs = plt.subplots(figsize=(8, 12), nrows=3, layout="tight")
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)

        
        

    def update_plot(self, signal, mode="part", function=fft):
        tmp = (r"Re$(X[k])$", r"Im$(X[k])$") if mode == "part" else (r"$|(X[k])|$", r"$\angle(X[k])$")
        ylabels = ("Signal x[k]", *tmp)

        for ax, ylabel in zip(self.axs, ylabels):
            ax.clear()
            ax.set_xlabel(r"k")
            ax.set_ylabel(ylabel)
            ax.set_xlim(-0.5, signal.size - 0.5)
        
        fourier = function(signal)
        y1, y2 = (fourier.real, fourier.imag) if mode == "part" else (np.abs(fourier), np.angle(fourier))
        self.axs[0].stem(signal)
        self.axs[1].stem(y1)
        self.axs[2].stem(y2)
        self.canvas.draw()
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.signal = np.zeros(64)

        # widgets
        central_widget = QWidget()
        self.graph = Graph()
        self.function_selector = FunctionSelector()
        self.mode_selector = ModeSelector()
        self.select_file_button = QPushButton("Open")

        # layout
        self.setCentralWidget(central_widget)
        
        vlayout = QVBoxLayout()
        for widget in (self.function_selector, self.mode_selector, self.select_file_button):
            vlayout.addWidget(widget)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.graph)
        hlayout.addLayout(vlayout)

        central_widget.setLayout(hlayout)

        self.graph.update_plot(self.signal)

        # connections
        self.function_selector.button_group.buttonClicked.connect(self.update_plot)
        self.mode_selector.button_group.buttonClicked.connect(self.update_plot)
        self.select_file_button.clicked.connect(self.on_select_file_button_pressed)
        
    def update_plot(self):
        function = self.function_selector.get_checked_function()
        mode = self.mode_selector.get_checked_mode()
        self.graph.update_plot(self.signal, mode, function)
    

    def on_select_file_button_pressed(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            caption="Pick a signal",
            filter="Numpy array (*.npy)"
        )
        if path:
            self.signal = np.load(path)
            self.update_plot()
            
        

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.showMaximized()
app.exec()