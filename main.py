import logging

from form import (
    export_to_xlsx,
    read_csv_reply
)
from craweler import (
    get_player_id,
    get_player_matches
)

logging.basicConfig(level = logging.DEBUG)

def main():
    player_data = read_csv_reply("LOL數據調查.csv")
    match_data = []
    for email, playername in player_data:
        print(f"conducting queries on {playername}")
        player_id =  get_player_id(playername)
        match_data += get_player_matches(player_id)
    export_to_xlsx(match_data, "test.xlsx")
if __name__ == "__main__" :
    main()