import requests

from bs4 import BeautifulSoup



# Function to scrape book data

def scrape_books(url):

    # Send a GET request to the webpage

    response = requests.get(url)

   

    # Check if the request was successful

    if response.status_code == 200:

        # Parse the HTML content

        soup = BeautifulSoup(response.content, 'html.parser')

       

        # Find all book containers on the page

        books = soup.find_all('article', class_='product_pod')

       

        # List to store book data

        book_data = []

       

        # Loop through each book and extract data

        for book in books:

            title = book.h3.a['title']  # Book title

            price = book.find('p', class_='price_color').text  # Book price

            availability = book.find('p', class_='instock availability').text.strip()  # Availability

           

            # Append book data to the list

            book_data.append({

                'Title': title,

                'Price': price,

                'Availability': availability

            })

       

        return book_data

    else:

        print(f"Failed to retrieve data from {url}")

        return None



# URL of the page to scrape

url = 'https://books.toscrape.com/'



# Call the scrape_books function

books_info = scrape_books(url)



# Print the scraped data

if books_info:

    for index, book in enumerate(books_info, start=1):

        print(f"Book {index}:")

        print(f"  Title: {book['Title']}")

        print(f"  Price: {book['Price']}")

        print(f"  Availability: {book['Availability']}")

        print()

