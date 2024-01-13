from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Initialize Selenium
driver = webdriver.Firefox()  # Use the browser driver of your choice

# List of inputs to submit
inputs = [ 151262,
    151276,
    151283,
    151288,
    151289,
    151293,
    151298,
    151304,
    151318,
    151445,
    151448,
    151461,
    151534,
    151536,
    151565,
    151569,
    151589,
    151630,
    151634,
    151694,
    151716,
    151732,
    151736,
    151739,
    151746,
    151752,
    151767,
    151771,
    151807,
    151815]  # Replace with your inputs

# URL of the webpage
url = 'https://hscresult.comillaboard.gov.bd/h23/'

# List to store the student names, their corresponding input IDs, and GPAs
students = []

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
    time.sleep(1.75)  # Adjust as needed

    # Extract the student's name
    name_element = driver.find_element(By.CLASS_NAME, 'cap_lt')
    student_name = name_element.text

    # Extract the student's GPA (replace 'actual-class' with the actual class of the element containing the GPA)
    gpa_elements = driver.find_elements(By.CLASS_NAME, 'txt_bold')
    student_gpa = gpa_elements[1].text  # Index 1 corresponds to the second element

    # Add the student name, input ID, and GPA to the list
    students.append((student_name, i, student_gpa))

# Initialize the PDF document
doc = SimpleDocTemplate("students.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
Story = []

# Get the sample style sheet
styles = getSampleStyleSheet()

# Print the list of students, their input IDs, and GPAs
for i, student in enumerate(students):
    Story.append(Paragraph(f"<b>Name: {student[0]}</b>", styles["BodyText"]))
    Story.append(Paragraph(f"ID: {student[1]}", styles["BodyText"]))
    Story.append(Paragraph(f"<b>GPA: {student[2]}</b>", styles["BodyText"]))
    Story.append(Spacer(1, 24))

# Build the PDF document
doc.build(Story)
