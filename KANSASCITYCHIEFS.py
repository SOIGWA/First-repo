# KANSAS CITY CHIEFS
Patrick_Mahomes = {
  'Name':'Patrick Mahomes',
  'Position':'Quaterback',
  'Jersey No': 15,
  'Yards Gained':1389,
  'Touchdowns':7
}
DeAndre_Hopkins = {
  'Name':'DeAndre Hopkins',
  'Position':'WideReciver',
  'Jersey No':8,
  'Yards Gained':610,
  'Touchdowns':5
}
Chris_Jones = {
  'Name':'Chris Jones',
  'Position':'DefensiveTackle',
  'Jersey No':95,
  'Yards Gained':120,
  'Touchdowns':0
}
Nick_Bolton = {
  'Name':'Nick Bolton',
  'Position':'Linebacker',
  'Jersey No':32,
  'Yards Gained':0,
  'Touchdowns':0
}
print(f"Positions: {Nick_Bolton['Position']},{Chris_Jones['Position']},{DeAndre_Hopkins['Position']},{Patrick_Mahomes['Position']}")

DeAndre_Hopkins['Yards Gained'] +=93
DeAndre_Hopkins['Touchdowns'] +=1

players=[Patrick_Mahomes,DeAndre_Hopkins,Chris_Jones,Nick_Bolton]
Total_Yards =sum(player['Yards Gained']for player in players)
Total_Touchdowns =sum(player['Touchdowns'] for player in players)
average_yards = Total_Yards/ len(players)
average_Touchdowns = Total_Touchdowns /len(players)

print(f"Average Yards Gained :{average_yards:.3f}")
print(f"Average Touchdowns: {average_Touchdowns:.3f}")

