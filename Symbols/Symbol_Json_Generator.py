import json

data = {
    "FILENAMES_LIST": ['Keypad01.png', 'Keypad02.png', 'Keypad03.png', 'Keypad04.png', 'Keypad05.png', 'Keypad06.png',
                       'Keypad07.png', 'Keypad08.png', 'Keypad09.png', 'Keypad10.png', 'Keypad11.png', 'Keypad12.png',
                       'Keypad13.png', 'Keypad14.png', 'Keypad15.png', 'Keypad16.png', 'Keypad17.png', 'Keypad18.png',
                       'Keypad19.png', 'Keypad20.png', 'Keypad21.png', 'Keypad22.png', 'Keypad23.png', 'Keypad24.png',
                       'Keypad25.png', 'Keypad26.png', 'Keypad27.png', 'Keypad28.png', 'Keypad29.png', 'Keypad30.png',
                       'Keypad31.png'],
    "NAMES_LIST": ["copyright", "filledstar", "hollowstar", "smileyface", "doublek", "omega", "squidknife", "pumpkin",
                   "hookn", "teepee", "six", "squigglyn", "at", "ae", "metledthree", "euro", "circle", "nwithat",
                   "dragon",
                   "questionmark", "paragraph", "rightc", "leftc", "pitchfork", "tripod", "cursive", "track", "ballon",
                   "weirdnose", "upsidedowny", "bt"]
}
file = open("Symbols_Data.json", "w")
json_data = json.dumps(data, indent=4)
file.write(json_data)
file.close()