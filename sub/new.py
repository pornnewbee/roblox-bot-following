from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re  
from selenium.webdriver.firefox.options import Options  

# 代理服务器地址
proxy = "127.0.0.1:7897"

# 固定用户名和密码
putUsername = "UN111068676"
putPassword = "Tg112211"

# 默认使用 Firefox 浏览器
print("Ok. Starting Firefox with Proxy... ")
firefox_options = Options()
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.http", "127.0.0.1")
firefox_options.set_preference("network.proxy.http_port", 7897)
firefox_options.set_preference("network.proxy.ssl", "127.0.0.1")
firefox_options.set_preference("network.proxy.ssl_port", 7897)

browser = webdriver.Firefox(options=firefox_options)  

try:
    # 访问 Roblox 登录页面
    print("Logging in... ")
    browser.get("https://roblox.com/login")

    # 等待输入框加载
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
    username = browser.find_element(By.ID, "login-username")
    password = browser.find_element(By.ID, "login-password")

    # 输入用户名和密码
    username.send_keys(putUsername)
    password.send_keys(putPassword)

    # 点击登录按钮
    loginBtn = browser.find_element(By.ID, "login-button")
    loginBtn.click()

    # 等待登录完成
    time.sleep(10)

    # 开始循环随机关注用户
    while True:
        # 生成随机用户 ID
        idRandom = random.randint(1500000001, 8162450098)
        print(f"Checking user with ID: {idRandom}")

        # 访问用户页面
        browser.get(f"https://roblox.com/users/{idRandom}")

        try:
            # 检测是否是 404 页面
            error_element = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@class='error-title']"))
            )
            if "Page cannot be found or no longer exists" in error_element.text:
                print(f"User {idRandom} does not exist (404). Skipping to next user.")
                continue
        except:
            pass  

        try:
            # 等待 "Add Friend" 按钮加载完毕
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'web-blox-css-tss-1283320-Button-textContainer') and text()='Add Friend']"))
            )

            # 获取好友数
            friend_count_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='profile-header-social-counts']/li[1]/a/span/b"))
            )

            # 提取好友数
            match = re.search(r"\d+", friend_count_element.text)
            friend_count = int(match.group()) if match else 0

            print(f"User {idRandom} has {friend_count} friends.")

            # 如果好友数小于 50，则跳过该用户
            if friend_count < 50:
                print("Skipping user due to insufficient friends.")
                continue

            # 点击 "More" 按钮
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More']"))
            ).click()

            # 等待并点击 "Follow" 按钮
            followUser = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li[.//span[text()='Follow']]"))
            )
            followUser.click()
            print(f"FOLLOWED user {idRandom}! Moving to next random ID...")

        except Exception as e:
            print(f"Could not process user {idRandom}. Error: {e}")

        # 等待 3 秒后执行下一个操作
        time.sleep(3)

except Exception as e:
    print(f"Critical error: {e}")

finally:
    # 关闭浏览器，释放资源
    if browser:
        browser.quit()
