# Welcome to Keep it Lean
> A Python Django web app ERP, Enterprise Resource Planning software, for small business owners to manage and track inventory.

## Background
After spending two years at Austin Peay State University, for Supply Chain Management, I spent the breaks in between semesters working at a small metal sign shop. My time was spent in the supply room to help ship products. During my time there, I was able to help eliminate waste by implimenting stations. I realized that this small company needed more and a typical ERP system was out of budget. I sat down with the COO and listened to his issues about what problems the shop faced when it came to inventory management. I took his insight and notes from my study and created an all in one, user friendly ERP, for small businesses. 

## General App Functionality
The following functionalities are part of Keep it Lean:

1. User registration (forked from Steve and Joe over at Nashville Software School - thanks! ;) )
1. User login (forked from Steve and Joe)
1. User logout (forked from Steve and Joe)
1. Business: add, edit, detail, list
1. Users: add, edit, detail, list
1. Products: add, edit, delete, list
1. Manufacturing Process: add, edit, delete, list

## App Flow
This app has 4 goals:
1. Create custom barcodes for products
1. Track orders by scanning barcode 
1. Track orders through color coded indications on 
1. Impliment lean one piece flow methodology to eliminate unecessary waste

Typical flow:

1. Owner creates new business
1. Owner creates order in system using order number and prints custom made barcode
1. Owner is transfered to systems home page to view all orders currently being created
1. Owner can scan order barcode and view order details i.e current order location in warehouse and past location in warehouse
1. Line Manager can process order to next step when complete
1. Owner can mark order as complete once all steps have been finished 


## To Clone
1. Create a directory
1. cd into that directory
1. Clone the repository
1. Start a virtual environment
1. Run `pip install django`
1. Create migrations `python manage.py makemigrations website`
1. Apply migrations to db `python manage.py migrate`
1. run `python manage.py runserver`
1. Open up your browser and navigate to the running server
1. Register, add orders, and track your product orders

## Created by John Nathan Wood
I'm a graduate of [Nashville Software School](http://nashvillesoftwareschool.com/) 
Learn more about me at [johnnathanwood.com](http://www.johnnathanwood.com/)

### Stretch Goals for Future Verisons
- Each department can register a barcode scanner to scan product into next manufacturing step 
- Auto time trials so owner or COO can impliment changes
- Line managers can mark product as defect and owner will get notified 
- Auto update emails sent to customer on where their order is at in its manufacturing process

