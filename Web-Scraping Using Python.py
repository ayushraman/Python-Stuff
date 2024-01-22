import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#This is a Scraping Example to show how to download Multiple Files with Web Scraping, Here I have shown how to download PDFs.

#To change folder name feel free to edit the "Foldername" Element in the Line Below

def download_pdf(url, folder='FolderName'):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        if not os.path.exists(folder):
            os.makedirs(folder)

        pdf_links = soup.find_all('a', href=lambda href: (href and href.endswith('.mp4')))
        for link in pdf_links:
            pdf_url = urljoin(url, link['href'])
            download_path = os.path.join(folder, os.path.basename(pdf_url))

            with open(download_path, 'wb') as pdf_file:
                pdf_response = requests.get(pdf_url)
                pdf_file.write(pdf_response.content)
                print(f"Downloaded: {download_path}")
    else:
        print(f"Error: {response.status_code}")

# Input your Desired site to Scrape in the Url to Scrape Section Below

if __name__ == "__main__":
    url_to_scrape = "URL_to_Scrape"
    download_pdf(url_to_scrape)
