import sys
import random

""" program to create funny names """

print("Welcome to the game \n")
print(" you will genereate a funny name")

first_name =  ('Baby Oil1', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
				"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
				'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
				'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns','Cleet', 
				'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
				'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
				'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
				'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
				'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 
				'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
				'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
				'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo',
				'Scratchensniff', 'Scut', "Sid 'The Squirts'",
				'Skidmark', 'Slaps','Snakes', 'Snoobs', 'Snorki',
				'Soupcan Sam', 'Spitzitout’, ’Squids', 'Stinky', 'Storyboard',
				'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'",
                'Worms')

last_name =    ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
				'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
				'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
				'Goodensmith', 'Goodpasture', 'Guster', 'Henderso',
				'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
				'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
				"M’Bernbo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
				'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
				'Pealike', 'Pennywhistl', 'Peterson', 'Pieplow', 'Pinkerton',
				'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
				'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
				'Stroganoff', 'Sugar-Gold’, ’Swackhamer', 'Tippins',
				'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
				'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
				'Winterkorn', 'Woolysocks')

while True:
    firstName = random.choice(first_name)

    lastName = random.choice(last_name)

    print(f'{firstName} {lastName} \n\n',file = sys.stderr)
    try_agin =input(" if you what to quit enter 'n' else press Enter \n")

    if try_agin.lower() == 'n':
        break
input('\n press enter to quit')