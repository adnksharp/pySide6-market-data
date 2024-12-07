import sys
import yfinance as yf
import webbrowser as web

from PySide6.QtWidgets import QApplication, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from PySide6.QtGui import QPalette

from ui_form import Ui_Widget

colors = {
        'high': '#5bf2fa',
        'low': '#2c3e7f',
        'on': '#f75d54',
        'off': '#812b2d'
        }

class Canvas(FigureCanvas):
    def __init__(self, *args):
        fig = Figure(facecolor=QPalette().color(QPalette.Window).name())
        fig.set_tight_layout(True)

        self.axes = fig.add_subplot(111, facecolor=QPalette().color(QPalette.Window).name())
        self.axes.tick_params(labelcolor=colors['off'], color=colors['on'])

        for spine in self.axes.spines.values():
            spine.set_edgecolor(colors['high'])

        super(Canvas, self).__init__(fig)

    def update(self, xp, data):
        self.axes.clear()
        self.axes.plot(xp, data, color=QPalette().color(QPalette.Text).name(), linewidth=2)
        self.axes.set_xlim([xp[0], xp[len(xp) - 1]])

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.period = 'ytd'
        self.interval = '1wk'
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.search.clicked.connect(self.getTicker)
        self.ui.period.currentIndexChanged.connect(self.changePeriod)
        self.ui.interval.currentIndexChanged.connect(self.changeInterval)
        self.ui.pushButton.clicked.connect(self.symbolHelp)
        
    def symbolHelp(self):
        if self.ui.symbol.text().isalpha():
            web.open('https://es.finance.yahoo.com/quote/' + self.ui.symbol.text().upper())
        else:
            web.open('https://es.finance.yahoo.com/lookup/')
        
    def clearHeaders(self, layout):
        if layout is not None:
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    widget = item.widget()
                    widget.deleteLater()
                elif item.layout():
                    self.clearHeaders(item.layout())
                    
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
                info = data.info
                self.ui.name.setText(info['longName'])
                info.pop('longBusinessSummary')
                info.pop('companyOfficers')
                
                now = data.analyst_price_targets
                history = data.history(period=self.period, interval=self.interval)
                
                label = [i for i in history.index]
                history = [ i for i in history['Close']]
                
                self.graph = Canvas()
                self.clearHeaders(self.ui.verticalLayout)
                self.graph.update(label, history)
                self.ui.verticalLayout.addWidget(self.graph)
                
                self.ui.label_4.setText(f'Actual: {now["current"]}   Máx: {now["high"]}   Mín: {now["low"]}   Media: {now["mean"]}   Mediana: {now["median"]}')
                
            else:
                self.ui.symbol.setText('')
                self.ui.label_4.setText('')
                self.ui.name.setText('Empresa no encontrada')
                self.graph = Canvas()
                self.clearHeaders(self.ui.verticalLayout)
                self.graph.update([0, 1], [0, 0])
                self.ui.verticalLayout.addWidget(self.graph)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
