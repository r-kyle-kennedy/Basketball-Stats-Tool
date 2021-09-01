import constants
import random
PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS

players_clean_data = []

def clean_data(player):
    name = player['name']
    guardians = player['guardians'].split(' and ')
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


def balance_teams(players):
    random.shuffle(players)
    panthers = []
    bandits = []
    warriors = []
    teams = [panthers, bandits, warriors]
    inexperienced_players = 0
    experienced_players = 0

    for player in players:
        if player['experience']:
            if experienced_players < len(TEAMS):
                teams[experienced_players].append(player)
                experienced_players += 1
            else:
                experienced_players = 1
                teams[0].append(player)
        else:
            if inexperienced_players < len(TEAMS):
                teams[inexperienced_players].append(player)
                inexperienced_players += 1
            else:
                inexperienced_players = 1
                teams[0].append(player)
    return teams

def get_avg_height(team):
    total = 0
    for player in team:
        total += player['height']
    avg = total / len(team)
    return round(avg, 2)


def select_team(teams, num_as_str):
    try:
        return teams[int(num_as_str)-1]
    except:
        return select_team(teams, input(f'{num_as_str} is not a valid selection, please choose a team between 1 and {len(teams)}  '))


def get_experienced_players(team):
    experienced_players=[]
    inexperienced_players=[]
    for player in team:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    return [experienced_players, inexperienced_players]

def build_teams(teams):
    team_info = []
    for idx, team in enumerate(teams):
        team_info.append(
        {
        'team': TEAMS[idx],
        'players': team,
        'number_of_players': len(team),
        'avg_height': get_avg_height(team),
        'experienced_players': get_experienced_players(team)[0],
        'inexperienced_players': get_experienced_players(team)[1]
        }
        )

    return team_info

def setup_print():
    print('BASKETBALL TEAM STATS TOOL\n')
    print('----MENU---\n')
    print('Options:')
    print('1) Display Team Stats')
    print('2) Quit \n')
    return input('Enter Option(1 or 2):  ')

if __name__ == '__main__':
    for player in PLAYERS:
        clean_data(player)

    balanced_teams = balance_teams(players_clean_data)
    teams = build_teams(balanced_teams)
    user_choice = setup_print()

    while user_choice != '2':
        print()
        print('Teams:')
        for idx, team in enumerate(TEAMS):
            print(f'{idx+1}) {team}')
        print()
        current_team = select_team(teams, input('Which team?  '))
        print()
        print(f'Team: {current_team["team"]} Stats')
        print('-'*(len(current_team["team"])+12))
        print(f'Total players: {current_team["number_of_players"]}')
        print(f'Total experienced players: {len(current_team["experienced_players"])}')
        print(f'Total inexperienced_players: {len(current_team["inexperienced_players"])}')
        print(f'Average height: {current_team["avg_height"]}\n')
        print('Players on Team:')
        player_string = ''
        for player in current_team['players']:
            player_string += player['name'] + ', '
        print(player_string[:len(player_string)-2])
        print()
        print('Guardians: ')
        guardian_string = ''
        for player in current_team['players']:
            for guardian in player['guardians']:
                guardian_string += guardian + ', '
        print(guardian_string[:len(guardian_string)-2])
        print()
        user_choice = setup_print()
