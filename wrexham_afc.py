class Player:
    def __init__(self, PlayerNumber, Forename, Surname, Position) -> None:
        self.PlayerNumber = PlayerNumber
        self.Forename = Forename
        self.Surname = Surname
        self.Position = Position
        self.CommunityInvolvement = 0
        self.Injured = False

    def get_player_info(self):
        return self.Forename + " " + self.Surname + " " + self.Position

    def change_community_involvement(self, new_involvement):
        self.CommunityInvolvement += new_involvement
    
    def change_injured(self):
        self.Injured = not self.Injured

POSITIONS = ['Goalkeeper', 'Defender', 'Captain', 'Midfielder', 'Forward']

with open('wrexham_afc.txt', 'r') as file:
    players_data = file.readlines()
    players = []

    for player_data in players_data:
        parts = player_data.split(',')
        players.append(Player(parts[0], parts[1], parts[2], parts[3]))

    for player in players:
        print(player.get_player_info())
        