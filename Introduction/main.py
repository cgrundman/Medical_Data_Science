# Write a function distanceToSun which asks the user to input the name of a planet of our solar system in command line,
# and prints the distance between the planet and the Sun in kilometres.


def distance_to_sun(planet_name):
    if planet_name == 'mercury':
        print('Mercury is 57,900,000km away from the Sun.')
    elif planet_name == 'venus':
        print('Venus is 108,200,000km away from the Sun.')
    elif planet_name == 'earth':
        print('Earth is 149,600,000km away from the Sun.')
    elif planet_name == 'mars':
        print('Mars is 227,900,000km away from the Sun.')
    elif planet_name == 'jupiter':
        print('Jupiter is 778,600,000km away from the Sun.')
    elif planet_name == 'saturn':
        print('Saturn is 1,433,500,000km away from the Sun.')
    elif planet_name == 'uranus':
        print('Uranus is 2,872,500,000km away from the Sun.')
    elif planet_name == 'neptune':
        print('Neptune is 4,495,100,000km away from the Sun.')
    else:
        print('Error, maybe there was a spelling error.')


entry = input('Enter the name of a planet:\n').lower()
distance_to_sun(entry)
