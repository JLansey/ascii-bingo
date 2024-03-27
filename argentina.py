# This list should be sorted in order of difficulty for there to be even difficulty across the different sheets
sorted_list = [
    "Mate", "Vos", "Sos", "Re", "Che", "Dale", "Boludo", "Parrilla", "Asado", "Alfajor", "Dulce de leche", "Milanesa",
    "Obvio", "Fernet",
    "Medialuna", "Quilombo", "Tranqui", "Subte / Sube", "Boliche", "Merienda", "Buena onda", "Que onda", "Empanada",
    "Chongx", "Chamuyx", "La Plata", "Bariloche", "Rosario", "Cordoba", "Mendoza", "Santa Fe", "Patagonia",
    "Iguazu", "Kiosco", "Ushuaia", "Antarctica", "Uruguay", "Claro", "Tango", "Milonga", "La Boca",
    "Boca/River", "Belgrano", "Palermo", "Ecobici", "Milei", "Trump", "Palta", "Posho", "Messi", "Chipa / Chipas",
    "Medialuna/s de grassa", "Nueva Shork", "Shanqui", "Capital Federal", "Provincia de Buenos Aires", "Tini",
    "Recoleta", "Cachengue",
    "Flashero", "Hijo de puta", "Guapetón", "Moises Villa", "Dale dale", "Guanaco", "Vicuña", "Llama", "Voy a ir yendo",
    "La concha de tu madre", "La concha de la lora", "Tereré", "Peron", '"no hay plata"', "Frutilla", "Shanquilandia",
    "Boludeces", "Movistar", "Mundo Lingo",
    "WOWISIMO"
]

constraints = [
    {"Vos", "Sos"},  # Variants in language usage.
    {"Mate", "Tereré"},  # Variants of a common drink.
    {"Boludo", "Boludeces"},  # Related slang.
    {"Parrilla", "Asado"},  # Related culinary terms.
    {"Medialuna", "Medialuna/s de grassa"},  # Variants of a food item.
    {"La Boca", "Boca/River"},  # Geographical area and related football rivalry.
    {"Capital Federal", "Provincia de Buenos Aires"},  # Geographical locations.
    {"La concha de tu madre", "La concha de la lora"},  # Insults and their variants.
    {"Milei", "Trump"},  # Public figures known for polarizing opinions.
    {"Rosario", "Santa Fe"},  # Cities within the same province.
    {"Bariloche", "Patagonia"},  # Touristic spots, one within the other.
    {"Iguazu", "Ushuaia", "Antarctica"},  # Distant or unique Argentine locations.
    {"Cordoba", "Mendoza"},  # Major cities, often compared.
    {"Palta", "Frutilla"},  # Common food items.
    {"Dale", "Dale dale"},  # Variants of a common expression.
    {"Shanquilandia", "Shanqui"},
]

# this word will appear once in the center of every card
# set to None if you want the center word to be randomly selected instead
center_word = "WOWISIMO"

# https://patorjk.com/software/taag/#p=display&f=Slant&t=boludo%20BINGO
ascii_art_header = '''    __          __          __         ____  _____   ____________ 
   / /_  ____  / /_  ______/ /___     / __ \/  _/ | / / ____/ __ \\
  / __ \/ __ \/ / / / / __  / __ \   / /_/ // //  |/ / / __/ / / /
 / /_/ / /_/ / / /_/ / /_/ / /_/ /  / /_/ // // /|  / /_/ / /_/ / 
/_.___/\____/_/\__,_/\__,_/\____/  /_____/___/_/ |_/\____/\____/ ®
'''

