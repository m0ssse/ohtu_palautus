from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.table import Table
from rich.console import Console

def display_table(player_data, season, country):
    table = Table(title = f"Season {season} players from {country}")
    table.add_column("Player")
    table.add_column("Teams")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Points")
    for player in player_data:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals+player.assists))
    console = Console()
    console.print(table)

def main():
    while True:
        print("Please input which season's stats you would like to show (2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25)")
        year = input()
        url = f"https://studies.cs.helsinki.fi/nhlstats/{year}/players"
        try:
            stats = PlayerStats(PlayerReader(url))
        except:
            print("Invalid year!")
            continue
        print("Please input the country whose players you wish to display (USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS)")
        country = input()
        data = stats.top_scores_from_country(country)
        display_table(data, year, country)

if __name__=="__main__":
    main()