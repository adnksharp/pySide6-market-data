import sys
import yfinance as yf
from notifypy import Notify as noty

from PySide6.QtWidgets import QApplication, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtGui import QPalette

from ui_form import Ui_Widget

colors = {
        'high': '#5bf2fa',
        'low': '#2c3e7f',
        'on': '#f75d54',
        'off': '#812b2d'
        }

class Canvas(FigureCanvas):
    def __init__(self):
        fig = Figure(facecolor=QPalette().color(QPalette.Window).name())
        fig.set_tight_layout(True)

        self.axes = fig.add_subplot(facecolor=QPalette().color(QPalette.Window).name())
        self.axes.tick_params(labelcolor=colors['on'], color=colors['high'])

        for spine in self.axes.spines.values():
            spine.set_edgecolor(colors['on'])

        self.axes.set_xlabel('Tiempo (s)', color=QPalette().color(QPalette.WindowText).name())
        self.axes.set_ylabel('PPM', color=QPalette().color(QPalette.WindowText).name())

        super(Canvas, self).__init__(fig)

    def update(self, data):
        self.axes.clear()
        self.axes.plot(data, color=colors['high'])

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.info = {}
        self.now = {}
        self.period = 'ytdx'
        self.interval = '1wk'
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.search.clicked.connect(self.getTicker)
        self.ui.period.currentIndexChanged.connect(self.changePeriod)
        self.ui.interval.currentIndexChanged.connect(self.changeInterval)
        
    def changePeriod(self):
        match self.ui.period.currentIndex():
            case 0:
                opt = ['1m', '2m', '5m', '15m', '30m', '1h']
            case 1:
                opt = ['5m', '15m', '30m', '60m', '90m', '1d']
            case 2:
                opt = ['30m', '60m', '90m', '1d', '5d', '1wk']
            case 3:
                opt = ['60m', '90m', '1d', '5d', '1wk', '1mo']
            case _:
                opt = ['1d', '5d', '1wk', '1mo', '3mo']
        
        self.ui.interval.clear()
        self.ui.interval.addItems(opt)
                
        opt = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.period = opt[self.ui.period.currentIndex()]
        
    def changeInterval(self):
        self.interval = self.ui.interval.currentText()
        
    def getTicker(self):
        symbol = self.ui.symbol.text().upper()
        self.ui.symbol.setText(symbol)
        if symbol.isalpha():
            data = yf.Ticker(symbol)
            if data.info['trailingPegRatio']:
                self.info = data.info
                self.ui.name.setText(self.info['longName'])
                self.info.pop('longBusinessSummary')
                self.info.pop('companyOfficers')
                self.now = data.analyst_price_targets
                self.h = data.history(period=self.period, interval=self.interval)
            else:
                self.now = {}
                self.info = {}
                
                self.ui.symbol.setText('')
                self.ui.name.setText('Empresa no encontrada')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
