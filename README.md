# yify-bay-crawler

This piece of code retrieves all the magnet links in `thepiratebay.d4.re` uploaded by the user `YIFY` and stores them in a MySQL database.

## Settings
Rename `settings.py.sample` to `settings.py` and set your own parameters.

## Run
```
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

python ybc.py
```
