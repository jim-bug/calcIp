# calcip

## Introduzione
Calcip è un progetto software in grado di estrarre quanto possibile da un indirizzo ip e la sua corrispettiva subnet mask.
Calcip nasce come strumento di verifica di subnetting e supernetting per le configurazioni dei router svolte presso il mio istituto. Volevo trovare un modo di unire due materie
e calcip ne è la dimostrazione, dato che è stato totalmente modificato con la versione 2 utilizzando l'ingegnieria del software.

## Descrizione
Calcip oltre ad essere in grado di estrarre quanto possibile da un ip e la sua corrispettiva subnetmask, è in grado di effettuare subnetting e supernetting,
richiedendo solamente la nuova subnet mask per il subnetting o supernetting. Calcip permette una visualizzazione a colori dei bit e byte dedicati alla rete e all'host attraverso le ANSI escape.



## Utilizzo
Per utilizzare calcip bisogna seguire la seguente sintassi:
```bash
python3 Main.py [OPTIONS] [IP/CIDR_SUBNETMASK] [SUBNETMASK] [SUPERNET_MASK]
```
Un esempio pratico è il seguente, con previsto solo l'ip:
```bash
python3 Main.py 192.168.1.67/24
```
Esempio con il subnetting:
```bash
python3 Main.py -s 192.168.1.67/24 29
```
Esempio con supernetting:
```bash
python3 Main.py -S 192.168.1.67/24 23
```

## Licenza
Calcip ha la licenza GNU GPL v3.0.

## Contatti
Per contattarmi potete scrivermi presso questo indirizzo email: ignazioandsperandeo@gmail.com
