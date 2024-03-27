# NYC themed bingo words
sorted_list = [
    "Statue of Liberty", "Empire State Building", "Times Square", "Central Park", "Broadway",
    "Bagel", "Subway", "Yankees", "Mets", "Knicks", "Hot Dog",
    "Uptown", "Midtown", "Downtown", "Expensive", "Sushi", "Elevator", "Penn Station", "Grand Central",
    "Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island",
    "Pizza", "Cab", "Fifth Avenue", "Wall Street", "MTA", "New Jersey", "Connecticut",
    "The Met", "Guggenheim", "Schlep", "Hutzpah",
    "Grand Central", "Chrysler Building", "High Line", "Rockefeller Center", "World Trade Center",
    "Kvetch", "Kibbitz", "Lincoln Tunnel",
    "Chinatown", "Little Italy", "Harlem", "The village", "American Museum of Natural History",
    "Central Park Zoo", "Brooklyn Bridge", "Coney Island", "Madison Square Garden", "FAO Schwarz"
]

constraints = [
    {"Yankees", "Mets"},  # NYC baseball teams.
    {"Knicks", "Nets"},  # NYC basketball teams.
    {"Schlep", "Hutzpah", "Kvetch", "Kibbitz"}, # Yiddish
    {"Brooklyn", "Manhattan", "Queens", "Bronx", "Staten Island"},  # Boroughs.
    {"Penn Station", "Grand Central"},
    {"Bagel", "Pizza", "Hot Dog", "Sushi"},  # Iconic NYC foods.
    {"Uptown", "Midtown", "Downtown"},
    {"Empire State Building", "Chrysler Building", "World Trade Center"},  # Skyscrapers.
    {"Central Park", "High Line", "Central Park Zoo"},  # Public parks.
    {"Times Square", "Broadway"},  # Entertainment.
    {"Statue of Liberty", "Ellis Island"},  # Monuments.
    {"Wall Street", "Federal Reserve"},  # Financial districts.
    {"New Jersey", "Connecticut"},
    {"The Met", "Guggenheim", "American Museum of Natural History"}
    ]

center_word = None

ascii_art_header = '''    _   ____  ________   ____  _____   ____________ 
   / | / /\ \/ / ____/  / __ )/  _/ | / / ____/ __ \\
  /  |/ /  \  / /      / __  |/ //  |/ / / __/ / / /
 / /|  /   / / /___   / /_/ // // /|  / /_/ / /_/ / 
/_/ |_/   /_/\____/  /_____/___/_/ |_/\____/\____/  
'''
