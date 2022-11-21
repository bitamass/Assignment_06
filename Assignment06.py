#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Bmassoudi, 2021-Nov-19, added functions and docstrings
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strID = int()
intID = int()
strTitle= ''
strArtist=''
table=[]
intRowNr=int()
          
# -- PROCESSING -- #
class DataProcessor:
    """Processing the data in the memory"""
      # TODONE add functions for processing here
      # 3.3.1 Ask user for new ID, CD Title and Artist
      # TODONE move IO code into function
    def CD_appendRow(strID, strTitle, strArtist): 
        """function to append input data into dict.
        Args:
            'ID': intID, 'Title': strTitle, 'Artist': strArtist 
            data to be appended into memory
        Return:
            None
        """   
       #3.3.2 Add item to the table
       # TODONE move processing code into function
        print(strTitle,strArtist)
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}     
        lstTbl.append(dicRow)
         
          #for row in lstTbl:
              #print ('{}\t{} (by:{})'.format(*row.values()))
          #print('======================================')
          #IO.show_inventory(lstTbl)
        
          #return lstTbl
           # start loop back at top.
          
        # TODONE move processing code into function
    def delete_file (table):
          """Function to delete data from user input from dic.
          Args:
              intIDDel-ID number to be deleted
          Returns:
                  None
              """
          #3.5.1 get Userinput for which CD to delete
          # 3.5.1.1 display Inventory to user
          #IO.show_inventory(lstTbl)
          # 3.5.1.2 ask user which ID to remove
          intIDDel = int(input('Which ID would you like to delete? ').strip())
          print('you have chosen to delete CD # ',intIDDel)
          # 3.5.2 search thru table and delete CD
          #TODONE move processing code into function
          # Delete the row which matches the input ID value
          intRowNr = -1
          blnCDRemoved = False
          for row in table:
              intRowNr += 1
              if int(row['ID']) == intIDDel:
                  del table[intRowNr]
                  blnCDRemoved = True
                  break
          if blnCDRemoved:
              print('The CD # ',intIDDel,' was removed')
          else:
              print('Could not find this CD!')
          return table

class FileProcessor:
    """Processing the data to and from text file"""
    
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        #lstTbl.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': data[0], 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
            #print(table)
            #print(lstTbl)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """Function to copy the contents of Python memory to text file.
        Args:
            file_name (string)
            table (list of dict) 
        return:
            none
        """
        #TODONE Add code here
        # 3.6.1 Display current inventory and ask user for confirmation to save
        #strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        #if strYesNo == 'y':
        # 3.6.2.1 save data
        # TODONE move processing code into function
        objFile = open(file_name, 'w')
        for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
        objFile.close()
            #else:
                #input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        return

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TODONE add I/O functions as needed
    @staticmethod
    def add_file():
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
       # print(strID, strTitle,strArtist)
        return strID, strTitle, strArtist


# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop

while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
            break
    # 3.2 process load inventory
    if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileProcessor.read_file(strFileName, lstTbl)
                IO.show_inventory(lstTbl)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstTbl)
            continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        A1, A2, A3= IO.add_file()
        DataProcessor.CD_appendRow(A1, A2, A3)
        continue

    # 3.4 process display current inventory 
    elif strChoice == 'i':
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
            # 3.5.1 get Userinput for which CD to delete
            # 3.5.1.1 display Inventory to user
           IO.show_inventory(lstTbl)
          # intIDDel = int(input('Which ID would you like to delete? ').strip())
           DataProcessor.delete_file(lstTbl)
           continue  # start loop back at top.

    # 3.6 process save inventory to file
    elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstTbl)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                FileProcessor.write_file(strFileName, lstTbl)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.


    print('General Error')




