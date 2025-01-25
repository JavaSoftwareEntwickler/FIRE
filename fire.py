
import matplotlib.pyplot as plt

# Funzione che calcola la crescita del capitale tenendo conto di rendita, inflazione e prelievi
def calcola_crescita(capitale_iniziale, tasso_rendita, tasso_inflazione, prelievo_annuo, anni):
    capitale = capitale_iniziale
    capitali_nominali = []
    capitali_reali = []
    
    for anno in range(1, anni + 1):
        # Calcolo del capitale nominale con prelievo
        capitale *= (1 + tasso_rendita)
        capitale -= prelievo_annuo  # Prelievo annuale
        
        # Calcolo del capitale reale (tenendo conto dell'inflazione)
        capitale_reale = capitale / (1 + tasso_inflazione)**anno
        
        capitali_nominali.append(capitale)
        capitali_reali.append(capitale_reale)
    
    return capitali_nominali, capitali_reali

# Parametri di input
capitale_iniziale = float(input("Inserisci il capitale iniziale (€): "))
tasso_rendita = float(input("Inserisci il tasso di rendita annuo (%): ")) / 100
tasso_inflazione = float(input("Inserisci il tasso di inflazione annuo (%): ")) / 100
prelievo_annuo = float(input("Inserisci l'importo del prelievo annuale (€): "))
anni = 100

# Calcolo della crescita del capitale
capitali_nominali, capitali_reali = calcola_crescita(capitale_iniziale, tasso_rendita, tasso_inflazione, prelievo_annuo, anni)

# Creazione del grafico
plt.figure(figsize=(10,6))
plt.plot(range(1, anni + 1), capitali_nominali, label='Capitale Nominale', color='blue')
plt.plot(range(1, anni + 1), capitali_reali, label='Capitale Reale', color='red', linestyle='--')
plt.xlabel('Anno')
plt.ylabel('Capitale (€)')
plt.title(f'Crescita del Capitale in 100 Anni con Prelievi\n(inflazione e rendita applicati)')
plt.legend()
plt.grid(True)
plt.show()
