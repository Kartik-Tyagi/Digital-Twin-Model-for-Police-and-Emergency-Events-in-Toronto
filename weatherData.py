import os
import pandas as pd

# Path to the folders containing the CSV files
folder_paths = [
    "C:/Users/tyagi/Downloads/Toronto Intl A/",
    "C:/Users/tyagi/Downloads/Toronto City Centre/",
    "C:/Users/tyagi/Downloads/Toronto City/",
    "C:/Users/tyagi/Downloads/Toronto North York/",
    "C:/Users/tyagi/Downloads/Toronto Buttonville A/"
]

output_folder = '.'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for i, folder in enumerate(folder_paths):
    all_data = []
    
    # Read the files in order from 2016 to 2021
    years = ['2016', '2017', '2018', '2019', '2020', '2021']
    for year in years:
        file_path = os.path.join(folder, f"{year}.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            all_data.append(df)
        else:
            print("Could not find ", file_path)

    # Combine all the data into one dataframe
    combined_data = pd.concat(all_data, ignore_index=True)
    
    # Save the combined data to a new CSV file
    output_file = os.path.join(output_folder, f'combined_folder_{i + 1}.csv')
    combined_data.to_csv(output_file, index=False)
    print(f"Combined file saved to {output_file}")


ward_df = []
pd_1 = pd.read_csv("./combined_folder_1.csv")
pd_2 = pd_1.copy()
pd_3 = pd.read_csv("./combined_folder_2.csv")
pd_4 = pd.read_csv("./combined_folder_3.csv")
pd_5 = pd.read_csv("./combined_folder_4.csv")
pd_6 = pd_5.copy()
pd_7 = pd_5.copy()
pd_8 = pd_4.copy()
pd_9 = pd_4.copy()
pd_10 = pd_3.copy()
pd_11 = pd_4.copy()
pd_12 = pd_4.copy()
pd_13 = pd_4.copy()
pd_14 = pd_4.copy()
pd_15 = pd_4.copy()
pd_16 = pd_4.copy()
pd_17 = pd.read_csv("./combined_folder_5.csv")
pd_18 = pd_5.copy()
pd_19 = pd_4.copy()
pd_20 = pd_4.copy()
pd_21 = pd_17.copy()
pd_22 = pd_17.copy()
pd_23 = pd_17.copy()
pd_24 = pd_17.copy()
pd_25 = pd_17.copy()
ward_df.append(pd_1)
ward_df.append(pd_2)
ward_df.append(pd_3)
ward_df.append(pd_4)
ward_df.append(pd_5)
ward_df.append(pd_6)
ward_df.append(pd_7)
ward_df.append(pd_8)
ward_df.append(pd_9)
ward_df.append(pd_10)
ward_df.append(pd_11)
ward_df.append(pd_12)
ward_df.append(pd_13)
ward_df.append(pd_14)
ward_df.append(pd_15)
ward_df.append(pd_16)
ward_df.append(pd_17)
ward_df.append(pd_18)
ward_df.append(pd_19)
ward_df.append(pd_20)
ward_df.append(pd_21)
ward_df.append(pd_22)
ward_df.append(pd_23)
ward_df.append(pd_24)
ward_df.append(pd_25)

for i in range(25):
    ward_df[i].insert(0, "Ward", i + 1)

# Combine all the data into one dataframe
final_data = pd.concat(ward_df, ignore_index=True)

#Deleting irrelevant columns
final_data.drop('Longitude (x)', axis=1, inplace=True)
final_data.drop('Latitude (y)', axis=1, inplace=True)
final_data.drop('Station Name', axis=1, inplace=True)
final_data.drop('Climate ID', axis=1, inplace=True)
final_data.drop('Date/Time', axis=1, inplace=True)
final_data.drop('Data Quality', axis=1, inplace=True)
final_data.drop('Max Temp Flag', axis=1, inplace=True)
final_data.drop('Min Temp Flag', axis=1, inplace=True)
final_data.drop('Mean Temp Flag', axis=1, inplace=True)
final_data.drop('Heat Deg Days Flag', axis=1, inplace=True)
final_data.drop('Cool Deg Days Flag', axis=1, inplace=True)
final_data.drop('Total Rain Flag', axis=1, inplace=True)
final_data.drop('Total Snow Flag', axis=1, inplace=True)
final_data.drop('Total Precip Flag', axis=1, inplace=True)
final_data.drop('Snow on Grnd Flag', axis=1, inplace=True)
final_data.drop('Dir of Max Gust Flag', axis=1, inplace=True)
final_data.drop('Spd of Max Gust Flag', axis=1, inplace=True)
final_data.drop('Gust Flag', axis=1, inplace=True)

# Save the combined data to a new CSV file
final_data.to_csv("./weather_data_ward_level.csv", index=False)
print("Combined file saved to weather_data_ward_level.csv")


#import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Set Chrome options
# chrome_options = Options()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--allow-insecure-localhost')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--remote-debugging-port=9222')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
# )

# # Initialize WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Open the webpage
# url = 'https://www.timeanddate.com/weather/canada/toronto/historic'
# driver.get(url)
# time.sleep(5)

# # Find all date links
# date_links = driver.find_elements(By.CSS_SELECTOR, '.weatherLinks a')

# # Filter links for specific years (2016 to 2021)
# target_links = [
#     link for link in date_links 
#     if any(year in link.get_attribute('href') for year in ['2016', '2017', '2018', '2019', '2020', '2021'])
# ]

# all_data = []

# # Loop through filtered links
# for i in range(len(target_links)):
#     try:
#         # Refetch links to avoid stale element exception
#         date_links = driver.find_elements(By.CSS_SELECTOR, '.weatherLinks a')
#         target_links = [
#             link for link in date_links 
#             if any(year in link.get_attribute('href') for year in ['2016', '2017', '2018', '2019', '2020', '2021'])
#         ]

#         link = target_links[i]
#         date_text = link.text
#         print(f"Fetching data for: {date_text}")

#         # Retry mechanism for clicking
#         for _ in range(3):
#             try:
#                 driver.execute_script("arguments[0].click();", link)  # Use JS click
#                 time.sleep(5)
#                 break
#             except Exception as e:
#                 print(f"Retrying click for {date_text} due to error: {e}")
#                 time.sleep(2)

#         # Use BeautifulSoup to parse the table
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         table = soup.find('table', {'id': 'wt-his'})

#         if table:
#             rows = table.find_all('tr')
#             for row in rows:
#                 cols = row.find_all('td')
#                 cols = [col.text.strip() for col in cols]
#                 if cols:
#                     cols.insert(0, date_text)  # Add the date for context
#                     all_data.append(cols)

#     except Exception as e:
#         print(f"Failed to load data for {date_text}: {e}")

# # Close browser
# driver.quit()

# # Save data to a DataFrame and export to Excel
# if all_data:
#     df = pd.DataFrame(all_data, columns=['Date', 'Time', 'Temp', 'Weather', 'Wind', 'Humidity', 'Barometer', 'Visibility'])
#     df.to_excel('weather_data.xlsx', index=False)
#     print("Data saved to weather_data.xlsx")
# else:
#     print("No data was collected.")

# # Base URL pattern (change this based on the actual structure)
# BASE_URL = 'https://www.timeanddate.com/weather/canada/toronto/historic?month={month}&year={year}'

# # Create an empty list to store data
# all_data = []

# # Loop through each year and month
# years = range(2016, 2022)  # 2016 to 2021
# months = range(1, 13)      # January to December

# for year in years:
#     for month in months:
#         url = BASE_URL.format(year=year, month=month)
#         print(f"Fetching data from: {url}")
        
#         try:
#             # Fetch the webpage
#             response = requests.get(url)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Find table (adjust the selector based on the HTML structure)
#             table = soup.find('table', {'id': 'wt-his'})
#             if table:
#                 # Extract table rows
#                 rows = table.find_all('tr')
#                 for row in rows:
#                     cols = row.find_all('td')
#                     cols = [col.text.strip() for col in cols]
#                     if cols:
#                         # Add a year and month column to track the source
#                         cols.insert(0, year)
#                         cols.insert(1, month)
#                         all_data.append(cols)
            
#             # Delay to avoid getting blocked
#             time.sleep(1)
        
#         except Exception as e:
#             print(f"Failed to fetch data from {url}: {e}")

# # Convert the data to a pandas DataFrame
# columns = ['Year', 'Month', 'Day', 'Temperature', 'Precipitation', 'Wind Speed']  # Adjust based on actual table headers
# df = pd.DataFrame(all_data, columns=columns)

# # Save to Excel
# df.to_excel('weather_data.xlsx', index=False)

# print("Data saved to 'weather_data.xlsx'")