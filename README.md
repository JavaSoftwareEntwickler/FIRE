# Simulatore di Crescita del Capitale

Questo progetto simula la crescita del capitale nel tempo, tenendo conto di un tasso di rendita, un tasso di inflazione e un prelievo annuale. Il programma genera un grafico che mostra l'evoluzione del capitale nel corso di 100 anni, sia in termini nominali che reali.

## Funzionalità

- Permette di impostare un capitale iniziale.
- Consente di definire un tasso di rendita annuale.
- Permette di definire un tasso di inflazione annuale.
- Consente di impostare un importo di prelievo annuale.
- Mostra la crescita del capitale nel tempo con un grafico che confronta il capitale nominale e il capitale reale (tenendo conto dell'inflazione).

## Requisiti

Per eseguire questo progetto, avrai bisogno di Python 3 e di alcune librerie esterne. Il file `requirements.txt` contiene l'elenco delle librerie necessarie.

### Librerie richieste

- `PySimpleGUI`: Utilizzato per creare l'interfaccia grafica del simulatore.
- `matplotlib`: Utilizzato per creare il grafico della crescita del capitale.
- `numpy`: Dipendenza necessaria per `matplotlib` per calcoli efficienti.

## Come usare il progetto

### 1. Clona il repository (opzionale)

Se non hai già il progetto sul tuo computer, puoi clonarlo utilizzando Git:

```bash
    git clone git@github.com:JavaSoftwareEntwickler/FIRE.git
    cd FIRE
```

### 2. Crea un ambiente virtuale (opzionale)

Se non hai già il progetto sul tuo computer, puoi clonarlo utilizzando Git:

```bash
    python -m venv venv
```

Attivare l'ambiente virtuale:

- Su Windows:


```bash
    venv\Scripts\activate
```

- Su macOS/Linux:


```bash
    source venv/bin/activate
```

### 3. Installa le dipendenze

Una volta creato e attivato l'ambiente virtuale, puoi installare le librerie necessarie utilizzando il file

```bash
    pip install -r requirements.txt

```
### 4. Esegui il programma

Una volta installate le dipendenze, puoi eseguire il programma Python. Esegui il file principale del progetto, ad esempio:

```bash
    python fire.py
```


