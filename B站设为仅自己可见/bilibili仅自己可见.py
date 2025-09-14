# @Author: 29564
# @Email: yankefa@qq.com
# @FileName: bilibili仅自己可见.py
# @DateTime: 2025/9/13 21:41
# @SoftWare: PyCharm
from scipy.stats import randint
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# 处理 alert 弹窗的关键模块
from selenium.webdriver.common.alert import Alert


import time
import random

class Bilibili:
    url = 'https://member.bilibili.com/platform/upload-manager/article?page={}'
    service = Service(executable_path=r'F:\anaconda3\Scripts\msedgedriver.exe')
    cookies = [
     {"name": "buvid3", "value": "CE0DB76C-F828-B122-1804-4C95856D0C0684662infoc", "domain": ".bilibili.com"},
    {"name": "b_nut", "value": "1728107783", "domain": ".bilibili.com"},
    {"name": "_uuid", "value": "C462EE8D-DF73-C723-B8106-AC96BA4A2F5599754infoc", "domain": ".bilibili.com"},
    {"name": "enable_web_push", "value": "disable", "domain": ".bilibili.com"},
    {"name": "rpdid", "value": "|(YuRlRJR)|0J'u~k)uk)m|R", "domain": ".bilibili.com"},
    {"name": "LIVE_BUVID", "value": "AUTO8217281301171895", "domain": ".bilibili.com"},
    {"name": "hit-dyn-v2", "value": "1", "domain": ".bilibili.com"},
    {"name": "buvid_fp_plain", "value": "undefined", "domain": ".bilibili.com"},
    {"name": "CURRENT_BLACKGAP", "value": "0", "domain": ".bilibili.com"},
        {"name": "is-2022-channel", "value": "1", "domain": ".bilibili.com"},
        {"name": "enable_feed_channel", "value": "ENABLE", "domain": ".bilibili.com"},
        {"name": "DedeUserID", "value": "507937155", "domain": ".bilibili.com"},
        {"name": "DedeUserID__ckMd5", "value": "55a132d765307396", "domain": ".bilibili.com"},
        {"name": "fingerprint", "value": "6bd81dde161de02943cc59ad3f60429d", "domain": ".bilibili.com"},
        {"name": "buvid_fp", "value": "6bd81dde161de02943cc59ad3f60429d", "domain": ".bilibili.com"},
        {"name": "header_theme_version", "value": "OPEN", "domain": ".bilibili.com"},
        {"name": "theme-tip-show", "value": "SHOWED", "domain": ".bilibili.com"},
        {"name": "theme-avatar-tip-show", "value": "SHOWED", "domain": ".bilibili.com"},
        {"name": "CURRENT_QUALITY", "value": "80", "domain": ".bilibili.com"},
        {"name": "buvid4",
         "value": "32B8E43E-E902-D8F2-D8DA-E15EB8931D5484662-024100505-+moX2UEVVHFUapXXr4A5TAM4A3EWy90ftJnWSU2rClcBo+/Q82swPGbB0p15gvoS",
         "domain": ".bilibili.com"},
        {"name": "bili_ticket",
         "value": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTc5MTQ1NzgsImlhdCI6MTc1NzY1NTMxOCwicGx0IjotMX0.Sz8R5z8h_JJ4YSoq7X_cbA4au1tTzQ7zVjljbaJmhbk",
         "domain": ".bilibili.com"},
        {"name": "bili_ticket_expires", "value": "1757914518", "domain": ".bilibili.com"},
        {"name": "PVID", "value": "4", "domain": ".bilibili.com"},
        {"name": "SESSDATA",
         "value": "72a8e035%2C1773322943%2C28570%2A92CjBHsy82p2PzofLvxG6yxINggT7bS8x5g4ib0QPJ4o3iesJQAQJynWB5mWpW_44X7mESVndPVjRrY3MwUFBEaXgzNFpWVzdSN2Noc0hfdFJHRmxXWlpnX0JCN3NrMDhNclpxc2VMNUtLLUN1OS1HUW03aHdRbnNweFU3MVhaWGl0U3JPMURzR2NRIIEC",
         "domain": ".bilibili.com"},
        {"name": "bili_jct", "value": "c0ae3b535f8080bf8f1469e72406cdf2", "domain": ".bilibili.com"},
        {"name": "sid", "value": "57iag7i3", "domain": ".bilibili.com"},
        {"name": "bp_t_offset_507937155", "value": "1112107989466087424", "domain": ".bilibili.com"},
        {"name": "CURRENT_FNVAL", "value": "4048", "domain": ".bilibili.com"},
        {"name": "home_feed_column", "value": "4", "domain": ".bilibili.com"},
        {"name": "browser_resolution", "value": "1370-720", "domain": ".bilibili.com"},
        {"name": "b_lsid", "value": "A9514393_199435B4393", "domain": ".bilibili.com"}
        ]
    browser = webdriver.Edge(service=service)
    browser.maximize_window()

    def __init__(self):

        self.browser.get(self.url.format(1))

        for cookie in self.cookies:
            self.browser.add_cookie(cookie)


    def open_edit(self):
        self.browser.find_element(By.XPATH,"//span[@class='label']/span[@class='des']").click()


    def close_button(self):
        time.sleep(random.uniform(1.5, 2.5))
        try:
            # 等待关闭按钮出现（最多等待10秒）
            close_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='form-item']//div[@class='v-popover']/span[@class='v-popover-close-wrp']"))
            )
            # 点击关闭按钮
            close_button.click()
            print("提示框已关闭")
        except Exception as e:
            print(f"关闭提示框时出错：{e}")

    def open_setting(self):#打开设置
        time.sleep(random.uniform(1.5, 2.5))
        try:
            # 等待关闭按钮出现（最多等待10秒）
            open_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='label']/span[@class='des']"))
            )
            # 点击关闭按钮
            open_button.click()
            print("更多设置已打开")
        except Exception as e:
            print(f"设置打开时出错：{e}")
        #self.browser.find_element(By.XPATH,"//span[@class='label']/span[@class='des']").click()
    def setOnly(self):#点击仅有自己可见
        time.sleep(random.uniform(1.5, 2.5))
        try:
            # 等待关闭按钮出现（最多等待10秒）
            onlymy_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='check-radio-v2-container']/span[@class='check-radio-v2-name'])[2]"))
            )
            # 点击关仅自己可见
            onlymy_button.click()
            print("已点击仅自己可见")
        except Exception as e:
            print(f"打开提示框时出错：{e}")
        # try:
        #     # 等待关闭按钮出现（最多等待10秒）
        #     open_button = WebDriverWait(self.browser, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//span[@class='label']"))
        #     )
        #     # 点击关闭按钮
        #     open_button.click()
        #     print("提示框已打开")
        # except Exception as e:
        #     print(f"关闭提示框时出错：{e}")
        # self.browser.find_element(By.XPATH,"//span[@class='label']/span[@class='des']").click()
    def click_submit(self):
        time.sleep(random.uniform(1.5, 2.5))
        try:
            # 等待关闭按钮出现（最多等待10秒）
            onlymy_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='submit-add']"))
            )
            # 点击关闭按钮
            onlymy_button.click()
            print("点击立即投稿")

        except Exception as e:
            print(f"点击立即投稿时出错：{e}")
    def Backforward(self):
        time.sleep(random.uniform(1.5, 2.5))
        self.browser.back()

        # _alert = self.browser.switch_to.alert()
        # _alert.accept()

        # time.sleep(5)
        # icons = self.browser.find_elements(By.XPATH, "//a[@class='bili-btn']/i[@class='bcc-iconfont bcc-icon-Mediumx']")
        # icons[1].click()

    # def Isalert(self):
    #     try:
    #         # 尝试切换到Alert，若存在则执行确认
    #         alert = self.browser.switch_to.alert
    #         alert.accept()
    #         print("Alert已确认")
    #     except NoAlertPresentException:
    #         # 无Alert时捕获异常，执行后续逻辑
    #         print("当前页面无Alert")
    def main(self):
        time.sleep(random.uniform(1.5, 2.5))
        flag = 1
        for pn in range(1, 23):
            self.browser.get(self.url.format(pn))
            for index in range(0,10):
                time.sleep(random.randint(1,2))
                icons = self.browser.find_elements(By.XPATH, "//a[@class='bili-btn']/i[@class='bcc-iconfont bcc-icon-Mediumx']")
                icons[index].click()

                self.open_setting()
                self.setOnly()
                self.click_submit()
                self.Backforward()






def main():
    bilibili = Bilibili()
    bilibili.main()
if __name__ == '__main__':
    main()
