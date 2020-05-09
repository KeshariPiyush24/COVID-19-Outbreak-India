from matplotlib import pyplot as plt
import csv
import re
import replicate
pattern = re.compile(r'[A-Za-z]+,(\d+),(\d+),(\d+),(\d+).*')
with open('data.csv', 'rt') as f:
    f.readline()
    plt.title('Pie Chart Representing overall data')
    pie = pattern.match(f.readline())
    plt.style.use('seaborn-dark')
    plt.pie([pie.group(i) for i in range(2, 5)], autopct='%2.2f%%', labels=['Recovered', 'Deaths', 'Active'], startangle=90, wedgeprops={
        'edgecolor': 'white'})
    plt.rcParams['figure.dpi'] = 100
    plt.tight_layout()
    plt.show()
