import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import sys
import os
import subprocess
from urllib.request import urlopen
import re
import platform


# setup
def wait_for(sec=2):
    time.sleep(sec)

# check if msedge is up to date


url = "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# remove first </h2> because it is not for a version header
html = html.replace("</h2>", "a", 1)

# find <h2> and </h2> of current version header
version_index = html.find("<h2 id=\"version-")
version_index_end = html.find("</h2>")
# version_data contains the header with version
version_data = html[version_index:version_index_end]
# remove everything but the actual text in the header
version_index = version_data.find(">")
version_data = version_data[version_index:]

# find the numbers in the text of the header
msedge_current_version_data = re.findall("\\d+", version_data)
msedge_current_version = ""

# add dots to version (first four numbers found in the text)
for i in range(4):
    if i == 3:
        msedge_current_version += msedge_current_version_data[i]
    else:
        msedge_current_version += msedge_current_version_data[i] + "."

command = 'powershell -command "Get-AppxPackage -Name Microsoft.MicrosoftEdge.Stable | Foreach Version"'
#process = subprocess.run(["powershell", "-command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
msedge_local_version = subprocess.check_output(command).decode("utf-8")

# remove the last 4 characters of the "current version" because the powershell
# command returns \r at the end of the output
for i in range(2):
    msedge_local_version = msedge_local_version[:len(msedge_local_version)-1]

msedge_local_version = str(msedge_local_version)

if msedge_local_version == msedge_current_version:
    print("Microsoft Edge is up to date. Continuing")
else:
    print("Please update Microsoft Edge first. Quitting")
    sys.exit(1)

# download msedge web driver if it hasn't already been
files = os.listdir()
if "msedgedriver.exe" in files:
    pass
else:
    os_architecture = platform.architecture()[0]
    if os_architecture == "64bit":
        subprocess.run('curl -O https://msedgedriver.azureedge.net/' + msedge_current_version + '/edgedriver_win64.zip')
        subprocess.run('powershell -command "expand-archive edgedriver_win64.zip"')
        subprocess.run('powershell -command "move .\\edgedriver_win64\\msedgedriver.exe .\\ "')
    elif os_architecture == "32bit":
        subprocess.run('curl -O https://msedgedriver.azureedge.net/' + msedge_current_version + '/edgedriver_win32.zip')
        subprocess.run('powershell -command "expand-archive edgedriver_win32.zip"')
        subprocess.run('powershell -command "move .\\edgedriver_win32\\msedgedriver.exe .\\ "')

# search and mine points

search_list = [x for x in range(34)]

current_dir = os.getcwd()
driver = webdriver.Edge(service=Service(os.path.join(current_dir, 'msedgedriver.exe')))
url_base = 'http://www.bing.com/search?q='
wait_for(5)

# edge auto-logs in, delay so it can sign in
driver.get('https://bing.com')
wait_for(5)

for s in search_list:    
    try:
        driver.get(url_base + str(s))
    except Exception as e:
        print(e)
    wait_for()

# clean up
driver.close()
sys.exit()