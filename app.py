import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

# --- 1. OLDAL BEÁLLÍTÁSOK ---
st.set_page_config(page_title="Urológiai Nomogram", layout="wide")

# --- STÍLUS (CSS) ---
st.markdown("""
<style>
    .main { background-color: #F5F5F7; }
    h1, h2, h3 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1D1D1F; }
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 3em; 
        background-color: #0071E3; 
        color: white; 
        border: none; 
        font-weight: bold; 
    }
    .stButton>button:hover { background-color: #005BB5; color: white; }
    .result-box {
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        border: 1px solid #E5E5EA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .metric-label { 
        font-size: 0.9em; 
        color: #666; 
        margin-bottom: 5px; 
        text-transform: uppercase; 
        letter-spacing: 0.5px; 
    }
    .metric-value { 
        font-size: 1.3em; 
        font-weight: bold; 
        color: #333; 
    }
</style>
""", unsafe_allow_html=True)

# --- CÍMSOR ÉS JOGI NYILATKOZAT ---
st.title("Urológiai Diagnosztika")

st.warning("""
Jogi Nyilatkozat: Ez az alkalmazás kizárólag tájékoztató jellegű. 
A számítások a szakirodalomban publikált nomogramokon alapulnak (Liverpool, Miskolc, Toguri), de a klinikai döntéshozatal minden esetben a vizsgáló személy felelőssége.
A fejlesztő nem vállal felelősséget az eredmények alapján hozott döntésekért.
""")

st.markdown("### Unified Nomogram App")

# --- SEGÉDFÜGGVÉNYEK GRAFIKONHOZ ---
def create_plot(title, xlabel, ylabel, x_max, y_max):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    return fig, ax

def plot_patient_point(ax, x, y):
    ax.scatter(x, y, color='red', s=100, zorder=10, marker='x', label='Páciens értéke')
    ax.legend(loc='upper left')

# --- 1. LIVERPOOL NOMOGRAM LOGIKA ---
def liverpool_nomogram():
    st.info("Férfiak (50 év alatt). Általános áramlásvizsgálat (Haylen et al.).")

    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        vol = st.number_input("Ürített térfogat (ml)", min_value=0.0, value=400.0, step=10.0, key="l_v")
    with c2:
        qmax = st.number_input("Maximális áramlás (Qmax - ml/s)", min_value=0.0, value=25.0, step=1.0, key="l_qm")
        qave = st.number_input("Átlagos áramlás (Qave - ml/s)", min_value=0.0, value=15.0, step=1.0, key="l_qa")

    # Számítás
    if vol > 0:
        # Percentilisek meghatározása
        def get_band_text(val, limits):
            if val < limits[0]: return "< 5. percentilis (Kóros)", "#d32f2f" # Piros
            if val < limits[1]: return "5-10. percentilis (Alacsony)", "#f57c00" # Narancs
            if val < limits[2]: return "10-25. percentilis (Mérsékelt)", "#fbc02d" # Sárga
            if val < limits[3]: return "25-50. percentilis (Átlagos)", "#388e3c" # Zöld
            if val < limits[4]: return "50-75. percentilis (Jó)", "#388e3c"
            if val < limits[5]: return "75-90. percentilis (Kiváló)", "#388e3c"
            if val < limits[6]: return "90-95. percentilis (Kiemelkedő)", "#1976d2" # Kék
            return "> 95. percentilis (Magas)", "#1976d2"

        # Liverpool képlet: Q / sqrt(V)
        qmax_limits = [0.75, 0.95, 1.20, 1.50, 1.80, 2.10, 2.35]
        qave_limits = [0.45, 0.55, 0.70, 0.875, 1.05, 1.20, 1.30]

        res_qmax_val = qmax / math.sqrt(vol)
        res_qave_val = qave / math.sqrt(vol)

        txt_max, col_max = get_band_text(res_qmax_val, qmax_limits)
        txt_ave, col_ave = get_band_text(res_qave_val, qave_limits)

        # Eredmény kiírása
        with c3:
            st.markdown(f"""
            <div class="result-box">
                <div class="metric-label">Qmax Eredmény</div>
                <div class="metric-value" style="color: {col_max};">{txt_max}</div>
                <br>
                <div class="metric-label">Qave Eredmény</div>
                <div class="metric-value" style="color: {col_ave};">{txt_ave}</div>
            </div>
            """, unsafe_allow_html=True)

        # GRAFIKON RAJZOLÁS
        st.subheader("Grafikus ábrázolás")
        g1, g2 = st.columns(2)

        x_vals = np.linspace(50, 600, 100)
        
        with g1:
            fig1, ax1 = create_plot("Liverpool Qmax Nomogram", "Térfogat (ml)", "Qmax (ml/s)", 600, 40)
            percentiles = [5, 10, 25, 50, 75, 90, 95]
            for p, factor in zip(percentiles, qmax_limits):
                y_vals = factor * np.sqrt(x_vals)
                ax1.plot(x_vals, y_vals, label=f'{p}. pc', alpha=0.6, linewidth=1)
                if p in [5, 50, 95]: ax1.text(605, factor * np.sqrt(600), f'{p}%', fontsize=8)
            plot_patient_point(ax1, vol, qmax)
            st.pyplot(fig1)

        with g2:
            fig2, ax2 = create_plot("Liverpool Qave Nomogram", "Térfogat (ml)", "Qave (ml/s)", 600, 25)
            for p, factor in zip(percentiles, qave_limits):
                y_vals = factor * np.sqrt(x_vals)
                ax2.plot(x_vals, y_vals, label=f'{p}. pc', alpha=0.6, linewidth=1)
                if p in [5, 50, 95]: ax2.text(605, factor * np.sqrt(600), f'{p}%', fontsize=8)
            plot_patient_point(ax2, vol, qave)
            st.pyplot(fig2)

