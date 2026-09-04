n, m, k = input().strip().split()
num_teams = int(n)
num_rounds = int(m)
num_players = int(k)

teams = {}
players = {}

for i in range(num_teams):
  line = input().split()
  teams[line[0]] = line[1:]

for i in range(num_players):
  line = input().split()
  players[line[0]] = line[1:]

teams_rank = {
  team: {pref: id for id, pref in enumerate(preferences)}
  for team, preferences in teams.items()
}

players_rank = {
  player: {pref: id for id, pref in enumerate(preferences)}
  for player, preferences in players.items()
}

next_pick = {t: 0 for t in teams}

current_team = {p: None for p in players}

team_rosters = {t: set() for t in teams}

teams_still_drafting = [t for t in teams if num_rounds > 0]

draft_failed = False

while teams_still_drafting:
  t = teams_still_drafting.pop()

  if len(team_rosters[t]) >= num_rounds:
    continue

  # Check if the team has run out of players to draft before filling their roster
  if next_pick[t] >= len(teams[t]):
    draft_failed = True
    break

  candidate = teams[t][next_pick[t]]
  next_pick[t] += 1

  if current_team[candidate] is None:
    current_team[candidate] = t
    team_rosters[t].add(candidate)
  else:
    rival_team = current_team[candidate]
    if players_rank[candidate][t] < players_rank[candidate][rival_team]:
      team_rosters[rival_team].discard(candidate)
      current_team[candidate] = t
      team_rosters[t].add(candidate)
      teams_still_drafting.append(rival_team)
    else:
      teams_still_drafting.append(t)
      continue
  if len(team_rosters[t]) < num_rounds:
    teams_still_drafting.append(t)

if draft_failed:
  print("Hello darkness my old friend!")
else:
  for t in teams:
    print(t, *team_rosters[t])

  