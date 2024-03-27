# Boston themed bingo words
sorted_list = [
    "Red Sox", "Clam Chowder", "Fenway", "Harvard",
    "MIT", "Bunker Hill","Sam Adams","Harpoon", "Medford", "Somerville", "Cambidge",
    "Charles River", "Southie", "Freedom Trail","Boston University",
    "Boston Common", "North End", "Wicked", "Dunken", "CVS", "Irish", "Italian",
    "Lobstah", "Patriots", "Celtics", "Bruins", "Whicked", "Loud Bicycle",
    "The T", "Blue Line", "Green Line", "Red Line", "Orange Line", "Charlie Card",
    "Beacon Hill", "Back Bay", "Brookline", "The Harbor", "Lincoln Labs", "Logan",
    "Quincy Market", "Faneuil Hall", "Newbury Street", "Copley", "Smaaht","Paul Revere",
     "The Cape", "Martha's Vineyard", "Nantucket", "Boston Tea Party", "Red line is down/delayed", "Green line is down/delayed",
    "Ben Affleck", "Mark Wahlberg", "i-robot", "Boston Dynamics"
]

constraints = [
    {"Red Sox", "Patriots", "Celtics", "Bruins"},  # Boston sports teams.
    {"Clam Chowder", "Lobstah"},  # Iconic Boston foods.
    {"Freedom Trail", "Bunker Hill"},  # Historical sites.
    {"Fenway Park", "Boston Marathon"},  # Iconic Boston events/locations.
    {"Medford", "Somerville", "Cambidge"}, # cool neighborhoods
    {"Harvard", "MIT"},  # Universities.
    {"Irish", "Italian"},
    {"Blue Line", "Green Line", "Red Line", "Orange Line"},  # T lines.
    {"Beacon Hill", "Back Bay", "Southie", "Brookline"},  # Neighborhoods.
    {"Boston Common", "Boston Public Garden"},  # Public parks.
    {"Quincy Market", "Faneuil Hall"}, # Tourist spots
    {"Sam Adams", "Paul Revere"},  # Old people related.
    {"Big Dig", "Mass Pike"},  # Infrastructure.
    {"Ben Affleck","Mark Wahlberg"},
    {"Red line is down/delayed", "Green line is down/delayed"},
    {"i-robot", "Boston Dynamics"}
]

center_word = None

# https://patorjk.com/software/taag/#p=display&f=Slant&t=Boston%20BINGO
ascii_art_header = '''    ____             __                 ____  _____   ____________ 
   / __ )____  _____/ /_____  ____     / __ )/  _/ | / / ____/ __ \\
  / __  / __ \/ ___/ __/ __ \/ __ \   / __  |/ //  |/ / / __/ / / /
 / /_/ / /_/ (__  ) /_/ /_/ / / / /  / /_/ // // /|  / /_/ / /_/ / 
/_____/\____/____/\__/\____/_/ /_/  /_____/___/_/ |_/\____/\____/  
'''
