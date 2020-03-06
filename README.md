# lopuboss
Lõputöö

Eesmärk- skreipida veebilehelt jäähokiliiga NHL tulemused ning nende tulemuste põhjal koostada liigatabel.

Tehnoloogia - kasutatud Python 3.8.1; MS Visual Studio Code; BeautifulSoup 4.8.1 skreipimiseks

Kirjeldus protsessist - Määratleme URL-i, kus kohast andmed kätte saada ning seejärel toimub data "puhastamine". Programmi alguses loome ka databaasi kõikidest olemasolevatest meeskondadest. Peale Beautifulsoup'i "puhastamist" on esimene samm eemaldada kuupäev listist.
![Koodirida](/assets/capture1.PNG)

Teine samm- loome 4 listi, sest andmed oleks vaja sorteerida nelja listi (kodumeeskond, võõrsilmeeskond, skoor, lisaaeg). Kolmas samm on skoori eraldamine datast. Neljas samm teeb lisaaja listi. Viies samm puhastab listist pealtvaatajate arvu ja mängupikkuse eemaldades kõik numbrid listist. 
![Koodirida](/assets/capture2.PNG)

Kuues samm eraldab listist kodu ja võõrsil meeskonna ning sorteerib need vastavalt oma nimekirjadesse. Viimane samm kombineerib need listid omavahel üheks nimekirjaks. 
![Koodirida](/assets/capture3.PNG)


Tulemus - Eesmärgist suutsin saavutada skreipimise ja andmete puhastamise ning olulise data viimise ühte nimekirja. Järgmiseks sammuks saab liigatabeli tegemine.

