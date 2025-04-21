"""
Perform drag and drop using Action Chains concept in this url

https://jqueryui.com/droppable/

"""


#import all necessary requirements

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

#Action Chains

from selenium.webdriver.common.action_chains import ActionChains


#Classes store data and locators

class Data:
    url="https://jqueryui.com/droppable/"

#Locators

class Locators:
    Source_Box="draggable" #ID
    Target_Box="droppable" #ID

class Drag_Drop(Data,Locators):

    def start(self):
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get(Data.url)
            self.driver.maximize_window()
            sleep(5)
            return None
        except (NoSuchElementException,ElementNotVisibleException) as error:
            print("Error",error)


    def drag_and_drop(self):

        try:


            frame_element=self.driver.find_element(By.XPATH,value='//*[@id="content"]/iframe')
            self.driver.switch_to.frame(frame_element)
            sleep(5)
            # creating object for actions chains
            action = ActionChains(self.driver)
            # creating drag and drop function
            source_element=self.driver.find_element(by=By.ID,value=Locators.Source_Box)
            target_element=self.driver.find_element(by=By.ID,value=Locators.Target_Box)
            sleep(5)

            #Perform Drag and Drop
            action.drag_and_drop(source_element,target_element).perform()
            sleep(5)
            print("Successful Drag and Drop")
        except (NoSuchElementException,ElementNotVisibleException) as error:
            print("Error",error)













