from selenium import webdriver

# Replace the 'self.driver = webdriver.Firefox()' with the following
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference('network.proxy.http',"127.0.0.1")
profile.set_preference('network.proxy.http_port',"8090")
driver=webdriver.Firefox(profile)
# End of Replacement


driver.get('http://nodegoat.herokuapp.com/login')
driver.close()
