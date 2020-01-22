import sqlite3
from Charpresent import *
from Charview import *
simplewepon = ["Club", "Dagger", "Dart", "Gauntlet", "Heavy Crossbow", "Heavy Mace", "Javelin", "Light Crossbow",
               "Light Mace", "Longspear", "Morningstar", "Punching Dagger", "Quarterstaff", "Shortspear", "Sickle",
               "Sling", "Spear", "Spiked Gauntlet", "Unarmed Strike", "2 Handaxe"]
martialwepon = ["Greataxe", "Armor Spikes", "Throwing Axe", "Battleaxe", "Falchion", "Flail, Heavy", "Flail, Light",
                "Glaive", "Greatclub", "Greatsword", "Guisarme", "Halberd", "Hammer, Light", "Handaxe", "Katana",
                "Lance, Heavy", "Lance, Light", "Longbow", "Longbow, Composite", "Longspear", "Longsword",
                "Pick, Heavy", "Pick, Light", "Ranseur", "Rapier", "Sap", "Scimitar", "Scythe", "Shield Spikes",
                "Shortbow", "Shortbow, Composite", "Sword, Bastard", "Sword, Short", "Trident", "Wakizashi",
                "Waraxe, Dwarven", "Warhammer", "Armor Spikes", "Battleaxe", "Composite Longbow", "Composite Shortbow",
                "Falchion", "Flail", "Glaive", "Greatclub", "Greatsword", "Guisarme", "Halberd", "Handaxe",
                "Heavy Flail", "Heavy Pick", "Heavy Shield", "Kukri", "Lance", "Light Hammer", "Light Pick",
                "Light Shield", "Longbow", "Longsword", "Ranseur", "Rapier", "Sap", "Scimitar", "Scythe", "Short Sword",
                "Shortbow", "Throwing Axe", "Trident", "Warhammer"]
melee = ["Armor Spikes", "Axe, Orc Double""Axe, Throwing", "Battleaxe", "Bolts, Crossbow", "Chain, Spiked", "Club",
         "Dagger", "Dagger, Punching", "Falchion", "Flail, Dire", "Flail, Heavy", "Flail, Light", "Gauntlet",
         "Gauntlet, Spiked", "Glaive", "Greataxe", "Greatclub", "Greatsword", "Guisarme", "Halberd", "Halfspear",
         "Hammer, Light", "Handaxe", "Javelin", "Kama", "Katana", "Kukri", "Kusari-gama", "Lance, Heavy",
         "Lance, Light", "Longspear", "Longsword", "Mace, Heavy", "Mace, Light", "Morningstar", "Nunchaku",
         "Pick, Heavy", "Pick, Light", "Quarterstaff", "Ranseur", "Rapier", "Sap", "Scimitar", "Scythe",
         "Shield Spikes", "Shortspear", "Siangham", "Sickle", "Sword, Bastard", "Sword, Short", "Sword, Two-Bladed",
         "Trident", "Unarmed Strike", "Wakizashi", "Waraxe, Dwarven", "Warhammer", "Armor Spikes", "Arrows",
         "Bastard Sword", "Battleaxe", "Club", "Crossbow Bolts", "Dagger", "Dire Flail", "Dwarven Urgrosh",
         "Dwarven Waraxe", "Falchion", "Flail", "Gauntlet", "Glaive", "Gnome Hooked Hammer", "Greataxe", "Greatclub",
         "Greatsword", "Guisarme", "Halberd", "Handaxe", "Heavy Flail", "Heavy Mace", "Heavy Pick", "Heavy Shield",
         "Kama", "Kukri", "Lance", "Light Hammer", "Light Mace", "Light Pick", "Light Shield", "Longspear", "Longsword",
         "Morningstar", "Nunchaku", "Orc Double Axe", "Punching Dagger", "Quarterstaff", "Ranseur", "Rapier",
         "Repeating Crossbow Bolts", "Sai", "Sap", "Scimitar", "Scythe", "Short Sword", "Shortspear", "Siangham",
         "Sickle", "Spear", "Spiked Chain", "Spiked Gauntlet", "Throwing Axe", "Trident", "Two-Bladed Sword",
         "Unarmed Strike", "Warhammer", "Whip"]
ability = ['Strength', 'Constitution', 'Dexterity', 'Wisdom', 'Intellegence', 'Charisma']
listc = ["Bard", "Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
listr = ["Human", "Goliath", "Dragonborn", "Gnome", "Genesai", "Aarakocra", "Dwarf", "Tiefling", "Halfling", "Halfelf",
         "Elf"]
lista = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral",
         "Neutral Neutral" "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil", "Lg", "Ln", "Le", "Ng",
         "N", "Nn", "Ne", "Ce", "Cn", "Ce"]
