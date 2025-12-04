class Player:
  player_count = 0;
  def __init__(self, name):
    self.name = name;
    Player.player_count += 1;

  def display_player_count(cls):
    print(f"Total Player : {cls.player_count}");

p1 = Player("Rakibul");
p2 = Player("Shuvo");
p3 = Player("Murad");

p3.display_player_count();
