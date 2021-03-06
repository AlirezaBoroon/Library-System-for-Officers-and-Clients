# Library System for Officers and Clients
- ***Library Project contains two main codes, one is for Customers(=Cliens) and another is for the Officers.***

## :man_student: / :woman_student:	Customers Program (Customers.py):
- Clients are able to do:
  - View all books of Library
  - Borrow book up to 3 books
    - Borrow based on a keyword (search)
    - View all available books
    - Cancel book Borrow requests
  - Return the Borrowed book
    - Return the book based on index in the borrowed books by this specific user
    - Cancel Return request
  - Reserve a book for future (after being available)
    - Reserve based on a keyword (search)
    - Cancel Reesrve request
  - See all the related Transactions or specific type of them
    - See all related Transactions
    - See Transactions based on type of request
    - See Visulization of all Transactions based on time and activity
  - Change the password
    - The password should be at least 8 digits
<hr>

## :woman_office_worker: / :man_office_worker:	Officers Program (Officers.py):
- Officers are able to do:
  - View all books of Library
    - All books
    - Specific books (search)
  - Mange Users (Customers)
    - Approve Registrations
    - Ban Users
  - Issue Bill for Returning requests
    - If Customer return the book before 20 days, it costs 0.
  - View Borrowing requests
    - Approve requests
    - Reject requests
  - View Returning requests
    - Approve requests
    - Reject requests
  - View Reserving requests
    - Approve requests
    - Reject requests
  - See all Transactions or specific type of them
    - See all related Transactions
    - See Transactions based on type of request
    - See Visulization of all Transactions based on time and activity of the Customers
  - Change the password
    - The password should be at least 8 digits
    
***An Officer Assistant: Notifications system is for checking and informing to the officers for new requests which are in the "Waiting" Status.***

<hr>

## :card_index_dividers:		Customers Data file:
***Customers Data stores in a file which is "Data_Customers.csv".***
***This file has this information:***
  - Username
    - This is for logging in.
  - Encrypted Password
    - The password is encrypted using Affine Cipher.
  - Name
    - This is for displaying.
  - Remaining-requests
    - Every person has 3 requests for borrowing, every borrowing lower it by 1.
  - Book-id#1
    - Every person has borrowed books ids as one of its information.
    - Every book has an id in the list of books.
  - #1 date
    - Every book when is borrowed, has a date of borrowing.
  - Book-id#2
  - #2 date
  - Book-id#3
  - #3 date
  - Status
    - Every Person has a Status in the library:
      - Approved
      - Not Approved
      - Banned
      
      ***Default value is "Not Approved", others are set by officers.***
<hr>

## :card_file_box:			Officers Data file:
***Officers Data stores in a file which is "Data_Officers.csv".***
***This file has this information:***
  - Username
    - This is for logging in.
  - Encrypted Password
    - The password is encrypted using Affine Cipher.
  - Name
    - This is for displaying.
    
***This data stored in this file, are written manually by editing the file.***
<hr>

## :shopping_cart:			Transactions Data file:
***Transactions Data stores in a file which is "Data_Transactions.csv".***
***This file has this information:***
  - Month
    - The Month that transaction is made.
  - Day
    - The Day that transaction is made.
  - Hour
    - The Hour that transaction is made.
  - Minute
    - The Minute that transaction is made.
  - Username
    - Transaction is made by this Username.
  - Book-id
    - Transaction is about this book id.
  - Status
    - Waiting
    - Approved
    - Canceled
    
    ***Default value is "Waiting", for others: "Approved" is set by Officers, "Canceled" is set by the Customer.***
  - Type of request
    - Borrowing
    - Returning
    - Reserving
    
    ***These type of request are based on the request sent by user.***
<hr>

## :books:			Books Data file:
***Books Data stores in a file which is "Data_Books.csv".***
***This file has this information:***
  - Name
    - Book name
  - Author
  - Year
    - Year of publishing
  - Publisher
  - Pages
  - Country
  - Status
    - accessible
    - not accessible
    
    ***A book which is not borrowed, its Status is "accessible", otherwise it's "not accessible".***
  - Reserve-Status
    - reserved
    - not reserved
    
    ***A book which is borrowed can be "reserved" when Customer makes a request for it, otherwise it's "not reserved".***
