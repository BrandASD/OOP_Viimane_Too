
class Karakter():
    def __init__(self,nimi,elud,tugevus):
        self.nimi=nimi
        self.elud=elud
        self.tugevus=tugevus
    def kaotaelusid(self,elud):
        elud-=1
        print(" Elusid on alles: ",elud)
    def lisaelusid(self,elud):
        elud+=1
        print(elud)
class Vaenlane(Karakter):
    def __init__(self,elud,tugevus):
        self.elud=elud
        self.tugevus=tugevus
    def kaotaelusid(self,elud):
        elud-=1
        print("Elusid on alles: ",elud)
hero=Karakter("Peeter",15,5)
boogieman=Vaenlane(25,3)
hero.kaotaelusid(15)
boogieman.kaotaelusid(25)

