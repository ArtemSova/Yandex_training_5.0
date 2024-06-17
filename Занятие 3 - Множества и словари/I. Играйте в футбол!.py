teams_goals_total = {}
teams_goals_mean = {}
teams_games = {}
teams_open_games = {}
palyer_open_games = {}
player_goals_total = {}
player_team = {}
player_goal_minutes = {}

with open('input.txt', 'r') as file:
    while True:
        line = str(file.readline())
        if line == '':
            break

        if line.startswith('"'):
            line = line.split()
            first_team = False
            second_team = False

            team_1 = None
            team_2 = None
            team_1_count = None
            team_2_count = None
            for i in line:
                if i == '-':
                    pass
                elif first_team == False:
                    if i.endswith('"'):
                        if team_1 != None:
                            team_1 += ' ' + i
                            first_team = True
                        else:
                            team_1 = i
                            first_team = True
                    elif team_1 != None:
                        team_1 += ' ' + i
                    else:
                        team_1 = i
                elif second_team == False:
                    if i.endswith('"'):
                        if team_2 != None:
                            team_2 += ' ' + i
                            second_team = True
                        else:
                            team_2 = i
                            second_team = True
                    elif team_2 != None:
                        team_2 += ' ' + i
                    else:
                        team_2 = i
                else:
                    team_1_count, team_2_count = map(int, i.split(':'))

            # Общее колич голов команд
            if team_1 in teams_goals_total:
                teams_goals_total[team_1] += team_1_count
            else:
                teams_goals_total[team_1] = team_1_count

            if team_2 in teams_goals_total:
                teams_goals_total[team_2] += team_2_count
            else:
                teams_goals_total[team_2] = team_2_count

            # количество игр команд и сред колич голов команд
            if team_1 in teams_games:
                teams_games[team_1] += 1
            else:
                teams_games[team_1] = 1

            if team_2 in teams_games:
                teams_games[team_2] += 1
            else:
                teams_games[team_2] = 1

            # Среднее колич голов команд
            teams_goals_mean[team_1] = teams_goals_total[team_1] / teams_games[team_1]
            teams_goals_mean[team_2] = teams_goals_total[team_2] / teams_games[team_2]

            first_team_goal = None
            first_player_goal = None

            # Статистика игроков
            for i in range(team_1_count+team_2_count):
                if i < team_1_count:
                    player = str(file.readline())
                    player = player[:-2]
                    player = player.split()
                    player_name = None
                    player_time = None
                    for j in player:
                        if j.isdigit():
                            player_time = int(j)
                        else:
                            if player_name == None:
                                player_name = str(j)
                            else:
                                player_name += ' ' + str(j)

                    if player_name not in player_team:
                        player_team[player_name] = team_1

                    if player_name in player_goals_total:
                        player_goals_total[player_name] += 1
                    else:
                        player_goals_total[player_name] = 1

                    if player_name in player_goal_minutes:
                        if player_time in player_goal_minutes[player_name]:
                            player_goal_minutes[player_name][player_time] += 1
                        else:
                            player_goal_minutes[player_name][player_time] = 1
                    else:
                        player_goal_minutes[player_name] = {player_time: 1}

                    if first_team_goal == None:
                        first_team_goal = (player_time, team_1)
                    if first_player_goal == None:
                        first_player_goal = (player_time, player_name)

                if team_2_count == 0 and i == 0:
                    if first_team_goal != None:
                        if first_team_goal[1] in teams_open_games:
                            teams_open_games[first_team_goal[1]] += 1
                        else:
                            teams_open_games[first_team_goal[1]] = 1

                    if first_player_goal != None:
                        if first_player_goal[1] in palyer_open_games:
                            palyer_open_games[first_player_goal[1]] += 1
                        else:
                            palyer_open_games[first_player_goal[1]] = 1

                if i >= team_1_count:
                    player = str(file.readline())
                    player = player[:-2]
                    player = player.split()
                    player_name = None
                    player_time = None
                    for j in player:
                        if j.isdigit():
                            player_time = int(j)
                        else:
                            if player_name == None:
                                player_name = str(j)
                            else:
                                player_name += ' ' + str(j)

                    if player_name not in player_team:
                        player_team[player_name] = team_2

                    if player_name in player_goals_total:
                        player_goals_total[player_name] += 1
                    else:
                        player_goals_total[player_name] = 1

                    if player_name in player_goal_minutes:
                        if player_time in player_goal_minutes[player_name]:
                            player_goal_minutes[player_name][player_time] += 1
                        else:
                            player_goal_minutes[player_name][player_time] = 1
                    else:
                        player_goal_minutes[player_name] = {player_time: 1}

                    if i == team_1_count:
                        if first_team_goal == None:
                            if team_2 in teams_open_games:
                                teams_open_games[team_2] += 1
                            else:
                                teams_open_games[team_2] = 1

                            if player_name in palyer_open_games:
                                palyer_open_games[player_name] += 1
                            else:
                                palyer_open_games[player_name] = 1
                        else:
                            if player_time < first_team_goal[0]:
                                if team_2 in teams_open_games:
                                    teams_open_games[team_2] += 1
                                else:
                                    teams_open_games[team_2] = 1

                                if player_name in palyer_open_games:
                                    palyer_open_games[player_name] += 1
                                else:
                                    palyer_open_games[player_name] = 1

                            else:
                                if first_team_goal[1] in teams_open_games:
                                    teams_open_games[first_team_goal[1]] += 1
                                else:
                                    teams_open_games[first_team_goal[1]] = 1

                                if first_player_goal[1] in palyer_open_games:
                                    palyer_open_games[first_player_goal[1]] += 1
                                else:
                                    palyer_open_games[first_player_goal[1]] = 1

        elif line.startswith('Total goals'):
            if line.startswith('Total goals for'):
                teamtg = line.rstrip()[16:]
                if teamtg in teams_goals_total:
                    print(teams_goals_total[teamtg])
                else:
                    print(0)
            else:
                playertg = line.rstrip()[15:]
                if playertg in player_goals_total:
                    print(player_goals_total[playertg])
                else:
                    print(0)

        elif line.startswith('Mean goals'):
            if line.startswith('Mean goals per game for'):
                teammg = line.rstrip()[24:]
                if teammg in teams_goals_mean:
                    print(teams_goals_mean[teammg])
                else:
                    print(0)
            else:
                palyermg = line.rstrip()[23:]
                if palyermg in player_team:
                    if palyermg in player_goals_total:
                        answer = player_goals_total[palyermg] / teams_games[player_team[palyermg]]
                        print(answer)
                    else:
                        print(0)
                else:
                    print(0)
        
        elif line.startswith('Goals on'):
            line = line.rstrip()
            if line.startswith('Goals on minute'):
                minute = None
                playergo = None
                string = line.split()
                for i in string:
                    if i in ['Goals', 'on', 'minute', 'by']:
                        pass
                    elif i.isdigit():
                        minute = int(i)
                    else:
                        if playergo == None:
                            playergo = i
                        else:
                            playergo += ' ' + i

                if playergo in player_goal_minutes:
                    if minute in player_goal_minutes[playergo]:
                        print(player_goal_minutes[playergo][minute])
                    else:
                        print(0)
                else:
                    print(0)

            elif line.startswith('Goals on first'):
                time_first = None
                playergof = None
                string = line.split()
                for i in string:
                    if i in ['Goals', 'on', 'first', 'minutes', 'by']:
                        pass
                    elif i.isdigit():
                        time_first = int(i)
                    else:
                        if playergof == None:
                            playergof = i
                        else:
                            playergof += ' ' + i

                if playergof in player_goal_minutes:
                    counter = 0
                    for i in player_goal_minutes[playergof]:
                        if i <= time_first:
                            counter += player_goal_minutes[playergof][i]
                    print(counter)
                else:
                    print(0)

            else:
                time_last = None
                playergol = None
                string = line.split()
                for i in string:
                    if i in ['Goals', 'on', 'last', 'minutes', 'by']:
                        pass
                    elif i.isdigit():
                        time_last = int(i)
                    else:
                        if playergol == None:
                            playergol = i
                        else:
                            playergol += ' ' + i

                if playergol in player_goal_minutes:
                    counter = 0
                    for i in player_goal_minutes[playergol]:
                        if i >= (91 - time_last):
                            counter += player_goal_minutes[playergol][i]
                    print(counter)
                else:
                    print(0)

        elif line.startswith('Score opens by'):
            subject = line.rstrip()[15:]
            if subject in teams_open_games:
                print(teams_open_games[subject])
            elif subject in palyer_open_games:
                print(palyer_open_games[subject])
            else:
                print(0)

