import pymongo
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DarazScraper:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
            self.client.server_info() 
            self.db = self.client["daraz_db"]
        except pymongo.errors.ServerSelectionTimeoutError:
            print("Error: Unable to connect to MongoDB.")
            exit()
        except Exception as e:
            print(f"MongoDB Connection Error: {e}")
            exit()

    def scrape(self, query, user_email):
        url = f"https://www.daraz.pk/catalog/?q={query}"
        user_collection = f"scraped_data_{user_email.replace('@', '_').replace('.', '_')}"
        collection = self.db[user_collection]

        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(url)
            products = []
            items = driver.find_elements(By.XPATH, './/div[@class="Ms6aG"]')[:10]

            for item in items:
                try:
                    title = item.find_element(By.XPATH, './/div[@class="RfADt"]').text
                    price = item.find_element(By.XPATH, './/span[@class=\"ooOxS\"]').text
                    try:
                        rating = item.find_element(By.XPATH, './/span[contains(@class, "rating")]').text
                    except:
                        rating = "No Rating"
                    try:
                        reviews = item.find_elements(By.XPATH, './/div[@class="mdmmT _32vUv"]').text
                    except:
                        reviews = "No Reviews"

                    products.append({
                        "Product Name": title,
                        "Price": price,
                        "Rating": rating,
                        "Reviews": reviews,
                    })
                except Exception as e:
                    print(f"Error extracting product details: {e}")
                    continue

            if products:
                collection.insert_many(products) 
                print(f"Data saved to MongoDB collection: {user_collection}")
            return products
        finally:
            driver.quit()