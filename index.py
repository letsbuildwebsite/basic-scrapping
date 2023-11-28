import csv
from bs4 import BeautifulSoup

# Read the HTML content
with open('input.html', 'r') as html_file:
    html_content = html_file.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all company sections
company_sections = soup.find_all('div', class_='plant_info')

# Prepare headers for CSV file
headers = ['Company', 'Industry', 'Location','address', 'Phone', 'Tier', 'Activeness', 'Status', 'Account Manager', 'Business Developer']

# Initialize rows
rows = []

# Extract data for each company
for section in company_sections:
    # Extract company name
    company_name = section.find_previous('h1').text.strip()
    
    # Extract industry
    industry = section.find_previous('h2').text.strip()
    
    # Extract location
    location = section.find_previous('h3').text.strip()
    
    # Extract address
    address = section.find_all('div')[0].find('span', class_='plant_info_content').text.strip()
    
    # Extract phone
    phone = section.find_all('div')[1].find('span', class_='plant_info_content').text.strip()
    
    # Extract tier
    tier = section.find_all('div')[2].find_next('span', class_='plant_info_content').text.strip()
    
    # Extract activeness
    activeness = section.find_all('div')[3].find_next('span', class_='plant_info_content').text.strip()
    
    # Extract status
    status = section.find_all('div')[4].find_next('span', class_='plant_info_content').text.strip()
    
    # Extract account manager
    account_manager  = section.find_all('div')[5].find_next('span', class_='plant_info_content').text.strip()
    
    # Extract business developer
    business_developer = section.find_all('div')[6].find_next('span', class_='plant_info_content').text.strip()
    
    # Create a row for the company
    row = [
        company_name,
        industry,
        location,
        address,
        phone,
        tier,
        activeness,
        status,
        account_manager,
        business_developer
    ]
    
    # Add row to the list of rows
    rows.append(row)

# Save data to CSV file
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    writer.writerows(rows)