lists = ["Athletics", "Acrobatics", "Sleight Of Hand", "Stealth", "Arcana", "History", "Investigation", "Nature",
         "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation",
         "Performance", "Persuasion"]
cantripbard = ["Dancing Lights", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation",
               "True Strike", "Vicious Mockery"]
cantripcleric = ["Guidance","Light","Mending","Resistance","Sacred Flame","Spare The Dying","Thaumaturgy"]
cantripdruid = ["Druidcraft","Guidance","Mending","Poison Spray","Produce Flame","Resistance","Shillelagh"]
cantripssorcerer = ["Acid Splash","Chill Touch","Dancing Lights","Fire Bolt","Light","Mage Hand","Mending","Message","Minor Illusion","Poison Spray","Prestidigitation","Ray Of Frost","Shocking Grasp","True Strike" ]
cantripswarlock =["Chill Touch","Eldritch Blast","Mage Hand","Minor Illusion","Poison Spray","Prestidigitation","True Strike"]
cantripswizard = ["Acid Splash","Chill Touch","Dancing Lights","Fire Bolt","Light","Mage Hand","Mending","Message","Minor Illusion","Poison Spray","Prestidigitation","Ray of Frost","Shocking Grasp","True Strike "]

cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Druidcraft", "Eldritch Blast", "Fire Bolt", "Guidance",
            "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation",
            "Produce Flame", "Ray Of Frost", "Resistance", "Sacred Flame", "Shillelagh", "Shocking Grasp",
            "Spare The Dying", "Thaumaturgy", "True Strike", "Vicious Mockery"]
spelllevel1 = ["Alarm", "Animal Friendship", "Bane", "Bless", "Burning Hands", "Charm Person", "Color Spray", "Command",
               "Comprehend Languages", "Create Or Destroy Water", "Cure Wounds", "Detect Evil And Good", "Detect Magic",
               "Detect Poison and Disease", "Disguise Self", "Divine Favor", "Entangle", "Expeditious Retreat",
               "Faerie Fire", "False Life", "Feather Fall", "Find Familiar", "Floating Disk", "Fog Cloud", "Goodberry",
               "Grease", "Guiding Bolt", "Healing Word", "Hellish Rebuke", "Heroism", "Hideous Laughter",
               "Hunter's Mark", "Identify", "Illusory Script", "Inflict Wounds", "Jump", "Longstrider", "Mage Armor",
               "Magic Missile", "Protection From Evil And Good", "Purify Food And Drink", "Sanctuary", "Shield",
               "Shield Of Faith", "Silent Image", "Sleep", "Speak With Animals", "Thunderwave"]
spelllevel2 = ["Unseen Servant", "Acid Arrow", "Aid", "Alter Self", "Animal Messenger", "Arcane Lock",
               "Arcanists Magic Aura", "Augury", "Barkskin", "Blindness Deafness", "Blur", "Branding Smite",
               "Calm Emotions", "Continual Flame", "Darkness", "Darkvision", "Detect Thoughts", "Enhance Ability",
               "Enlarge Reduce", "Enthrall", "Find Steed", "Find Traps", "Flame Blade", "Flaming Sphere",
               "Gentle Repose", "Gust Of Wind", "Heat Metal", "Hold Person", "Invisibility", "Knock",
               "Lesser Restoration", "Levitate", "Locate Animals Or Plants", "Locate Object", "Magic Mouth",
               "Magic Weapon", "Mirror Image", "Misty Step", "Moonbeam", "Pass Without Trace", "Prayer Of Healing",
               "Protection From Poison", "Ray Of Enfeeblement", "Rope Trick", "Scorching Ray", "See Invisibility",
               "Shatter", "Silence", "Spider Climb", "Spike Growth", "Spiritual Weapon", "Suggestion", "Warding Bond",
               "Web", "Zone of Truth"]
spelllevel3 = ["Animate Dead", "Beacon of Hope", "Bestow Curse", "Blink", "Call Lightning", "Clairvoyance",
               "Conjure Animals", "Counterspell", "Create Food And Water", "Daylight", "Dispel Magic", "Fear",
               "Fireball", "Fly", "Gaseous Form", "Glyph Of Warding", "Haste", "Hypnotic Pattern", "Lightning Bolt",
               "Magic Circle", "Major Image", "Mass Healing Word", "Meld Into Stone", "Nondetection", "Phantom Steed",
               "Plant Growth", "Protection From Energy", "Remove Curse", "Revivify", "Sending", "Sleet Storm""Slow",
               "Speak With Dead", "Speak With Plants", "Spirit Guardians", "Stinking Cloud", "Tiny Hut", "Tongues",
               "Vampiric Touch", "Water Breathing", "Water Walk", "Wind Wall"]
