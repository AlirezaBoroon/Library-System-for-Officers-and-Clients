# This program is for Officers of the Library.
# You can test the project with running these two programs (Officers.py & Customers.py)
# *Notice: Please change every address of each file in the code to prevent the directory Error.

class Person:
    def __init__(self, Username, Password):
        self.u= Username
        self.p= Password
class Officer (Person):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)
        self.u= Username
        self.p= Password
    def Get_Name(self):
        Officers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Officers.csv")
        Oname= Officers_Data.loc[Officers_Data.Username == self.u, "Name"].values.tolist()
        return Oname[0]
    def Log_in(self):
        Officers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Officers.csv")# every time when we want to read, it is suggested that we have to read the data again, because sometimes the code uses the old data.
        Uvalidornot= Officers_Data["Encrypted password"].where(Officers_Data['Username']== self.u).values.tolist()
        for i in range(0, len(Uvalidornot)):
            qa= isinstance(Uvalidornot[i], str)
            if qa== True:
                ciphpass= Uvalidornot[i]
                break
        else:
            # else in python after a loop has a good application, if loop was not broke with break command, the else will be executed.
            return False
        passwordstocheck= Password(self.p)
        Pvalidornot= passwordstocheck.Check(ciphpass)
        if Pvalidornot== True:
            return True
        else:
            return False
    def Changing_Passwords(self):
        newpassobj= Password(self.p)
        newcipheredPass= newpassobj.Encrypt()
        Officers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Officers.csv")
        Officers_Data.loc[Officers_Data.Username == self.u, "Encrypted password"]= newcipheredPass
        Officers_Data= Officers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Officers.csv', index=False)
        return True
    def Managing_Users():
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        print("1: All Users\n2: Search for a User")
        while True:
            mchoice= int(input())
            if mchoice== 1:
                cm= 1
                break
            elif mchoice== 2:
                cm= 2
                break
        if cm== 1:
            print(Customers_Data)
            if Customers_Data.empty== True:
                print("The specific list is empty.")
                return False
        elif cm== 2:
            Customers_DataU= Customers_Data['Username'].tolist()
            print("Please enter your keyword:")
            Word= input()
            search_in_users_ideces= []
            for i in range(0, len(Customers_DataU)):
                if Word in Customers_DataU[i]: 
                    search_in_users_ideces.append(i)     
            userswithword= Customers_Data.iloc[search_in_users_ideces] 
            print(userswithword)
            if userswithword.empty== True:
                print("The specific list is empty.")
                return False
        print("\nPlease enter the index of user:")
        user_i= int(input())
        print("1: Approve user\n2: Ban user\n3: Do nothing.")
        while True:
            muchoice= int(input())
            if muchoice== 1:
                Customers_Data.loc[Customers_Data.index == user_i, "Status"]= "Approved"
                Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
                print("The Approved Status has been set for the user.")
                break
            elif muchoice== 2:
                Customers_Data.loc[Customers_Data.index == user_i, "Status"]= "Banned"
                Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
                print("The Banned Status has been set for the user.")
                break
            elif muchoice== 3:
                print("-------")
                break
        return True
    def Issue_Bill(user, timel):
        from datetime import datetime
        monthnow= int(datetime.now().strftime('%m'))
        daynow= int(datetime.now().strftime('%d'))
        otime= timel[0]
        monthold= ''
        for i in range(0, len(otime)):
            if otime[i]!= '-':
                monthold= monthold+ otime[i]
            else:
                flag= i
                break
        dayold= ''
        for i in range(flag+ 1, len(otime)):
            dayold= dayold+ otime[i]
        differentday= int(daynow)- int(dayold)
        if differentday< 0:
            differentday= -differentday
        print("This is the Bill for the user", user, "return request:\n ••••")
        if int(monthnow)== int(monthold):
            if differentday> 20:
                if differentday<= 7:
                    cost= differentday* 2
                    print("The Bill costs", cost, "because the customer returned the book about one week late, for", differentday, "days.")
                else:
                    firstcost= 7* 2
                    secondcost= (differentday-7)* 5
                    tcost= firstcost+ secondcost
                    print("The Bill costs", tcost, "because the customer returned the book more than one week late, for", differentday, "days.")
            else:
                print("The Bill costs 0, because the customer returned the book on time.\n")
        else:
            months= int(monthnow)- int(monthold)
            days= (months* 30)- differentday
            # 30 is a default value for days of month.
            firstcost= 7* 2
            secondcost= (days-7)* 5
            tcost= firstcost+ secondcost
            print("The Bill costs", tcost, "because the customer returned the book more than one week late, for", days, "days.")
        return True
    def Get_WaitingsBorrR():
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        relat_transc= Transactions_Data[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Borrowing")]
        RforBBorr= Transactions_Data.loc[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Borrowing"), "Book-id"].unique().tolist()
        print("All Waiting-Borrowing transactions are as follows:\n")
        print(relat_transc)
        print("\nHint: The indeces of transactions are the numbers behind them.\n\n")
        if len(RforBBorr)== 0:
            return False
        elif len(RforBBorr)== 1:
            print("And the related book to these transactions is:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBBorr)
            print(gettingbook)
            return True
        else:
            print("And the related books to these transactions are:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBBorr)
            print(gettingbook)
            return True
    def Get_WaitingsReturnR():
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        relat_transc= Transactions_Data[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Returning")]
        RforBReturn= Transactions_Data.loc[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Returning"), "Book-id"].unique().tolist()
        print("All Waiting-Returning transactions are as follows:\n")
        print(relat_transc)
        print("\nHint: The indeces of transactions are the numbers behind them.\n\n")
        if len(RforBReturn)== 0:
            return False
        elif len(RforBReturn)== 1:
            print("And the related book to these transactions is:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBReturn)
            print(gettingbook)
            return True
        else:
            print("And the related books to these transactions are:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBReturn)
            print(gettingbook)
            return True
    def Get_WaitingsReserveR():
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        relat_transc= Transactions_Data[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Reserving")]
        RforBReserve= Transactions_Data.loc[(Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Reserving"), "Book-id"].unique().tolist()
        print("All Waiting-Reserving transactions are as follows:\n")
        print(relat_transc)
        print("\nHint: The indeces of transactions are the numbers behind them.\n\n")
        if len(RforBReserve)== 0:
            return False
        elif len(RforBReserve)== 1:
            print("And the related book to these transactions is:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBReserve)
            print(gettingbook)
            return True
        else:
            print("And the related books to these transactions are:\n")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBReserve)
            print(gettingbook)
            return True
    def Rejecting_Borr(listofindeces):
        # for rejecting requests of borrowing
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Rejected"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Rejecting Borrowing request has been done successfully.")
        return True
    def Approving_Borr(listofindeces):
        # approving Borrowing reqs by officers.
        import math
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            u= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Username"].values.tolist()[0]
            if math.isnan(Customers_Data.loc[Customers_Data.Username == u, "Book-id#1"]):
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                j= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Book-id"].tolist()[0]
                Books_Data.loc[Books_Data.index == int(j), "Status"]= 'not accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#1"]= j
                tmonth= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Month"].tolist()[0]
                tday= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Day"].tolist()[0]
                date= str(tmonth)+ '-'+ str(tday)
                Customers_Data.loc[Customers_Data.Username == u, "#1 date"]= date
                if (Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"].values.tolist()[0]> 0):
                    Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]- 1
                    print("Approving Borrowing request has been done successfully.")
            elif math.isnan(Customers_Data.loc[Customers_Data.Username == u, "Book-id#2"]):
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                j= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Book-id"].tolist()[0]
                Books_Data.loc[Books_Data.index == int(j), "Status"]= 'not accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#2"]= j
                tmonth= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Month"].tolist()[0]
                tday= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Day"].tolist()[0]
                date= str(tmonth)+ '-'+ str(tday)
                Customers_Data.loc[Customers_Data.Username == u, "#2 date"]= date
                if (Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"].values.tolist()[0]> 0):
                    Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]- 1
                    print("Approving Borrowing request has been done successfully.")
            elif math.isnan(Customers_Data.loc[Customers_Data.Username == u, "Book-id#3"]):
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                j= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Book-id"].tolist()[0]
                Books_Data.loc[Books_Data.index == int(j), "Status"]= 'not accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#3"]= j
                tmonth= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Month"].tolist()[0]
                tday= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Day"].tolist()[0]
                date= str(tmonth)+ '-'+ str(tday)
                Customers_Data.loc[Customers_Data.Username == u, "#3 date"]= date
                if (Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"].values.tolist()[0]> 0):
                    Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]- 1
                    print("Approving Borrowing request has been done successfully.")
            else:
                print("The User doesn't have enough remaining-requests.")
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Rejected"
                return False
        Customers_Data= Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
        Books_Data= Books_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv', index=False)
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        return True
    def Rejecting_Return(listofindeces):
        # reject returning requests
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Rejected"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Rejecting Returning request has been done successfully.")
        return True
    def Approving_Return(listofindeces):
        import math
        import pandas as pd
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        tt= []
        # Here actually just one request will be approved.
        for i in range(0, len(listofindeces)):
            u= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Username"].values.tolist()[0]
            j= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Book-id"].values.tolist()
            if len(j)== 0:
                print("The Transaction does not exist!.")
                return False
            if Customers_Data.loc[Customers_Data.Username == u, "Book-id#1"].values.tolist()[0]== j[0]:
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                Books_Data.loc[Books_Data.index == int(j[0]), "Status"]= 'accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#1"]= math.nan
                tt.append(Customers_Data.loc[Customers_Data.Username == u, "#1 date"].values.tolist()[0])
                Customers_Data.loc[Customers_Data.Username == u, "#1 date"]= math.nan
                Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]+ 1
                print("Approving Returning request has been done successfully.")
            elif Customers_Data.loc[Customers_Data.Username == u, "Book-id#2"].values.tolist()[0]== j[0]:
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                Books_Data.loc[Books_Data.index == int(j[0]), "Status"]= 'accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#2"]= math.nan
                tt.append(Customers_Data.loc[Customers_Data.Username == u, "#2 date"].values.tolist()[0])
                Customers_Data.loc[Customers_Data.Username == u, "#2 date"]= math.nan
                Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]+ 1
                print("Approving Borrowing request has been done successfully.")
            elif Customers_Data.loc[Customers_Data.Username == u, "Book-id#3"].values.tolist()[0]== j[0]:
                Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
                Books_Data.loc[Books_Data.index == int(j[0]), "Status"]= 'accessible'
                Customers_Data.loc[Customers_Data.Username == u, "Book-id#3"]= math.nan
                tt.append(Customers_Data.loc[Customers_Data.Username == u, "#3 date"].values.tolist()[0])
                Customers_Data.loc[Customers_Data.Username == u, "#3 date"]= math.nan
                Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]= Customers_Data.loc[Customers_Data.Username == u, "Remaining-requests"]+ 1
                print("Approving Borrowing request has been done successfully.")
        # Notice: after all the processes of above are done!(not just one of them) then we apply changes for all the storages.
        Customers_Data= Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
        Books_Data= Books_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv', index=False)
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        Officer.Issue_Bill(u, tt)
        return True
    def Rejecting_Reserve(listofindeces):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Rejected"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Rejecting Reserving request has been done successfully.")
    def Approving_Reserve(listofindeces):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        for i in range(0, len(listofindeces)):
            j= Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Book-id"].tolist()[0]
            Books_Data.loc[Books_Data.index == int(j), "Reserve-Status"]= 'reserved'
            Transactions_Data.loc[Transactions_Data.index == listofindeces[i], "Status"]= "Approved"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        Books_Data= Books_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv', index=False)
        print("Approving Reserving request has been done successfully.")
        return True
class Password:
    def __init__(self, String):
        self.s= String
    def Check(self, Encrypted_pass):
        alphabet= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "|", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "[", "]", "{", "}", "å", ";", ":", "\"", ",", ".", "/", "<", ">", "?", "£", "¢", "€", "¥", "∞", "§", "¶", "™", "©", "®", "º", "≠", "≈", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        strL= list(self.s)
        dceo= open("C:/Users/A.M.Brn/Desktop/Course Project/CODE/¢OHah.]z€a.txt", "r")
        b= int(dceo.readline())
        a= int(dceo.readline())
        strL2indeces= []
        for i in range (0, len(strL)):
            for j in range (0, len(alphabet)):
                if alphabet[j]== strL[i]:
                    strL2indeces.append(j)
        converted_numeric_list= []
        for i in range (0, len(strL2indeces)):
            n= (a*strL2indeces[i])+b
            while n> 100:
                n= n- 101
            converted_numeric_list.append(n)
        converted_letter_list= []
        for i in range (0, len(converted_numeric_list)):
            converted_letter_list.append(alphabet[converted_numeric_list[i]])
        encrypted_string= ""
        for i in range (0, len(converted_letter_list)):
            encrypted_string+= converted_letter_list[i]
        if encrypted_string== Encrypted_pass:
            return True
        else:
            return False
    def Encrypt(self):
        alphabet= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "|", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "[", "]", "{", "}", "å", ";", ":", "\"", ",", ".", "/", "<", ">", "?", "£", "¢", "€", "¥", "∞", "§", "¶", "™", "©", "®", "º", "≠", "≈", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        strL= list(self.s)
        dceo = open("C:/Users/A.M.Brn/Desktop/Course Project/CODE/¢OHah.]z€a.txt", "r")
        b= int(dceo.readline())
        a= int(dceo.readline())
        strL2indeces= []
        for i in range (0, len(strL)):
            for j in range (0, len(alphabet)):
                if alphabet[j]== strL[i]:
                    strL2indeces.append(j)
        converted_numeric_list= []
        for i in range (0, len(strL2indeces)):
            n= (a*strL2indeces[i])+b
            while n> 100:
                n= n- 101
            converted_numeric_list.append(n)
        converted_letter_list= []
        for i in range (0, len(converted_numeric_list)):
            converted_letter_list.append(alphabet[converted_numeric_list[i]])
        encrypted_string= ""
        for i in range (0, len(converted_letter_list)):
            encrypted_string+= converted_letter_list[i]
        return encrypted_string
class Books_Manager:
    def __init__(self, Index):
        self.i= Index
    def Getting_All():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        print(Books_Data)
        return True
    def Getting_viaIndeces(listofindeces):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        BookswithIndc= Books_Data.iloc[listofindeces]
        return BookswithIndc
    def Searching(Word):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        BooksNames= Books_Data['Name'].tolist()
        searchinbooksideces= []
        for i in range(0, len(BooksNames)):
            if Word in BooksNames[i]: 
                searchinbooksideces.append(i)     
        bookswithword= Books_Data.iloc[searchinbooksideces] 
        print(bookswithword)
    def AddNewBook():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        print("Adding a New Book to the library:")
        print("Please enter: Book name")
        book_name= input()
        print("Enter: Author")
        book_author= input()
        print("Enter: Year")
        book_year= input()
        print("Enter: Publisher")
        book_publisher= input()
        print("Enter: Pages")
        book_pages= input()
        print("Enter: Country")
        book_country= input()
        print("Is the book accessible? 1: Yes / 0: No")
        while True:
            choice= input()
            if choice== '1':
                book_accessible= 'accessible'
                break
            elif choice== '0':
                book_accessible= 'not accessible'
                break
        new_book= {'Name':book_name, 'Author':book_author,'Year':book_year,'Publisher':book_publisher,'Pages':book_pages, 'Country':book_country, 'Status': book_accessible, 'Reserve-Status':'not reserved'}
        Books_Data= Books_Data.append(new_book, ignore_index = True)
        Books_Data= Books_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv', index=False)
        print("Done, The book has been added.\n")
        return True
class Transaction(Officer):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)
        self.u= Username
        self.p= Password
    def All_Transc():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        related_t= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(related_t)):# this is for converting book id to the name of the books of books dataframe.
            j= related_t.loc[related_t.index == i, "Book-id"]
            book_name= Books_Data.loc[Books_Data.index == int(j), "Name"].values.tolist()[0]
            related_t.loc[related_t.index == i, "Book-id"]= book_name
        related_t.rename(columns = {'Book-id':'Book'}, inplace = True)# converting book-id column with Book, after changing the values of column book-id.
        print(related_t)
        return True
    def Trascn_based_on_Type(ttype):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        related_t_ty= Transactions_Data[(Transactions_Data["Type of request"]== ttype)]
        print("Transactions list based on", ttype, "is:")
        print(related_t_ty)
        return True
    def Visulizing_All_Transc():
        # officers can easily see the transactions visually.
        import matplotlib.pyplot as plt
        from datetime import datetime
        month= datetime.now().strftime('%m')
        related_t= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        ys= []
        xs= []
        for i in range(1, int(month)+1):
            for j in range(1, 32):
                if related_t[(related_t["Month"]== i) & (related_t["Day"]== j)].count().tolist()[0]!= 0:
                    ys.append(related_t[(related_t["Month"]== i) & (related_t["Day"]== j)].count().tolist()[0])
                    xs.append("%d/%d" %(i, j))
        plt.title('Transactions Visualization for days')
        plt.xlabel('Days of all activities')
        plt.ylabel('Occurations')
        plt.plot(xs, ys, color='black', linestyle='dashed', linewidth = 3,
                marker='o', markerfacecolor='green', markersize=12)
        plt.grid()
        plt.plot(xs, ys, 'o')
        plt.show()
        print("The chart which was showed is the visualization of customers activity based on days.")
        return True
def Notifications_Sys():
    import time
    from playsound import playsound
    # for playing sound
    nflag= 0
    while True:
        import pandas as pd
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        indeces= Transactions_Data[(Transactions_Data['Status'] == 'Waiting')].index.tolist()
        borrs= 0
        retus= 0
        resvs= 0
        if len(indeces)> nflag:
            playsound("C:/Users/A.M.Brn/Desktop/Course Project/CODE/elegant-notification-sound.mp3")
            for i in range(0, len(indeces)):
                if (Transactions_Data.loc[Transactions_Data.index == indeces[i], "Type of request"]== "Borrowing").bool():
                    borrs+= 1
                    nflag+= 1
                if (Transactions_Data.loc[Transactions_Data.index == indeces[i], "Type of request"]== "Returning").bool():
                    retus+= 1
                    nflag+= 1
                if (Transactions_Data.loc[Transactions_Data.index == indeces[i], "Type of request"]== "Reserving").bool():
                    resvs+= 1
                    nflag+= 1
        if borrs> 0:
            print("*Notification:", borrs, "number of new Borrowing request(s).")
        if retus> 0:
            print("*Notification:", retus, "number of new Returning request(s).")
        if resvs> 0:
            print("*Notification:", resvs, "number of new Reserving request(s).")
        time.sleep(1)
        # checks every 1 second.
def main_fun(): 
    while True:
        print("***Officers Program***")
        while True:
            print("1: Log in\n2: *Shut Down the Program*")
            while True:
                choice= int(input())
                if choice== 1:
                    flag= 1
                    break
                elif choice== 2:
                    flag= 2
                    break
            if flag== 1:
                print("Log in to your account")
                print("Enter your Username:")
                Logusername= input()
                print("Please enter your Password:")
                Logpassword= input()
                Oldperson= Officer(Logusername, Logpassword)
                real_person= Oldperson.Log_in()
                if real_person== True:
                    print("Successfully logged in.")
                    break
                else:
                    print("The Username or Password is Incorrect please try again.")
                    continue
            elif flag== 2:
                print("Shutting Down...")
                return
        while True:
            print("Hi officer", Oldperson.Get_Name(), "welcome to the Officer panel.")
            print("The Main Menu:")
            while True:
                print("1: Books Management \n2: Borrowing Requests \n3: Returning Requests \n4: Reserving Requests \n5: Seeing Transactions history \n6: Changing the Password \n7: Managing customers accounts \n8: Logging out")
                choice= int(input())
                if choice== 1:
                    print("1: All books \n2: Search for book(s) \n3: Add a New Book")
                    choice= int(input())
                    if choice== 1:
                        print("The library books are as follows:")
                        Books_Manager.Getting_All()
                        print("Hint: The indeces of books are the numbers behind them.")
                    elif choice== 2:
                        print("Please search your word:")
                        searchw= input()
                        Books_Manager.Searching(searchw)
                        print("Hint: The indeces of books are the numbers next to them.")
                    elif choice== 3:
                        print("Are you sure you want to add a new book to the library list of books? 1: Yes / 0: No")
                        flag= 1
                        while True:
                            choice= input()
                            if choice== '1':
                                break
                            elif choice== '0':
                                flag= 0
                                print("Canceled")
                                break
                        if flag== 0:
                            continue
                        Books_Manager.AddNewBook()
                elif choice== 2:
                    print("* Approving and Rejecting Customers borrowing requests. *")
                    waitin_book_fun_reseult= Officer.Get_WaitingsBorrR()
                    if waitin_book_fun_reseult== False:
                        print("There is not any book borrowing request.")
                        continue
                    if waitin_book_fun_reseult== True:
                        print("1: Approve\n2: Reject")
                        choice= int(input())
                        if choice== 1:
                            print("Please enter number of transactions which you want to approve their borrowing requests:")
                            hmany= int(input())
                            listofApprovedBooksBorrReq= []
                            for i in range(0, hmany):
                                print("Enter the transaction index of", i+1,":")
                                ind= int(input())
                                listofApprovedBooksBorrReq.append(ind)
                            print("Are you sure for approving?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                if Officer.Approving_Borr(listofApprovedBooksBorrReq)== True:
                                    print("Approving has been set.")
                                else:
                                    print("Not Approved.")
                            else:
                                print("Canceled.")
                                continue
                        if choice== 2:
                            print("Please enter number of transactions which you want to reject their borrowing requests:")
                            hmany= int(input())
                            listofRejectedBooksBorrReq= []
                            for i in range(0, hmany):
                                print("Enter the transaction index of", i+1,":")
                                ind= int(input())
                                listofRejectedBooksBorrReq.append(ind)
                            print("Are you sure for rejecting?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                Officer.Rejecting_Borr(listofRejectedBooksBorrReq)
                            else:
                                print("Canceled.")
                                continue
                elif choice== 3:
                    print("* Approving and Rejecting Customers returning requests. *")
                    waitin_book_fun_reseult= Officer.Get_WaitingsReturnR()
                    if waitin_book_fun_reseult== False:
                        print("There is not any book returning request.")
                        continue
                    if waitin_book_fun_reseult== True:
                        print("1: Approve\n2: Reject")
                        choice= int(input())
                        if choice== 1:
                            hmany= 1
                            listofApprovedBooksReturnReq= []
                            for i in range(0, hmany):
                                print("Please enter the transaction index:")
                                ind= int(input())
                                listofApprovedBooksReturnReq.append(ind)
                            print("Are you sure for approving?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                Officer.Approving_Return(listofApprovedBooksReturnReq)
                            else:
                                print("Canceled.")
                                continue
                        elif choice== 2:
                            print("Please enter number of transactions which you want to reject their returning requests:")
                            hmany= int(input())
                            listofRejectedBooksReturnReq= []
                            for i in range(0, hmany):
                                print("Enter the transaction index of", i+1,":")
                                ind= int(input())
                                listofRejectedBooksReturnReq.append(ind)
                            print("Are you sure for rejecting?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                Officer.Rejecting_Return(listofRejectedBooksReturnReq)
                            else:
                                print("Canceled.")
                                continue
                elif choice== 4:
                    print("* Approving and Rejecting Customers reserving requests. *")
                    waitin_book_fun_reseult= Officer.Get_WaitingsReserveR()
                    if waitin_book_fun_reseult== False:
                        print("There is not any book reserving request.")
                        continue
                    if waitin_book_fun_reseult== True:
                        print("1: Approve\n2: Reject")
                        choice= int(input())
                        if choice== 1:
                            print("Please enter number of transactions which you want to approve their reserving requests:")
                            hmany= int(input())
                            listofApprovedBooksReserveReq= []
                            for i in range(0, hmany):
                                print("Enter the transaction index of", i+1,":")
                                ind= int(input())
                                listofApprovedBooksReserveReq.append(ind)
                            print("Are you sure for approving?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                Officer.Approving_Reserve(listofApprovedBooksReserveReq)
                            else:
                                print("Canceled.")
                                continue
                        if choice== 2:
                            print("Please enter number of transactions which you want to reject their reserving requests:")
                            hmany= int(input())
                            listofRejectBooksReserveReq= []
                            for i in range(0, hmany):
                                print("Enter the transaction index of", i+1,":")
                                ind= int(input())
                                listofRejectBooksReserveReq.append(ind)
                            print("Are you sure for rejecting?\n1: Yes\n2: No")
                            choice= int(input())
                            if choice== 1:
                                Officer.Rejecting_Reserve(listofRejectBooksReserveReq)
                            else:
                                print("Canceled.")
                                continue
                elif choice== 5:
                    print("Transactions system\nDo you want to see all the transactions or specific type of customers requests?\n1: All transactions\n2: See based on type of the requests")
                    choice= int(input())
                    if choice== 1:
                        print("The below Transactions list is related to the customers:")
                        Transaction.All_Transc()
                        print("Do you want to see the visualization by time?\n1: Yes\n2: No")
                        choice= int(input())
                        if choice== 1:
                            print("The Activities Visualization:")
                            Transaction.Visulizing_All_Transc()
                        elif choice== 2:
                            continue
                    elif choice== 2:
                        print("Please select which type of request transactions list you want to see?\n1: Borrowings\n2: Returnings\n3: Reservings")
                        choice= int(input())
                        if choice== 1:
                            ttype= "Borrowing"
                        if choice== 2:
                            ttype= "Returning"
                        if choice== 3:
                            ttype= "Reserving"
                        Transaction.Trascn_based_on_Type(ttype)
                elif choice== 6:
                    print("**Changing Password**")
                    flag= 1
                    while True:
                        print("Please enter your old Password: ('q' for cancel)")
                        oldpassword= input()
                        if oldpassword== 'q' or oldpassword== 'Q':
                            flag= 0
                            break
                        Officers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Officers.csv")
                        Uvalidornot= Officers_Data["Encrypted password"].where(Officers_Data['Username']== Oldperson.u).values.tolist()
                        for i in range(0, len(Uvalidornot)):
                            qa= isinstance(Uvalidornot[i], str)
                            if qa== True:
                                ciphpass= Uvalidornot[i]
                                break
                        passwordstocheck= Password(oldpassword)
                        oldPvalidornot= passwordstocheck.Check(ciphpass)
                        if oldPvalidornot== True:
                            print("Old Password Checked.")
                            break
                        else:
                            print("The old Password you've entered doesn't match, Please try again.")
                            continue
                    if flag== 0:
                        continue
                    while True:
                        while True:
                            print("Now Please enter your new Password:")
                            newpasswordtry1= input()
                            if len(newpasswordtry1)<= 7:
                                print("Please enter a strong password (The password must be at lease 8 digits.) ")
                                continue
                            else:
                                break
                        print("Please enter your new Password again:")
                        newpasswordtry2= input()
                        if newpasswordtry1== newpasswordtry2:
                            break
                        else:
                            print("The new Passwords aren't the same, Please try again.")
                            continue
                    Pchanger= Officer(Logusername, newpasswordtry1)
                    Pchanger.Changing_Passwords()
                    print("Success. New Password has been set.")
                    continue
                elif choice== 7:
                    print("* Managing Users System: *")
                    Officer.Managing_Users()
                elif choice== 8:
                    print("Are you sure you want to log out of account?\n1: Yes\n2: No")
                    while True:
                        choice= int(input())
                        if choice== 1:
                            lflag= 1
                            break
                        elif choice== 2:
                            lflag= 2
                            break
                    if lflag== 1:
                        break
            if lflag== 1:
                break
#start0:
# importing libraies and data:
import pandas as pd
import math
print("Hello, Welcome to the Officers program")
import threading
t1 = threading.Thread(target= Notifications_Sys)
t2 = threading.Thread(target= main_fun)
# starting thread 1
t1.start()
# starting thread 2
t2.start()
t1.join()
t2.join()
while True:
    print("Are you sure you want to quit? 1 for yes, 0 for no.")
    choice= int(input())
    if choice== 1:
        print("End of the Officers Program.")
        break
    elif choice== 0:
        main_fun()
# end
