from element import BasePageElement
from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect
import datetime
import testconfig
import os

class RMBasePage(object):

    def __init__(self, driver):
        self.driver = driver

class RMPage(RMBasePage):
    def is_title_matches(self,string):
        return string in self.driver.title

    def click_login_button(self):
        vars = testconfig.getVars(self)
        element = self.driver.find_element_by_name('username')
        element.send_keys(vars.username)
        element = self.driver.find_element_by_name('password')
        element.send_keys(vars.password)
        element.submit()

    def click_create_recordsmanagement_button(self):
	vars = testconfig.getVars(self)
        now = datetime.datetime.now()
        today = now.strftime("%H%M%y%m%d")
        sitename = today + ' Site'
        element = self.driver.find_element(*MainPageLocators.MAINMENU_SITES)
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_BUTTON)
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_NAME)
        element.click()
        element.click()
        element = self.driver.find_element_by_name('title')
        element.send_keys(sitename)
        element.click()
        element = self.driver.find_element_by_name('description')
        element.send_keys(today + ' free text description')
        element.click()
        element = self.driver.find_element_by_name('shortName')
        element.send_keys(today)
        element = self.driver.find_element_by_name('sitePreset')
        element.send_keys("R")
        element.click()
        element = self.driver.find_element_by_id('alfresco-rm-createSite-instance-ok-button-button')
        element.click()
        element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')

    def click_rm_tools_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/')
    
    def click_rm_tools_audit_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-audit')
    
    def click_rm_tools_custom_metadata_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-custom-metadata')

    def click_rm_tools_define_roles_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-define-roles')
    
    def click_rm_tools_email_mappings_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-email-mappings')

    def click_rm_tools_events_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-events')
    
    def click_rm_tools_list_of_values_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-list-of-values')
    
    def click_rm_tools_references_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-references')
    
    def click_rm_tools_user_rights_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-user-rights')
    
    def click_rm_tools_user_and_groups_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/rm-console/rm-user-and-groups')
    
    def click_rm_search_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/site/rm/rmsearch')

