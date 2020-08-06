import json
import datetime

class Naloga():
    def __init__(self, id, id_pr, tekst, datum=None , ura=None, prioriteta=None):
        self.tekst = tekst
        self.datum = datum
        self.ura = ura
        self.opravljeno = False
        self.prioriteta = prioriteta
        self.id = id
        self.id_pr = id_pr
    
    def v_seznam(self):
        slovar = {
            'tekst': self.tekst,
            'datum': self.datum,
            'ura': self.ura,
            'opravljeno': self.opravljeno,
            'prioriteta': self.prioriteta,
            'id': self.id
        }
        return slovar

    @classmethod
    def iz_slovarja_nal(cls, nal_slovar, id_pr):
        tekst = nal_slovar['tekst']
        datum = nal_slovar['datum']
        ura = nal_slovar['ura']
        opravljeno = nal_slovar['opravljeno']
        prioriteta = nal_slovar['prioriteta']
        id = nal_slovar['id']
        naloga = cls(id, id_pr, tekst, datum, ura, prioriteta)
        naloga.opravljeno = opravljeno  
        return naloga   


class Projekt():
    def __init__(self, id, ime):
        self.ime = ime
        self.seznam_nalog = []
        self.naslednji_id = 0
        self.id = id
    
    def nova_naloga(self, tekst, datum=None , ura=None, prioriteta=None):
        naloga = Naloga(self.naslednji_id, self.id, tekst, datum, ura, prioriteta)
        self.seznam_nalog.append(naloga)
        self.naslednji_id += 1

    def izbrisi_nalogo(self, id):
        for naloga in self.seznam_nalog:
            if naloga.id == id:
                self.seznam_nalog.remove(naloga)
                break
    
    def v_seznam(self):
        nov = []
        for naloga in self.seznam_nalog:
            nov.append(naloga.v_seznam())
        slovar = {
            'ime': self.ime,
            'naslednji_id': self.naslednji_id,
            'seznam_nalog': nov,
            'id': self.id
            }
        return slovar

    @classmethod
    def iz_slovarja_pr(cls, pr_slovar):
        ime = pr_slovar['ime']
        naslednji_id = pr_slovar['naslednji_id']
        id = pr_slovar['id']

        nov = []
        for nal_slovar in pr_slovar['seznam_nalog']:
            naloga = Naloga.iz_slovarja_nal(nal_slovar, id)
            nov.append(naloga)
        projekt = cls(id, ime)
        projekt.seznam_nalog = nov
        projekt.naslednji_id = naslednji_id
        return projekt
        




class Uporabnik():
    def __init__(self, ime, geslo):
        self.seznam_projektov = []
        self.ime = ime
        self.zasifrirano_geslo = geslo
        self.naslednji_id_pr = 0
    
    def shrani(self, ime_datoteke):
        nov = []
        for projekt in self.seznam_projektov:
            nov.append(projekt.v_seznam())
        slovar = {
            'ime': self.ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'seznam_projektov': nov,
            'naslednji_id_pr': self.naslednji_id_pr
        }
        with open(ime_datoteke, 'w',encoding="utf-8") as datoteka:
            json.dump(slovar, datoteka, ensure_ascii=False, indent=4)


    def nov_projekt(self, ime):
        for projekt in self.seznam_projektov:
            if projekt.ime == ime:
                return 'error'   
        projekt = Projekt(self.naslednji_id_pr, ime)
        self.seznam_projektov.append(projekt)
        self.naslednji_id_pr += 1

    def izbrisi_projekt(self, ime):
        for projekt in self.seznam_projektov:
            if projekt.ime == ime:
                self.seznam_projektov.remove(projekt)
                break 
    
    def naloge_po_dnevih(self):
        naloge = []
        for projekt in self.seznam_projektov:
            naloge.extend(projekt.seznam_nalog)

        naloge.sort(key=lambda naloga: naloga.datum + naloga.ura)
        return naloge

    def naloge_po_dnevih_prihodnje(self):
        naloge = self.naloge_po_dnevih()
        danes = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
        prihodnje_naloge = [naloga for naloga in naloge if naloga.datum >= danes]
        
        return prihodnje_naloge
        
        
    
    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke, encoding='utf-8') as datoteka:
            slovar = json.load(datoteka)
        ime = slovar['ime']
        naslednji_id_pr = slovar['naslednji_id_pr']
        zasifrirano_geslo = slovar['zasifrirano_geslo']
        uporabnik = cls(ime, zasifrirano_geslo)
        nov = []
        for pr_slovar in slovar['seznam_projektov']:
            projekt = Projekt.iz_slovarja_pr(pr_slovar)
            nov.append(projekt)
        uporabnik.seznam_projektov = nov
        uporabnik.naslednji_id_pr = naslednji_id_pr
        return uporabnik
            

            

        





u = Uporabnik("Špela", "Sc.1003067")
u.nov_projekt("Tenis")
u.seznam_projektov[0].nova_naloga("Timi", [2020,7,21], [16, 0], 5)
u.nov_projekt("Izpit za avto")
u.seznam_projektov[1].nova_naloga("1 ura", [2020,8,6], [19, 38], 1)
u.seznam_projektov[1].nova_naloga("glavna", [2020,8,6], [20, 0], 3)
u.seznam_projektov[0].nova_naloga("Timi", [2020,8, 14], [16, 0], 4)
#print(u.shrani("test.json"))
print([naloga.v_seznam() for naloga in u.naloge_po_dnevih_prihodnje()])

'''
u2 = Uporabnik.nalozi_stanje("test.json")
print(u2.shrani("test2.json"))
'''