import webbrowser
from tqdm import tqdm  # progress Bar
from html_manager.parser import Parser
from html_manager.request import Request
domain = "https://candidat.pole-emploi.fr"
# locations = (citycode , distance around (km), name)
# distances around can be 5, 10 , 20, 30, 40, 50, 60, 70, 80, 90, 100
# the citycode must be found in url on the pole emploi site ("lieux=45234")
locations = [
    ('45234', '50', "Orleans (45000)"),
    ('58086', '100', "Cosne Cours Sur Loire (58200)"),
    ('18058', '100', "Chateauneuf Sur Cher (18190)"),
    ('03192', '100', "Nades (03450)"),
    ('23147', '100', "Nouzerolles (23360)"),
    ('41002', '100', "Ange (41400)"),
]
key_words = [
    "python",
    "django",
]
# posted_days can be 1, 3, 7, 14, 31
posted_days = '3'
# links to the offers contain base_result_url
base_result_url = "/offres/recherche/detail"
parser = Parser()
request = Request()


def search_url(location, key_word):
    """
        build full url with search parameters
    """
    citycode, distance, name = location
    url = (
        f'/offres/recherche?domaine=M18&emission={posted_days}'
        f'&lieux={citycode}&motsCles={key_word}&offresPartenaires=true'
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


def location_jobs(location, key_word):
    """
        returns a list of links to the pages of the jobs found
    """
    job_urls = []
    url = domain + search_url(location, key_word)
    print(f'Recherche des emplois \"{key_word}\" pour le lieu : {location}')
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
            # if no show more results button in page => break the loop
            break
    print(f'{len(job_urls)} Emplois trouvés')
    return job_urls


def jobs_containing_the_keyword(all_jobs_link, key_word):
    """
        select all the jobs containing 
        the key_word in the job detail
    """
    my_selection = []
    for job_link in tqdm(all_jobs_link):
        url = domain + job_link
        # get the full html in job detail page
        html_in_page = request.html_in_page(url)
        # select jobs
        if key_word.lower() in html_in_page.lower():
            my_selection.append(url)
    return my_selection


def main():
    my_selection = []
    for key_word in key_words:
        all_jobs_link = []
        for location in locations:
            for job in location_jobs(location, key_word):
                if job not in all_jobs_link:
                    all_jobs_link.append(job)
        print(
            f'{len(all_jobs_link)} Offres trouvées'
            f' (après suppression des doublons)\n'
            f'Recherche des offres dont le détail'
            f' contiennent le mot-clé {key_word}:\n'
        )
        my_selection.extend(
            jobs_containing_the_keyword(all_jobs_link, key_word)
        )
    for url in my_selection:
        webbrowser.open_new_tab(url)


if __name__ == '__main__':
    main()
