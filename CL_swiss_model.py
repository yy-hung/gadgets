#瑞士轮欧冠抽签模拟器_经常不成功版_2024
import random

class Club:
  def __init__(self, name_eng, name_chn, country, pot, rival):
    self.name_eng = name_eng
    self.name_chn = name_chn
    self.country = country
    self.pot = pot
    self.rival = rival


  def __str__(self):
      return f"Club(name_eng={self.name_eng}, name_chn={self.name_chn}, country={self.country}, pot={self.pot}, rival={self.rival})"

  def __repr__(self):
      return self.__str__()

#clubs
mancity = Club("Manchester City", "曼城", "ENG", 1, 0)
bayern = Club("Bayern Munich", "拜仁", "GER", 1, 0)
rm = Club("Real Madrid", "皇马", "ESP", 1, 0)
psg = Club("PSG", "巴黎圣日尔曼", "FRA", 1, 0)
liverpool = Club("Liverpool", "利物浦", "ENG", 1, 0)
inter = Club("Inter", "国际米兰", "ITA", 1, 0)
dortmund = Club("Dortmund", "多特蒙德", "GER", 1, 0)
leipzig = Club("RB Leipzig", "RB莱比锡", "GER", 1, 0)
barca = Club("Barcelona", "巴塞罗那", "ESP", 1, 0)
pot1 = [mancity, bayern, rm, psg, liverpool, inter, dortmund, leipzig, barca]


leverkusen = Club("Bayer Leverkusen", "勒沃库森", "GER", 2, 0)
a_madrid = Club("Atletico Madrid", "马德里竞技", "ESP", 2, 0)
atlanta = Club("Atlanta", "亚特兰大", "ITA", 2, 0)
juventus = Club("Juventus", "尤文图斯", "ITA", 2, 0)
benfica = Club("Benfica", "本菲卡", "POR", 2, 0)
arsenal = Club("Arsenal", "阿森纳", "ENG", 2, 0)
bruge = Club("Club Bruges", "布鲁日", "BEL", 2, 0)
donetsk = Club("Shakhtar Donetsk", "顿涅茨克矿工", "UKR", 2, 0)
ac_milan = Club("AC Milan", "AC米兰", "ITA", 2, 0)
pot2 = [leverkusen, a_madrid, atlanta, juventus, benfica, arsenal, bruge, donetsk, ac_milan]


feyenoord = Club("Feyenoord", "费耶诺德", "NET", 3, 0)
sporting_cp = Club("Sporting Lisbon", "葡萄牙体育", "POR", 3, 0)
psv = Club("PSV Eindhoven", "埃因霍温", "NET", 3, 0)
zagreb = Club("Dinamo Zagreb", "萨格勒布迪纳摩", "CRO", 3, 0)
salzburg = Club("Salzburg", "萨尔茨堡红牛", "AUST", 3, 0)
lille = Club("Lille", "里尔", "FRA", 3, 0)
zvezda = Club("Red Star Belgrade", "贝尔格莱德红星", "SER", 3, 0)
young_boys = Club("Young Boys", "年轻人", "SWI", 3, 0)
celtic = Club("Celtic", "凯尔特人", "SCO", 3, 0)
pot3 = [feyenoord, sporting_cp, psv, zagreb, salzburg, lille, zvezda, young_boys, celtic]

bratislava = Club("Slovan Bratislava", "布拉迪斯拉发", "SLO", 4, 0)
monaco = Club("Monaco", "摩纳哥", "FRA", 4, 0)
praha = Club("Sparta Prague", "布拉格斯巴达", "CZE", 4, 0)
aston = Club("Aston Villa", "阿斯顿维拉", "ENG", 4, 0)
bologna = Club("Bologna", "博洛尼亚", "ITA", 4, 0)
girona = Club("Girona", "赫罗纳", "ESP", 4, 0)
stuttgart = Club("Stuttgart", "斯图加特", "GER", 4, 0)
graz = Club("Sturm Graz", "格拉茨风暴", "AUST", 4, 0)
brestois = Club("Brest", "布雷斯特", "FRA", 4, 0)
pot4 = [bratislava, monaco, praha, aston, bologna, girona, stuttgart, graz, brestois]
pots = [pot1, pot2, pot3, pot4]

all_clubs = [mancity, bayern, rm, psg, liverpool, inter, dortmund, leipzig, barca, 
             leverkusen, a_madrid, atlanta, juventus, benfica, arsenal, bruge, donetsk, ac_milan,
             feyenoord, sporting_cp, psv, zagreb, salzburg, lille, zvezda, young_boys, celtic,
             bratislava, monaco, praha, aston, bologna, girona, stuttgart, graz, brestois]
current_lst = []

  
count = 0

for i in all_clubs:
   i.rival = []
num = 0
m = 0
while m < 36:
  i = all_clubs[num]
  for pot in pots:
    selectable = [club for club in pot if club.country != i.country and len(club.rival) < 8 and club not in i.rival]
    number = 2
    if pot == pot1:
      if len(i.rival) >= 2:
          continue
      if len(i.rival) == 1:
        number = 1
    if pot == pot2:
      if len(i.rival) >= 4:
          continue
      if len(i.rival) == 3:
        number = 1
    if pot == pot3:
      if len(i.rival) >= 6:
          continue
      if len(i.rival) == 5:
        number = 1
    if pot == pot4:
      if len(i.rival) >= 8:
          continue
      if len(i.rival) == 7:
        number = 1
       
           
    if len(selectable) >= 2:
      selected = random.sample(selectable, number)
      for j in selected:
        j.rival += [i]
        i.rival += [j]
        selectable = []
    else:
       print(f"Not enough clubs to sample from for {i.name_chn} in pot {pots.index(pot) + 1}")
  new_lst = []
  for k in i.rival:
    new_lst += [k.name_chn]
  print (i.name_chn, new_lst)
  m += 1
  num += 9
  if num >= 36:
     num += 1
     num = num % 9
  



  



