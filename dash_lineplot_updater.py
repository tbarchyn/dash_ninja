# Dash lineplot - simple lineplots of pandas frames
# 22 Sept 2017
# Tom Barchyn
# This is mostly copied from the dash documentation (credit goes to them)

import time
import threading
import pandas as pd
import numpy as np
import os

class dash_updater (threading.Thread):
    def __init__ (self, df, pars):
        '''
        dash updater (this runs continuously to update the dataframe)
        df = the dataframe to update
        pars = the parameter dictionary
        '''
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event ()
        self.df = df
        self.pars = pars
        self.fake_max_row = 100
        return
    
    def run (self):
        '''
        method to run the main loop to update the dataframe
        '''
        while not self.stoprequest.isSet():
            try:
                self.update_df ()
            except:
                pass
            
            time.sleep (self.pars['update_interval'])
        
        return
    
    def update_df (self):
        '''
        method to update the dataframe
        '''
        
        # FAKE UPDATES READING FROM DISK
        df = pd.read_csv (self.pars['filename'])
        self.df = df.ix [0:self.fake_max_row, :]            # chop the df
        self.fake_max_row = self.fake_max_row + 10
        print ('updated to: ' + str (self.fake_max_row))
        return
    
    def join (self):
        '''
        method to set the stop request
        '''
        self.stoprequest.set()
        return
    
