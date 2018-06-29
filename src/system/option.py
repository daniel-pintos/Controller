from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()

assert opts.headless
brower = Chrome("C:\\chromedriver.exe")
brower.get("http://duckduckgo.com")
brower.fullscreen_window()
