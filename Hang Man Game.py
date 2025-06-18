import os
os.system('cls')
import random
word_categories = {
    "Animal": [
        "Lion", "Elephant", "Tiger", "Giraffe", "Zebra", "Bear", "Wolf", "Kangaroo", "Panda", "Camel",
        "Fox", "Leopard", "Cheetah", "Rhino", "Hippopotamus", "Bat", "Monkey", "Goat", "Sheep", "Cow",
        "Dog", "Cat", "Donkey", "Buffalo", "Crocodile", "Alligator", "Deer", "Reindeer", "Otter", "Porcupine",
        "Squirrel", "Hedgehog", "Rabbit", "Mouse", "Rat", "Antelope", "Jaguar", "Hyena", "Koala", "Moose"
    ],
    "Country": [
        "Egypt", "Germany", "Brazil", "Japan", "Canada", "Italy", "Spain", "France", "China", "India",
        "Mexico", "Russia", "Turkey", "Australia", "Argentina", "Iraq", "Iran", "Kenya", "Nigeria", "Sweden",
        "Norway", "Denmark", "Finland", "Chile", "Colombia", "Peru", "Venezuela", "Thailand", "Vietnam", "Pakistan",
        "Afghanistan", "Indonesia", "Philippines", "Morocco", "Algeria", "Tunisia", "South Africa", "Uganda", "Sudan", "Ukraine"
    ],
    "Fruit": [
        "Apple", "Banana", "Mango", "Orange", "Grape", "Watermelon", "Peach", "Pear", "Pineapple", "Cherry",
        "Plum", "Kiwi", "Papaya", "Pomegranate", "Apricot", "Fig", "Date", "Lemon", "Lime", "Blueberry",
        "Raspberry", "Strawberry", "Blackberry", "Grapefruit", "Guava", "Coconut", "Dragonfruit", "Passionfruit", "Lychee", "Cranberry",
        "Currant", "Tangerine", "Nectarine", "Persimmon", "Jackfruit", "Durian", "Starfruit", "Mulberry", "Olive", "Soursop"
    ],
    "Color": [
        "Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Orange", "Brown", "Black", "White",
        "Grey", "Cyan", "Magenta", "Gold", "Silver", "Beige", "Maroon", "Navy", "Teal", "Olive",
        "Violet", "Indigo", "Turquoise", "Peach", "Coral", "Salmon", "Amber", "Bronze", "Ivory", "Charcoal",
        "Mustard", "Mint", "Lavender", "Ruby", "Sapphire", "Emerald", "Plum", "Chocolate", "Copper", "Sand"
    ],
    "Sport": [
        "Football", "Tennis", "Cricket", "Basketball", "Swimming", "Baseball", "Rugby", "Volleyball", "Golf", "Boxing",
        "Cycling", "Skating", "Skiing", "Wrestling", "Karate", "Judo", "Badminton", "Fencing", "Rowing", "Surfing",
        "Archery", "Hockey", "Handball", "Pingpong", "Billiards", "Snowboarding", "Ice Skating", "Water Polo", "Climbing", "Sailing",
        "Diving", "Motocross", "Triathlon", "Marathon", "Parkour", "Weightlifting", "Gymnastics", "Snooker", "Speed Skating", "Kickboxing"
    ],
    "Profession": [
        "Doctor", "Nurse", "Engineer", "Teacher", "Lawyer", "Architect", "Scientist", "Dentist", "Mechanic", "Electrician",
        "Carpenter", "Plumber", "Farmer", "Pilot", "Chef", "Waiter", "Artist", "Musician", "Soldier", "Policeman",
        "Firefighter", "Journalist", "Accountant", "Banker", "Librarian", "Pharmacist", "Actor", "Director", "Barber", "Driver",
        "Tailor", "Butcher", "Baker", "Cashier", "Photographer", "Guard", "Receptionist", "Cleaner", "Translator", "Therapist"
    ],
    "Vehicle": [
        "Car", "Truck", "Bus", "Motorcycle", "Bicycle", "Van", "Train", "Airplane", "Helicopter", "Boat",
        "Ship", "Submarine", "Scooter", "Skateboard", "Tram", "Taxi", "Yacht", "Jeep", "Canoe", "Ferry",
        "Wagon", "Minivan", "Ambulance", "Firetruck", "Bulldozer", "Crane", "Forklift", "Glider", "Jetski", "Rickshaw",
        "Hovercraft", "Tank", "Rocket", "Spaceship", "Segway", "Caravan", "Snowmobile", "Gondola", "Pickup", "Monster Truck"
    ],
    "Body Part": [
        "Head", "Eye", "Ear", "Nose", "Mouth", "Face", "Hair", "Neck", "Shoulder", "Arm",
        "Elbow", "Wrist", "Hand", "Finger", "Chest", "Back", "Waist", "Hip", "Leg", "Knee",
        "Ankle", "Foot", "Toe", "Brain", "Heart", "Lung", "Liver", "Stomach", "Intestine", "Skin",
        "Bone", "Muscle", "Vein", "Artery", "Tongue", "Tooth", "Jaw", "Throat", "Spine", "Eyelash"
    ],
    "Clothing": [
        "Shirt", "Pants", "Jeans", "Jacket", "Coat", "Sweater", "T-shirt", "Shorts", "Skirt", "Dress",
        "Socks", "Shoes", "Boots", "Sandals", "Hat", "Cap", "Scarf", "Gloves", "Belt", "Tie",
        "Suit", "Hoodie", "Uniform", "Pajamas", "Raincoat", "Vest", "Robe", "Blazer", "Beanie", "Leggings",
        "Turban", "Kimono", "Sari", "Veil", "Cardigan", "Tracksuit", "Swimsuit", "Cloak", "Helmet", "Bandana"
    ],
    "Tool": [
        "Hammer", "Screwdriver", "Wrench", "Pliers", "Saw", "Drill", "Chisel", "Axe", "Tape Measure", "Level",
        "Ladder", "Shovel", "Hoe", "Rake", "Scissors", "Knife", "Mallet", "File", "Sandpaper", "Crowbar",
        "Wheelbarrow", "Toolbox", "Clamp", "Vice", "Welder", "Jackhammer", "Pickaxe", "Anvil", "Spade", "Compass",
        "Caliper", "Measuring Tape", "Soldering Iron", "Trowel", "Paintbrush", "Roller", "Wire Cutter", "Glue Gun", "Bolt", "Nut"
    ],
    "City": [
        "Cairo", "London", "Paris", "Berlin", "Tokyo", "Madrid", "Rome", "Moscow", "Beijing", "New York",
        "Sydney", "Dubai", "Istanbul", "Mumbai", "Delhi", "Jakarta", "Los Angeles", "Chicago", "Toronto", "Bangkok",
        "Seoul", "Singapore", "Barcelona", "Lisbon", "Vienna", "Prague", "Buenos Aires", "Cape Town", "Nairobi", "Karachi",
        "Manila", "Tehran", "Riyadh", "Baku", "Copenhagen", "Helsinki", "Oslo", "Stockholm", "Zurich", "Athens"
    ],
    "Insect": [
        "Ant", "Bee", "Wasp", "Butterfly", "Moth", "Mosquito", "Dragonfly", "Grasshopper", "Cricket", "Fly",
        "Termite", "Beetle", "Cockroach", "Bug", "Flea", "Louse", "Weevil", "Gnat", "Aphid", "Cicada",
        "Firefly", "Centipede", "Millipede", "Mantis", "Hornet", "Damsel Fly", "Silverfish", "Earwig", "Ladybug", "Thrip",
        "Leafhopper", "Spittlebug", "Bark Beetle", "Stinkbug", "Tick", "Mite", "Whitefly", "Lacewing", "Mayfly", "Boll Weevil"
    ],
    "Planet": [
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Ceres",
        "Eris", "Makemake", "Haumea", "Moon", "Sun", "Io", "Europa", "Ganymede", "Callisto", "Titan",
        "Enceladus", "Phoebe", "Triton", "Charon", "Deimos", "Phobos", "Himalia", "Miranda", "Ariel", "Umbriel",
        "Oberon", "Dione", "Tethys", "Rhea", "Iapetus", "Mimas", "Hyperion", "Janus", "Atlas", "Pan"
    ],
    "Element": [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
        "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
        "Iron", "Copper", "Zinc", "Silver", "Gold", "Platinum", "Mercury", "Lead", "Nickel", "Tin",
        "Cobalt", "Manganese", "Barium", "Strontium", "Bromine", "Iodine", "Radon", "Uranium", "Thorium", "Radium"
    ],
    "Emotion": [
        "Happy", "Sad", "Angry", "Scared", "Excited", "Surprised", "Nervous", "Anxious", "Confused", "Bored",
        "Hopeful", "Jealous", "Lonely", "Guilty", "Embarrassed", "Relaxed", "Grateful", "Proud", "Ashamed", "Worried",
        "Frustrated", "Overwhelmed", "Calm", "Energetic", "Afraid", "Tired", "Loved", "Joyful", "Annoyed", "Curious",
        "Satisfied", "Disappointed", "Peaceful", "Angsty", "Content", "Desperate", "Eager", "Envious", "Hurt", "Miserable"
    ]
}

