# Build a data processing program

# Read data from a csv file, then store that in an SQLite DB
# Query the DB for analysis (top grossing movies, top audience scores, etc)
# Generate a Word document report with tables
# Export the results to JSON format

import csv, sqlite3

def read_csv_file_into_db():
    movie_file_path = 'C:/OKCoders_Pro_Python/movies.csv'

    # Read data from the csv file
    movie_file = open(movie_file_path)
    movie_file_reader = csv.reader(movie_file)
    movie_data_list = list(movie_file_reader)

    store_movie_data_in_sqlitedb(movie_data_list)

def store_movie_data_in_sqlitedb(data_list):
    # isolation_level specifies how changes to the db are committed. In this case, specifying None tells sqlite to auto-commit each transaction, so we do not have to manually call commit() each time we want to save data in the db or update something
    movie_database = sqlite3.connect('movie_data.db', isolation_level = None)
    
    movie_database.execute(f'CREATE TABLE IF NOT EXISTS movie_data (Film TEXT NOT NULL, Genre TEXT, Lead_Studio TEXT, Audience_Score_Pct TEXT, Profitability TEXT, Rotten_Tomatoes_Pct TEXT, Worldwide_Gross TEXT, Release_Year TEXT)')

    # Get the data for each movie, from the data_list that is passed in, starting art the list at index 1. So here, data gets a list of nested lists, beginning at index 1 in the data_list coming in
    data = data_list[1:]

    # Insert the data into the db. The function executemany() allows us to specify a parameterized query for each nested list in data above. When the function runs with the given arguments, it will automatically loop through all nested lists and input the data from them as specified by the question marks. Remember to close the connection once done.
    movie_database.executemany('INSERT INTO movie_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
    
    movie_database.execute('DELETE FROM movie_data WHERE rowid NOT IN (SELECT MIN(rowid) FROM movie_data GROUP BY Film);')

    movie_database.close()
    
def show_top_ten_grossing_movies_worldwide():
    movie_db = sqlite3.connect('movie_data.db', isolation_level = None)
    
    query = '''
        SELECT Film, Genre, Worldwide_Gross
        FROM movie_data
        ORDER BY CAST(REPLACE(Worldwide_Gross, '$', '') AS REAL) DESC
        LIMIT 10;
    '''
    
    top_grossing_rows = movie_db.execute(query).fetchall()
    
    print('\nShowing top ten worldwide-grossing movies from 2007-2011, in descending order:\n')
    
    for film, genre, gross_profit in enumerate(top_grossing_rows):
        print(f'{film} ({genre}) — {gross_profit} million')
        
    movie_db.close()

def show_top_ten_profitable_movies():
    movie_db = sqlite3.connect('movie_data.db', isolation_level = None)
    
    query = '''
        SELECT Film, Genre, Profitability
        FROM movie_data
        ORDER BY CAST(Profitability AS REAL) DESC
        LIMIT 10;
    '''
    
    top_profitable_rows = movie_db.execute(query).fetchall()
    
    print('\nShowing top ten profitable movies from 2007-2011, in descending order. The higher the profitability ratio, the more profit the movie made.\n')
    
    for film, genre, profit in top_profitable_rows:
        print(f'{film} ({genre}) — Profitability: {float(profit):.2f}')
        
    movie_db.close()
    
def movies_by_top_ten_audience_percentages():
    movie_db = sqlite3.connect('movie_data.db', isolation_level = None)
    
    query = '''
        SELECT Film, Genre, Audience_Score_Pct
        FROM movie_data
        ORDER BY CAST(Audience_Score_Pct AS INTEGER) DESC
        LIMIT 10;
    '''
    
    audience_percentage_rows = movie_db.execute(query).fetchall()
    
    print('Showing movies with the top 10 audience score percentages\n:')
    
    for film ,genre, audience_percentage in audience_percentage_rows:
        print(f'{film} ({genre}) - {audience_percentage}%')
        
    movie_db.close()

def print_movie_db():
    movie_db = sqlite3.connect('movie_data.db', isolation_level = None)
    rows = movie_db.execute('SELECT * FROM movie_data').fetchall()
   
    for row in rows:
        print(row) # prints each tuple (row) in the db
        
def show_user_options():
    print('\nWelcome! Please choose from the following options (enter "q" anytime to quit):\n')
    
    print('''
          1. Show 
          ''')
    
def show_user_menu():
    # Storing menu option in this dictionary; allow for additional choices to be added later if required
    menu_options = {
        "1": ('Show top 10 worldwide-grossing movies', show_top_ten_grossing_movies_worldwide),
        "2": ('Show top 10 profitable movies', show_top_ten_profitable_movies),
        "3": ('Show movies by top 10 audience percentages', movies_by_top_ten_audience_percentages),
        "4": ('Print all movie data', print_movie_db),
    }
    
    print('Welcome! This program allows you to load a movie database and perform select actions with that data. Enter "q" anytime to quit.\n')

    while True:
        # Show menu options
        for key, (label, _) in menu_options.items():
            print(f'{key}. {label}')

        choice = input("\nEnter your choice here: ").strip()

        if choice.lower() == "q":
            break

        # Validate menu choice
        if choice not in menu_options:
            print("Invalid option — please choose a valid number.")
            continue
        
        # menu_options[choice] returns a tuple, from which you can select the label and the function, based on which option (choice) the user selected
        selected_label, selected_function = menu_options[choice]

        print(f'\nYou selected: {selected_label}\n')
        selected_function() # Run the function selected by the user/chosen from the menu
        
        print('\nKeep choosing, or q to quit:\n')

if __name__ == '__main__':
    show_user_menu()
