import constants
PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS

players_clean_data = []
def clean_data(player):
    name = player['name']
    guardians = player['guardians'].split('and')
    experience = player['experience']
    height = int(player['height'].split()[0])

    cleaned_player = {
        'name' : name,
        'guardians' : guardians,
        'experience': experience,
        'height': height
    }

    if cleaned_player['experience'] == 'YES':
        cleaned_player['experience'] = True
    else:
        cleaned_player['experience'] = False

    players_clean_data.append(cleaned_player)
    print(f'clean = {cleaned_player}')

if __name__ == '__main__':
    for player in PLAYERS:
        clean_data(player)
        print(f'original = {player}')
