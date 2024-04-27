# python setup.py bdist_msi

def write_players_to_file(player, filename ="Player\\players.txt"):
     with open(filename, "r") as file:
        players = [line.strip() for line in file]
        if len(players) >= 4:
            with open(filename, "w") as file:
                    file.write(player)
        else:
            with open(filename, "a") as file:
                    file.write("\n" + player)

# write_players_to_file("Ekene-onwon")
# write_players_to_file("Hanson")
# write_players_to_file("Rowland")
# write_players_to_file("Okwusi")
# write_players_to_file("Abraham")