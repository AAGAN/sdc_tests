from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from iFlow_Estimator_inputs import *

waitToLoad = 0.5
# for parsing the html, mainly on BOM pages
from html.parser import HTMLParser
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

#start the managed chrome webdriver window
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized --incognito")
driver = webdriver.Chrome('C:\\Users\\jahmada\\OneDrive - Johnson Controls\\Downloads\\chromedriver.exe',options=options)
driver.implicitly_wait(10)
driver.get(server)

# sign in
usernameField = driver.find_element_by_id('fUsername')
usernameField.clear()
usernameField.send_keys(fUsername)
passwordField = driver.find_element_by_id('fPassword')
passwordField.clear()
passwordField.send_keys(fPassword)
passwordField.send_keys(Keys.RETURN)
try:
    cookieButton = driver.find_element_by_link_text('Got it!')
    cookieButton.click()
except:
    print('no cookie question')
loginButton = driver.find_element_by_css_selector('#login > div > div > div > div > div > table > tbody > tr:nth-child(3) > td > a')
loginButton.click()

#Start a new project
projectsPage = driver.current_window_handle
newProjectButton = driver.find_element_by_link_text('New Project')
newProjectButton.click()

#fill the new porject form and submit it
driver.switch_to.window("New Project")
driver.find_element_by_id('cboUnits').send_keys(cboUnits)
projectName = driver.find_element_by_id('projectname')
projectName.clear()
projectName.send_keys(projectname)
systemType = driver.find_element_by_name('cboSystem')
systemType.send_keys(cboSystem)
saveButton = driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button')
saveButton.click()

#switch back to the project page and select the last created project
driver.switch_to.window(projectsPage)
#driver.get('https://www.suppressiondesigncenter.com/fsdc/projects.php')
driver.find_element_by_css_selector('#tProjects > tbody > tr:nth-child(1) > td.minheight > a:nth-child(7)').click()

#System Details page
driver.find_element_by_id('cboBrand').send_keys(cboBrand)
time.sleep(waitToLoad)
driver.find_element_by_id('cboSystype').send_keys(cboSystype)
time.sleep(waitToLoad)
driver.find_element_by_id('cboSysApproval').send_keys(cboSysApproval)
time.sleep(waitToLoad)
driver.find_element_by_id('cboAgenttype').send_keys(cboAgenttype)
time.sleep(waitToLoad)
driver.find_element_by_id('cboDesignStandards').send_keys(cboDesignStandards)
time.sleep(waitToLoad)
driver.find_element_by_id('cboFireClasses').send_keys(cboFireClasses)
time.sleep(waitToLoad)
driver.find_element_by_id('cboReserve').send_keys(cboReserve)
time.sleep(waitToLoad)

minTemp = driver.find_element_by_id('txtMinTemp')
minTemp.clear()
minTemp.send_keys(txtMinTemp)
time.sleep(waitToLoad)

maxTemp = driver.find_element_by_id('txtMaxTemp')
maxTemp.clear()
maxTemp.send_keys(txtMaxTemp)
time.sleep(waitToLoad)

altitude = driver.find_element_by_id('txtAltitude')
altitude.clear()
altitude.send_keys(txtAltitude)
time.sleep(waitToLoad)

pressureChange = driver.find_element_by_id('txtPressureChange')
pressureChange.clear()
pressureChange.send_keys(txtPressureChange)
time.sleep(waitToLoad)

designConcentration = driver.find_element_by_id('txtDesignConcentration')
designConcentration.clear()
designConcentration.send_keys(txtDesignConcentration)
time.sleep(waitToLoad)

driver.find_element_by_id('txtDischargeTime').send_keys(txtDischargeTime)
time.sleep(waitToLoad)
driver.find_element_by_id('cboSystemPressures').send_keys(cboSystemPressures)
time.sleep(waitToLoad)
driver.find_element_by_id('cboContainerApproval').send_keys(cboContainerApproval)
time.sleep(waitToLoad)
driver.find_element_by_id('cboContainerSizes').send_keys(cboContainerSizes)
time.sleep(waitToLoad)
driver.find_element_by_id('cboNozzles').send_keys(cboNozzles)
time.sleep(waitToLoad)
driver.find_element_by_id('cboMulti').send_keys(cboMulti)

#click on save and continue button to go to the hazard management page
driver.find_element_by_css_selector('body > table:nth-child(4) > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(2) > button').click()

