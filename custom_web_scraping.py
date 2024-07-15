from autoscraper import AutoScraper
import pandas as pd

custom_url = "https://www.amazon.in/s?k=oppo"

# Loading the file
amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search')

# Get the custom result
result = amazon_scraper.get_result_similar(custom_url, group_by_alias=True)

# Formatting result list
final_result = []
# print(list(result.values())[0])
for i in range(len(list(result.values())[0])):
    try:
        final_result.append({alias: result[alias][i] for alias in result})
    except:
        pass
# print(final_result)

# empty dictionary & custom check list
data = {'Title': [], 'Price': []}
custom_check = ["Amazon's Choice", "Bestseller", "Top Pick", "Best"]

# Populating the dictionary 
for title in final_result:
    # custom check
    if any(title["Title"].startswith(prefix) for prefix in custom_check):
        continue 
    data["Title"].append(title['Title'])
for price in final_result:
    data["Price"].append(price['Price'])
    if len(data["Price"]) == len((data["Title"])):
        break

# Make dataframe from the dictionary and save it
df = pd.DataFrame.from_dict(data)

# Save DataFrame to Excel, overwrite if file exists
df.to_excel("data.xlsx", index=False, engine='openpyxl')

