import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ Test Login Function

def test_login(driver, logger):
    main_url = "https://www1.duhs.edu.pk/projects/database/login.php"
    try:
        # ✅ Open DUHS Login Page
        driver.get(main_url)
        logger.info("🔄 Opened DUHS Login Page: %s", main_url)

        # ✅ Enter login credentials
        driver.find_element(By.ID, "cnic").send_keys("33333-3333333-3")
        logger.info("✅ Entered CNIC")

        dob_input = driver.find_element(By.ID, "passwordField")
        driver.execute_script("arguments[0].value = '2003-03-03';", dob_input)
        logger.info("✅ Entered Date of Birth")
        
        driver.find_element(By.ID, "empidField").send_keys("333333")
        logger.info("✅ Entered Employee ID")

        # ✅ Enter Captcha
        element_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/div[4]/font/strong").text
        input_field = driver.find_element(By.ID, "number")
        input_field.send_keys(element_text)

        # ✅ Validate Captcha Input
        assert input_field.get_attribute("value") == element_text, "❌ Captcha Mismatch!"
        logger.info("✅ Captcha entered correctly: %s", element_text)
        
        # ✅ Click "Next"
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "form1"))
        )
        next_button.click()
        logger.info("✅ Clicked 'Signin' Button on Form Login")
          
        # ✅ Enter Google Email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        )
        email_input.send_keys("babar.khan@duhs.edu.pk")
        logger.info("✅ Entered Google Email: babar.khan@duhs.edu.pk")
        
        # ✅ Click "Next"
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        next_button.click()
        logger.info("✅ Clicked 'Next' Button on Google Sign-In")
        
        # ✅ Enter Google Email Password
        password = os.getenv("DUHS_MAIL_PSWD")  # Set this environment variable in your system
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Passwd"))
        )
        password_input.send_keys(password)
        logger.info("✅ Entered Google Password")

        # ✅ Click "Next"
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        next_button.click()
        logger.info("✅ Clicked 'Next' Button on Google Sign-In")

        # ✅ Wait for Redirection to DUHS Dashboard (`index.php`)
        WebDriverWait(driver, 15).until(EC.url_contains("index.php"))
        logger.info("✅ Successfully redirected to DUHS Dashboard: %s", driver.current_url)

        # ✅ Assert the Final Page Title
        expected_title = "DATABASE"
        WebDriverWait(driver, 10).until(EC.title_contains(expected_title))
        assert expected_title in driver.title, f"❌ Redirect Failed! Expected '{expected_title}', got '{driver.title}'"
        logger.info("✅ Verified Correct Page Title: %s", driver.title)
        
    except Exception as e:
        logger.error("❌ An error occurred: %s", str(e))
        raise