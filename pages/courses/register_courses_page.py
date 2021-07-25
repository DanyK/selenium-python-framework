import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = ".//form[@id='search']//input[@placeholder='Search Course']"
    _search_icon = ".//form[@id='search']//button[@class='find-course search-course']"
    _course = "//div[contains(@class,'zen-course-list')]"
    # _all_courses = ""
    _enroll_button = ".//div[@id='zen_cs_desc_with_promo_dynamic']//button[contains(text(),'Enroll in Course')]"
    _cc_num = ".//input[@placeholder='Card Number']"
    _cc_exp = ".//input[@placeholder='MM / YY']"
    _cc_cvv = ".//input[@placeholder='Security Code']"
    _submit_enroll = ".//form[@id='checkout-form']//div[contains(@class,'col-xs-12')]//i[contains(@class," \
                     "'fa fa-arrow-right')] "
    _enroll_error_message = ".//form[@id='checkout-form']//span[contains(text(),'Your card number is incorrect.')]"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_icon, locatorType="xpath")
        time.sleep(2)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        # This frame takes at least 2 seconds to show, it may take more for you
        time.sleep(2)
        # self.switchToFrame(name="__privateStripeFrame3155")  # name of the frame for card number. This won't work
        # across different browsers
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame3157")  # name of the frame for expiry date. This won't work
        # across different browsers
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame3156")  # name of the frame for security code. This won't work
        # across different browsers
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    # This method will wrap all the credit card information (all into one method)
    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    # The arguments of this method are optional because maybe there is an scenario where you just want to click the
    # enroll button without entering the credit card details
    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")  # scroll down to go to payment
        self.enterCreditCardInformation(num, exp, cvv)  # enter credit card info
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
        # result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Buy")
        # return not result
