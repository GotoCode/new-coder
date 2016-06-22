'''
Code for API  Tutorial from NewCoder.io

Author: GotoCode
'''

from __future__ import print_function

import requests



CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'



class CPIData(object):
    '''
    Abstraction of CPI data provided by FRED
    
    This stores a single value per year
    '''

    def __init__(self):
        # each year available in CPI data is represented as key:value pair
        self.year_cpi   = {}
        
        # these years bound the time-scale of available CPI data
        self.last_year  = None
        self.first_year = None


    def load_from_url(self, url, save_as_file=None):
        '''
        Loads data from a given URL
        
        The downloaded file can also be save into a location
        for later re-use with the 'save_as_file' param
        '''
        
        # keep as little data as possible in memory
        # disable gzip-compression with 'Accept-Encoding' set to 'None'
        fp = requests.get(url, stream=True, headers={'Accept-Encoding' : None}).raw
        
        # if no output file is passed in, return raw data
        if save_as_file is None:

            return self.load_from_file(fp)

        else:
        
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
                    
            with open(save_as_file) as fp:
                return self.load_from_file(fp)
        

    def load_from_file(self, fp):
        '''
        Loads CPI data from a given file-like object
        '''
        
        current_year = None
        year_cpi = []
        
        for line in fp:
            
            # actual data only starts with the line 'DATE'
            while not line.startswith('DATE '):
                pass
            
            # remove newline and tokenize input line
            data = line.strip().split()
            
            # extract year and CPI data for current item
            year = int(data[0].split('-')[0])
            cpi  = float(data[1])
            
            if self.first_year is None:
                self.first_year = year
            
            self.last_year = year
            
            # compute avg CPI for current year
            # once we reach a new year, reset the avg. yearly CPI
            if current_year != year:
            
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                    
                year_cpi = []
                current_year = year
                
            year_cpi.append(cpi)
            
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
            
            
            
    def get_adjusted_price(self, price, year, current_year=None):
        '''
        Returns adapted price from a given year compared
        to what current year has been specified
        '''
        
        if current_year is None or current_year > 2013:
            current_year = 2013
        
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year
        
        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]
        
        return float(price) / year_cpi * current_cpi



def main():
    '''This function handles the main logic of the script'''
    
    # grab CPI/Inflation data
    
    # grab API/game platform data
    
    # Figure out current price for each platform,
    # adjusted for price according to CPI
    
    # generate a plot/bar graph for (adjusted) price data
    
    # generate a CSV for (adjusted) price data

