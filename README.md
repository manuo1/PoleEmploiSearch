Simple python script to improve searches on the &quot;Pôle Emploi&quot; website
_!! Does not use the API, only on the website and therefore does not need a token !!_

On the website it is not possible to search on several places at the same time, and with separate searches on several places the searches bring out a lot of duplicates.

The script will get the list of jobs for each location and remove the duplicates.

The search on website also results &quot;similar&quot; for jobs that don&#39;t even contain the searched word in the job description, the script will select only jobs that contain the search word in the job description.

Finally, the script opens all the selected offers in the browser.

####How to use:

Instal requirements (pip install -r requirements.txt)

Open pole\_emploi\_search.py ​​and customize:

* Search locations &quot;locations&quot;

* Searched words &quot;keywords&quot;

Run pole\_emploi\_search.py

Wait for the search to finish (progress bar)

At the end of the search, the offers open in your browser

####Thanks :

* [Beautifulsoup 4](https://pypi.org/project/beautifulsoup4/)
* [tqdm](https://pypi.org/project/tqdm/)