spelllevel4 = ["Arcane Eye", "Banishment", "Black Tentacles", "Blight", "Compulsion", "Confusion",
               "Conjure Minor Elementals", "Conjure Woodland Beings", "Control Water", "Death Ward", "Dimension Door",
               "Divination", "Dominate Beast", "Fabricate", "Faithful Hound", "Fire Shield", "Freedom Of Movement",
               "Giant Insect", "Greater Invisibility", "Guardian Of Faith", "Hallucinatory Terrain", "Ice Storm",
               "Locate Creature", "Phantasmal Killer", "Polymorph", "Private Sanctum", "Resilient Sphere",
               "Secret Chest", "Stone Shape", "Stoneskin", "Wall Of Fire"]
spelllevel5 = ["Animate Objects", "Antilife Shell", "Arcane Hand", "Awaken", "Cloudkill", "Commune",
               "Commune With Nature", "Cone Of Cold", "Conjure Elemental", "Contact Other Plane", "Contagion",
               "Creation", "Dispel Evil And Good", "Dominate Person", "Dream", "Flame Strike", "Geas",
               "Greater Restoration", "Hallow", "Hold Monster", "Insect Plague", "Legend Lore", "Mass Cure Wounds",
               "Mislead", "Modify Memory", "Passwall", "Planar Binding", "Raise Dead", "Reincarnate", "Scrying",
               "Seeming", "Telekinesis", "Telepathic Bond", "Teleportation Circle", "Tree Stride", "Wall of Force",
               "Wall of Stone"]
spelllevel6 = ["Blade Barrier", "Chain Lightning", "Circle Of Death", "Conjure Fey", "Contingency", "Create Undead",
               "Disintegrate", "Eyebite", "Find The Path", "Flesh To Stone", "Forbiddance", "Freezing Sphere",
               "Globe Of Invulnerability", "Guards And Wards", "Harm", "Heal", "Heroes Feast", "Instant Summons",
               "Irresistible Dance", "Magic Jar", "Mass Suggestion", "Move Earth", "Planar Ally", "Programmed Illusion",
               "Sunbeam", "Transport Via Plants", "True Seeing", "Wall Of Ice", "Wall Of Thorns", "Wind Walk",
               "Word Of Recall"]
spelllevel7 = ["Arcane Sword", "Conjure Celestial", "Delayed Blast Fireball", "Divine Word", "Etherealness",
               "Finger of Death", "Fire Storm", "Forcecage", "Magnificent Mansion", "Mirage Arcane", "Plane Shift",
               "Prismatic Spray", "Project Image", "Regenerate", "Resurrection", "Reverse Gravity", "Sequester",
               "Simulacrum", "Symbol", "Teleport"]
spelllevel8 = ["Animal Shapes", "Antimagic Field", "Antipathy Sympathy""Clone""Control Weather", "Demiplane",
               "Dominate Monster", "Earthquake", "Feeblemind", "Glibness", "Holy Aura", "Incendiary Cloud", "Maze"]
spelllevel9 = ["Mind Blank", "Power Word Stun", "Sunburst", "Astral Projection", "Foresight", "Gate", "Imprisonment",
               "Mass Heal", "Meteor Swarm", "Power Word Kill", "Prismatic Wall", "Shapechange",
               "Storm Of Vengeance""Time Stop", "True Polymorph", "True Resurrection", "Weird", "Wish"]
spellsbard = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic",
              "Disguise Self", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism", "Hideous Laughter", "Identify",
              "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals", "Thunderwave",
              "Unseen Servant", "Animal Messenger", "Blindness/Deafness", "Calm Emotions", "Detect Thoughts",
              "Enhance Ability", "Enthrall", "Heat Metal", "Hold Person", "Invisibility", "Knock", "Lesser Restoration",
              "Locate Animals Or Plants", "Locate Object", "Magic Mouth", "See Invisibility", "Shatter", "Silence",
              "Suggestion", "Zone Of Truth", "Bestow Curse", "Clairvoyance", "Dispel Magic", "Fear", "Glyph Of Warding",
              "Hypnotic Pattern", "Major Image", "Nondetection", "Plant Growth", "Sending", "Speak With Dead",
              "Speak With Plants", "Stinking Cloud", "Tiny Hut", "Tongues", "Compulsion", "Confusion", "Dimension Door",
              "Freedom Of Movement", "Greater Invisibility", "Hallucinatory Terrain", "Locate Creature", "Polymorph",
              "Animate Objects", "Awaken", "Dominate Person", "Dream", "Geas", "Greater Restoration", "Hold Monster",
              "Legend Lore", "Mass Cure Wounds", "Mislead", "Modify Memory", "Planar Binding", "Raise Dead", "Scrying",
              "Seeming", "Teleportation Circle", "Eyebite", "Find The Path", "Guards And Wards", "Irresistible Dance",
              "Mass Suggestion", "Programmed Illusion", "True Seeing", "Arcane Sword", "Etherealness", "Forcecage",
              "Magnificent Mansion", "Mirage Arcane", "Project Image", "Regenerate", "Resurrection", "Symbol",
              "Teleport", "Dominate Monster", "Feeblemind", "Glibness", "Mind Blank", "Power Word Stun", "Foresight",
              "Power Word Kill", "True Polymorph"]
