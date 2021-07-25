import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _my_courses = "MY COURSES"
    _user_settings_icon = "//*[@id='navbar-inverse-collapse']//div[@class='dropdown']"

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToUserSettings(self):
        # self.elementClick(locator=self._user_settings_icon, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
