import time
import pathlib 
import json
import click
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
#mettre le path de votre chromedriver


def save_data(data,name,folder_path):
    """save data in a specific folder path with the name as argument"""
    try:
        pathlib.Path(folder_path+name).mkdir(parents=True, exist_ok=False)
        images=[]
        images.append(data['image'])
        for e in data['posts']:
            images.append(data['posts'][e]['image'])
        i=0
        for e in images:
            try:
                urllib.request.urlretrieve(e,folder_path+name+"/"+str(i) + '.png')
                i=i+1
                print("succ")
            except:
                i=i+1
                print("errr")
        with open(folder_path+name+"\data.json", "a+", encoding="utf8") as json_file:
            json_file.write("\n")
            json.dump(data, json_file, ensure_ascii=False)
    except:
        print("folder already exists")
        pass


