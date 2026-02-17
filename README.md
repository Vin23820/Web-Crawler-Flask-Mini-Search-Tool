# Web Crawler – Flask Mini Search Tool

This project is a simple web crawler built using Flask. 
It allows users to enter a website URL and search for a keyword within the page content.

# Features

- Fetches website content
- Searches for keyword in paragraph text
- Displays matched results
- Basic error handling

#  Tech Stack

Backend:
- Python 3.11
- Flask 3.0.2
- Requests 2.31.0
- BeautifulSoup 4.12.3
Frontend:
- HTML
- CSS

# Project Structure

flask-web-crawler/
│
├── app.py
├── crawler.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css
# How to Run

1. Install dependencies:
   pip install -r requirements.txt
2. Run:
   python app.py
3. Open:
   http://127.0.0.1:5000/
# Future Improvements

- Crawl multiple pages
- Add pagination
- Add search history
- Improve UI design
# Author

M.Vinay

