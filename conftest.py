import pytest
import logging
import sys
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib3

# ✅ Disable urllib3 & Selenium warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.ERROR)
logging.getLogger("WDM").setLevel(logging.ERROR)  # WebDriver Manager logs

# ✅ Prevent pytest from showing warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# ✅ Configure Logger as a Fixture
@pytest.fixture(scope="session")
def logger():
    """✅ Setup Logger"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filemode="w",
    )
    return logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver(logger):  # ✅ Pass logger to track WebDriver activity
    """✅ Setup WebDriver with ChromeDriverManager once for all tests."""
    logger.info("🚀 Starting WebDriver Session")
    
    # ✅ Ensure the correct version of ChromeDriver is installed automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    yield driver  # ✅ Keeps browser open for all tests
    driver.quit()  # ✅ Closes browser after ALL tests finish
    logger.info("✅ Browser Closed")
