

def test_find_panda(browser):
    browser.get("https://plugins.jenkins.io/shiningpanda/")
    header_name = browser.find_element_by_xpath("//*[@class='title-wrapper']/h1")
    assert header_name.text == "ShiningPanda"
