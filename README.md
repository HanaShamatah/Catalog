# catalog

This project is a version of [Item Catalog project](https://github.com/HanaShamatah/Item-Catalog), prepared to use it in Linux Server Configuration AWS Lightsail project
to deploy it in Amazon Lightsail Linux Server.  
This repository has all required edits to the [original project](https://github.com/HanaShamatah/Item-Catalog) to run in AWS server:  
- Rename application.py to init.py.
- Edit the path of open functions to full path '/var/www/catalog/catalog/client_secrets.json' instead of 'client_secrets.json'
in init.py.
- Edit database engine source to connect to postgres created database ('postgresql://catalog:catalog@localhost/catalog')
instead of ('sqlite:///clothescategories.db') in init.py, database setup file catalog_database.py, 
and fill data file filldatabase_clothes.py.
- Update client_secrets.py from downloaded json file after adding http://52.59.248.6.xip.io to Authorized Javascript origins 
and update Authorized redirect URIs with http://52.59.248.6.xip.io/gconnect, and http://52.59.248.6.xip.io/login.
- Update Client id to the new one configured in Google console to this project in login.html file.
