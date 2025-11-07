from rich.table import Table
from rich.console import Console

from player_reader import PlayerReader
from player_stats import PlayerStats

SEASON_OPTIONS_STR = "2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25"
SEASON_OPTIONS = set(SEASON_OPTIONS_STR.split("/"))
COUNTRY_OPTIONS_STR = "USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS"
COUNTRY_OPTIONS = set(COUNTRY_OPTIONS_STR.split("/"))

def display_table(player_data, season, country):
    table = Table(title = f"Season {season} players from {country}")
    table.add_column("Player")
    table.add_column("Teams")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Points")
    for player in player_data:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.score()))
    console = Console()
    console.print(table)

def main():
    while True:
        print(f"Please input which season's stats you would like to show ({SEASON_OPTIONS_STR})")
        year = input()
        if year not in SEASON_OPTIONS:
            print("Invalid year!")
            continue
        url = f"https://studies.cs.helsinki.fi/nhlstats/{year}/players"
        stats = PlayerStats(PlayerReader(url))

        print(f"Please input the country whose players you wish to display ({COUNTRY_OPTIONS_STR})")
        country = input()
        if country not in COUNTRY_OPTIONS:
            print("Invalid country!")
            continue
        data = stats.top_scores_from_country(country)
        display_table(data, year, country)

if __name__=="__main__":
    main()
