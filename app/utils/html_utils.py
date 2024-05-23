from bs4 import BeautifulSoup

def extract_text_from_html(file_content):
    soup = BeautifulSoup(file_content, "html.parser")
    return soup.get_text()