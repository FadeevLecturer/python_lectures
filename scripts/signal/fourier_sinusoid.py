import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtCore import *
from PySide6.QtWidgets import *


LENGTH = 128
COEFFICIENT = r"\frac{2\pi}{" + str(LENGTH) + r"}"
plt.rc('text', usetex=True)
plt.rcParams["text.latex.preamble"] = r"""
\usepackage{amsmath}
"""


def get_signal(magnitudes, frequencies, phases):
    A1, A2, A3 = magnitudes
    w1, w2, w3 = frequencies
    k1, k2, k3 = phases
    
    c = 2 * np.pi / LENGTH
    t = np.arange(LENGTH)
    return A1*np.cos(c*w1*(t - k1)) + A2*np.cos(c*w2*(t - k2)) + A3*np.cos(c*w3*(t - k3))


class FrequencySelector(QDial):
    def __init__(self):
        super().__init__()
        self.setMinimum(0)
        self.setMaximum(LENGTH // 2)
        self.setValue(0)


class PhaseSelector(QSlider):
    def __init__(self):
        super().__init__(Qt.Orientation.Horizontal)
        self.setMinimum(-LENGTH)
        self.setMaximum(LENGTH)
        self.setValue(0)


class MagnitudeSelector(QSlider):
    def __init__(self, max_height=5, resolution=10):
        super().__init__(Qt.Orientation.Vertical)
        self.setMinimum(-resolution)
        self.setMaximum(resolution)
        self.setValue(0)
        self.max_height = max_height
        self.resolution = resolution

    def get_scaled_value(self):
        return self.value() * self.max_height / self.resolution


class FrequencyBoard(QGroupBox):
    def __init__(self):
        super().__init__("Frequencies")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dials = [FrequencySelector() for _ in range(3)]
        for dial in self.dials:
            layout.addWidget(dial)

    def connect(self, f):
        for dial in self.dials:
            dial.valueChanged.connect(f)

    def get_values(self):
        return [dial.value() for dial in self.dials]


class PhaseBoard(QGroupBox):
    def __init__(self):
        super().__init__("Phases")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.sliders = [PhaseSelector() for _ in range(3)]
        for slider in self.sliders:
            layout.addWidget(slider)

    def connect(self, f):
        for slider in self.sliders:
            slider.valueChanged.connect(f)

    def get_values(self):
        return [slider.value() for slider in self.sliders]


class MagnitudeBoard(QGroupBox):
    def __init__(self):
        super().__init__("Magnitudes")
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.sliders = [MagnitudeSelector() for _ in range(3)]
        for slider in self.sliders:
            layout.addWidget(slider)

    def connect(self, f):
        for slider in self.sliders:
            slider.valueChanged.connect(f)

    def get_values(self):
        return [slider.get_scaled_value() for slider in self.sliders]



class Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.fig = plt.figure(figsize=(14, 8))
        self.ax1 = self.fig.add_axes((0.1, 0.55, 0.85, 0.4))
        self.ax2 = self.fig.add_axes((0.1, 0.08, 0.35, 0.4))
        self.ax3 = self.fig.add_axes((0.6, 0.08, 0.35, 0.4))
        self.axs = (self.ax1, self.ax2, self.ax3)
        self.canvas = FigureCanvasQTAgg(self.fig)
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        
    def update_plot(self,  magnitudes, frequencies, phases):
        signal = get_signal(magnitudes, frequencies, phases)
        fourier = rfft(signal)
        abs = np.abs(fourier)
        angle = np.angle(fourier)
        angle = np.where(abs > 0.0001, angle, 0)

        ylabels = (r"$x[k]$", r"$|X[k]|$", r"$\angle X[k]$")
        for ax, ylabel in zip(self.axs, ylabels):
            ax.clear()
            ax.set_xlabel(r"$k$", size=14)
            ax.set_ylabel(ylabel, size=14)
        self.ax1.stem(signal)
        self.ax2.stem(abs)
        self.ax3.stem(angle)
        self.ax3.set_yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
        self.ax3.set_yticklabels([r"$-\pi$", r"-$\dfrac{\pi}{2}$", "$0$", r"$\dfrac{\pi}{2}$", r"$\pi$"])
        self.ax3.grid()
        self.canvas.draw()
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # widgets
        central_widget = QWidget()
        self.graph = Graph()
        self.freq = FrequencyBoard()
        self.phase = PhaseBoard()
        self.magn = MagnitudeBoard()
        
        # layout
        self.setCentralWidget(central_widget)
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.freq)
        hlayout.addWidget(self.graph)
        hlayout.addWidget(self.magn)
        
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.phase)
        
        central_widget.setLayout(vlayout)
        self.update_plot()

        for widget in (self.freq, self.phase, self.magn):
            widget.connect(self.update_plot)

        
    def update_plot(self, *args):
        frequencies = self.freq.get_values()
        phases = self.phase.get_values()
        magnitudes = self.magn.get_values()
        self.graph.update_plot(magnitudes, frequencies, phases)
            
        

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.showMaximized()
app.exec()