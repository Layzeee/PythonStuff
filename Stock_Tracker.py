#Dylan Joel Lim Wei Han, 185540R, IT2153-04
#stockItems object
class stockItems:
    def __init__(self, id, name, price, quantity, expiry):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
        self.expiry = expiry

#sample List
stockList = [stockItems(3691234,"Apple", 3, 1000000, "11/11/1999"),stockItems(36912, "Orange", 246, 1000000, "11/11/1999"),stockItems(369123456,"Milk", 369, 1000001, "11/11/1999"),stockItems(369144, "Wine", 69, 1000000, "11/11/1999")]
#Insertion sort function
def insertionSort( theSeq ):
    n = len( theSeq )

    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]

        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value.id < theSeq[pos - 1].id:
            # Shift the items to the right during the search
                theSeq[pos] = theSeq[pos-1]
                pos -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = value

# Sorts a sequence in ascending order using
# the bubble sort algorithm
def bubbleSort( theSeq ):
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
    # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j].id > theSeq[j + 1].id:
            # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

# A recursive implementation of Binary Search
def recBinarySearch( target, theValues, low, high ):
    # If the sequence of values cannot be subdivided further,
    # we are done
    if low > high: # BASE CASE #1
        return -1

    else:
        # Find the midpoint of the sequence
        mid = (low + high) // 2 # or int((low + high) / 2)
        
        # Does the element at the midpoint contain the target?
        if theValues[mid].id == target:
            return mid # BASE CASE #2
        
        # or does the target precede the element at the midpoint?
        elif target < theValues[mid].id:
            return recBinarySearch(target, theValues, low, mid - 1)
        
        # or does the target follows the element at the midpoint?
        else:
            return recBinarySearch(target, theValues, mid + 1, high)

#grocerMenu Function
def grocerMenu():
    #Prints Menu
    print("Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Items")
    print("4. Sort/Search")
    print("5. Total and Average Stock")
    get_input = input("Enter Number: ")

    if get_input == "1": #add new product as object to the list
        try:
            a = int(input("Enter Product ID: "))
            b = input("Enter Item Name: ")
            c = int(input("Enter Price: $"))
            d = int(input("Enter Quantity: "))
            e = input("Enter Expiry: ")
            stockList.append(stockItems(a,b,c,d,e))
        except:
            print("Invalid Product")
            return grocerMenu()

    elif get_input == "2": #remove item from the list
        a = input("Enter Item Name: ")
        for i in stockList:
            if i.name == a:
                stockList.remove(i)

    elif get_input == "3": #display all items in list
        for i in stockList:
            print("\n"+str(i.id) + "\n" + i.name+"\n"+ "$" + str(i.price) + "\n" + str(i.quantity) + "\n" + i.expiry)

    elif get_input == "4": #to sort and search the list
        sortType = input("Enter Type of sort (Bubble or Insertion): ")
        if sortType == "Bubble":
            bubbleSort(stockList)
        elif sortType == "Insertion":
            insertionSort(stockList)
        else:
            print("Invalid Type")
            return grocerMenu()
        try:
            searchTarget = int(input("Enter Search ID: "))
        except:
            print("Invalid Number")
            return grocerMenu()
        t = stockList[recBinarySearch(searchTarget, stockList, 0, len(stockList) - 1)]
        print("\n" +str(t.id) + "\n" + t.name+"\n"+ "$" + str(t.price) + "\n" + str(t.quantity) + "\n" + t.expiry + "\n")
    
    elif get_input == "5":
        total = 0
        for i in stockList:
            total += i.quantity
        average = str(total // len(stockList))
        print("Total stock: " + str(total) + "\n" + "Average stock: " + average)

    else: #invalid input
        print("Invalid Number")
    return grocerMenu()

grocerMenu()