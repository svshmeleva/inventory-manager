# warehouse-stock-manager
Python script to manage warehouse of a shoe shop.

# General information

Current stock data is stored in text file as comma separated values. Following fields are present:
1. Country of origin
2. Product code
3. Product name
4. Cost
5. Quantity

Text UI allows user to do following actions:
1. View details of all items in the warehouse
2. Add new shoes to warehouse
3. Re-stock shoes
4. Search shoes by product code
5. Display total value for items
6. Display information of product with the higest quantity
7. Display information about the most expensive shoes

# Installation

To download the script please clone git repo:
```
  git clone https://github.com/svshmeleva/warehouse-stock-manager.git
```

or download and extract the [zip file](https://github.com/svshmeleva/warehouse-stock-manager/archive/refs/heads/main.zip).

# Usage example
When program starts main menu is displayed
![Screenshot 2023-02-16 221212](https://user-images.githubusercontent.com/120607373/219506575-f35f076b-092d-4f41-bc1d-3c00ea9eef5b.jpg)

View all (choose 1 from main menu) - prints out all data from txt file as table
![Screenshot 2023-02-16 221427](https://user-images.githubusercontent.com/120607373/219506466-59117d28-098f-4966-91ef-7b01f12b22c2.jpg)

Search by code (choose 4 from main menu) gives a menu:
- if choose 'c' finds shoe by code and prints out relevant information in a easy readable view
![Screenshot 2023-02-16 221711](https://user-images.githubusercontent.com/120607373/219506782-2adb863e-3108-4f60-ac58-9d0c094d29fb.jpg)

- if choose 's' prints out for all shoes code for all shoes as a table

![Screenshot 2023-02-16 224242](https://user-images.githubusercontent.com/120607373/219506845-26ff9e65-615b-44a6-9373-11898d2cd66d.jpg)
