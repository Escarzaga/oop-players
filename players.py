class Player():
    def __init__(self, p_first_name, p_last_name, p_height_cm, p_weight_kg):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.height_cm = p_height_cm
        self.weight_kg = p_weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(p_first_name=first_name, p_last_name=last_name, p_height_cm=height_cm, p_weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
#super define un objeto superior, es para agregar lo que falta. llama al objeto padre

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(p_first_name=first_name, p_last_name=last_name, p_height_cm=height_cm, p_weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cars = red_cards


kev_dur = BasketballPlayer(first_name="Kevin",
                           last_name="Durant",
                           height_cm=210,
                           weight_kg=108,
                           points=27.2,
                           rebounds=7.1,
                           assists=4)

lebron = BasketballPlayer(first_name="Lebron",
                          last_name="James",
                          height_cm=203,
                          weight_kg=113,
                          points=27.2,
                          rebounds=7.4,
                          assists=7.2)

messi = FootballPlayer(first_name="Lionel",
                       last_name="Messi",
                       height_cm=170,
                       weight_kg=67,
                       goals=575,
                       yellow_cards=67,
                       red_cards=0)

ronaldo = FootballPlayer(first_name="Cristiano",
                         last_name="Ronaldo",
                         height_cm=184,
                         weight_kg=79,
                         goals=586,
                         yellow_cards=95,
                         red_cards=11)

print("/////  Introduce Football player's information  //////")

f_name = input("Player's first name: ")
l_name = input("Player's last name: ")
heightcm = input("player's height: ")
weightkg = input("Player's weight: ")
n_goals = input("Player's goals scored: ")
y_cards = input("Player's yellow cards: ")
r_cards = input("Player's red cards: ")

new_player = FootballPlayer(first_name=f_name,
                            last_name=l_name,
                            height_cm=heightcm,
                            weight_kg=weightkg,
                            goals=n_goals,
                            yellow_cards=y_cards,
                            red_cards=r_cards)

with open("footballplayer_dict.txt", "w") as footballplayer_file:
    footballplayer_file.write(str(new_player.__dict__))

print("Player's Info successfully introduced!")
print("Player's info: {0}".format(new_player.__dict__))


