# MSEdgePointsMiner
Mines microsoft edge rewards points

Made from python.
This script will download the necessary files (msedge webdriver), then open a new msedge window and search terms in bing to get you free ms rewards points.

# Usage

Before running the script you need to install the Selenium module:
```
python -m venv venv
.\venv\Scripts\activate
pip install selenium
```

If you want, you can build an .exe to run instead of the .py.
```
pip install pyinstaller
pyinstaller --onefile -w .\msepoints.py
```