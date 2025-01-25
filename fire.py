import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Funzione per disegnare il grafico
def draw_graph(capitale_nominale, capitale_reale):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(1, len(capitale_nominale) + 1), capitale_nominale, label='Capitale Nominale', color='blue')
    ax.plot(range(1, len(capitale_reale) + 1), capitale_reale, label='Capitale Reale', color='red', linestyle='--')
    ax.set_title('Crescita del Capitale in 100 Anni')
    ax.set_xlabel('Anno')
    ax.set_ylabel('Capitale (€)')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    return fig

# Funzione per aggiungere il grafico al canvas
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# Layout dell'interfaccia grafica
layout = [
    [sg.Text('Simulatore di Crescita del Capitale', font=("Helvetica", 16))],
    [sg.Text('Capitale Iniziale (€):'), sg.InputText(key='-CAPITALE-', size=(20, 1))],
    [sg.Text('Tasso di Rendita Annua (%):'), sg.InputText(key='-RENDITA-', size=(20, 1))],
    [sg.Text('Tasso di Inflazione Annua (%):'), sg.InputText(key='-INFLAZIONE-', size=(20, 1))],
    [sg.Text('Prelievo Annuale (€):'), sg.InputText(key='-PRELIEVO-', size=(20, 1))],
    [sg.Button('Calcola'), sg.Button('Esci')],
    [sg.Column([[sg.Canvas(key='-CANVAS-')]], expand_x=True, expand_y=True, size=(1000, 600), scrollable=True)]
]

# Creazione della finestra
window = sg.Window(
    'Simulatore di Crescita del Capitale', 
    layout, 
    resizable=True,  # Permette alla finestra di essere ridimensionabile
    finalize=True)
canvas_elem = window['-CANVAS-'].Widget

# Gestione degli eventi
figure_canvas_agg = None
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Esci':
        break

    if event == 'Calcola':
        try:
            # Ottieni i valori inseriti dall'utente
            capitale_iniziale = float(values['-CAPITALE-'])
            tasso_rendita = float(values['-RENDITA-']) / 100
            tasso_inflazione = float(values['-INFLAZIONE-']) / 100
            prelievo_annuo = float(values['-PRELIEVO-'])
            anni = 100

            # Calcola la crescita del capitale
            capitali_nominali, capitali_reali = calcola_crescita(capitale_iniziale, tasso_rendita, tasso_inflazione, prelievo_annuo, anni)

            # Rimuovi il grafico precedente
            if figure_canvas_agg:
                figure_canvas_agg.get_tk_widget().forget()

            # Disegna il nuovo grafico
            fig = draw_graph(capitale_nominale=capitali_nominali, capitale_reale=capitali_reali)
            figure_canvas_agg = draw_figure(canvas_elem, fig)

        except ValueError:
            sg.popup_error("Per favore, inserisci valori validi!")

# Chiudi la finestra
window.close()
