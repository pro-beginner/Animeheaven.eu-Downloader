# Animeheaven.eu-Downloader

This is a python script to download anime series from the popular website animeheaven.eu.

Requirments:
* python 3.X
* pip
* bs4      :  pip install bs4
* requests :  pip install requests

now run a command like:
$python AnimeHeavenDownloader.py <the url of the chosen anime> <selected destination> <starting_episode> <ending_episode>
  
Now to get the url, visit http://animeheaven.eu and go to the page of the anime that dispays all the available episodes,
copy the same url:
  for eg:
    for Dragon Ball Super, the url looks like,
      http://animeheaven.eu/i.php?a=Dragon%20Ball%20Super
      
      a sample query would look like,
      $python AnimeHeavenDownloader.py http://animeheaven.eu/i.php?a=Dragon%20Ball%20Super /users/me/Downloads 1 100
     
Note: Our current implementation does not show the exent of download at each instance of time, but keep pateince the download is taking place, successful dowmnload of each episode is notified. 


