from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class WebScraper:
    def __init__(self, path):
        self.driver_option = webdriver.ChromeOptions()
        self.driver_option.add_argument('—incognito')
        self.chromedriver_path = path

    def create_driver(self):
        return webdriver.Chrome(executable_path=self.chromedriver_path, options=self.driver_option)

    @staticmethod
    def get_element(browser: webdriver.Chrome, path, timeout: int = 10):
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located(
            (By.XPATH, path)))
        return browser.find_element_by_xpath(path)

    @staticmethod
    def check_if_element_disappear(browser: webdriver.Chrome, path, timeout: int = 10):
        try:
            WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, path)))
        except TimeoutException:
            pass
        finally:
            return True

    def get_most_active_stocks(self, amount):
        browser = self.create_driver()
        stocks_symbols = list()
        browser.get('https://finance.yahoo.com/most-active')
        cookie_btn = WebScraper.get_element(
            browser, '//div[@class="actions couple"]//form[@class="consent-form"]//button[@class="btn primary"]')
        cookie_btn.click()
        WebScraper.check_if_element_disappear(
            browser, '//div[@class="actions couple"]//form[@class="consent-form"]//button[@class="btn primary"]',
            timeout=1)
        for _ in range(2):
            change_btn = WebScraper.get_element(
                browser, '//div[@class="Ovx(a) Ovx(h)--print Ovy(h) "]//table[@class="W(100%)"]//thead//tr//th[5]')
            change_btn.click()
            WebScraper.check_if_element_disappear(
                browser, '//section[@class="Ta(start) Bxz(bb) Px(20px) Maw($newGridWidth) Bgc($lv2BgColor) Mx(a)]"//div[@class="Pos(a)"',
                timeout=1)

        for i in range(1, amount + 1):
            symbol = WebScraper.get_element(browser,
                                            '//div[@class="Ovx(a) Ovx(h)--print Ovy(h) "]//table//tbody//tr[' +
                                            str(i) + ']//td[1]//a')
            stocks_symbols.append(symbol.text)
        browser.quit()
        return stocks_symbols
