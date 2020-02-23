# -*- coding:utf-8 -*-

'''
Scrap google image data for autoencoder training
'''

from selenium import wedriver
import yaml

import time

def read_yaml(path):
    '''
    read the yaml with all the instructions

    return value: dictionnary with the content of the yaml file
    '''
    f = open(path, "r")
    content = yaml.safe_load(f)
    f.close()
    return content

def scrap_one_img(url, path):
    '''
    scrap one image and store it in a specified path

    url: url of the image
    path: where to store the image

    return value: void
    '''
    ## todo

def scrap_all_img(url):
    '''
    url: url of the page to scrap
    '''
    driver = webdriver.Firefox()
    driver.get(url)
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

if __name__ == "__main__":
    ## todo
