import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def logged_in_driver(driver, logger):
    """Logs in the user and returns the driver at the form page."""
    from test_login import test_login  # Import the existing login function
    test_login(driver, logger)  # Run login test to authenticate and Perform login

    # ✅ Ensure login was successful before testing the form
    WebDriverWait(driver, 10).until(EC.url_contains("index.php"))
    return driver # ✅ Reuse the browser session

def test_form_submission(logged_in_driver, logger):
    """Test form functionality after successful login."""
    driver = logged_in_driver # ✅ Already logged in
    driver.get("https://www1.duhs.edu.pk/projects/database/index.php")  # Form Page
    logger.info("🔄 Opened Form Page: %s", driver.current_url)
    
    # ✅ Fill in the form
    input_field = driver.find_element(By.NAME, "name")

    is_readonly = input_field.get_attribute("readonly")

    assert is_readonly is not None, "❌ The field is editable but should be readonly!"
    logger.info("✅ Field is correctly set as readonly.")
    

    # # ✅ Fill in the form fields (Example: Updating profile info)
    # driver.find_element(By.ID, "full_name").send_keys("John Doe")
    # driver.find_element(By.ID, "email").send_keys("john.doe@example.com")

    # # ✅ Click Submit
    # submit_button = driver.find_element(By.ID, "submit_btn")
    # submit_button.click()

    # # ✅ Verify Success Message
    # success_msg = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, "success_message"))
    # ).text

    # assert "Form submitted successfully" in success_msg, "❌ Form submission failed!"
    # print("✅ Form test passed!")