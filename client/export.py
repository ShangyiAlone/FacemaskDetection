# coding=utf-8
import sys
import pandas as pd
import warnings
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTableWidget, \
    QTableWidgetItem, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.font_manager as fm
import os

class ExportWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        # 更新 DataFrame 列名
        self.df = pd.DataFrame(data, columns=['ID', '路径', '是否戴口罩', '置信度', '图片中的位置'])

        self.setWindowTitle("数据可视化")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)
        layout.addWidget(self.table)
        self.load_data_to_table()

        self.export_button = QPushButton("输出为Excel")
        self.export_button.clicked.connect(self.export_to_excel)
        layout.addWidget(self.export_button)

        # 水平布局用于平行放置按钮
        button_layout = QHBoxLayout()

        self.bar_chart_button = QPushButton("柱状图")
        self.bar_chart_button.clicked.connect(self.show_bar_chart)
        button_layout.addWidget(self.bar_chart_button)

        self.line_chart_button = QPushButton("折线图")
        self.line_chart_button.clicked.connect(self.show_line_chart)
        button_layout.addWidget(self.line_chart_button)

        self.pie_chart_button = QPushButton("饼图")
        self.pie_chart_button.clicked.connect(self.show_pie_chart)
        button_layout.addWidget(self.pie_chart_button)

        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_data_to_table(self):
        for row_idx, row_data in enumerate(self.data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def export_to_excel(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)", options=options)
        if file_path:
            self.df.to_excel(file_path, index=False)
            print(f"Data exported to {file_path}")

    def show_bar_chart(self):
        self.visualize_window = VisualizeWindow(self.df, 'bar')
        self.visualize_window.show()

    def show_line_chart(self):
        self.visualize_window = VisualizeWindow(self.df, 'line')
        self.visualize_window.show()

    def show_pie_chart(self):
        self.visualize_window = VisualizeWindow(self.df, 'pie')
        self.visualize_window.show()


class VisualizeWindow(QMainWindow):
    def __init__(self, df, chart_type):
        super().__init__()
        self.df = df
        self.chart_type = chart_type
        self.setWindowTitle("数据可视化")
        self.setGeometry(150, 150, 800, 600)

        layout = QVBoxLayout()
        self.label = QLabel(self)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.plot_data()

    def plot_data(self):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # 配置 matplotlib 使用中文字体
        font_path = 'client/SimHei.ttf'  # 请确保这个路径是正确的，指向下载的字体文件
        my_font = fm.FontProperties(fname=font_path)

        if self.chart_type == 'bar':
            ax.bar(self.df['ID'], self.df['置信度'])
            ax.set_title('置信度', fontproperties=my_font)
            ax.set_xlabel('ID', fontproperties=my_font)
            ax.set_ylabel('置信度', fontproperties=my_font)
        elif self.chart_type == 'line':
            ax.plot(self.df['ID'], self.df['置信度'])
            ax.set_title('置信度', fontproperties=my_font)
            ax.set_xlabel('ID', fontproperties=my_font)
            ax.set_ylabel('置信度', fontproperties=my_font)
        elif self.chart_type == 'pie':
            mask_counts = self.df['是否戴口罩'].value_counts()
            ax.pie(mask_counts, labels=mask_counts.index, autopct='%1.1f%%', startangle=90)
            ax.set_title('是否戴口罩的比例', fontproperties=my_font)

        # Save figure to a file
        fig.savefig('plot.png')

        # Display the figure in the QLabel
        pixmap = QPixmap('plot.png')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 示例数据，按照你给定的数据结构
    sample_data = [
        ["item1", "path/to/item1", False, 0.95, "location1"],
        ["item2", "path/to/item2", True, 0.85, "location2"],
        ["item3", "path/to/item3", False, 0.75, "location3"]
    ]
    main_win = ExportWindow(sample_data)
    main_win.show()
    sys.exit(app.exec_())

