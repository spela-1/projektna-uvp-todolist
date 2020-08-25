import model

s = model.Seznam_uporabnikov('uporabniki')

s.dodaj_uporabnika("Špela", "Sc.1003067")
s.dodaj_uporabnika("Tim1234", "tk")
s.uporabniki["Špela"].nov_projekt("Tenis")
s.uporabniki["Špela"].seznam_projektov[0].nova_naloga("igra", [2020,7,21], [16, 0], 5)
s.uporabniki["Špela"].nov_projekt("Izpit za avto")
s.uporabniki["Špela"].seznam_projektov[1].nova_naloga("1 ura", [2020,8,6], [19, 38], 1)
s.uporabniki["Špela"].seznam_projektov[1].nova_naloga("glavna", [2020,8,6], [20, 0], 3)
s.uporabniki["Špela"].seznam_projektov[0].nova_naloga("servis", [2020,8, 14], [16, 0], 4)
s.deli_projekt("Špela", 0, "Tim1234")
s.shrani_uporabnika("Špela")
s.shrani_uporabnika("Tim1234")
#print([naloga.v_seznam() for naloga in u.naloge_po_dnevih_prihodnje()])

'''
u2 = Uporabnik.nalozi_stanje("test.json")
print(u2.shrani("test2.json"))

u2 = Uporabnik.nalozi_stanje("test.json")
print(u2.seznam_projektov[0].deljeno_z)
'''

s2 = model.Seznam_uporabnikov('uporabniki')
d = s2.deljeni_projekti("Tim1234")
print(len(d), d[0].ime)