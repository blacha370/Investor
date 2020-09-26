from selenium import webdriver
import time


class WebScraper:
    def __init__(self, path):
        self.driver_option = webdriver.ChromeOptions()
        self.driver_option.add_argument('—incognito')
        self.chromedriver_path = path

    def create_driver(self):
        return webdriver.Chrome(executable_path=self.chromedriver_path, options=self.driver_option)

    @staticmethod
    def click_element(browser: webdriver.Chrome, path):
        element = browser.find_element_by_xpath(path)
        element.click()

    def get_most_active_stocks(self, amount):
        browser = self.create_driver()
        browser.get('https://finance.yahoo.com/most-active')
        WebScraper.click_element(
            browser, '//div[@class="actions couple"]//form[@class="consent-form"]//button[@class="btn primary"]')
        for i in range(2):
            WebScraper.click_element(
                browser, '//div[@class="Ovx(a) Ovx(h)--print Ovy(h) "]//table[@class="W(100%)"]//thead//tr//th[5]')
            time.sleep(0.5)
        stocks_symbols = list()
        for i in range(1, amount + 1):
            symbol = browser.find_element_by_xpath('//div[@class="Ovx(a) Ovx(h)--print Ovy(h) "]//table//tbody//tr[' +
                                                   str(i) + ']//td[1]//a')
            stocks_symbols.append(symbol.text)
        browser.quit()
        return stocks_symbols
