# ARW FOSS Order Management  

This is a Flask Python application using the SQLAlchemy package to handle database interactions. This repository provides code for the application as well as a docker-compose.yml file to spin up a database.  

## Instrucitons for use in development environment
### Setup
1 Download the files from the repository  
2 Download and install Docker and docker-compose  
3 Start the database by running the following command from the terminal:  
`docker-compose -f "db\docker-compose.yml" up -d -build`  
4 Run the script "wsgi.py"
5 Navigate to "http://localhost:5000" on a web browser to open the application.
### Use
- To add products, customers, or vendors: simply click the appropriate link on the navigation bar and enter the queried information. A list of the entered entities is displayed.
- To enter a sales or purchase order: Add the order via the appropriate link and fill out the form. You must choose an existing customer/vendor.
- To add items to a sale or purchase order: Add the item number and quantity on the sale/purchase items page.
- To view the inventory: click the inventory link.

## Configuration
The database configuration is handled in the docker-compose.yml file. The environment variables can be modified to set database login credentials. The app configuration is handled with the config.py and .env files. The secret key and SQLAlchemy URI and settings can be modified there.

## About Version 0.1
This application is under development as a hobby project. The goal is to deliver a useful open-source solution for small businesses looking to manage their order fulfillment and inventory replenishment processes. The current release has an simple web interface and the most basic functionality that I condiser a "working system".
