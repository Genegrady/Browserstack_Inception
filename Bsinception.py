from threading import Thread
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from concurrent.futures import ThreadPoolExecutor


BROWSERSTACK_URL = 'https://genegrady_zGMDwK:XY6JqwRAggsPCGXnAkxs@hub-cloud.browserstack.com/wd/hub'

caps = [{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'firefox',
      'browser_version': 'latest',
      'name': 'Parallel Test1', # test name
      'build': 'BStack-[Python] Sample Build' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'Edge',
      'browser_version': 'latest',
      'name': 'Parallel Test2', # test name
      'build': 'BStack-[Python] Sample Build'
      },
      {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'Chrome',
      'browser_version': 'latest',
      'name': 'Parallel Test3', # test name
      'build': 'BStack-[Python] Sample Build'
      },
      {
      'device': 'iPhone 12 Pro',
      'os_browser': '14',
      'real_mobile': 'true',
      'name': 'Parallel Test5',
      'build': 'BStack-[Python] Sample Build'
}]


# driver initialization
def run_session(desired_cap):
    driver = webdriver.Remote(
      command_executor=BROWSERSTACK_URL,
      desired_capabilities=desired_cap)
      # launch URL
    driver.get("https://www.google.com") #locate search location by class name
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Browserstack")
    search.submit()

    browserstack_click = driver.find_element(By.CSS_SELECTOR, 'h3.LC20lb.MBeuO.DKV0Md')
    browserstack_click.click()

    username = "eugene.g+demo@browserstack.com"
    password = "Hey_demo_170"

    google_sign_in =driver.find_element(By.CSS_SELECTOR, "a[title='Sign In']")
    google_sign_in.click()

    user_sign_in = driver.find_element(By.ID, 'user_email_login')
    user_sign_in.send_keys(username)


    password_sign_in = driver.find_element(By.ID, 'user_password')
    password_sign_in.send_keys(password)

    driver.find_element(By.ID, "user_submit").click()
    driver.find_element(By.ID, "live_cross_product_explore").click()
    time.sleep(10)
    quick_launch = driver.find_element(By.CLASS_NAME, "os-section__svg-icon")#Use quick launch to open chrome browser
    quick_launch.click()

    chrome_ninety_six_launch = driver.find_element(By.CSS_SELECTOR, "div[role='presentation'][data-rbd-draggable-id='1960692']")
    chrome_ninety_six_launch.click()

    driver.maximize_window()

    time.sleep(20)

    #Close options

    driver.find_element(By.CSS_SELECTOR, "div.base-tooltip.base-tooltip--direction-top.base-tooltip--type-dark.toolbar__head__icon__tooltip.base-tooltip--align-right").click()
    driver.find_element(By.CLASS_NAME, "spotlight__button").click()
    driver.find_element(By.ID, "skip-local-installation").click()

    #search for Browserstack in google on canvas

    canvas_click = driver.find_element(By.ID, "flashlight-overlay-native")

    action = ActionChains(driver)
    action.move_to_element(canvas_click).perform()
    action.send_keys("Browserstack").perform()
    action.key_down(Keys.ENTER)

    if (driver.title=="BrowserStack - Google Search"):
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
    driver.quit()

#The `ThreadPoolExecutor` function takes `max_workers` as an argument which represents the number of threads in threadpool and execute multiple sessions on each of the thread as and when each session completes execution.
with ThreadPoolExecutor(max_workers=2) as executor:
	executor.map(run_session, caps)