# --- 2. MISKOLC NOMOGRAM LOGIKA ---
def miskolc_nomogram():
    st.info("Fiú gyermekek. Részletes percentilis becslés (Szabó & Fegyverneki, 1995).")

    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        vol = st.number_input("Ürített térfogat (ml)", min_value=0.0, value=150.0, step=10.0, key="m_v")
        bsa_sel = st.selectbox("Testfelszín (BSA)", options=[1, 2, 3], 
                               format_func=lambda x: {1:"< 0.92 m² (Kicsi)", 2:"0.92 - 1.42 m² (Közepes)", 3:"> 1.42 m² (Nagy)"}[x])
    with c2:
        qmax = st.number_input("Maximális áramlás (Qmax)", min_value=0.0, value=18.0, step=1.0, key="m_qm")
        qave = st.number_input("Átlagos áramlás (Qave)", min_value=0.0, value=10.0, step=1.0, key="m_qa")

    if vol > 0:
        ln_v = math.log(vol + 1)
        
        # Miskolc paraméterek
        params = {
            1: {'max': (5.7244, -13.6033, 3.8131, 6.5131), 'ave': (3.4010, -7.4933, 4.9999, -7.8369)},
            2: {'max': (5.2440, -14.1997, 4.9923, 3.4560), 'ave': (3.1713, -8.5399, 4.0800, -2.6337)},
            3: {'max': (5.4150, -16.1122, 8.5447, -7.4559), 'ave': (4.3957, -14.5260, 6.8810, -11.0350)}
        }
        p_curr = params[bsa_sel]

        def calc_miskolc_percentile(val, A5, B5, A95, B95):
            L5 = A5 * ln_v + B5
            L95 = A95 * ln_v + B95
            mean = (L95 + L5) / 2
            sd = (L95 - L5) / 3.29
            z = (val - mean) / sd
            
            if z < -1.645: return "< 5. percentilis (Kóros)", "#d32f2f"
            if z < -1.28: return "5-10. percentilis (Alacsony)", "#f57c00"
            if z < -0.675: return "10-25. percentilis (Mérsékelt)", "#fbc02d"
            if z < 0: return "25-50. percentilis (Átlagos)", "#388e3c"
            if z < 0.675: return "50-75. percentilis (Jó)", "#388e3c"
            if z < 1.28: return "75-90. percentilis (Kiváló)", "#388e3c"
            if z < 1.645: return "90-95. percentilis (Kiemelkedő)", "#1976d2"
            return "> 95. percentilis (Magas)", "#1976d2"

        txt_max, col_max = calc_miskolc_percentile(qmax, *p_curr['max'])
        txt_ave, col_ave = calc_miskolc_percentile(qave, *p_curr['ave'])

        with c3:
            st.markdown(f"""
            <div class="result-box">
                <div class="metric-label">Qmax Becslés</div>
                <div class="metric-value" style="color: {col_max};">{txt_max}</div>
                <br>
                <div class="metric-label">Qave Becslés</div>
                <div class="metric-value" style="color: {col_ave};">{txt_ave}</div>
            </div>
            """, unsafe_allow_html=True)

        # GRAFIKON
        st.subheader("Miskolc görbék")
        mg1, mg2 = st.columns(2)
        x_vals = np.linspace(20, 600, 100)
        ln_x = np.log(x_vals + 1)

        def plot_miskolc_curves(ax, title, A5, B5, A95, B95, patient_y, y_limit):
            ax.set_title(title)
            ax.set_ylim(0, y_limit)
            z_scores = [-1.645, -1.28, -0.675, 0, 0.675, 1.28, 1.645]
            labels = [5, 10, 25, 50, 75, 90, 95]
            mean_A = (A95 + A5) / 2
            mean_B = (B95 + B5) / 2
            sd_A = (A95 - A5) / 3.29
            sd_B = (B95 - B5) / 3.29

            for z, lab in zip(z_scores, labels):
                A_z = mean_A + z * sd_A
                B_z = mean_B + z * sd_B
                y_vals = A_z * ln_x + B_z
                ax.plot(x_vals, y_vals, label=f'{lab}. pc', linewidth=1, alpha=0.7)
                if lab in [5, 50, 95]: ax.text(605, y_vals[-1], f'{lab}%', fontsize=8)
            plot_patient_point(ax, vol, patient_y)

        with mg1:
            figm1, axm1 = create_plot("Qmax (Fiú)", "Térfogat (ml)", "ml/s", 600, 50)
            plot_miskolc_curves(axm1, "Qmax Nomogram", *p_curr['max'], qmax, 50)
            st.pyplot(figm1)

        with mg2:
            figm2, axm2 = create_plot("Qave (Fiú)", "Térfogat (ml)", "ml/s", 600, 30)
            plot_miskolc_curves(axm2, "Qave Nomogram", *p_curr['ave'], qave, 30)
            st.pyplot(figm2)

