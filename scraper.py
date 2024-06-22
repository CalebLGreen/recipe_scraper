import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.bbc.co.uk/food/recipes/one_pan_halloumi_veggie_49929')
soup = BeautifulSoup(page.content, "html.parser")
all = soup.find(id="main-content")

ingr_section = soup.find("div", class_="recipe-ingredients-wrapper")

# Ensure ingr_section is not None
if ingr_section:
    # Extract the text from each list item
    ingredients = [item.get_text(strip=True) for item in ingr_section.find_all("li", class_="recipe-ingredients__list-item")]

    # Create a DataFrame from the ingredients list
    df = pd.DataFrame(ingredients, columns=["Ingredients"])

    # Print the DataFrame
    print(df)
else:
    print("Ingredients section not found.")

recipe = []
for row in df.iterrows():
    print(row, type(row), len(row))