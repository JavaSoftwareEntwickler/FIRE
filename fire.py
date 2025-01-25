import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle

# Funzione che calcola la crescita del capitale
def calcola_crescita(capitale_iniziale, tasso_rendita, tasso_inflazione, prelievo_annuo, anni):
    capitale = capitale_iniziale
    capitali_nominali = []
    capitali_reali = []
    
    for anno in range(1, anni + 1):
        capitale *= (1 + tasso_rendita)
        capitale -= prelievo_annuo
        capitale_reale = capitale / (1 + tasso_inflazione)**anno
        capitali_nominali.append(capitale)
        capitali_reali.append(capitale_reale)
    
    return capitali_nominali, capitali_reali

# Funzione per disegnare il grafico con interattività
def draw_graph_interactive(capitale_nominale, capitale_reale):
    fig, ax = plt.subplots(figsize=(8, 6))
    x = range(1, len(capitale_nominale) + 1)
    
    line_nominale, = ax.plot(x, capitale_nominale, label='Capitale Nominale', color='blue')
    line_reale, = ax.plot(x, capitale_reale, label='Capitale Reale', color='red', linestyle='--')
    ax.set_title('Crescita del Capitale in 100 Anni')
    ax.set_xlabel('Anno')
    ax.set_ylabel('Capitale (€)')
    ax.legend()
    ax.grid(True)

    # Tooltip per mostrare i valori
    annot = ax.annotate("", xy=(0, 0), xytext=(15, 15),
                        textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    # Evidenziare un'area con un rettangolo
    rect = Rectangle((0, 0), 0, 0, linewidth=1, edgecolor='green', facecolor='green', alpha=0.3)
    ax.add_patch(rect)

    # Funzione per aggiornare il tooltip
    def update_annot(line, ind):
        x, y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        text = f"Anno: {int(x[ind['ind'][0]])}\nCapitale: €{y[ind['ind'][0]]:,.2f}"
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.8)

    # Evento di hovering
    def on_hover(event):
        visible = annot.get_visible()
        for line in [line_nominale, line_reale]:
            cont, ind = line.contains(event)
            if cont:
                update_annot(line, ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
        if visible:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    # Evento di selezione (per evidenziare un'area)
    def on_select(event):
        if event.xdata and event.ydata:
            start = max(1, int(event.xdata) - 5)
            end = min(len(capitale_nominale), int(event.xdata) + 5)
            rect.set_xy((start, 0))
            rect.set_width(end - start)
            rect.set_height(max(capitale_nominale + capitale_reale))
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)
    fig.canvas.mpl_connect("button_press_event", on_select)

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
    [sg.Column([[sg.Canvas(key='-CANVAS-')]], expand_x=True, expand_y=True, size=(500, 300), scrollable=True)]
]

# Creazione della finestra
window = sg.Window(
    'Simulatore di Crescita del Capitale',
    layout,
    resizable=True,
    finalize=True
)

# Permette al canvas di adattarsi
window['-CANVAS-'].Widget.pack(fill='both', expand=True)

# Variabile per il grafico
figure_canvas_agg = None

# Gestione degli eventi
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

            # Disegna il nuovo grafico interattivo
            fig = draw_graph_interactive(capitale_nominale=capitali_nominali, capitale_reale=capitali_reali)
            figure_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

        except ValueError:
            sg.popup_error("Per favore, inserisci valori validi!")

# Chiudi la finestra
window.close()
