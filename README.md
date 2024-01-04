# calcip
Calcip è un pacchetto software che consente di estrarre quasi tutto quello che si può estrarre da un indirizzo ipv4 accompagnato dalla sua subnet mask. Calcip è interamente scritto in python, ed è open source.

## Funzionamento:
Inizialmente viene diviso l'input e viene ricavata la subnet mask in notazione CIDR(tipo int) e l'indirizzo ip(tipo str), successivamente in una struttura dati inietto n volte 1 per il valore della subnet mask in notazione CIDR il restante è tutto 0. In questa maniera
ho la subnet mask in binario. L'obiettivo è quello di avere ip e subnet mask sia in binario e sia in decimale, per fare questo ho definito due funzioni binary_ipv4() e decimal_ipv4(). Prima di usarle però ho trasformato l'ip da stringa a lista di stringhe, 
in modo tale da poter scorrere senza effettuare estrazioni di sottostringhe. Quello che manca è l'indirizzo di network(bit dell'host tutti a 0) e di broadcast(bit dell'host tutti a 1) per trovare l'indirizzo di network sfrutto un operazione che si fa con la subnte mask
ossia fare l'and bit a bit dell'indirizzo(in questo caso dato in input) con la subnet mask, il risultato sarà l'indirizzo di network di quell'ipv4. Per l'indirizzo di broadcast ho iniettato in una struttura dati ogni bit dell'indirizzo dato in input per quante volte è
la subnetmask in notazione CIDR, appena ho finito la parte di network, inietto solamente 1 alla struttura dati, così facendo ho l'indirizzo di broadcast. Infine ho mandato tutto a video, con un particolare, ossia che tutti i bit dedicati alla network sono mandati a video
in verde, invece i bit dedicati agli host sono mandati a video in rosso.

## Come usarlo:
Per usare calcip è previsto eseguirlo da CLI e passargli come parametro l'ipv4 accompagnato dalla sua subnet mask in notazione CIDR. Calcip ancora non prevede controlli approfonditi sull'input dato di conseguenza l'input deve essere valido.
Entrare nella directory calcip e digitare:
```bat
python main.py 192.168.10/24

```