# --- 3. TOGURI NOMOGRAM LOGIKA ---
def toguri_nomogram():
    st.warning("Figyelem: Ez a nomogram kifejezetten az alacsony áramlás (obstrukció) szűrésére készült (Toguri et al., 1982).")

    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        vol = st.number_input("Ürített térfogat (ml)", min_value=0.0, value=140.0, step=10.0, key="t_v")
        bsa_sel = st.selectbox("Testfelszín (BSA)", options=[0, 1], 
                               format_func=lambda x: {0:"< 1.1 m² (Kicsi)", 1:"≥ 1.1 m² (Nagy)"}[x])
    with c2:
        qmax = st.number_input("Maximális áramlás (Qmax)", min_value=0.0, value=12.0, step=1.0, key="t_qm")
        qave = st.number_input("Átlagos áramlás (Qave)", min_value=0.0, value=8.0, step=1.0, key="t_qa")

    if vol > 0:
        # Toguri Adatok
        limits_max_small = [(62.5, 4.0, 4.5, 5.0, 5.5, 6.0), (112.5, 7.3, 9.0, 10.0, 8.5, 10.0), (162.5, 10.0, 12.5, 11.5, 13.0, 14.0), (9999, 11.0, 14.0, 13.5, 13.0, 15.0)]
        limits_max_large = [(62.5, 5.5, 8.0, 6.0, 7.0, 8.0), (112.5, 11.0, 13.0, 13.5, 13.0, 14.0), (162.5, 14.0, 16.0, 15.0, 17.0, 18.0), (9999, 16.0, 19.0, 17.0, 19.0, 20.0)]
        limits_ave_small = [(62.5, 3.4, 3.8, 4.5, 4.9, 5.0), (112.5, 4.9, 5.6, 6.0, 6.6, 6.9), (162.5, 7.9, 8.3, 8.9, 9.3, 9.6), (9999, 7.4, 7.9, 9.4, 9.7, 10.0)]
        limits_ave_large = [(62.5, 6.0, 6.3, 6.6, 6.8, 7.4), (112.5, 8.2, 8.8, 9.1, 9.4, 10.1), (162.5, 10.1, 11.4, 11.7, 12.0, 12.0), (9999, 11.1, 11.5, 11.7, 12.4, 13.2)]

        current_limits_max = limits_max_large if bsa_sel == 1 else limits_max_small
        current_limits_ave = limits_ave_large if bsa_sel == 1 else limits_ave_small

        def evaluate_toguri(val, v_in, table):
            row = next(r for r in table if v_in < r[0])
            thresholds = sorted(row[1:]) 
            if val < thresholds[0]: return "< 5. percentilis (Kóros)", "#d32f2f"
            if val < thresholds[1]: return "5-10. percentilis (Nagyon Alacsony)", "#f57c00"
            if val < thresholds[2]: return "10-15. percentilis (Alacsony)", "#fbc02d"
            if val < thresholds[3]: return "15-20. percentilis (Alacsony)", "#fbc02d"
            if val < thresholds[4]: return "20-25. percentilis (Mérsékelt)", "#388e3c"
            return "> 25. percentilis (Normál)", "#388e3c"

        txt_max, col_max = evaluate_toguri(qmax, vol, current_limits_max)
        txt_ave, col_ave = evaluate_toguri(qave, vol, current_limits_ave)

        with c3:
            st.markdown(f"""
            <div class="result-box">
                <div class="metric-label">Qmax Szűrés</div>
                <div class="metric-value" style="color: {col_max};">{txt_max}</div>
                <br>
                <div class="metric-label">Qave Szűrés</div>
                <div class="metric-value" style="color: {col_ave};">{txt_ave}</div>
            </div>
            """, unsafe_allow_html=True)

        # GRAFIKON
        st.subheader("Alsó tartomány grafikon (Szűrés)")
        tg1, tg2 = st.columns(2)

        def plot_toguri_steps(ax, table, patient_y, y_top):
            colors = ['#d32f2f', '#e64a19', '#f57c00', '#ff9800', '#ffd54f']
            labels = ['5 pc', '10 pc', '15 pc', '20 pc', '25 pc']
            
            for i in range(5): 
                vals = [r[i+1] for r in table]
                ax.hlines(vals[0], 0, 62.5, colors=colors[i], linestyles='-', label=labels[i] if i==0 or i==4 else "")
                ax.hlines(vals[1], 62.5, 112.5, colors=colors[i], linestyles='-')
                ax.hlines(vals[2], 112.5, 162.5, colors=colors[i], linestyles='-')
                ax.hlines(vals[3], 162.5, 300, colors=colors[i], linestyles='-', label=labels[i] if i==4 else "")
            
            ax.text(10, table[0][5] + 2, "NORMÁL TARTOMÁNY (>25pc)", color='green', fontweight='bold', fontsize=9)
            ax.set_xlim(0, 300)
            ax.set_ylim(0, y_top)
            plot_patient_point(ax, vol, patient_y)

        with tg1:
            figt1, axt1 = create_plot("Qmax Szűrő (5-25. percentilis)", "Térfogat (ml)", "ml/s", 300, 25)
            plot_toguri_steps(axt1, current_limits_max, qmax, 25)
            st.pyplot(figt1)

        with tg2:
            figt2, axt2 = create_plot("Qave Szűrő (5-25. percentilis)", "Térfogat (ml)", "ml/s", 300, 20)
            plot_toguri_steps(axt2, current_limits_ave, qave, 20)
            st.pyplot(figt2)


# --- FŐMENÜ (TABOK) ---
tabs = st.tabs(["Liverpool", "Miskolc", "Toguri"])

with tabs[0]:
    liverpool_nomogram()
with tabs[1]:
    miskolc_nomogram()
with tabs[2]:
    toguri_nomogram()

# --- LÁBLÉC (COPYRIGHT) ---
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: gray; font-size: 0.8em;">
    © 2025 <b>Gémesi Marcell</b> | Minden jog fenntartva.<br>
    A szoftver szellemi tulajdona a készítőt illeti.
</div>
""", unsafe_allow_html=True)
