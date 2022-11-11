import sys

import matplotlib.pyplot as plt
from scipy.linalg import dft

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtCore import *
from PySide6.QtWidgets import *

DEFAULT_LENGTH = 64
MAXIMUM_LENGTH = 128
plt.rc('text', usetex=True)
plt.rcParams["text.latex.preamble"] = r"""
\usepackage{amsmath}
"""


class LengthSelector(QSpinBox):
    def __init__(self, default_value):
        super().__init__()
        self.setValue(default_value)
        self.setMinimum(0)
        self.setMaximum(MAXIMUM_LENGTH)


class IndexSelector(QSlider):
    def __init__(self, default_max):
        super().__init__(orientation=Qt.Orientation.Horizontal)
        self.setValue(0)
        self.setMinimum(0)
        self.setMaximum(default_max - 1)


class Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.fig, self.axs = plt.subplots(figsize=(12, 6), nrows=2, layout="tight")
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.update_plot(0, DEFAULT_LENGTH)
        

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        

    def update_plot(self, index, length):
        for ax, part in zip(self.axs, (r"Re$(\omega_k[n])$", r"Im$(\omega_k[n])$")):
            ax.clear()
            ax.set_xlabel(r"$n$", size=20)
            ax.set_ylabel(part, size=20)
            ax.set_ylim(-1.1, 1.1)
            ax.set_yticks([-1, 0, 1])
        
        basis = dft(length).T
        real, imag = basis[index].real, basis[index].imag
        eq = r"\omega_k[n] = e^{j\tfrac{2\pi}{N}nk}"
        self.fig.suptitle(fr"${eq}$, $k={index}$, $N={length}$", size=24)
        self.axs[0].stem(real)
        self.axs[1].stem(imag)
        self.canvas.draw()
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.length = DEFAULT_LENGTH
        
        # widgets
        central_widget = QWidget()
        self.graph = Graph()
        self.length_selector = LengthSelector(default_value=DEFAULT_LENGTH)
        self.index_selector = IndexSelector(default_max=DEFAULT_LENGTH)
        length_selector_label = QLabel("Длина сигнала")
        index_selector_label = QLabel("n")
        
        # layout
        self.setCentralWidget(central_widget)
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(length_selector_label)
        hlayout.addWidget(self.length_selector)
        hlayout.addWidget(index_selector_label)
        hlayout.addWidget(self.index_selector)
        
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.graph)
        vlayout.addLayout(hlayout)

        central_widget.setLayout(vlayout)

        # connections
        self.length_selector.valueChanged.connect(self.update_length)
        self.index_selector.valueChanged.connect(self.update_index)

    def update_index(self, index):
        self.index = index
        self.graph.update_plot(self.index, self.length)

    def update_length(self, length):
        self.length = length
        self.index_selector.setMaximum(self.length - 1)
        self.graph.update_plot(self.index, self.length)
    
        

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.showMaximized()
app.exec()