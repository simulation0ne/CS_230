# Dashboard for Inventory Management - Web App that manages inventory (Django)

This app was built to manage inventory, specifically the inventory at my current place of employment, Sutton Garten Company.
Sutton Garten has two main inventory items that they sell and rent to customer - Bottles of Gas, and Tubs of Dry Ice.
The Bottles can be different sizes, and can have a large range of gasses inside.  The Tubs are 500 lbs each and can be filled with various types of Dry Ice.

**Depending on how you have your machine set up, you may have to use `python3` of `pip3` in place of the `python` or `pip`, respectively.**

__Prerequisites to run this app:__
* have python 3.6 or greater installed.
* Go to your home directory and use `sudo -H easy_install pip` to install pip __if you have not done so yet__.
* Go to your home directory and us `sudo -H pip install django` to install django __if you have not done so yet__.
* Clone this repo into your desired location on your machine.

__In order to run the app:__
* Navigate through the repo to the `Final` directory.
* Use `python manage.py runserver` to start the server.
* Use your browser to navigate to the specified url the app is running on.

# How the app works
__The App is broken down into three parts:__.

* Sales
* Dashboard
* Warehouse

## Sales

The Sales team are those that are responsible for the majority of managing customers and order tickets.
These are the ones who add new customers to the system, as well as add new orders to those customers.

__In this section you can:__
* View the list of current customers
* Add a new customer to the list of customers
* Select a customer name to view a detailed view of that customer and their orders.
* Select an order in that detail view to see a detailed view of the order.
* Add another order to that customer from the customer detail view.
* Add another order by entering the customer's id number from the main sales screen.

## Dashboard

The Dashboard is meant for management to view how the company's inventory and progress is doing. 
So far it only displays the total inventory items in and out of stock, as well as the orders that have been shipped out.
There is so much I want to add to this in the future, including clicking sections of the progress bars for more dashboard details,
sorting orders by day, and adding other aspects of the company such as employee clock-in and out, main gas tank levels, and more.

__In this section you can:__
* View the amount of tubs in the shop and the amount currently shipped out.
* View the amount of bottles in the shop and the amount currently shipped out.
* View the amount of orders that have been shipped out and the amount waiting to be shipped.

## Warehouse

The Warehouse section is the team responsible for the adding of tubs and bottles to inventory, as well as filling them. 
Once filled, the Warehouse team marks them as full and ready to be shipped in the system. They can also remove tubs and bottles 
from the system if it is necessary. They also ship out orders, and return items to the inventory when they come back from customers.

__In this section you can:__
* Add Tubs and Bottles to the system.
* Update Tubs and Bottles to specify what is in them and what state they are in.
* Ship out orders by attatching tubs and bottles to the correct orders.
* Return orders by returning the items to the system as they come back from customers.
* Remove Tubs or Bottles if the customer has damaged them in an irreversible way.

## That's It!
In the future I would love to add to this, I had such a great time learning everything and building this app.  
And it could be so much better with some more time and effort. Hopefully this will be updated in the future!
