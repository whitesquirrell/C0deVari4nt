import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class NeoWeb():
    def __init__(self) -> None:
        self.browser = webdriver.Chrome("bin/chromedriver.exe")

        self.browser.get("http://localhost:7474")
        # self.browser.implicitly_wait(1)
        time.sleep(2)

        self.login()

        # self.return_all_nodes()


    def login(self):
        user_field = self.browser.find_element_by_xpath("//input[@data-testid='username']")
        pass_field = self.browser.find_element_by_xpath("//input[@data-testid='password']")

        user_field.send_keys("neo4j")
        pass_field.send_keys("codevariant")

        login_form = self.browser.find_element_by_css_selector("form")

        login_form.submit()

        time.sleep(8)


    ## TODO code editor div not interactable and send_keys dont work!!
    def execute_query(self, query: str):
        query_field = self.browser.find_element_by_xpath("//div[@class='view-line']")
        # query_field.click()
        # query_field.send_keys("bruh")

        myElem = WebDriverWait(self.browser, 5000).until(EC.presence_of_element_located((By.XPATH, "//div[@class='view-line']")))
        myElem.send_keys("match")

        # span_class = f'''
        #     <span class="mtk4">match</span>
        #     <span class="mtk15">&nbsp;</span>
        #     <span class="mtk3">(</span>
        #     <span class="mtk15">n</span>
        #     <span class="mtk4">)</span>
        #     <span class="mtk4">&nbsp;</span>
        #     <span class="mtk4">return</span>
        #     <span class="mtk4">&nbsp;n</span>
        # '''
        # self.browser.execute_script(f"arguments[0].innerHTML = '{span_class}'", query_field)

        # code = "let parent = document.querySelector(\"[class='view-line']\").firstChild" \
        #     + ""

        time.sleep(5)

    def return_all_nodes(self):
        self.execute_query("MATCH (n) return n")


    def update_grass(self):
        self.browser.find_element_by_name("DBMS").click()
        self.browser.find_element_by_xpath("//div[contains(text(), '*') and @data-testid='sidebarMetaItem']").click()

        time.sleep(2)
        raw_style = self.browser.execute_script("return window.localStorage.getItem('neo4j.grass');")
        style = json.loads(raw_style)

        print(style["Source"])


if __name__ == "__main__":
    nw = NeoWeb()
    nw.update_grass()
