# Library System for Officers and Clients
- ***Library Project contains two main codes, one is for Customers(=Cliens) and another is for the Officers.***

## :man_student: / :woman_student:	Customers Program:
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

## :woman_office_worker: / :man_office_worker:	Officers Program:
- Officers are able to do:
  - View all books of Library
    - All books
    - Specific books (search)
  - Mange Users (Customers)
    - Approve Registerations
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
    
***An Officer Assistant: Notifications system is for checking and inform the officers for new requests which are in the "Waiting" Status.***
