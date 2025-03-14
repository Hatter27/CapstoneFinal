Medicine Inventory System for Small Pharmacies

Introduction

The Medicine Inventory System for Small Pharmacies is an offline application developed using Python Flask and SQLite. It is designed to help small pharmacies efficiently manage their medicine inventory, sales, and discounts. The system features role-based access, where new users must be approved by an admin before they can log in. It also includes functionalities such as discount management for senior citizens and PWDs, sales tracking, and inventory monitoring.

Table of Contents

Features

Installation

Usage

Technologies Used

Contact


Features

User Authentication – Secure login and registration system, with admin approval required for new users.

Role-Based Access – Two types of users: Admin and Staff.

Medicine Management – Add, edit, and delete medicines in the inventory.

Manage Discounts – Automatic 20% discount for Senior Citizens and PWDs, with an option for regular customers without a discount.

View Deleted Medicines – Track deleted medicines and restore them if necessary.

View Sales & Revenue – Admin and staff can view all sales transactions and total revenue.

Stock & Expiry Notifications – Alerts for low-stock and near-expiry medicines.

Offline Functionality – The system runs without an internet connection, as it has been converted into a .exe file.


Installation

For Standalone .exe Version:

Download the installer – Obtain the .exe installer file.



Install the application – Click the Medicine Inventory.exe to install



Launch the system – Open the application after installation to start using it.




For Development Version (Source Code):

Clone the repository


git clone https://github.com/Hatter27/CapstoneFinal.git
cd CapstoneFinal


Install required dependencies


pip install -r requirements.txt


Run the Flask server


python app.py


Access the system via browser


http://127.0.0.1:5000



Usage

Logging In

Admin: Has full access, including approving new user registrations.

Staff: Can manage inventory, track sales, and apply discounts.


Using System Features

Add Medicines – Go to "Add Medicine" and input medicine details.

Manage Discounts – In "Manage Discounts", select whether the customer is Regular, Senior Citizen, or PWD to apply the appropriate discount.

Delete & Restore Medicines – In "View Deleted Medicines", users can restore deleted medicines.

Track Sales & Revenue – "View Sales" and "View Revenue" display all transactions and total earnings.

Monitor Stock & Expiry – The system provides alerts for low-stock and expiring medicines.


Technologies Used

Frontend: HTML, CSS, JavaScript, Bootstrap

Backend: Python Flask

Database: SQLite

Standalone Version: Converted to .exe for offline use


Contact

For inquiries or support, feel free to contact us:

Email: nikoaabella13@gmail.com

Location: Cadiz City

Phone: 09504056580
