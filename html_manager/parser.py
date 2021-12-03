from bs4 import BeautifulSoup

class Parser(BeautifulSoup):

    def links_in_html(self, html_in_page):
        links = []
        soup = BeautifulSoup(html_in_page, 'html.parser')
        for a_tag in soup.find_all('a'):
            link = str(a_tag.get('href'))
            links.append(link)
        return links 
    
