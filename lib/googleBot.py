'''
Data_Criação: 2020-08-28
Projeto.....: Google Search Bot
Arquivo.....: googleBot.py
Descrição...: módulo de bot para pesquisas no google
Autor.......: Victor Hugo Martins de Oliveira - Morvy
GitHub_User.: Victor-Morvy
Observações.:
- Github link do projeto: https://github.com/Victor-Morvy/googleBot
              ...

Atualizações:
    - 2020-08-27:
        - [R00] Criação do projeto
    - 2020-08-28:
        - [R01] Funções básicas criadas, bot funcionando
        - Obs.: O google detectou ser um bot
    - 2020-08-29:
        - O projeto encontra-se privado para outros usuários no GitHub
    - 2020-08-30:

              ...

Referencias:
    https://pypi.org/project/webdrivermanager
    https://selenium-python.readthedocs.io/
'''

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import random
import os

class GoogleSearchBot():

    def __init__(self, interestLink, searchListArgs, maxPages=10, autoCloseTab=False, maxRandTimeInPage=5, autoCloseBrowser=False):
        self.option = Options()
        self.option.add_argument("--no-sandbox")  # bypass OS security model
        self.option.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        self.option.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.option.add_experimental_option('useAutomationExtension', False)

        #Attributes
        self.msg_error = ""
        #number of page amount (too much pages opened may cause lag)
        self.interestLink = interestLink
        #argument list ["","",""]
        self.searchListArgs = searchListArgs
        #if autoCloseTab is true, the bot will automatically change for new tab and close after you open that
        #False as default
        self.autoCloseTab = autoCloseTab
        #The maximum random time in page will set the time who the bot will "Sleep" in search page
        self.maxRandTimeInPage = maxRandTimeInPage
        self.totalSearchPages = maxPages
        #Auto close the browser when task is finished
        self.autoCloseBrowser = autoCloseBrowser

        # Google open driver and xPaths configs
        self.xPathGoogleNext = '//*[@id="pnnext"]'

    #will open the driver
    def start_driver(self):
        #download and creating webdriver in machine
        self.driver = webdriver.Chrome(options=self.option, executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://www.google.com")

        #set actions object
        self.actions = ActionChains(self.driver)

    #will close the driver
    '''
    def close_driver(self):
        self.driver.close()
    '''

    # set some options of object
    def options(self, interestLink_, searchArgList_, maxPages_=10, autoCloseTab_=False, maxRandTimeInPage_=5, autoCloseBrowser_=False):
        self.interestLink = interestLink_
        self.searchListArgs = searchArgList_
        self.totalSearchPages = maxPages_
        self.autoCloseTab = autoCloseTab_
        self.maxRandTimeInPage = maxRandTimeInPage_
        self.autoCloseBrowser = autoCloseBrowser_

    #get the size of list search arguments
    def get_list_search_args_size(self):
        return len(self.searchListArgs)

    #check if exists next button in the google page
    def _check_next_exists(self):
        try:
            self.driver.find_element_by_xpath(self.xPathGoogleNext)
        except NoSuchElementException as e:
            return False
        return True

    #execute the action "next page"
    def _next_page(self):
        if self._check_next_exists():
            self._link = self.driver.find_element_by_xpath(self.xPathGoogleNext)
            self._link.click()
            return 1
        else:
            return 0

    def execute(self):
        self.start_driver()
        self.openedPages = 0
        print(f"Interest  link: {self.interestLink}")
        print(f"List of arguments: {self.searchListArgs}")  # Debug------------------------------------
        try:

            #for in list of arguments
            for listArgElement in self.searchListArgs:
                print(f"Searching argument: {listArgElement}....") #Debug------------------------------------

                # submit the search in google
                self.input_element = self.driver.find_element_by_name("q")
                self.input_element.clear()
                self.input_element.send_keys(listArgElement)
                self.input_element.submit()

                time.sleep(0.2)

                for i in range(self.totalSearchPages):
                    time.sleep(random.randrange(1, self.maxRandTimeInPage))

                    print(f"page index: {i+1}")# Debug-------------------------------------
                    time.sleep(0.5)
                    try:
                        #get all interest elements to click
                        self.elementsToClick = self.driver.find_elements_by_xpath(
                            f'//*[@id="rso"]//div/div[1]/a[contains(@href,\'{self.interestLink}\')]/div')
                    except SystemError as e:
                        self.msg_error = e
                        print(self.msg_error)
                        pass

                    #for each element found in page
                    for elementToClick in self.elementsToClick:
                        time.sleep(0.1)

                        #save the main tab
                        self.mainTab = self.driver.current_window_handle

                        #Open the link in new tab
                        self.actions.key_down(Keys.LEFT_CONTROL).perform()
                        elementToClick.click()
                        self.openedPages += 1
                        self.actions.key_up(Keys.LEFT_CONTROL).perform()

                        if self.autoCloseTab:
                            #Select new tab, wait run page and close
                            self.driver.switch_to.window(self.driver.window_handles[-1])
                            #time.sleep(0.3)
                            self.driver.close()
                            self.driver.switch_to.window(self.mainTab)

                    if not self._next_page():
                        break

            print(f"Total pages opened: {self.openedPages}")# Debug-------------------------------------

            time.sleep(1.5)

            if self.autoCloseBrowser:
                self.driver.close()

        except (Exception, ValueError, TypeError) as e:
            self.msg_error = e
            print(self.msg_error)
            pass
            #self.driver.close()
