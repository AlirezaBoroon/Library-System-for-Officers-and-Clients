# This program is used for Clients of Library
# Every client has its own data in the Data_Customers.csv file.
# Every client has two main attributes in the Customer class, Username and Password
# Every password stores as encrypted text in Data_Customers.csv file, no one can know the password even with watching them!.
# Encryption process uses built-in Affine Cipher with two keys stored in a weird file!.
# Having keys itself does not help!, we have to have the program code, 'cause it's almost a unique process.

class Person:
    def __init__(self, Username, Password):
        self.u= Username
        self.p= Password
class Customer (Person):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)
        self.u= Username
        self.p= Password
    def Get_Name(self):
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        Cname= Customers_Data.loc[Customers_Data.Username == self.u, "Name"].values.tolist()
        return Cname[0]
    def Log_in(self):
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        # every time when we want to read, it is suggested that we have to read the data again, because sometimes the code uses the old data.
        Uvalidornot= Customers_Data["Encrypted password"].where(Customers_Data['Username']== self.u).values.tolist()
        for i in range(0, len(Uvalidornot)):
            qa= isinstance(Uvalidornot[i], str)
            if qa== True:
                ciphpass= Uvalidornot[i]
                break
        else:# else in python after a loop has a good application, if loop was not broke with break command, the else will be executed.
            return False
        passwordstocheck= Password(self.p)
        Pvalidornot= passwordstocheck.Check(ciphpass)
        if Pvalidornot== True:
            return True
        else:
            return False
    def isApproved(self):
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        if (Customers_Data.loc[Customers_Data.Username == self.u, "Status"]== 'Approved').bool():
            return 1
        elif (Customers_Data.loc[Customers_Data.Username == self.u, "Status"]== 'Banned').bool():
            return -1
        else:
            return 0
    def Register(self, Name):
        passobj= Password(self.p)
        cipheredPass= passobj.Encrypt()
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        usern= Customers_Data[(Customers_Data['Username'] == self.u)].index.tolist()
        if len(usern)== 0:
            new_row= {'Username':self.u, 'Encrypted password':cipheredPass, 'Name':Name, 'Remaining-requests':3, 'Book-id#1':math.nan, '#1 date':math.nan, 'Book-id#2':math.nan, '#2 date':math.nan, 'Book-id#3':math.nan, '#3 date':math.nan, 'Status':'Not Approved'}
        else:
            return False
        Customers_Data= Customers_Data.append(new_row, ignore_index = True)
        Customers_Data= Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
        # we must have this equality, which means to edit the Customer_Data.
        return True
    def Changing_Passwords(self):
        newpassobj= Password(self.p)
        newcipheredPass= newpassobj.Encrypt()
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        Customers_Data.loc[Customers_Data.Username == self.u, "Encrypted password"]= newcipheredPass
        Customers_Data= Customers_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv', index=False)
        return True
    def Borrowing(self, Booki):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        if Customers_Data.loc[Customers_Data.Username == self.u, "Remaining-requests"].values.tolist()[0]== 0:
            print("Error, You don't have any request left for Borrowing.")
            return False
        print("Are you sure you want to borrow this book?\n1: Yes\n2: No")
        while True:
            choice= int(input())
            if choice== 1:
                break
            elif choice== 2:
                return False
        status= "Waiting"
        tyofreq= "Borrowing"
        # import datetime as dt
        # t = dt.datetime.now()
        from datetime import datetime
        month= datetime.now().strftime('%m')
        day= datetime.now().strftime('%d')
        hour= datetime.now().strftime('%H')
        minute= datetime.now().strftime('%M')
        new_transac= {'Month':month, 'Day':day,'Hour':hour,'Minute':minute,'Username':self.u, 'Book-id':Booki, 'Status': status, 'Type of request':tyofreq}
        Transactions_Data= Transactions_Data.append(new_transac, ignore_index = True)
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Borrowing request has been sent to the library officer successfully.")
        return True
    def Reserving(self, Booki):
        print("Are you sure you want to reserve this book?\n1: Yes\n2: No")
        while True:
            choice= int(input())
            if choice== 1:
                break
            elif choice== 2:
                return False
        status= "Waiting"
        tyofreq= "Reserving"
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        from datetime import datetime
        month= datetime.now().strftime('%m')
        day= datetime.now().strftime('%d')
        hour= datetime.now().strftime('%H')
        minute= datetime.now().strftime('%M')
        new_transac= {'Month':str(month), 'Day':str(day),'Hour':str(hour),'Minute':str(minute),'Username':self.u, 'Book-id':Booki, 'Status': status, 'Type of request':tyofreq}
        Transactions_Data= Transactions_Data.append(new_transac, ignore_index = True)
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Reserving request has been sent to the library officer successfully.")
        return True
    def Get_WaitingsBorrR(self):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        RforBBorr= Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Borrowing"), "Book-id"].values.tolist()
        # for i in range(0, len(RforBBorr)):
        #     newdf= Transactions_Data.iloc[int(RforBBorr[i])]
        #     BooksRequested= pd.concat([BooksRequested, newdf], axis= 1)
        if len(RforBBorr)== 0:
            return False, 0
        elif len(RforBBorr)== 1:
            print("The borrowed book is as follows:")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBBorr)
            print(gettingbook)
            return True, gettingbook.index.values.tolist()
        else:
            print("The borrowed books are as follows:")
            gettingbook= Books_Manager.Getting_viaIndeces(RforBBorr)
            print(gettingbook)
            return True, 0
    def Get_WaitingsReturnR(self):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        RforBReturn= Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Returning"), "Book-id"].values.tolist()
        if len(RforBReturn)== 0:
            return False
        print("The Book-id sections, represented for the following book(s) which you were looking for:")
        gettingbook= Books_Manager.Getting_viaIndeces(RforBReturn)
        print(gettingbook)
        return True
    def Get_WaitingsReserveR(self):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        RforBReserve= Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Status"]== "Waiting") & (Transactions_Data["Type of request"]== "Reserving"), "Book-id"].values.tolist()
        if len(RforBReserve)== 0:
            return False
        print("The Book-id sections, represented for the following book(s) which you were looking for:")
        gettingbook= Books_Manager.Getting_viaIndeces(RforBReserve)
        print(gettingbook)
        return True
    def Cancelling_Borr(self, listofindeces):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Book-id"]== listofindeces[i]) & (Transactions_Data["Type of request"]== "Borrowing"), "Status"]= "Canceled"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        if len(listofindeces)== 1:
            print("Canceling Borrowing request has been done successfully.")
        else:
            print("Canceling Borrowing request(s) has been done successfully.")
        return True
    def Cancelling_Return(self, listofindeces):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Book-id"]== listofindeces[i]) & (Transactions_Data["Type of request"]== "Returning"), "Status"]= "Canceled"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        if len(listofindeces)== 1:
            print("Canceling Returning request has been done successfully.")
        else:
            print("Canceling Returning request(s) has been done successfully.")
        return True
    def Cancelling_Reserve(self, listofindeces):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        for i in range(0, len(listofindeces)):
            Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Book-id"]== listofindeces[i]) & (Transactions_Data["Type of request"]== "Reserving"), "Status"]= "Canceled"
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        if len(listofindeces)== 1:
            print("Canceling Reserving request has been done successfully.")
        else:
            print("Canceling Reserving request(s) has been done successfully.")
        return True
    def Get_Borroewedindec(self):
        Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
        BooksIndecesList= Customers_Data.loc[Customers_Data.Username == self.u, ["Book-id#1", "Book-id#2", "Book-id#3"]].values.tolist()[0]
        return BooksIndecesList
    def Returning(self, Booki):
        print("Are you sure you want to return this book?\n1: Yes\n2: No")
        while True:
            choice= int(input())
            if choice== 1:
                break
            elif choice== 2:
                return False
        status= "Waiting"
        tyofreq= "Returning"
        # import datetime as dt
        # t = dt.datetime.now()
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        from datetime import datetime
        month= datetime.now().strftime('%m')
        day= datetime.now().strftime('%d')
        hour= datetime.now().strftime('%H')
        minute= datetime.now().strftime('%M')
        new_transac= {'Month':str(month), 'Day':str(day),'Hour':str(hour),'Minute':str(minute),'Username':self.u, 'Book-id':Booki, 'Status': status, 'Type of request':tyofreq}
        Transactions_Data= Transactions_Data.append(new_transac, ignore_index = True)
        Transactions_Data= Transactions_Data.to_csv('C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv', index=False)
        print("Returning request has been sent to the library officer successfully.")
    def Get_reserve(self):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        if (Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Type of request"]== "Reserving") & (Transactions_Data["Status"]== "Approved")]).count().tolist()[0]!= 0:
            print("Your request for reserving is now approved by officer, please get your book.")
        elif (Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Type of request"]== "Reserving") & (Transactions_Data["Status"]== "Waiting")]).count().tolist()[0]!= 0:
            print("Your request for reserving is not approved by officer yet.")
        elif (Transactions_Data.loc[(Transactions_Data["Username"] == self.u) & (Transactions_Data["Type of request"]== "Reserving") & (Transactions_Data["Status"]== "Canceled")]).count().tolist()[0]!= 0:
            print("Your request for reserving is Canceled by yourself.")
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
    def Getting_Availables():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        AceessbileB= Books_Data[Books_Data["Status"]== "accessible"]
        print(AceessbileB)
    def Getting_viaIndeces(listofindeces):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        BookswithIndc= Books_Data.iloc[listofindeces]
        return BookswithIndc
    def Getting_Reservables():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        not_reservedB= Books_Data[Books_Data["Reserve-Status"]== "not reserved"]
        print(not_reservedB)
    def Searching(Word):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        BooksNames= Books_Data['Name'].tolist()
        searchinbooksideces= []
        # for i in range(0, len(BooksNames)):
        #     if Word in BooksNames[i]:
        #         searchinbooksideces.append(i)
        for i in range(0, len(BooksNames)):
            if Word in BooksNames[i]: 
                searchinbooksideces.append(i)     
        bookswithword= Books_Data.iloc[searchinbooksideces] 
        print(bookswithword)
    def Get_ReturnApprovedBooks(self):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        books = pd.DataFrame()
        import math
        validl= []
        for i in range(0, len(self.i)):
            if math.isnan(self.i[i])== False:
                validl.append(int(self.i[i]))
        for i in range(0, len(validl)):
            newdf= Books_Data.iloc[validl[i]]
            books= pd.concat([books, newdf], axis= 1)
        print(books)
        print("Hint: The indeces of books are the numbers above.")
        if books.empty:
            return False
        print("Please enter the book index which you want to return to the library?")
        indexofretb= int(input("Book index:"))
        return indexofretb
    def Getting_NotReserveds():
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        not_reservedB= Books_Data[Books_Data["Reserve-Status"]== "not reserved"]
        print("The reservable books are as follows:\n", not_reservedB)
    def Searching_inReservation(Word):
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        not_reservedB= Books_Data[Books_Data["Reserve-Status"]== "not reserved"]
        BooksNames= not_reservedB['Name'].tolist()
        searchinbooksideces= []
        # for i in range(0, len(BooksNames)):
        #     if Word in BooksNames[i]:
        #         searchinbooksideces.append(i)
        for i in range(0, len(BooksNames)):
            if Word in BooksNames[i]: 
                searchinbooksideces.append(i)     
        bookswithword= Books_Data.iloc[searchinbooksideces] 
        print(bookswithword)
        if bookswithword.empty:
            return False
        else:
            return True
class Transaction(Customer):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)
        self.u= Username
        self.p= Password
    def All_Transc(self):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
        related_t= Transactions_Data[Transactions_Data["Username"]== self.u].reset_index()
        for i in range(0, len(related_t)):# this is for converting book id to the name of the books of books dataframe.
            j= related_t.loc[related_t.index == i, "Book-id"].tolist()[0]
            book_name= Books_Data.loc[Books_Data.index == int(j), "Name"].values.tolist()[0]
            related_t.loc[related_t.index == i, "Book-id"]= book_name
        related_t.rename(columns = {'Book-id':'Book'}, inplace = True)# converting book-id column with Book, after changing the values of column book-id.
        print(related_t)
        return True
    def Trascn_based_on_Type(self, ttype):
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        related_t_ty= Transactions_Data[(Transactions_Data["Username"]== self.u) & (Transactions_Data["Type of request"]== ttype)]
        print("Your transactions list based on", ttype, "is:")
        print(related_t_ty)
        return True
    def Visulizing_All_Transc(self):
        import matplotlib.pyplot as plt
        from datetime import datetime
        month= datetime.now().strftime('%m')
        Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
        related_t= Transactions_Data[Transactions_Data["Username"]== self.u]
        ys= []
        xs= []
        for i in range(1, int(month)+1):
            for j in range(1, 32):
                if related_t[(related_t["Month"]== i) & (related_t["Day"]== j)].count().tolist()[0]!= 0:
                    ys.append(related_t[(related_t["Month"]== i) & (related_t["Day"]== j)].count().tolist()[0])
                    # a real notice: if we change the data in the program of a database in system, we get the data in string format but when editing or even opening! with numbers
                    # we get numbers as integers! not strings.
                    xs.append("%d/%d" %(i, j))
        plt.title('Transactions Visualization')
        plt.xlabel('Days of activity')
        plt.ylabel('Occurations')
        plt.plot(xs, ys, color='black', linestyle='dashed', linewidth = 3,
                marker='o', markerfacecolor='green', markersize=12)
        plt.grid()
        plt.plot(xs, ys, 'o')
        plt.show()
        print("The chart showed is the visualization of your activity based on days.")
        return True
def main_fun():
    while True:
        print("***Customers Program***")
        while True:
            print("1: Log in to account \n2: Register an account")
            choice= int(input())
            if choice== 1:
                print("Please enter your Username:")
                Logusername= input()
                print("Please enter your Password:")
                Logpassword= input()
                Oldperson= Customer(Logusername, Logpassword)
                real_person= Oldperson.Log_in()
                if real_person== True:
                    print("Successfully logged in.")
                    break
                else:
                    print("The Username or Password is Incorrect please try again.")
                    continue
            elif choice== 2:
                print("Please enter your name:")
                name= input()
                while True:
                    print("Please enter your Username (using for logging in):")
                    username= input()
                    if len(username)<= 4:
                        print("The Username should be at least 5 letters.")
                        continue
                    else:
                        break
                while True:
                    print("Please enter your Password:")
                    password= input()
                    if len(password)<= 7:
                        print("Please enter a strong password (The password must be at least 8 digits.)")
                        continue
                    else:
                        break
                Newperson= Customer(username, password)
                Regisvalidorn= Newperson.Register(name)
                if Regisvalidorn== True:
                    print("Thank you, You have been Successfully Registered in the library.")
                    continue
                else:
                    print("The Username already exists!, Please try again.")
                    continue
            elif choice== 2154:
                print("Shutting down...")
                return
        print("Hi", Oldperson.Get_Name(), "welcome.")
        # Here the program checks that the user's account is approved or not.
        app= Oldperson.isApproved()
        # in python, 0 equals to False and otherwise..., so when we have more than two conditions(beside True and False) we don't use boolean.
        if app== -1:
            print("The officer has banned your account due to a reason, please contact the library.")
            continue
        elif app== 0:
            print("Your account is not approved by an officer yet, please try again later.")
            continue
        while True:
            print("The Main Menu:")
            print("1: Getting books table \n2: Borrowing Books \n3: Returning Books \n4: Reservation \n5: Seeing related transactions history \n6: Changing the Password \n7: Logging out")
            choice= int(input())
            if choice== 1:
                print("Do you want to see all the library books or you want to search for a specific book?\n1: All books \n2: Search a book")
                choice= int(input())
                if choice== 1:
                    print("The library books are as follows:")
                    Books_Manager.Getting_All()
                    print("Hint: The indeces of books are the numbers behind them.")
                elif choice== 2:
                    print("Please enter your keyword:")
                    searchw= input()
                    Books_Manager.Searching(searchw)
                    print("Hint: The indeces of books are the numbers next to them.")
            elif choice== 2:
                print("Borrowing books requests system is used to borrow accessible books\n1: Borrow book request\n2: Cancel borrow request")
                choice= int(input())
                if choice== 1:
                    print("For borrow request:\n1: If you know the book index\n2: If you don't know the index of the book you want")
                    choice= int(input())
                    if choice== 1:
                        print("Please enter the book index:")
                        index= int(input())
                        # Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
                        # Customers_Data.loc[Customers_Data.Username == Logusername, "Remaining requests"] = int(Customers_Data.loc[Customers_Data.Username == Logusername, "Remaining requests"])-1
                        # balaee bad az taeede officer bashad.
                        # spebook= Books_Manager(index)
                        # spebook.Borrowing()
                    elif choice== 2:
                        print("1: All available books\n2: search for a book")
                        choice= int(input())
                        if choice== 1:
                            print("The available library books are as follows:")
                            Books_Manager.Getting_Availables()
                            print("Hint: The indeces of books are the numbers behind them.")
                        elif choice== 2:
                            print("Please search your keyword:")
                            searchw= input()
                            Books_Manager.Searching(searchw)
                            print("Hint: The indeces of books are the numbers behind them.")
                        print("Now please enter the book index:")
                        index= int(input())
                    if Oldperson.Borrowing(index)== False:
                        print("The process canceled.")
                elif choice== 2:
                    waitin_book_fun_reseult= Oldperson.Get_WaitingsBorrR()
                    if waitin_book_fun_reseult[0]== False:
                        print("You currently don't have any book borrowing request.")
                        continue
                    if waitin_book_fun_reseult[1]== 0:
                        print("Please enter how many of the book(s) borrowing request(s) you want for canceling:")
                        hmany= int(input())
                        listofCanceledBooksBorrReq= []
                        for i in range(0, hmany):
                            print("Enter the book index of", i+1,":")
                            ind= int(input())
                            listofCanceledBooksBorrReq.append(ind)
                        print("Are you sure?\n1: Yes\n2: No")
                        choice= int(input())
                        if choice== 1:
                            Oldperson.Cancelling_Borr(listofCanceledBooksBorrReq)
                        else:
                            continue
                    else:
                        book_index_list= waitin_book_fun_reseult[1]
                        if choice== 1:
                            Oldperson.Cancelling_Borr(book_index_list)
                        else:
                            continue
            elif choice== 3:
                print("Returning books requests system is used to return the books by customer.\n1: Return book request\n2: Cancel return request")
                choice= int(input())
                if choice== 1:
                    print("For return request:\n1: If you know the book index\n2: If you don't know the book index")
                    choice= int(input())
                    if choice== 1:
                        print("Please enter the book index:")
                        indeces= [int(input())]
                    elif choice== 2:
                        BooksIndecesList= Oldperson.Get_Borroewedindec()
                        approvedbook= Books_Manager(BooksIndecesList)
                        indeces= approvedbook.Get_ReturnApprovedBooks()
                        if indeces== False:
                            print("You don't have any returning book request.")
                            continue
                    if Oldperson.Returning(indeces)== False:
                        print("The process canceled.")
                elif choice== 2:
                    if Oldperson.Get_WaitingsReturnR()== False:
                        print("You currently don't have any book returning request.")
                        continue
                    print("Please enter how many of the book(s) returning request(s) you want for cancelling:")
                    hmany= int(input())
                    listofCanceledBooksreturnReq= []
                    for i in range(0, hmany):
                        print("Enter the book index of", i+1)
                        ind= int(input())
                        listofCanceledBooksreturnReq.append(ind)
                    Oldperson.Cancelling_Return(listofCanceledBooksreturnReq)
            elif choice== 4:
                print("Reservation system is used to reserve books for future by customer.\n1: Book reserving request\n2: Cancel reserved request\n3: Getting reserved book")
                choice= int(input())
                if choice== 1:
                    print("For Book reserving request:\n1: If you know the book index\n2: If you don't know the book index")
                    choice= int(input())
                    if choice== 1:
                        print("Please enter the book index:")
                        index= int(input())
                    elif choice== 2:
                        print("1: All Reservable books\n2: search for a book")
                        choice= int(input())
                        if choice== 1:
                            print("The Reservable library books are as follows:")
                            Books_Manager.Getting_Reservables()
                            print("Hint: The indeces of books are the numbers behind them.")
                        elif choice== 2:
                            print("Please search your keyword:")
                            searchw= input()
                            valid_search_or_not= Books_Manager.Searching_inReservation(searchw)
                            print("Hint: The indeces of books are the numbers behind them.")
                            if valid_search_or_not== False:
                                print("There is not any book reservable with the word you entered.")
                                continue
                        print("Now please enter the book index:")
                        index= int(input())
                    if Oldperson.Reserving(index)== False:
                        print("The process canceled.")
                elif choice== 2:
                    if Oldperson.Get_WaitingsReserveR()== False:
                        print("You currently don't have any book reserving request.")
                        continue
                    print("Please enter how many of the book(s) reserving request(s) you want for canceling:")
                    hmany= int(input())
                    listof_Canceled_Books_reserve_Req= []
                    for i in range(0, hmany):
                        print("Enter the book index of", i+1)
                        ind= int(input())
                        listof_Canceled_Books_reserve_Req.append(ind)
                    Oldperson.Cancelling_Reserve(listof_Canceled_Books_reserve_Req)
                elif choice== 3:
                    Oldperson.Get_reserve()
            elif choice== 5:
                Transaction_obj= Transaction(Oldperson.u, Oldperson.p)
                print("Transactions system\nDo you want to see all the related transactions or specific type of your request?\n1: All transactions\n2: See based on type of the requests")
                choice= int(input())
                if choice== 1:
                    print("The below Transactions list is related to you based on your Username and activity:")
                    Transaction_obj.All_Transc()
                    print("Do you want to see the visualization of your requests by time?\n1: Yes\n2: No")
                    choice= int(input())
                    if choice== 1:
                        print("The Activity Visualization:")
                        Transaction_obj.Visulizing_All_Transc()
                    elif choice== 2:
                        continue
                elif choice== 2:
                    print("Please select which type of request transactions list you want to see?\n1: Borrowing\n2: Returning\n3: Reserving")
                    choice= int(input())
                    if choice== 1:
                        ttype= "Borrowing"
                    if choice== 2:
                        ttype= "Returning"
                    if choice== 3:
                        ttype= "Reserving"
                    Transaction_obj.Trascn_based_on_Type(ttype)
            elif choice== 6:
                print("**Changing Password**")
                flag= 1
                while True:
                    print("Please enter your old Password: ('q' for cancel)")
                    oldpassword= input()
                    if oldpassword== 'q' or oldpassword== 'Q':
                        flag= 0
                        break
                    Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
                    Uvalidornot= Customers_Data["Encrypted password"].where(Customers_Data['Username']== Oldperson.u).values.tolist()
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
                # ^ it helps us that if user canceled the process, therefore the process will no longer continue.
                while True:
                    while True:
                        print("Now Please enter your new Password:")
                        newpasswordtry1= input()
                        if len(newpasswordtry1)<= 7:
                            print("Please enter a strong password (The password must be at least 8 digits.)")
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
                Pchanger= Customer(Logusername, newpasswordtry1)
                Pchanger.Changing_Passwords()
                print("Success. New Password has been set.")
                continue
            elif choice== 7:
                print("Are you sure you want to log out of account?\n1: Yes\n2: No")
                while True:
                    choice= int(input())
                    if choice== 1:
                        flag= 1
                        break
                    elif choice== 2:
                        flag= 2
                        break
                if flag== 1:
                    break
#start0:
# importing libraies and data:
import pandas as pd
import math
# loading the data:
# Customers_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Customers.csv")
# Books_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Books.csv")
# Transactions_Data= pd.read_csv("C:/Users/A.M.Brn/Desktop/Course Project/CODE/Data_Transactions.csv")
print("Hello, Welcome to the customers program")
main_fun()
while True:
    print("Are you sure you want to quit? 1 for yes, 0 for no.")
    choice= int(input())
    if choice== 1:
        print("End of the Customers Program.")
        break
    elif choice== 0:
        main_fun()
# end
