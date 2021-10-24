from selenium import webdriver
import time

username = '********************'
password = '********************'

browser = webdriver.Chrome()
browser.get('https://app.datawrapper.de/signin/')
time.sleep(0.25)
browser.find_element_by_css_selector('.button.svelte-wndn5c.svelte-wndn5c').click()
time.sleep(0.25)
browser.find_element_by_id("si-email").send_keys(username)
time.sleep(0.25)
browser.find_element_by_id("si-pwd").send_keys(password)
time.sleep(0.25)
browser.find_element_by_css_selector('.radio, .checkbox').click()
time.sleep(0.25)
browser.find_element_by_css_selector('.button.is-primary').click()
time.sleep(15)

browser.get('https://app.datawrapper.de/table/TeOgp/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/table/TeOgp/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/sGUaJ/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/sGUaJ/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/OBAjs/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/OBAjs/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/a1h4t/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/a1h4t/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/Wgvbt/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/Wgvbt/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/1k5uV/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/1k5uV/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/pJ0XE/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/pJ0XE/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/o0fOu/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/o0fOu/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/')
time.sleep(10)

browser.get('https://scv2pl.github.io/')
time.sleep(25)

browser.get('https://github.com/SCV2PL/SCV2PL.GitHub.IO')
time.sleep(10)

browser.get('https://github.com/SCV2PL/SCV2PL.GitHub.IO/blob/main/selenium_datawrapper.py')

print("All Operations - Successfully!")

#browser.implicitly_wait(10)
