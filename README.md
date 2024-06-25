# MSEdgePointsMiner
Mines microsoft edge rewards points

Made from python.
The program will open a new window in microsoft edge. It will then go to bing.com. You should be automatically logged into your microsoft account after a few seconds. If you are not, then click sign in when prompted. You will only earn points if signed in.


The program will search the numbers 0-33 (34 search terms). When I wrote this, the maximum number of points allowed per day from searching (on desktop) was 170, with each search giving you 5 points. It's different now (at least for me) but I'll just leave the code the way it is.

You need to download the MS Edge webdriver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/. Put the exe in the same directory as the python script.

You also need to run:
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

If you want to run the python script without having to use the command line and start a virtual environment every time, create a shortcut in the root directory to venv\Scripts\python.exe. Then when you want to run the script from the GUI, drag it onto the shortcut.