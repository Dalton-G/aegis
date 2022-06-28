# Gan Ming Liang
# TP063338

# Amadea Lim Yi Wen (teammate)
# TP064038

# Program name: AEGIS (Asian Event General Interface Solution)

import datetime # import datetme from python library for later use


def homepage():
    print("=== Welcome to Asian Event Management Service (AEMS) ===")
    print("Please select your position:")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    option = int(input("Please select an option: "))
    if option == 1:
        adminHome()
    elif option == 2:
        guestOption()
    elif option == 3:
        exitPage()
    else:
        print("Please select a valid option")
        homepage()


def guestOption():
    print("\n>>> What would you like to do? \n")
    print("1. View Category")
    print("2. View Event")
    print("3. Log in as a Member")
    print("4. Register as a Member")
    print("5. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        guestViewCategory()
    elif choice == 2:
        guestViewEvent()
    elif choice == 3:
        memberLogin()
    elif choice == 4:
        memberSignup()
    elif choice == 5:
        exitPage()
    else:
        print("option not supported, please try again")
        guestOption()


def adminHome():
    print("=== Please select an option below: ===")
    print("1. Admin Login")
    print("2. Admin Registration")
    print("3. Go Back")
    option = int(input("Your choice: "))
    if option == 1:
        adminLogin()
    elif option == 2:
        adminAuth()
    elif option == 3:
        homepage()
    else:
        print("Please select a valid option")
        adminHome()


def adminAuth():
    code = input("Please enter company referral code: ")
    if code != "AEMS0001":
        print("Incorrect referral code.")
        print("do you want to (1) Try Again, or (2) Go Back ?")
        choice = int(input("Your choice: "))
        if choice == 1:
            adminAuth()
        elif choice == 2:
            adminHome()
        else:
            print("option not supported, returning to homepage...")
            homepage()
    else:
        print("Verification successful!")
        adminSignup()


def adminSignup():
    adminHandler = open("adminList.txt", "r")
    print(">>> Welcome to AEMS admin registration page, please follow the instruction below <<<")
    username = input("Enter a username: ")
    password1 = input("Enter a password: ")
    password2 = input("Confirm your password: ")

    # database
    adminUN = []
    adminPW = []
    for i in adminHandler:
        a,b = i.split(", ")
        b = b.strip()
        adminUN.append(a)
        adminPW.append(b)

    if password1 != password2:
        print("Password does not match, please try again")
        adminSignup()
    elif len(password1) <= 8:
        print("Password must be longer than 8 characters, please try again")
        adminSignup()
    elif username in adminUN:
        print("Username already taken, please try again")
        adminSignup()
    else:
        db = open("adminList.txt", "a")
        db.write(username+", "+password1+"\n")
        print("Registration Successful!")
        db.close()
    adminHandler.close()
    adminHome()


def adminLogin():
    tempList = []
    adminHandler = open("adminList.txt", "r")
    while True:
        print(">>> Admin Login Page <<<")
        adminUN = input("Enter your username: ")
        adminPW = input("Enter your password: ")
        for i in adminHandler:
            tempList.append(i)
        if adminUN + ", " + adminPW + "\n" in tempList:
            print("Login successful!")
            print("Welcome back,", adminUN.capitalize())
            adminOption()
        else:
            print("\n >>> invalid credentials... \n")
            option = input("would you like to sign-up? \n [Y] for admin registration \n [N] to retry login \n Your choice: " )
            if option == "N":
                continue #repeat while loop
            elif option == "Y":
                adminAuth()
            else:
                print("invalid option, returning to homepage...")
                homepage()
        break
    adminHandler.close()


def adminOption():
    print("\n What would you like to do? \n")
    print("1. Add event")
    print("2. Modify event records")
    print("3. Display record details")
    print("4. Search specific record")
    print("5. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        addEvent()
    elif choice == 2:
        modifyEvent()
    elif choice == 3:
        print("display options: \n a. Event Category \n b. All Events \n c. Registered Customers \n d. Customer Payment")
        selection = str(input("Enter your option: "))
        if selection == "a":
            adminViewCategory()
        elif selection == "b":
            adminViewEvent()
        elif selection == "c":
            adminViewCustomerList()
        elif selection == "d":
            adminViewCustomerPayment()
        else:
            print("option not supported, try again")
            adminOption()
    elif choice == 4:
        print("Please select a search option: \n a. Search Customer \n b. Search Customer's payment")
        option = str(input("Enter your option: "))
        if option == "a":
            adminSearchCustomerInfo()
        elif option == "b":
            adminSearchCustomerPayment()
        else:
            print("option not supported, try again")
            adminOption()
    elif choice == 5:
        exitPage()
    else:
        print("option not supported, try again")
        adminOption()


def addEvent():
    eventHandler = open("eventList.txt", "r")
    print(">>> Welcome to AEMS event page, please select your category of events to add <<<")
    while True: # while loop is used to display the available categories for admin if they decide to add another event later on
        print("Event Category: \n 1. Sports/Martial Arts \n 2. Musical Performance \n 3. Dance/Performing Arts \n 4. Expo/Exhibition \n 5. Competition/Tournament \n 6. Others")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            eventCat = "Sports & Martial Arts"
            break
        elif choice == 2:
            eventCat = "Musical Performance"
            break
        elif choice == 3:
            eventCat = "Dance & Performing Arts"
            break
        elif choice == 4:
            eventCat = "Expo & Exhibition"
            break
        elif choice == 5:
            eventCat = "Competition & Tournament"
            break
        elif choice == 6:
            newCat = str(input("Enter the name of your category: "))
            eventCat = newCat
            break
        else:
            print("please select a valid option")
            continue

    # to obtain user inputs
    eventName = str(input("Enter event name: "))
    eventOrg = str(input("Enter event organizer: "))
    eventDate = str(input("Enter event start date in this format > [dd/mm/yyyy]: "))
    eventTime = str(input("Enter event start time in 24-hour format [eg: 16:30]: "))
    eventDuration = str(input("Enter event duration [eg: 2 days]: "))
    eventLocation = str(input("Enter the venue of the event: "))

    eventName = eventName.title() # for neatness/presentability purposes
    eventLocation = eventLocation.title() # for neatness/presentability purposes

    while True: # looping while to ask user whether event is free or not
        eventFee = str(input("Is your event free-of-charge? [Y/N]: "))
        if eventFee == "Y":
            eventPrice = "0.00"
            break
        elif eventFee == "N":
            eventPrice = str(input("Enter event price (per person) in RM [eg: 2.00]: ")) #string because we will concatenate it later (float will cause error)
            break
        else:
            print("Error: Please insert either [Y] or [N]")
            continue

    # defining empty list
    eCat = []
    eName = []
    eOrg = []
    eDate = []
    eTime = []
    eDura = []
    eLoca = []
    eFee = []

    # appending individual items into a list
    for i in eventHandler:
        a,b,c,d,e,f,g,h = i.split(", ")
        h = h.strip()
        eCat.append(a)
        eName.append(b)
        eOrg.append(c)
        eDate.append(d)
        eTime.append(e)
        eDura.append(f)
        eLoca.append(g)
        eFee.append(h)

    # appending content of each list into the text document
    db = open("eventList.txt", "a")
    db.write(eventCat+", "+eventName+", "+eventOrg+", "+eventDate+", "+eventTime+", "+eventDuration+", "+eventLocation+", "+eventPrice+"\n")
    print("Event added Successfully!")
    db.close()
    eventHandler.close()

    while True: # option to return to homepage or add another event
        print("Do you want to [1] return to admin homepage, [2] add another event?")
        option = int(input("Your choice: "))
        if option == 1:
            print("returned")
            adminOption()
        elif option == 2:
            addEvent()
        else:
            print("please select another option")
            continue
        break


def modifyEvent():
    eventdb = open("eventList.txt", "r")
    counter = 1
    print("Which event would you like to amend?")
    for i in eventdb: # display all available events
        a,b,c,d,e,f,g,h = i.split(", ")
        print(counter,"|", b)
        counter += 1
    eventdb.close()

    selection = int(input("Your choice: ")) # obtain user choice
    selection -= 1 # important: we minus 1 to get the index value (because index starts at 0)

    modifydb = open("eventList.txt", "r")
    modList = modifydb.readlines() # readlines() let us transfer the data from files into a temporary list
    editList = [] # empty string to be used later
    newList = modList # newlist copies modlist (for later use)
    tempIndex = modList[selection] # temp index finds the index of the selected event
    modifydb.close()

    print("\n>>> Current Event Details:") # display the selected events for users to refer to when modifying content(s)
    print(tempIndex)

    while True: # feature to display available categories presets
        print("Select New Event Category: \n 1. Sports/Martial Arts \n 2. Musical Performance \n 3. Dance/Performing Arts \n 4. Expo/Exhibition \n 5. Competition/Tournament \n 6. Others")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            mod1 = "Sports & Martial Arts"
            break
        elif choice == 2:
            mod1 = "Musical Performance"
            break
        elif choice == 3:
            mod1 = "Dance & Performing Arts"
            break
        elif choice == 4:
            mod1 = "Expo & Exhibition"
            break
        elif choice == 5:
            mod1 = "Competition & Tournament"
            break
        elif choice == 6:
            modCat = input("Enter the name of your category: ")
            mod1 = modCat
            break
        else:
            print("option not supported, try again")
            continue

    # obtain new details for the modified events
    mod2 = input("New event name: ")
    mod3 = input("New event organizer: ")
    mod4 = input("New event start date [eg: dd/mm/yyyy]: ")
    mod5 = input("New event start time [eg: 16:30]: ")
    mod6 = input("New event duration [eg: 2 days]: ")
    mod7 = input("New venue of the event: ")
    mod8 = input("New event price: ")

    # replace all changes in empty list
    editList.append(mod1)
    editList.append(mod2)
    editList.append(mod3)
    editList.append(mod4)
    editList.append(mod5)
    editList.append(mod6)
    editList.append(mod7)
    editList.append(mod8+"\n")
    finalEdit = ', '.join(editList) #join function to combine all strings into one string

    # delete the old event at the specific index and replace it with a new event at the same index (modification)
    del newList[selection]
    newList.insert(selection, finalEdit)

    # save changes into the .txt file
    db = open("eventList.txt", "w")
    for x in newList:
        db.write(x)
    db.close()
    print("Modification Successful!")
    adminOption()


def adminViewCategory():
    eventdb = open("eventList.txt", "r")
    # category counters are declared here
    counterCat1 = 0
    counterCat2 = 0
    counterCat3 = 0
    counterCat4 = 0
    counterCat5 = 0
    counterCat6 = 0
    for i in eventdb: # counter that display the total event in each cateogory
        a,b,c,d,e,f,g,h = i.split(", ")
        if "Sports & Martial Arts" in a:
            counterCat1 += 1
        elif "Musical Performance" in a:
            counterCat2 += 1
        elif "Dance & Performing Arts" in a:
            counterCat3 += 1
        elif "Expo & Exhibition" in a:
            counterCat4 += 1
        elif "Competition & Tournament" in a:
            counterCat5 += 1
        else:
            counterCat6 += 1

    print("Here are all the available Categories:")
    print("\n 1. Sports & Martial Arts\n", "Number of event in this Cat =", counterCat1)
    print("\n 2. Musical Performance\n", "Number of event in this Cat =", counterCat2)
    print("\n 3. Dance & Performing Arts\n", "Number of event in this Cat =", counterCat3)
    print("\n 4. Expo & Exhibition\n", "Number of event in this Cat =", counterCat4)
    print("\n 5. Competition & Tournament\n", "Number of event in this Cat =", counterCat5)
    print("\n 6. Others\n", "Number of event in this Cat =", counterCat6)
    eventdb.close()
    adminOption()


def adminViewEvent():
    eventdb = open("eventList.txt", "r")
    counter = 1
    print("here are all the event & their details:")
    for i in eventdb: # a clean ui that presents all available event in the eventList.txt file
        a,b,c,d,e,f,g,h = i.split(", ")
        print(counter,"|", b, "\nCategory:", a, "\nOrganizer:", c, "\nDate:", d, "\nTime:", e, "\nDuration:", f, "\nVenue:", g, "\nPrice (RM):", h, "\n")
        counter += 1
    eventdb.close()
    adminOption()


def adminViewCustomerList():
    memberdb = open("memberList.txt", "r")
    counter = 1
    print("here are all the members:")
    for i in memberdb:
        a,b = i.split(", ")
        print(counter,"|", a)
        counter += 1
    memberdb.close()
    adminOption()


def adminViewCustomerPayment():
    paymentdb = open("cartList.txt", "r")
    counter = 1
    print("here are all the payment details:")
    for i in paymentdb:
        a,b,c = i.split(", ")
        print(counter,"|", "\nMember Name:", a, "\nEvent Registered:", b, "\nPayment details:", c)
        counter += 1
    paymentdb.close()
    adminOption()


def adminSearchCustomerInfo():
    search = input("Enter customer username to search: ")
    searchdb = open("memberList.txt", "r")
    searchList = searchdb.readlines()
    flag = False
    searchdb.close()
    for i in range(0, len(searchList)): # looping algorithm to find the sequence where memberName is present
        searchTemp = searchList[i].split(", ")
        if search in searchTemp:
            flag = True
        else:
            pass

    if flag:
        print(search, "is a member of Asian Event Management Service")
    else:
        print(search, "is NOT a member of Asian Event Management Service")
    adminOption()


def adminSearchCustomerPayment():
    search = input("Enter customer username to search payment details: ")
    search = search.capitalize() # all usernames are saved with capitalize in events by default
    checkIndexList = []
    a = '1' # these are used as positive flags
    b = '0' # these are used as negative flags
    print("\n=== Here are the payment details for", search, "===")
    checkdb = open("cartList.txt", "r")
    checkList = checkdb.readlines()
    checkdb.close()
    for i in range(0, len(checkList)): # looping algorithm to find the sequence where memberName is present
        tempCheck = checkList[i].split(", ")
        if search in tempCheck:
            checkIndexList.append(a)
        else:
            checkIndexList.append(b)
    for i in range(0, len(checkIndexList)):
        if '1' in checkIndexList:
            x = checkIndexList.index('1')
            print(checkList[x].replace('\n',''))
            checkIndexList[x] = '0'
        else:
            pass
    adminOption()


def guestViewEvent():
    eventdb = open("eventList.txt", "r")
    counter = 1
    print("\nhere are all the event & their details: \n")
    for i in eventdb:
        a,b,c,d,e,f,g,h = i.split(", ")
        print(counter,"|", b, "\nCategory:", a, "\nOrganizer:", c, "\nDate:", d, "\nTime:", e, "\nDuration:", f, "\nVenue:", g, "\nPrice (RM):", h, "\n")
        counter += 1
    eventdb.close()
    back = input("press <enter> to return")
    if back == "":
        guestOption()
    else:
        guestOption()


def guestViewCategory():
    print("\nhere are the available event categories: \n")
    print("1. Sports & Martial Arts")
    print("2. Musical Performance")
    print("3. Dance & Performing Arts")
    print("4. Expo & Exhibition")
    print("5. Competition & Tournament")
    print("6. Others\n")
    back = input("press <enter> to return")
    if back == "":
        guestOption()
    else:
        guestOption()


def memberSignup():
    memberHandler = open("memberList.txt", "r")
    print(">>> Welcome to AEMS member registration page, please follow the instruction below <<<")
    username = input("Enter a username: ")
    password1 = input("Enter a password: ")
    password2 = input("Confirm your password: ")

    # database
    memberUN = []
    memberPW = []
    for i in memberHandler:
        a,b = i.split(", ")
        b = b.strip()
        memberUN.append(a)
        memberPW.append(b)

    if password1 != password2:
        print("Password does not match, please try again")
        memberSignup()
    elif len(password1) <= 8:
        print("Password must be longer than 8 characters, please try again")
        memberSignup()
    elif username in memberUN:
        print("Username already taken, please try again")
        memberSignup()
    else:
        db = open("memberList.txt", "a")
        db.write(username+", "+password1+"\n")
        print("Registration Successful!")
        db.close()
    memberHandler.close()
    guestOption()


def memberLogin():
    dt_today = str(datetime.datetime.today())
    tempList = []
    memberHandler = open("memberList.txt", "r")
    while True:
        print(">>> Member Login Page <<<")
        memberUN = input("Enter your username: ")
        memberPW = input("Enter your password: ")
        for i in memberHandler: # search database for users
            tempList.append(i)
        if memberUN + ", " + memberPW + "\n" in tempList:
            print("Login successful!")
            print("Welcome back,", memberUN.capitalize())
            memberName = memberUN.capitalize() # we saved their username as memberName
            cartItems = []
            cartTotal = 0

            while True:
                # option
                print("\nwhat would you like?")
                print("1. Add events to Shopping Cart")
                print("2. View purchased events")
                print("3. Exit")
                answer = int(input("Your Choice: "))

                if answer == 1: #add + payment + write
                    while True:
                        counter = 1
                        print("Which event would you like to add?")
                        eventdb = open("eventList.txt", "r")
                        for i in eventdb:
                            a,b,c,d,e,f,g,h = i.split(", ")
                            print(counter,"|", b)
                            counter += 1
                        eventdb.close()

                        # obtain user choice
                        try:
                            selection = int(input("Your choice: "))
                            if selection in range(0, counter):
                                selection -= 1
                                pass
                            else:
                                print("\n>>> selected value out of bound, try again\n")
                                continue

                        except ValueError:
                            print("\n>>> please insert an integer value\n")
                            continue

                        # open the eventlist to extract that specific event
                        itemdb = open("eventList.txt", "r")
                        itemList = itemdb.readlines()
                        itemIndex = itemList[selection].split(", ")
                        addItem = itemIndex[1]
                        itemPrice = itemIndex[7].replace('\n','') # prevents double spacing
                        itemPrice = float(itemPrice)
                        itemdb.close()

                        cartItems.append(addItem)
                        cartTotal += itemPrice
                        choose = input("do you want to add more items? <Y/N>")
                        if choose == "Y":
                            continue
                        elif choose == "N":
                            print("proceeding to payment...")
                            break
                        else:
                            print("option not supported, proceeding to payment")
                            break # add cart

                    while True:
                        print("total amount dued: ", cartTotal)
                        try:
                            payment = float(input("please enter your payment amount: "))
                            if payment == cartTotal:
                                print("payment successful!")
                                summaryPrice = str(cartTotal)
                                balance = 0.00
                                break
                            elif payment < cartTotal:
                                print("insufficient amount, please try again")
                                continue
                            elif payment > cartTotal:
                                balance = payment - cartTotal
                                print("payment successful! RM", balance, "have been returned to your account")
                                summaryPrice = str(cartTotal)
                                break
                            else:
                                print("please insert a valid number")
                                continue # payment
                        except ValueError:
                            print("\n>>> please insert a valid amount!\n")
                            continue

                    print("\nOrder Summary:")
                    print("You bought:", cartItems)
                    print("Total cost:", cartTotal)
                    print("You paid:", payment)
                    print("Balance returned:", balance)
                    print("order completed! thank you for your support!")
                    print('')
                    eventdb.close()

                    cartdb = open("cartList.txt", "a")
                    for i in cartItems:
                        cartdb.write(memberName+", "+i+", "+"paid on "+dt_today+"\n")
                    cartdb.close()
                    continue


                elif answer == 2:
                    checkIndexList = []
                    a = '1' # these are used as positive flags
                    b = '0' # these are used as negative flags
                    print("\n=== Here are all your registered events ===")
                    checkdb = open("cartList.txt", "r")
                    checkList = checkdb.readlines()
                    checkdb.close()
                    for i in range(0, len(checkList)): # looping algorithm to find the sequence where memberName is present
                        tempCheck = checkList[i].split(", ")
                        if memberName in tempCheck:
                            checkIndexList.append(a)
                        else:
                            checkIndexList.append(b) # output is a list like this [1,0,0,1,0,1] where 1 means member is present in record

                    for i in range(0, len(checkIndexList)):
                        if '1' in checkIndexList:
                            x = checkIndexList.index('1') # with the algorithm, we can simply print the line where the corresponding memberName is present
                            print(checkList[x].replace('\n','')) # this is to remove to 'new line' feature to prevent double spacing during output
                            checkIndexList[x] = '0' # then we replace the '1' in the algorithm to '0' after printing the values
                        else:
                            pass
                    continue

                elif answer == 3:
                    exitPage()

                else:
                    print("choice not supported, try again")
                    continue

                break
        else:
            print("\n >>> invalid credentials... \n")
            option = input("would you like to sign-up? \n [Y] for membership registration \n [N] to retry login \n Your choice: " )
            if option == "N":
                continue #repeat while loop
            elif option == "Y":
                memberSignup()
            else:
                print("invalid option, returning to homepage...")
                homepage()
        break
    memberHandler.close()


def exitPage():
    print("\nYou have exited the application")
    print("Thank you for using our services!")


homepage() #initiate this upon launching AEGIS
# admin authentication referral code = AEMS0001
# total function = 20
# total lines = 717
