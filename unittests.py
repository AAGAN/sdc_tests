import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from html.parser import HTMLParser
from iFlow_Estimator_inputs import *

j=0
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
    @classmethod
    def setUpClass(inst):
        #start the managed chrome webdriver window
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized --incognito")
        inst.driver = webdriver.Chrome('C:\\Users\\jahmada\\OneDrive - Johnson Controls\\Downloads\\chromedriver.exe',options=options)
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
        time.sleep(10)

        #return to the projects page 
        self.driver.find_element_by_link_text('Projects').click()

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

    @classmethod
    def tearDownClass(inst):
        #delete all the projects for this account
        projectList = inst.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        for _ in range(len(projectList)):
            inst.driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr[1]/td[2]/a[2]/img').click()
            time.sleep(1)
            inst.driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/button').click()

        projectList = inst.driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
        print(len(projectList))
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)