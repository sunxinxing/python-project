# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test90():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_90(self):
    self.driver.get("http://pfyhy.demo.xiaoi.com/manager")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("admin")
    self.driver.find_element(By.ID, "captcha").click()
    self.driver.find_element(By.ID, "captcha").send_keys("8355")
    self.driver.find_element(By.ID, "loginButton").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "extdd-3").click()
    self.driver.find_element(By.ID, "ext-gen715").click()
    self.driver.find_element(By.ID, "ext-comp-1078").click()
    self.driver.find_element(By.ID, "ext-comp-1078").send_keys("测试112")
    self.driver.find_element(By.ID, "ext-gen520").click()
    self.driver.find_element(By.ID, "ext-gen483").click()
    self.driver.find_element(By.ID, "ext-comp-1468").click()
    self.driver.find_element(By.ID, "ext-comp-1468").click()
    self.driver.find_element(By.ID, "ext-comp-1468").send_keys("测试112")
    element = self.driver.find_element(By.ID, "ext-gen999")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "ext-comp-1491").send_keys("测试112")
    self.driver.find_element(By.ID, "ext-gen1030").click()
    element = self.driver.find_element(By.ID, "ext-gen1030")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ext-comp-1662 .x-btn-bc").click()
    self.driver.find_element(By.ID, "ext-gen999").click()
    self.driver.find_element(By.ID, "ext-gen999").click()
    element = self.driver.find_element(By.ID, "ext-gen999")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ext-comp-1614 .x-btn-bc").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#ext-comp-1614 .x-btn-bc")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "ext-gen606").click()
    element = self.driver.find_element(By.ID, "ext-gen606")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, "#extdd-55 > .x-tree-ec-icon").click()
    self.driver.find_element(By.ID, "extdd-60").click()
    element = self.driver.find_element(By.ID, "extdd-60")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#extdd-13 > .x-tree-ec-icon").click()
    self.driver.find_element(By.ID, "extdd-15").click()
    self.driver.find_element(By.ID, "extdd-57").click()
    self.driver.find_element(By.ID, "ext-gen479").click()
    self.driver.find_element(By.ID, "ext-comp-1078").click()
    self.driver.find_element(By.ID, "ext-comp-1078").send_keys("测试11-改")
    self.driver.find_element(By.ID, "ext-gen520").click()
    self.driver.find_element(By.ID, "extdd-58").click()
    element = self.driver.find_element(By.ID, "extdd-57")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "extdd-15").click()
    self.driver.find_element(By.ID, "ext-gen481").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ext-comp-1663 .x-btn-mc").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ext-comp-1663 .x-btn-mc").click()
  