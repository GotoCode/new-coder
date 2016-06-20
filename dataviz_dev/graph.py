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
    

def visualize_type():
    '''Visualize data by category as a bar graph'''
    
    parsed_data = parse.parse(MY_FILE, ',')
    
    # create counter-dict mapping 'category -> num_occurrences'
    counter = Counter(item['Category'] for item in parsed_data)
    
    labels = tuple(counter.keys())
    
    xlocations = np.arange(len(labels)) + 0.5
    
    width = 0.5
    
    # plot bars for each y-axis data point
    plt.bar(xlocations, counter.values(), width=width)
    
    # place x-ticks at center of each bar
    plt.xticks(xlocations + width/2, labels, rotation=90)
    
    # make enough space for labels to fit
    plt.subplots_adjust(bottom = 0.4)
    
    # adjust size of entire figure
    plt.rcParams['figure.figsize'] = (12, 8)
    
    plt.savefig('Type.png')
    
    plt.clf()


def main():

    visualize_type()
    visualize_days()
    

if __name__ == '__main__':
    main()
