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


browser.get('https://app.datawrapper.de/chart/0oa9H/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/0oa9H/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/OY7HS/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/OY7HS/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/chart/sGUaJ/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/sGUaJ/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/lAQGz/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/lAQGz/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/table/NRnYP/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/table/NRnYP/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/table/ql6mK/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/table/ql6mK/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/chart/tQ7B8/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/tQ7B8/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/wRgAt/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/wRgAt/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/chart/quL4r/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/quL4r/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/pI4kl/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/pI4kl/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/map/9FOQh/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/9FOQh/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/hSZ64/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/hSZ64/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/chart/O1Psg/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/O1Psg/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/t4IUb/describe')
time.sleep(10)
browser.get('https://app.datawrapper.de/chart/t4IUb/publish')
time.sleep(10)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/map/8Ntt9/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/8Ntt9/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/jtJr0/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/jtJr0/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/map/No277/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/No277/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/FJtlg/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/FJtlg/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/chart/HyYXt/describe')
time.sleep(15)
browser.get('https://app.datawrapper.de/chart/HyYXt/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/BF3jL/describe')
time.sleep(15)
browser.get('https://app.datawrapper.de/chart/BF3jL/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()


browser.get('https://app.datawrapper.de/chart/qGF2F/describe')
time.sleep(15)
browser.get('https://app.datawrapper.de/chart/qGF2F/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/chart/gRs82/describe')
time.sleep(15)
browser.get('https://app.datawrapper.de/chart/gRs82/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://app.datawrapper.de/map/K8Lky/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/K8Lky/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)

browser.get('https://app.datawrapper.de/map/Il57Q/data')
time.sleep(15)
browser.get('https://app.datawrapper.de/map/Il57Q/publish')
time.sleep(15)
browser.find_element_by_css_selector('.button-wrapper.svelte-di7o7w').click()
time.sleep(10)


browser.get('https://scv2pl.github.io/scv2pl-en')


print("All Operations - Successfully!")

# python3 /home/luke_blue/Startup_Files/selenium_datawrapper.py
# browser.implicitly_wait(10)
