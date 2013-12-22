# -*- coding: utf-8 -*-
import random
tercih=0
atk =random.randrange(1,101)
otk =input("bir kutu numarası giriniz: ")
if otk !=atk :
	soru = input ("tercihiniz %s mı %s mı?" %(atk,otk))
	tercih = soru
	if tercih == atk :
		print "kazandınız"
	else:
		print "kaybettiniz"
while otk==atk :
	otk=random.randrange(1,101)
	soru = input ("tercihiniz %s mı %s mı?" %(atk,otk))
        tercih = soru
        if tercih == atk :
                print "kazandınız"
        else:
                print "kaybettiniz"
