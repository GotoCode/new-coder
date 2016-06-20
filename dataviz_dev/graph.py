'''
Part II of the DataViz Tutorial from NewCoder.io

Graphing parsed data using matplotlib
'''

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

import parse


MY_FILE = '../dataviz/data/sample_sfpd_incident_all.csv'


def visualize_days():
    '''Visualize data by day of the week'''
    
    parsed_data = parse.parse(MY_FILE, ',')
    
    counter = Counter(item['DayOfWeek'] for item in parsed_data)
    
    data_list = [
                    counter['Monday'],
                    counter['Tuesday'],
                    counter['Wednesday'],
                    counter['Thursday'],
                    counter['Friday'],
                    counter['Saturday'],
                    counter['Sunday']
                ]
    
    day_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    
    plt.plot(data_list)
    
    plt.xticks(range(len(day_tuple)), day_tuple)
    
    plt.savefig('Days.png')
    
    plt.clf()


def main():
    visualize_days()
    

if __name__ == '__main__':
    main()
