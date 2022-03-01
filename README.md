# MTAA_SIP JÁN HERCEG 102940
## ZADANIE
Na vašom počítači (alebo virtuálnom počítači) sprevádzkujte SIP Proxy, ktorá umožní prepájanie a realizáciu hovorov medzi štandardnými SIP klientami. Na implementáciu vašej SIP Proxy si môžete zvoliť akýkoľvek programovací jazyk a použiť akúkoľvek SIP knižnicu, ktorá pre daný programovací jazyk existuje. Vo výsledku však musíte spúšťať “váš kód”, v ktorom sú zakomponované knižnice, ktoré poskytujú funkcionalitu SIP Proxy. To znamená, že nemôžete zobrať existujúcu SIP Proxy ako napr. Asterisk, kde len skompilujete alebo priamo spustíte cudziu binárku… Hovor musí byť realizovaný medzi dvomi fyzickými zariadeniami v rámci LAN siete.
##Jazyk:
Python
##GitHub s vypracovaným zadaním a PCAP súbormi:
https://github.com/johnnyjonky/MTAA_SIP
##Implementácia: 
Prebral som “funkčnú knižnicu” sipfullproxy.py (https://github.com/tirfil/PySipFullProxy), ktorú som importol do môjho main.py, pomocou ktorého následne spúšťam SIP proxy server
Premenné, ktoré sú potrebné pre správne fungovanie sipfullproxy sú čítané a menené v maine pomocou ‘sipfullproxy.premenná’ – inak sa hodnoty premenných nemenili správnym spôsobom – menili sa iba v main.py
Socket server už však beží v main.py, takže nie je použité sipfullproxy.server (čo taktiež funguje, ale server chceme mať spustený pomocou main.py)
## Poznámky ku sipfullproxy.py:
Tento SIP proxy server bolo potrebné upraviť a spojazdniť – meniť priamo jeho kód, z dôvodu, že bol napísaný v staršej verzii pythonu, odkedy sa u niektorých vecí mohla zmeniť (a aj zmenila) syntax, prípadne niektoré časti kódu už nie sú korektné. 
Zmeny sa týkajú pridania funkcií .encode() a .decode(), prípadne sú pozmenené joiny a podobne. 
Taktiež je zakomentovaná časť kódu, ktorá zakazovala použitie SIP na lokálnych IP adresách.
V rámci zadania som taktiež pridal časti kódu, ktoré boli potrebné pre zmenu SIP stavových kódov.
Okrem tohto sa funkcionalita sipfullproxy.py nijako nemenila.
## Splnené minimálne požiadavky:
-	Registrácia účastníka (bez nutnosti autentifikácie) 
-	Vytočenie hovoru a zvonenie na druhej strane 
-	Prijatie hovoru druhou stranou, fungujúci hlasový hovor 
-	Ukončenie hlasového hovoru (prijatého aj neprijatého)
## Splnené doplnkové funkcionality:
-	Presmerovanie hovoru na iného účastníka
-	Možnosť realizovať videohovor
-	Úprava SIP stavových kódov z zdrojovom kóde proxy, napr. “486 Busy Here” zmeníte na “486 Obsadené”
--	 Zoznam zmenených stavových kódov:
---	200 OK -> 200 VIBAVENE OK
---	100 Trying -> 100 Skusam
---	180 Ringing -> 180 Zvoniiiiim
---	487 Request terminated -> 487 STERMINOVANE OK
---	480 Temporarily unavailable -> 480 NEPISTE MI KET – Temporarily unavailable
---	500 Server Internal Error -> 500 CERKA PLACE AKO DAST LEBO Server Internal Error
---	400 Bad request -> 400 DOSTE VI (Bad request)
## PCAP súbory:
Nachádzajú sa na githube pre všetky splnené požiadavky/funkcionality, s výnimkou zmenených SIP stavových kódov, nakoľko kódy sú viditeľné u už existujúcich pcap súborov.