spellsranger = ["Alarm",'Animal Friendship','Cure Wounds','Detect Magic','Detect Poison And Disease','Fog Cloud','Goodberry','Hunters Mark''Jump','Longstrider','Speak with Animals','Animal Messenger','Barkskin','Darkvision','Find Traps','Lesser Restoration','Locate Animals Or Plants','Locate Object','Pass Without Trace','Protection From Poison','Silence','Spike Growth','Conjure Animals','Daylight','Nondetection','Plant Growth','Protection From Energy','Speak With Plants','Water Breathing','Water Walk','Wind Wall','Conjure Woodland Beings','Freedom of Movement','Locate Creature','Stoneskin',"Commune With Nature","Tree Stride "]
spellssorcerer = ["Burning Hands",'Charm Person','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Expeditious Retreat','False Life','Feather Fall','Fog Cloud','Jump','Mage Armor','Magic Missile','Shield','Silent Image','Sleep','Thunderwave','Alter Self','Blindness/Deafness','Blur','Darkness','Darkvision','Detect Thoughts','Enhance Ability','Enlarge/Reduce','Gust Of Wind','Hold Person','Invisibility','Knock','Levitate','Mirror Image','Misty Step','Scorching Ray','See Invisibility','Shatter','Spider Climb','Suggestion','Web','Blink','Clairvoyance','Counterspell','Daylight','Dispel Magic','Fear','Fireball','Fly','Gaseous Form','Haste','Hypnotic Pattern','Lightning Bolt','Major Image','Protection From Energy','Sleet Storm','Slow','Stinking Cloud','Tongues','Water Breathing','Water Walk','Banishment','Blight','Confusion','Dimension Door','Dominate Beast','Greater Invisibility','Ice Storm','Polymorph','Stoneskin','Wall Of Fire','Animate Objects','Cloudkill','Cone Of Cold','Creation','Dominate Person','Hold Monster','Insect Plague','Seeming','Telekinesis','Teleportation Circle','Wall Of Stone','Chain Lightning','Circle Of Death','Disintegrate','Eyebite','Globe Of Invulnerability','Mass Suggestion','Move Earth','Sunbeam','True Seeing','Delayed Blast Fireball','Etherealness','Finger Of Death','Fire Storm','Plane Shift','Prismatic Spray','Reverse Gravity','Teleport','Dominate Monster','Earthquake','Incendiary Cloud','Power Word Stun','Sunburst','Gate','Meteor Swarm','Power Word Kill','Time Stop',"Wish"]
spellswarlock = ["Charm Person","Comprehend Languages","Expeditious Retreat","Hellish Rebuke","Illusory Script","Protection from Evil and Good","Unseen Servant","Darkness","Enthrall","Hold Person","Invisibility","Mirror Image","Misty Step","Ray of Enfeeblement","Shatter","Spider Climb","Suggestion","Counterspell","Dispel Magic","Fear","Fly","Gaseous Form","Hypnotic Pattern","Magic Circle","Major Image","Remove Curse","Tongues","Vampiric Touch","Banishment","Blight","Dimension Door","Hallucinatory Terrain","Contact Other Plane","Dream","Hold Monster","Scrying","Circle Of Death","Conjure Fey","Create Undead","Eyebite","Flesh To Stone","Mass Suggestion","True Seeing","Etherealness","Finger Of Death","Forcecage","Plane Shift","Demiplane","Dominate Monster","Feeblemind","Glibness","Power Word Stun","Astral Projection""Foresight","Imprisonment","Power Word Kill","True Polymorph"]


#create db
class databace:
    def __init__(self):
        self.connect = sqlite3.connect('Characters.db')
            #cursor= little gnome that does you db stuff you you
        self.tomithy = connect.cursor()
            # create tables
        self.tomithy.execute("""CREATE TABLE IF NOT EXISTS characters(
                        name text,
                        class text,
                        race text)""")



        #make changes save
        self.connect.commit()
        #close db connection once done
        self.connect.close()
        #when submit button in hit the iterations from Charview need to be brought here, formatted into a list and sent to Charmodle