#Hazard Management Page (https://www.suppressiondesigncenter.com/fsdc/systems/inert/iflow/hazards.php)
for haz in Hazards:
    driver.find_element_by_link_text('Create Hazard').click()

    hazardManagement = driver.current_window_handle
    
    #switch to the add hazard's window
    driver.switch_to.window('ewindow')

    hazardName = driver.find_element_by_id("hazardname")
    hazardName.clear()
    hazardName.send_keys(haz['hazardname'])

    designConcentration = driver.find_element_by_id('designconcentration')
    designConcentration.clear()
    designConcentration.send_keys(haz['designconcentration'])

    maxpressurechange = driver.find_element_by_id('maxpressurechange')
    maxpressurechange.clear()
    maxpressurechange.send_keys(haz['maxpressurechange'])

    driver.find_element_by_id('cboNozzle').send_keys(haz['cboNozzle'])
    roomExits = driver.find_element_by_id('roomexits')
    roomExits.clear()
    roomExits.send_keys(haz['roomexits'])

    for enc in haz['Enclosures']:
        for key in enc:
            inputField = driver.find_element_by_id(key)
            inputField.clear()
            inputField.send_keys(enc[key])
    
    #save the hazard
    driver.find_element_by_css_selector('body > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > button').click()

    driver.switch_to.window(hazardManagement)

#click on the continue button to go to the hazard review page
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/table[2]/tbody/tr/td/div/table/tbody/tr/td[2]/button').click()

#click on continue to go to System Options page
driver.find_element_by_id('cboContainerSizes').send_keys(cboContainerSizes)
time.sleep(waitToLoad)
driver.find_element_by_id('continue').click()

#system options page
for opt in systemOptions:
    driver.find_element_by_id(opt).send_keys(systemOptions[opt])
    
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/div/table/tbody/tr/td[2]/button').click()

#System BOM
time.sleep(1)
BOMTable = driver.find_element_by_id('BOM')
BOM = driver.find_elements_by_xpath('//*[@id="BOM"]/tbody/tr')
for i in BOM:
    #print(i.get_attribute('innerHTML'))
    #print(strip_tags(i.get_attribute('innerHTML')))
    #print(str(i.get_attribute('innerHTML')))
    print(parser.feed(str(i.get_attribute('innerHTML'))))
    parser.close()
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/div/table[2]/tbody/tr/td/div/table/tbody/tr/td[2]/button').click()

#Nozzle BOM
time.sleep(1)
BOMTable = driver.find_element_by_id('BOM')
BOM = driver.find_elements_by_xpath('//*[@id="BOM"]/tbody/tr')
for i in BOM:
    #print(i.get_attribute('innerHTML'))
    #print(strip_tags(i.get_attribute('innerHTML')))
    #print(str(i.get_attribute('innerHTML')))
    print(parser.feed(str(i.get_attribute('innerHTML'))))
    parser.close()
    
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/div/table[2]/tbody/tr/td/div/table/tbody/tr/td[2]/button').click()

#Vent BOM
driver.find_element_by_id('cboVenttype').send_keys(cboVenttype)
time.sleep(waitToLoad)
BOMTable = driver.find_element_by_id('BOM')
BOM = driver.find_elements_by_xpath('//*[@id="BOM"]/tbody/tr')
for i in BOM:
    #print(i.get_attribute('innerHTML'))
    #print(strip_tags(i.get_attribute('innerHTML')))
    #print(str(i.get_attribute('innerHTML')))
    print(parser.feed(str(i.get_attribute('innerHTML'))))
    parser.close()

driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[1]/div/table[2]/tbody/tr/td/div/table/tbody/tr/td[2]/button').click()

#report page 
time.sleep(1)
BOMTable = driver.find_element_by_id('BOM')
BOM = driver.find_elements_by_xpath('//*[@id="BOM"]/tbody/tr')
for i in BOM:
    #print(i.get_attribute('innerHTML'))
    #print(strip_tags(i.get_attribute('innerHTML')))
    #print(str(i.get_attribute('innerHTML')))
    print(parser.feed(str(i.get_attribute('innerHTML'))))
    parser.close()

#return to the projects page 
driver.find_element_by_link_text('Projects').click()

#delete all the projects for this account
projectList = driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
print(len(projectList))
for i in range(len(projectList)):
    driver.find_element_by_xpath('//*[@id="tProjects"]/tbody/tr[1]/td[2]/a[2]/img').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[2]/button').click()

projectList = driver.find_elements_by_xpath('//*[@id="tProjects"]/tbody/tr')
print(len(projectList))
driver.quit()