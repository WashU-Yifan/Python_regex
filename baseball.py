import sys,os,re

name_regex= re.compile(r"\b(^\w* \w*) batted\b")#group 1
bat_regex= re.compile(r".* batted (\d*) times") #bat group1, hit group 2
hit_regex=re.compile(r".* with (\d*) hits")
def na_regex(line):
    match =name_regex.match(line)
    if match:
        return match.group(1)
    else:
        return False

def nu_regex(line):
    match1 =bat_regex.match(line)
    match2=hit_regex.match(line)
    
    if match1 and match2:
        return match1.group(1),match2.group(1)
    else:
        return False

class player:
    def __init__(self, name,bat, hit):
        self.bat=bat
        self.name=name
        self.hit=hit

    def rate(self):
        return self.hit/self.bat

    def getname(self):
        return self.name
    
    def sethit(self, bat, hit):
        self.bat+=bat
        self.hit+=hit
        


if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename_to_execute")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")
players={}
f=open(filename)


for line in f:
    name=na_regex(line)
    bh= nu_regex(line)
    
    if name and bh :
        bat,hit=bh
        bat=int(bat)
        hit=int(hit)
        if name in players:
            players[name].sethit(bat,hit)
        else:
            players[name]=player(name, bat, hit)


v=[]
for name, p in players.items():
    v.append(p)
  #  print(name, p.getname())

#for p in v:
 #   print(p.getname(),p)

newv= sorted(v, key=lambda people: -people.rate())
#for p in newv:
  #  print(p.getname(),p)
for player in newv:
    print(player.getname(),": ", player.rate())

