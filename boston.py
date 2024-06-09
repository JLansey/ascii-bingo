# Boston themed bingo words
sorted_list = [
    "Red Sox", "The Sox", "Clam Chowder",
    "MIT", "Bunker Hill","Sam Adams","Harpoon", "Medford", "Somerville", "Cambridge",
    "Charles River", "Southie", "Freedom Trail","Boston University",
    "The Common", "The North End", "Wicked", "Dunkin", "CVS", "Irish", "Italian",
    "Lobstah", "The Patriots", "The Celtics", "The Bruins", "Loud Bicycle", "Market Basket",
    "Masshole", "haav'd ya'd", "Harvard",
    "The Greenway", "The emerald necklace",
    "The Charles",
    "Mass General", "Fenway",
    "Sweet Caroline ...",
    "JPlicks", "The Pru",
    "why is it this cold",
    "The T", "Blue Line", "Green Line", "Red Line", "Orange Line", "Charlie Card",
    "Beacon Hill", "Back Bay", "Brookline", "The Harbor", "Logan", "which way is it to *",
    "Quincy Market", "Faneuil Hall", "Newbury Street", "Sma'aht","Paul Revere",
     "The Cape", "Martha's Vineyard", "Nantucket", "Boston Tea Party", "Red line is down/delayed", "Green line is down/delayed",
    "Patriots day", "Lincoln Labs", "Boston Marathon",
    "Ben Affleck", "Mark Wahlberg", "i-robot", "Boston Dynamics", "pahk the cah in haav'd ya'd"
]

constraints = [
    {"Red Sox", "The Patriots", "The Celtics", "The Bruins", "The Sox", "Fenway"},  # Boston sports teams.
    {"Clam Chowder", "Lobstah"},  # Iconic Boston foods.
    {"Freedom Trail", "Bunker Hill"},  # Historical sites.
    {"Medford", "Somerville", "Cambridge"}, # cool neighborhoods
    {"Irish", "Italian"},
    {"Blue Line", "Green Line", "Red Line", "Orange Line"},  # T lines.
    {"Beacon Hill", "Back Bay", "Southie", "Brookline"},  # Neighborhoods.
    {"Boston Common", "Boston Public Garden"},  # Public parks.
    {"Quincy Market", "Faneuil Hall"}, # Tourist spots
    {"Sam Adams", "Paul Revere"},  # Old people related.
    {"Big Dig", "Mass Pike"},  # Infrastructure.
    {"Ben Affleck","Mark Wahlberg"},
    {"Red line is down/delayed", "Green line is down/delayed"},
    {"i-robot", "Boston Dynamics"},
    {"Beantown", "The Hub of the Universe"},
    {"blue bikes", "bike lane"},
    {"Patriots day", "Boston Marathon"},
    {"pahk the cah in haav'd ya'd", "haav'd ya'd", "Harvard"}
]

center_word = None

# https://patorjk.com/software/taag/#p=display&f=Slant&t=Boston%20BINGO
ascii_art_header = '''    ____             __                 ____  _____   ____________ 
   / __ )____  _____/ /_____  ____     / __ )/  _/ | / / ____/ __ \\
  / __  / __ \/ ___/ __/ __ \/ __ \   / __  |/ //  |/ / / __/ / / /
 / /_/ / /_/ (__  ) /_/ /_/ / / / /  / /_/ // // /|  / /_/ / /_/ / 
/_____/\____/____/\__/\____/_/ /_/  /_____/___/_/ |_/\____/\____/  
'''
