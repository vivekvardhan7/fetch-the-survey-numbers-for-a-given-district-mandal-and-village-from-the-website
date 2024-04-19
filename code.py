import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    # URL of the website
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the drop-down menu for the district
    district_menu = soup.find('select', {'name': 'district'})

    # Find the option for the given district
    district_option = district_menu.find('option', text=district)

    # Repeat the process for the mandal and village
    mandal_menu = soup.find('select', {'name': 'mandal'})
    mandal_option = mandal_menu.find('option', text=mandal)
    village_menu = soup.find('select', {'name': 'village'})
    village_option = village_menu.find('option', text=village)

    # If the district, mandal, and village are all found
    if district_option and mandal_option and village_option:
        # Send a POST request to the website with the selected district, mandal, and village
        data = {'district': district_option['value'], 'mandal': mandal_option['value'], 'village': village_option['value']}
        response = requests.post(url, data=data)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the drop-down menu for the survey numbers
        survey_menu = soup.find('select', {'name': 'survey'})

        # Get all the survey numbers
        survey_numbers = [option.text for option in survey_menu.find_all('option')]

        # Return the survey numbers
        return survey_numbers

    # If the district, mandal, or village is not found
    else:
        return None

# Input your desired district, mandal, and village here
district = "Adilabad"
mandal = "Mancherial"
village = "Kamanpur"
print(get_survey_numbers(district, mandal, village))
