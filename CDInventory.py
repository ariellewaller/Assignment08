#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AWaller, 2020-September-02, copy and paste class and static method code blocks from assignment07.
# Awaller, 2020-September-02, change all references of lstTbl to lstOfCDObjects.
# Awaller, 2020-September-02, change strFileName to .dat extension. 
# Awaller, 2020-September-02, Add code to custom CD class, creating constructor and properties. 
# Awaller, 2020-September-02, Modify show_inventory method to work with list of CD objects. 
# Awaller, 2020-September-02, Call the attribute for cd_id directly in the constructor. 
# Awaller, 2020-September-02, Load data from the file into a list of CD objects upon running the script.
#------------------------------------------#

import pickle 

# -- DATA -- #
strFileName = 'CDInventory.dat'
lstOfCDObjects = []

class CD:

    # TOCOMPLETED Add Code to the CD class
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    # CONSTRUCTOR 
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    # PROPERTIES 
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, id_input): 
        if not id_input.isnumeric():
            raise ValueError('The CD ID must be an integer.')
        self.__cd_id = id_input 
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title_input): 
        self.__cd_title = title_input 

    @property
    def cd_artist(self):
        return self.__cd_artist 
    
    @cd_artist.setter
    def cd_artist(self, artist_input): 
        self.__cd_artist = artist_input 
        


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    # TOCOMPLETED Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of
        dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary
        row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime. If intIDDel is found, this list is edited
            to remove the applicable dictionary. 
        """
        # Clear the existing data and allow to load data from file. 
        table.clear() 
        try: 
            # Open the binary data file in read mode. 
            objFile = open(file_name, 'rb')
        except IOError:
            print('File does not exist. Creating a new file...\n')
            # Create a new binary data file if it doesn't already exist.
            objFile = open(file_name, 'wb')
            # Close the file. 
            objFile.close()            
        else: 
            # Unpickle the list of dictionaries stored in the file and assign
            # this list of dictionaries back to table. 
            try:
                table = pickle.load(objFile)
            except EOFError: 
                print("Error! File is empty. You must write data to the file first.")
            # Close the file. 
            objFile.close()
            # Return the table.
            return table 
            
    # TOCOMPLETED Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """Function to write data from the list of dictionaries to a file.
        
        Takes the data from the 2D table and represeents one dictionary row in
        the table as one line in the file. (The values of each dictionary row
        are reperesented as one line in the table)
        
        Args:
            file_name (string): name of file used to write the data to
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.
        Returns:
            None.
        
        """
        # Open the binary file in write mode and assign the file object to a variable.
        objFile = open(file_name, 'wb')
        # Pickle the list of dictionaries (table) and write it as one object to
        # the file. 
        pickle.dump(table, objFile)
        # Close the file. 
        objFile.close()
        
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TOCOMPLETED: Add docstring
    """Handling Input / Output"""

    # TOCOMPLETED add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file')
        print('[a] Add CD')
        print('[i] Display Current Inventory')
        print('[s] Save Inventory to file')
        print('[x] Exit\n')

    # TOCOMPLETED add code to captures user's choice
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

    # TOCOMPLETED add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays a CD from the current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.

         Returns:
             None.

         """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        if table:
            for cd in table:
                print('{}\t{} (by:{})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))
            print('======================================')
        else: 
            print("The inventory is currently empty! Please add a CD first.")

    # TOCOMPLETED add code to get CD data from user
    @staticmethod
    def cd_information():
        """Collect user input for CD information to add CD to the current
        inventory table. 
        
        Args:
            None. 

         Returns:
             strID: string that holds the new CD ID.
             strTitle: string that holds the new CD title.
             strArtist: string that holds the new CD artist.
            """
        # Prompt user for CD information. 
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        # Return a tuple of the collected values. 
        return strID, strTitle, stArtist


# -- Main Body of Script -- #
# TODO Add Code to the main body
        
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects)
IO.show_inventory(lstOfCDObjects)

# Display menu to user
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()


    # show user current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # let user add data to the inventory
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist. TO-DONE: Moved IO code
        # into function.
        # # Unpack the tuple returned from the function. 
        cd_id, title, artist = IO.cd_information()
        # Add CD to the table.
        new_cd = CD(cd_id, title, artist)
        lstOfCDObjects.append(new_cd)
        # Display the new inventory table. 
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TO-DONE: Moved processing code into write_function.
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the\
              Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. \
                          otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            # Re-assign lstOfCDObjects to table returned from read_file method. 
            lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user exit program
    elif strChoice == 'x':
        break
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

