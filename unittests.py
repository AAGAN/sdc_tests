import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from html.parser import HTMLParser
from iFlow_Estimator_inputs import *
 
j=0
runAll = False
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        #for attr in attrs:
        #    print("     attr:", attr)
        pass
        
    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        pass

    def handle_data(self, data):
        global j
        if j==0:
            print('Part Number: ', data)
            j +=1 
        elif j==1:
            print('Quantity: ', data)
            j+=1
        else:
            print('Description: ', data)
            j=0

    def handle_comment(self, data):
        #print("Comment  :", data)
        pass

    def handle_entityref(self, name):
        #c = chr(name2codepoint[name])
        #print("Named ent:", c)
        pass

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        #print("Num ent  :", c)
        pass

    def handle_decl(self, data):
        #print("Decl     :", data)
        pass

parser = MyHTMLParser()

class testSDC(unittest.TestCase):

    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()


    #####Initialize
    @classmethod
    def setUpClass(inst):
        inst.vars = {}
        #start the managed chrome webdriver window
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized --incognito")
        inst.driver = webdriver.Chrome('chromedriver.exe',options=options)
        inst.driver.implicitly_wait(5)
        inst.driver.get(server)

        # sign in
        usernameField = inst.driver.find_element_by_id('fUsername')
        usernameField.clear()
        usernameField.send_keys(fUsername)
        passwordField = inst.driver.find_element_by_id('fPassword')
        passwordField.clear()
        passwordField.send_keys(fPassword)
        
        try:
            inst.driver.find_element_by_link_text('Got it!')
            cookieButton = inst.driver.find_element_by_link_text('Got it!')
            cookieButton.click()
        except:
            print('no cookie question')
        loginButton = inst.driver.find_element_by_css_selector('#login > div > div > div > div > div > table > tbody > tr:nth-child(3) > td > a')
        loginButton.click()

        try:
            inst.driver.find_elements_by_xpath('/html/body/div/table/tbody/tr[4]/td[2]/button[2]').click()
        except:
            print('no TOS page.')

    @unittest.skipIf(runAll == False, "development")
    def test_createInertSIProject(self):
        self.assertEqual(self.driver.current_url, server+'fsdc/projects.php')
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboUnits'] = 'Metric'
        addProjectInfo['projectname'] = 'test_createInertSIProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        self.assertEqual(len(projectList),1)

    def createInertSIProject(self):
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboUnits'] = 'Metric'
        addProjectInfo['projectname'] = 'test_createInertSIProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

    @unittest.skipIf(runAll == False, "development")
    def test_createInertUSProject(self):
        self.assertEqual(self.driver.current_url, server+'fsdc/projects.php')
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboUnits'] = 'US'
        addProjectInfo['projectname'] = 'test_createInertUSProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        self.assertEqual(len(projectList),1)

    def createInertUSProject(self):
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboUnits'] = 'US'
        addProjectInfo['projectname'] = 'test_createInertUSProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

    def createHalocarbonUSProject(self):
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboSystem'] = 'Halocarbon'
        addProjectInfo['cboUnits'] = 'US'
        addProjectInfo['projectname'] = 'test_createHalocarbonUSProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

    def createHalocarbonSIProject(self):
        self.deleteAllProjects()
        addProjectInfo = addProject
        addProjectInfo['cboSystem'] = 'Halocarbon'
        addProjectInfo['cboUnits'] = 'Metric'
        addProjectInfo['projectname'] = 'test_createHalocarbonSIProject'
        projectsPage = self.driver.current_window_handle
        newProjectButton = self.driver.find_element_by_link_text('New Project')
        newProjectButton.click()

        #fill the new porject form and submit it
        self.driver.switch_to.window("New Project")

        #This code deals with cases where some elements are disabled
        for inf in addProject:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(addProject[inf])
                    else:
                        i.send_keys(addProject[inf])
                        time.sleep(waitToLoad)

        saveButton = self.driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
        saveButton.click()

        #switch back to the project page and select the last created project
        self.driver.switch_to.window(projectsPage)

    ##### Testing Acoustic Nozzle

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleInertOrifice_US(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'Orifice', #'iFlow',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '1558',
            'vreceiverdist' : '3',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '70'
        }
        self.createInertUSProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        #print(self.driver.page_source)
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleInertiFlow_US(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'iFlow',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '1558',
            'vreceiverdist' : '3',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '70'
        }
        self.createInertUSProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleSapphire_US(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'Sapphire',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '1558',
            'vreceiverdist' : '3',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '70'
        }
        self.createHalocarbonUSProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleInertOrifice_SI(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'Orifice', #'iFlow',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '20',
            'vreceiverdist' : '1',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '20'
        }
        self.createInertSIProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '0-8',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '0-8',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '0-8',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleInertiFlow_SI(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'iFlow',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '20',
            'vreceiverdist' : '1',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '20'
        }
        self.createInertSIProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - INERT',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '601-900',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    @unittest.skipIf(runAll == False, "development")
    def test_acousticNozzleSapphire_SI(self):
        BOMEnclosure = {
            'vroomname' : 'Enc1',
            'cboHardware' : 'Sapphire',
            'vlength' : '0',
            'vwidth' : '0',
            'vheight' : '0',
            'vvolume' : '20',
            'vreceiverdist' : '1',
            'vtargetpress' : '119',
            'vdatarackcount' : '1',
            'vhumidity' : '82',
            'vpressure' : '0.918',
            'vtemp' : '20'
        }
        self.createHalocarbonSIProject()

        #Expand the project line and click on the "Hydraulic Run Manager"
        self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr/td[1]').click()
        time.sleep(waitToLoad)
        

        self.driver.find_element_by_link_text('Acoustic Nozzle Calculation').click()

        #click on new room button
        roomsPage = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[3]').click()

        self.driver.switch_to.window('ewindow')

        info = BOMEnclosure
        for inf in info:
            elements = self.driver.find_elements_by_name(inf)
            for i in elements:
                if i.is_enabled():
                    if i.get_property('tagName') == 'INPUT':
                        i.clear()
                        i.send_keys(info[inf])
                    else:
                        i.send_keys(info[inf])
                        time.sleep(waitToLoad)

        #Save the room info and return to rooms page
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[5]/div[1]/button[1]').click()
        self.driver.switch_to.window(roomsPage)

        #click on the room 
        self.driver.find_element_by_xpath('//*[@id="tRooms"]/tbody/tr').click()
        time.sleep(1)

        

        Nozzles = [
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - SAPPHIRE',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '2-4',
                'vNozzleCount' : '2'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - SAPPHIRE',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '2-4',
                'vNozzleCount' : '1'
            },
            {
                #'cboRun' , 'NameOfRun',
                'cboNozzType' : '3/4 Acoustic Nozzle - SAPPHIRE',# 'Standard Nozzle - INERT'
                'cboPeakRate' : '2-4',
                'vNozzleCount' : '1'
            }
        ]
        for noz in Nozzles:
            #click on the new button in the Nozzles iFrame
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            #self.driver.find_element_by_xpath('body > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr > td:nth-child(2) > button:nth-child(1)')
            time.sleep(waitToLoad)
            self.driver.switch_to.window('ewindow')
            for inf in noz:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(noz[inf])
                        else:
                            i.send_keys(noz[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/div[4]/div/button[2]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        addMaterial = [
            {
                'cboMaterialLocation' : 'Ceiling',
                'cboMaterialType': 'Energy mineral fiber, 1',
                'vArea': '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Concrete block, painted',
                'vArea' : '123.22'
            },
            {
                'cboMaterialLocation' : 'Wall',
                'cboMaterialType' : 'Plaster, 7/8", lath on studs',
                'vArea' : '276.74'
            },
            {
                'cboMaterialLocation' : 'Floor',
                'cboMaterialType' : 'Floors, concrete or terrazzo',
                'vArea' : '123.22'
            }
        ]
        for material in addMaterial:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id('frameRoom'))
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/button[1]').click()
            time.sleep(2)
            self.driver.switch_to.window('ewindow')
            
            for inf in material:
                elements = self.driver.find_elements_by_name(inf)
                for i in elements:
                    if i.is_enabled():
                        if i.get_property('tagName') == 'INPUT':
                            i.clear()
                            i.send_keys(material[inf])
                        else:
                            i.send_keys(material[inf])
                            time.sleep(waitToLoad)
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[4]/div/button[1]').click()
            time.sleep(waitToLoad)
            self.driver.switch_to.window(roomsPage)            
        

        #click on the calculate button
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/button[6]').click()
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

    #####DevOpsBugs

    #other design standard
    @unittest.skipIf(runAll == False, "development")
    def test_2690(self):
        self.driver.implicitly_wait(2)
        self.createInertSIProject()
        self.vars["window_handles"] = self.driver.window_handles
        self.vars["root"] = self.driver.current_window_handle
        self.driver.find_element(By.CSS_SELECTOR, "#tProjects td:nth-child(3)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Start").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'HYGOOD']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        dropdown = self.driver.find_element(By.ID, "cboSystype")
        time.sleep(waitToLoad)
        dropdown.find_element(By.XPATH, "//option[. = 'iFlow System']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSysApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'LPCB (CE)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboAgenttype").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboAgenttype")
        dropdown.find_element(By.XPATH, "//option[. = 'IG-541 (Inergen)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboAgenttype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'EN 15004']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboFireClasses")
        dropdown.find_element(By.XPATH, "//option[. = 'Surface Class A']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'Other']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        value = self.driver.find_element(By.ID, "txtDesignConcentration").get_attribute("value")
        assert value == "0"
        self.driver.find_element(By.ID, "cboSystemPressures").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystemPressures")
        dropdown.find_element(By.XPATH, "//option[. = '300 bar']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystemPressures").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboContainerApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboContainerApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'TPED']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboContainerApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboMulti").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboMulti")
        dropdown.find_element(By.XPATH, "//option[. = 'Selector Valve']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboMulti").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".swal-button").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(19)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "txtDesignConcentration").send_keys("45")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win9031"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win9031"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("8")
        self.driver.find_element(By.ID, "cWidth").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cWidth").send_keys("8")
        self.driver.find_element(By.ID, "cHeight").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cHeight").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win1265"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win1265"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("7")
        self.driver.find_element(By.ID, "cWidth").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cWidth").send_keys("7")
        self.driver.find_element(By.ID, "cHeight").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cHeight").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboiFlowManifold").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBracketing").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBracketing")
        dropdown.find_element(By.XPATH, "//option[. = 'iFlow 80 L Matrix']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBracketing").click()
        time.sleep(waitToLoad)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(10) td:nth-child(2) > .btn:nth-child(1)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Projects").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > img").click()
        time.sleep(waitToLoad)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div[2]/button").click()
        time.sleep(waitToLoad)
        time.sleep(1)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "New Project").click()
        time.sleep(waitToLoad)
        self.vars["win6927"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win6927"])
        self.driver.find_element(By.ID, "projectname").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "projectname").send_keys("test halocarbon other 2073")
        self.driver.find_element(By.ID, "cboSystem").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystem")
        dropdown.find_element(By.XPATH, "//option[. = 'Halocarbon']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystem").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "#tProjects td:nth-child(3)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Start").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'HYGOOD']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystype")
        dropdown.find_element(By.XPATH, "//option[. = 'Sapphire Plus (70 bar)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSysApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'LPCB (CE)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'EN 15004']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboFireClasses")
        dropdown.find_element(By.XPATH, "//option[. = 'Surface Class A']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'Other']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "txtDesignConcentration").click()
        time.sleep(waitToLoad)
        value = self.driver.find_element(By.ID, "txtDesignConcentration").get_attribute("value")
        assert value == "0"
        self.driver.find_element(By.LINK_TEXT, "Projects").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > img").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, ".swal-button--confirm").click()
        time.sleep(waitToLoad)

    #
    @unittest.skipIf(runAll == True, "development")
    def test_3677(self):
        self.driver.implicitly_wait(2)
        self.createInertSIProject()
        self.vars["window_handles"] = self.driver.window_handles
        self.vars["root"] = self.driver.current_window_handle
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "#tProjects td:nth-child(3)").click()
        time.sleep(waitToLoad)
        WebDriverWait(self.driver, 3000).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Start")))
        self.driver.find_element(By.LINK_TEXT, "Start").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'HYGOOD']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        # self.driver.find_element(By.ID, "cboSystype").click()
        # time.sleep(waitToLoad)
        #dropdown = self.driver.find_element(By.ID, "cboSystype")
        #dropdown.find_element(By.XPATH, "//option[. = 'iFlow System']").click()
        self.driver.find_element_by_id("cboSystype").send_keys('iFlow System')
        # time.sleep(waitToLoad)
        # self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSysApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'LPCB (CE)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboAgenttype").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboAgenttype")
        dropdown.find_element(By.XPATH, "//option[. = 'IG-541 (Inergen)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboAgenttype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'VdS 2380']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboFireClasses")
        dropdown.find_element(By.XPATH, "//option[. = 'Surface Class A']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystemPressures").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystemPressures")
        dropdown.find_element(By.XPATH, "//option[. = '300 bar']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystemPressures").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboContainerApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboContainerApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'TPED']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboContainerApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboMulti").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboMulti")
        dropdown.find_element(By.XPATH, "//option[. = 'Selector Valve']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboMulti").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win5840"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win5840"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("8")
        self.driver.find_element(By.ID, "cWidth").send_keys("8")
        self.driver.find_element(By.ID, "cHeight").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        WebDriverWait(self.driver, 3000).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Create Hazard")))
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win7306"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win7306"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("9")
        self.driver.find_element(By.ID, "cWidth").send_keys("9")
        self.driver.find_element(By.ID, "cHeight").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBracketing").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBracketing")
        dropdown.find_element(By.XPATH, "//option[. = 'iFlow 80 L Matrix']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBracketing").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(10) td:nth-child(2) > .btn:nth-child(1)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Projects").click()
        
    #note on container bank edit
    @unittest.skipIf(runAll == False, "development")
    def test_3520(self):
        self.driver.implicitly_wait(2)
        self.createHalocarbonSIProject()
        self.vars["window_handles"] = self.driver.window_handles
        self.vars["root"] = self.driver.current_window_handle
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "#tProjects td:nth-child(3)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Start").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'ANSUL']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'HYGOOD']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystype")
        dropdown.find_element(By.XPATH, "//option[. = 'Sapphire Plus (70 bar)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSysApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'LPCB (CE)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'EN 15004']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboFireClasses")
        dropdown.find_element(By.XPATH, "//option[. = 'Surface Class A']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "ckSystemManifold").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win3935"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win3935"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("5")
        self.driver.find_element(By.ID, "cWidth").send_keys("5")
        self.driver.find_element(By.ID, "cHeight").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.ID, "cnt").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continuebtn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continuebtn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continuebtn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Runs").click()
        time.sleep(waitToLoad)
        self.vars["win564"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "New Run").click()
        time.sleep(waitToLoad)
        self.vars["win4868"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win4868"])
        self.driver.find_element(By.ID, "runname").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "runname").send_keys("3520_1")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > img").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".dt-button:nth-child(1) > span").click()
        time.sleep(waitToLoad)
        self.vars["win2813"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2813"])
        self.driver.find_element(By.ID, "pct").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "pct").send_keys("100")
        self.driver.find_element(By.ID, "nozzletemp").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "nozzletemp")
        dropdown.find_element(By.XPATH, "//option[. = '360']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "nozzletemp").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        assert self.driver.find_element(By.CSS_SELECTOR, "td > i").text == "NOTE: The length of the section from node point 1 to node point 2 is the length of the siphon tube. The elevation change of this section is not the elevation change or length from the floor to the valve outlet as specified in the manual."
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboMethod").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(5) th").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(5) tr:nth-child(7)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "txtCylQty").clear()
        self.driver.find_element(By.ID, "txtCylQty").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        assert self.driver.find_element(By.CSS_SELECTOR, "td > i").text == "NOTE: The length of the section from node point 1 to node point 2 is the length of the siphon tube. The elevation change of this section is not the elevation change or length from the floor to the valve outlet as specified in the manual."
        self.driver.find_element(By.LINK_TEXT, "Projects").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > img").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, ".swal-button--confirm").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "New Project").click()
        time.sleep(waitToLoad)
        self.vars["win7261"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win7261"])
        self.driver.find_element(By.ID, "cboUnits").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboUnits")
        dropdown.find_element(By.XPATH, "//option[. = 'US']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboUnits").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "projectname").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "projectname").send_keys("3520")
        self.driver.find_element(By.ID, "cboSystem").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystem")
        dropdown.find_element(By.XPATH, "//option[. = 'Halocarbon']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystem").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "#tProjects td:nth-child(3)").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.LINK_TEXT, "Start").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboBrand")
        dropdown.find_element(By.XPATH, "//option[. = 'ANSUL']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboBrand").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSystype")
        dropdown.find_element(By.XPATH, "//option[. = 'Sapphire Plus (70 bar)']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSystype").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboSysApproval")
        dropdown.find_element(By.XPATH, "//option[. = 'UL/FM']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboSysApproval").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboDesignStandards")
        dropdown.find_element(By.XPATH, "//option[. = 'NFPA 2001']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboDesignStandards").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "cboFireClasses")
        dropdown.find_element(By.XPATH, "//option[. = 'Surface Class A']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cboFireClasses").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Create Hazard").click()
        time.sleep(waitToLoad)
        self.vars["win2035"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2035"])
        self.driver.find_element(By.ID, "cLength").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cLength").send_keys("15")
        self.driver.find_element(By.ID, "cWidth").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cWidth").send_keys("15")
        self.driver.find_element(By.ID, "cHeight").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "cHeight").send_keys("8")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td > table > tbody:nth-child(1) td:nth-child(1)").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.ID, "cnt").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continuebtn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "continuebtn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Runs").click()
        time.sleep(waitToLoad)
        self.vars["win4081"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "New Run").click()
        time.sleep(waitToLoad)
        self.vars["win8273"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win8273"])
        self.driver.find_element(By.ID, "runname").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "runname").send_keys("3520_1")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > img").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".dt-button:nth-child(1) > span").click()
        time.sleep(waitToLoad)
        self.vars["win8600"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win8600"])
        self.driver.find_element(By.ID, "nozzletemp").click()
        time.sleep(waitToLoad)
        dropdown = self.driver.find_element(By.ID, "nozzletemp")
        dropdown.find_element(By.XPATH, "//option[. = '360']").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "nozzletemp").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.ID, "pct").send_keys("100")
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .btn").click()
        time.sleep(waitToLoad)
        assert self.driver.find_element(By.CSS_SELECTOR, "td > i").text == "NOTE: The length of the section from node point 1 to node point 2 is the length of the siphon tube. The elevation change of this section is not the elevation change or length from the floor to the valve outlet as specified in the manual."
        self.driver.find_element(By.LINK_TEXT, "Projects").click()
        time.sleep(waitToLoad)

    #####clean up

    def deleteAllProjects(self):
        #self.assertEqual(self.driver.current_url, server+'fsdc/projects.php')
        #delete all the projects for this account
        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        for _ in range(len(projectList)):
            try:
                self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr[1]/td[2]/a[2]/img').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/button').click()
            except:
                print('All projects are deleted!')

        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))

    # @classmethod
    # def tearDownClass(inst):
    #     pass

    def tearDown(self):
        #delete all the projects for this account
        try:
            self.driver.find_element_by_link_text('Projects').click()
        except:
            print("Already on the projects page.")
            self.driver.find_element_by_link_text('My Projects').click()

        time.sleep(2)

        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        for _ in range(len(projectList)):
            try:
                self.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr[1]/td[2]/a[2]/img').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/button').click()
            except:
                print('All projects are deleted!')

        projectList = self.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))

    @classmethod
    def tearDownClass(inst):
        #delete all the projects for this account
        projectList = inst.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        for _ in range(len(projectList)):
            try:
                inst.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr[1]/td[2]/a[2]/img').click()
                time.sleep(2)
                inst.driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/button').click()
            except:
                print('All projects are deleted!')

        projectList = inst.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)