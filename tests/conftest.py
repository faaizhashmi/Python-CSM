import os
import time
from datetime import datetime
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'
pytest_plugins = [
    'lib.plugins.configuration'
]


@pytest.fixture(scope='session')
def browser(configuration):
    return configuration.get('BROWSER', 'chrome')


@pytest.fixture(scope='session')
def browser_options(configuration):
    return configuration.get('BROWSER_OPTIONS')


@pytest.fixture(scope="module")
def base_selenium(browser, browser_options):
    if browser == 'Chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def login_page(base_selenium):
#     return LoginPage(base_selenium)


# @pytest.fixture(scope="module")
# def login(base_selenium, login_page, configuration):
#     base_selenium.get(configuration.LOGIN_URL)
#     login_page.login(username=configuration.TEST_USER['username'], password=configuration.TEST_USER['password'])
#     merchant_page = MerchantPage(login_page.driver)
#     assert configuration.DASHBOARD_URL in merchant_page.driver.current_url, "Redirection after login is not correct"


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("Setting up a test failed: ", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['base_selenium']
            print("Executing test failed: ", request.node.nodeid)
            take_screenshot(driver, request.node.nodeid)


# make a screenshot with a name of the test, date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    nodeid = nodeid.replace(".py", "")
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    print("Screenshot: " + file_name)
    driver.save_screenshot("screenshots/" + file_name)
