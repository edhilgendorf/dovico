# dovico
## Install dependencies
source environment/bin/activate
pip3 install -r requirements.txt
download, install, and add geckodriver to path:
https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-macos.tar.gz
## Setup YAML
Copy dovico_example.yml to dovico.yml
Edit username, password, company
Set hours as needed. Days can be specified for hours if they differ. If multiple days have the same hour, use default as in example.
## Run script
execute sript: python3 dovico.py
There is a 20 second timer before it will start entering hours, in this time period select the current week you are editing.
### Example Run:
![](dovico_yml.mp4)
