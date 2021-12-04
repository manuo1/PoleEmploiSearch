Simple python script to improve searches on the &quot;Pôle Emploi&quot; site

On the site it is not possible to do a search on several places at the same time, and during separate searches on several places the offers bring out a lot of duplicates.

The script will retrieve the list of advertisements for each location and remove the duplicates.

The site also offers &quot;similar&quot; jobs that don&#39;t even contain the search word in the job, the script will select only jobs that contain the search word in the job description.

Finally, the script opens all the selected offers in the browser.

How to use:

Installation requirements (pip install -r requirements.txt)

Open pole\_emploi\_search.py ​​and customize:

-the search locations &quot;locations&quot;

-Searched words &quot;keywords&quot;

Run pole\_emploi\_search.py

Wait while the search is in progress, a progress bar indicates the progress.

At the end of the search, the offers open in your browser

Thanks :

thanks to beautifulsoup4: https://pypi.org/project/beautifulsoup4/

thanks to tqdm: https://pypi.org/project/tqdm/