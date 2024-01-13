from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdfkit
import time

# Specify the path to wkhtmltopdf
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

# Initialize Selenium
driver = webdriver.Firefox()  # Use the browser driver of your choice

# List of inputs to submit
inputs = [505208, 505209, 505210, 505211]  # Replace with your inputs

# URL of the webpage
url = 'https://hscresult.bise-ctg.gov.bd/hsc22/23/individual/'

# Iterate over each input
for i in inputs:
    # Open a new tab
    driver.execute_script("window.open('');")

    # Switch to the new tab (assuming it is the last one)
    driver.switch_to.window(driver.window_handles[-1])

    # Load the webpage
    driver.get(url)

    # Find the form input element
    input_element = driver.find_element(By.ID, 'roll')

    # Submit the form
    input_element.send_keys(i)
    input_element.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

    # Extract the student's name (replace 'actual-class' with the actual class of the element containing the name)
    name_element = driver.find_element(By.CLASS_NAME, 'cap_lt')
    student_name = name_element.text

    # Save the page as a PDF
    pdfkit.from_url(driver.current_url, f'{student_name}.pdf', configuration=config)

    # Go back to the original page
    driver.back()

    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

# Close the browser
driver.quit()
