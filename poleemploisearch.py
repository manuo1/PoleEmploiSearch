from html_manager.parser import Parser
from html_manager.request import Request
domain = "https://candidat.pole-emploi.fr" 
# locations = (citycode , distance around)
locations = [
    ('45234','50'),
    ('58086','100'),
    ('18058','100'),
    ('03192','100'),
    ('23147','100'),
    ('41002','100'),
]
#locations = [('45234','50')]
# posted_days can be 1,3,7,14 or 31
posted_days = '7'
base_result_url = "/offres/recherche/detail"
parser = Parser()
request = Request()

def search_url(location):
    """
        build full url with search parameters
    """
    citycode , distance = location
    url = (
        f'/offres/recherche?domaine=M18&emission={posted_days}'
        f'&lieux={citycode}&motsCles=python&offresPartenaires=true'
        f'&rayon={distance}&tri=0&typeContrat=CDI,CDD'
    )
    return url

def show_more_results_link(raw_urls):
    """
        check if there is a URL with "show more results". 
        This means that there are other results not displayed
        return the link to display the other results if it exists
    """
    for link in raw_urls:
        if 'afficherplusderesultats' in link:
            return link
    return None

def location_jobs(location):
    job_urls = []
    url = domain + search_url(location)
    print(f'Recherche des emplois pour {location}')
    # loop as long as there is the display more results button in the page
    while True:
        # get full html
        html_in_page = request.html_in_page(url)
        # get all Hyperlinks in the page
        raw_urls = parser.links_in_html(html_in_page)
        # add link with base_result_url to job_urls if not exist
        job_urls.extend(
            [link for link in raw_urls if base_result_url in link]
        )
        # loop with the show more results link to add next results
        if show_more_results_link(raw_urls):
            url = domain + show_more_results_link(raw_urls)
        else:
            # if no show more results in page => break the loop
            break
    print(f'{len(job_urls)} Emplois trouvés après suppression des doublons\n')    
    return job_urls


def main():
    all_location_jobs = []
    for location in locations:
        for job in location_jobs(location):
            if job not in all_location_jobs:
                all_location_jobs.append(job)

    print(f'{len(all_location_jobs)}Offres trouvées\n')
    
 

if __name__ == '__main__':
    main()