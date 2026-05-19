import pandas as pd

contacts = {
    "name": ["Bart", "Lisa", "Homer", "Marge"],
    "age": [10, 8, 39, 36],
    "phone_number": ["939-555-0113", "939-555-0114", "939-555-0115", "939-555-0116"],
    "astrological_sign": ["Taurus", "Virgo", "Virgo", "Pisces"],
}

df = pd.DataFrame(contacts)

df
# ==============================================================================
app_data = {
    "app_name": [
        "YouTube",
        "TikTok",
        "Instagram",
        "Spotify",
        "Duolingo",
        "Twitter",
        "Headspace",
        "Discord",
        "Depop",
    ],
    "category": [
        "Video",
        "Social Media",
        "Social Media",
        "Music",
        "Education",
        "Social Media",
        "Health",
        "Communication",
        "Shopping",
    ],
    "rating": [4.7, 4.6, 4.5, 4.6, 4.7, 4.3, None, 4.7, 4.4],
    "downloads_millions": [5000, 3000, 3500, 2000, None, 1500, 500, 600, 200],
}
apps = pd.DataFrame(app_data)

apps.head()
apps.tail()
apps.info()
apps.describe(include="all")
# ==============================================================================
characters_data = {
    "name": [
        "Thorne",
        "Elira",
        "Glim",
        "Brug",
        "Nyx",
        "Kael",
        "Mira",
        "Drogan",
        "Zara",
        "Fenwick",
    ],
    "race": [
        "Elf",
        "Human",
        "Gnome",
        "Half-Orc",
        "Tiefling",
        "Dragonborn",
        "Halfling",
        "Dwarf",
        "Aasimar",
        "Goblin",
    ],
    "class": [
        "Ranger",
        "Cleric",
        "Wizard",
        "Barbarian",
        "Rogue",
        "Paladin",
        "Bard",
        "Fighter",
        "Sorcerer",
        "Warlock",
    ],
    "level": [5, 3, 4, 2, 6, 7, 3, 5, 4, 2],
    "hp": [42, 28, 33, 25, 48, 56, 30, 44, 36, 24],
    "alignment": [
        "Chaotic Good",
        "Lawful Good",
        "Neutral",
        "Chaotic Neutral",
        "Chaotic Evil",
        "Lawful Neutral",
        "Neutral Good",
        "Neutral",
        "Chaotic Good",
        "Lawful Evil",
    ],
}
characters = pd.DataFrame(characters_data)
characters

characters_names = characters["name"]
basic_stats = characters[["name", "level", "hp"]]
basic_stats

alignment_removed = characters.drop("alignment", axis=1)
alignment_removed
