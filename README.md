# Krack8UIAutomation framework design


----installations-----
'please follow the requirements.txt file for installations' by 
"
cd path/to/your/project
pip install -r requirements.txt
"

pytest= 7.4.3
selenium= 4.11.2
pytest-html 2.0.1
pytest-xdist- 1.31.0
openpyxl-3.0.3 
----------------------
Folder Structure

Krack8UIAutomation
    |
    pageObjects(Package)
    |
    testCases(Package)
    |
    utilities(Package)
    |
    TestData(Folder)
    |
    Configurations(Folder)
    |
    Logs(Folder)
    |
    Screenshots(Folder)
    |
    Reports(Folder)
    |
    Run.bat

To run tests on default browser
 ---pytest -v -s path

To Run tests on desired browser
--pytest -s -v path --browser chrome
--pytest -s -v path --browser firefox

To Run tests on desired browser
--pytest -s -v -n=3 path --browser chrome
--pytest -s -v -n=3 path --browser firefox