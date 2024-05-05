from selenium import webdriver
service = webdriver.ChromeService(executable_path = r'/home/afnfyz/.local/lib/python3.10/site-packages/splinter/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Example usage: open a website
driver.get('https://www.google.com')
