import requests

url = 'https://sci-hub.se/https://ieeexplore.ieee.org/abstract/document/6997491#'

dashboardFile = requests.get(url, allow_redirects=True)

open('d:/dev/projects/new-wave/dashboard.pdf',
     'wb').write(dashboardFile .content)
