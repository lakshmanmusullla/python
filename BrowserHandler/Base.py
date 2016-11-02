'''
Created on Oct 27, 2016

@author: lakshman.musulla
'''
from selenium import webdriver
import logging
import ConfigParser
from logging.config import *
from logging import handlers
import os
from os import path

class Base(object):
    '''
    classdocs
    This class is used for performing testing on diffrerent browsers
    '''
    logging.config.fileConfig('logging.ini')
    log = logging.getLogger('BaseClass')
    log.debug('Starting ')
    config = ConfigParser.ConfigParser()
    config.read('properties.ini')
    
    
    def __init__(self):
        self.log.info("======= Base Class initialized ==========") 
        
        
    def get_driver(self):
        global driver
        execution_mode = self.config['Browser']['ExecutionMode']
        if execution_mode == "local" or execution_mode == "" or execution_mode is None:
            driver = self.initialize_driver()
        return driver
     
       
    def initialize_driver(self):
        try:
            global driver
            browsername = self.config['Browser']['browserName']
            drivers_folder_path = self.get_drivers_path()
            self.log.info("drivers folder path is:=>"+drivers_folder_path)
            self.log.info("========== initializing browser:=>"+browsername)

            if browsername == "firefox" or browsername == "Firefox" or browsername == "":
                driver = webdriver.Firefox()

            elif browsername == "chrome" or browsername == "Chrome":
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--disable-extensions')
                driver = webdriver.Chrome(self.get_chrome_driver_path(), 0, chrome_options)

            elif browsername == "ie" or browsername == "IE" or browsername == "internetexplorer":
                driver = webdriver.Ie(self.get_ie_driver_path())
            return driver

        except Exception as e:
            self.log.exception(str(e))
            raise e

    def get_drivers_path(self):
        curdir = os.curdir
        drivers_path = path.join(curdir, 'Drivers')
        return drivers_path

    def get_chrome_driver_path(self):
        drivers_path = self.get_drivers_path()
        chrome_driver_path = path.join(drivers_path, 'chromedriver.exe')
        return chrome_driver_path

    def get_ie_driver_path(self):
        drivers_path = self.get_drivers_path()
        ie_driver_path = path.join(drivers_path, 'IEDriverServer.exe')
        return ie_driver_path 
    
    def close_driver(self):
        self.driver.quit()  