category = random.choice(list(word_categories.keys()))

random_word = random.choice(word_categories[category])

print("The word is a \ an:", category)

max_attempts = 6
attempts = 0
wrong_letters = []
display = ['-'] * len(random_word)
print (''.join(display))


hang_man_ascii = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
print (hang_man_ascii[0])
while '-' in display and max_attempts> attempts:
    guessed = input('Please guess a letter: ')
    if guessed in wrong_letters:
      print (f'You already tried {guessed}! Try another letter')
      continue
    elif guessed in [letter.lower() for letter in random_word]:
      for i in range(len(random_word)):
        if guessed.lower() == random_word [i].lower():
          if guessed not in display:
            display [i] = random_word [i]
            print (f'Correct! You have {max_attempts - attempts} left attempts') 
            continue
    else:
      attempts += 1
      wrong_letters.append(guessed)
      print (f'Wrong! You have {max_attempts - attempts} left attempts')
      print (hang_man_ascii[attempts])
      print("Wrong letters:", ', '.join(wrong_letters))
    print(''.join(display))
if '-' not in display:
    print("""
  **********
   YOU WIN!
  **********
            """)
    print(f"The {category} is {random_word}")
else:
    print("""
  ************
   GAME OVER!
  ************
            """)
    print(f'The {category} is {random_word}')