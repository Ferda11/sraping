import requests
from bs4 import BeautifulSoup
import csv

def scraper(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find("div",class_='lnv-featured-article')

        with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerow(["Titre", "Lien", "Image", "Description"])

            for article in articles:
                title = article.select_one("h2").text.strip()
                link = article.find("a").attrs["href"]
                image = article.find("img").attrs["src"]
                description = article.find("p").text.strip()

            
                print(f"Titre: {title}, Lien: {link}, Image: {image}, Description: {description}")

                
                writer.writerow([title, link, image, description])

        print("Extraction et enregistrement dans le fichier CSV réussis.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    scraper("https://www.lenouvelliste.com/")
