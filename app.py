import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

# --- 1. OLDAL BEÁLLÍTÁSOK ---
st.set_page_config(page_title="Urológiai Nomogram", layout="wide", page_icon="🏥")

# --- STÍLUS (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #F5F5F7; }
    h1, h2, h3 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1D1D1F; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #0071E3; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #005BB5; color: white; }
    .result-box {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        border: 1px solid #E5E5EA;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    .metric-label { font-size: 0.9em; color: #86868B; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-value { font-size: 1.4em; font-weight: bold; color: #1D1D1F; }
    </style>
""", unsafe_allow_html=True)

# --- CÍMSOR ÉS JOGI NYILATKOZAT ---
st.title("🏥 Urológiai Diagnosztika")

st.warning("""
**Jogi Nyilatkozat:** Ez az alkalmazás kizárólag tájékoztató jellegű, és nem helyettesíti a szakorvosi diagnózist. 
A számítások a szakirodalomban publikált nomogramokon alapulnak (Liverpool, Miskolc, Toguri), de a klinikai döntéshozatal minden esetben az orvos felelőssége.
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
    st.info("💡 **Férfiak (50 év alatt).** Általános áramlásvizsgálat (Haylen et al.).")

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
            if val < limits[0]: return "< 5. percentilis (Kóros)", "error"
            if val < limits[1]: return "5-10. percentilis (Alacsony)", "warning"
            if val < limits[2]: return "10-25. percentilis (Mérsékelt)", "info"
            if val < limits[3]: return "25-50. percentilis (Átlagos)", "success"
            if val < limits[4]: return "50-75. percentilis (Jó)", "success"
            if val < limits[5]: return "75-90. percentilis (Kiváló)", "success"
            if val < limits[6]: return "90-95. percentilis (Kiemelkedő)", "success"
            return "> 95. percentilis (Magas)", "success"

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
                <div class="metric-value" style="color: {'#d32f2f' if col_max=='error' else '#f57c00' if col_max=='warning' else '#2e7d32'};">{txt_max}</div>
                <br>
                <div class="metric-label">Qave Eredmény</div>
                <div class="metric-value" style="color: {'#d32f2f' if col_ave=='error' else '#f57c00' if col_ave=='warning' else '#2e7d32'};">{txt_ave}</div>
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
                ax1.text(605, factor * np.sqrt(600), f'{p}%', fontsize=8)
            plot_patient_point(ax1, vol, qmax)
            st.pyplot(fig1)

        with g2:
            fig2, ax2 = create_plot("Liverpool Qave Nomogram", "Térfogat (ml)", "Qave (ml/s)", 600, 25)
            for p, factor in zip(percentiles, qave_limits):
                y_vals = factor * np.sqrt(x_vals)
                ax2.plot(x_vals, y_vals, label=f'{p}. pc', alpha=0.6, linewidth=1)
                ax2.text(605, factor * np.sqrt(600), f'{p}%', fontsize=8)
            plot_patient_point(ax2, vol, qave)
            st.pyplot(fig2)

# --- 2. MISKOLC NOMOGRAM LOGIKA ---
def miskolc_nomogram():
    st.info("💡 **Fiú gyermekek.** Részletes percentilis becslés (Szabó & Fegyverneki, 1995).")

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
            
            if z < -1.645: return "< 5. percentilis (Kóros)", "error"
            if z < -1.28: return "5-10. percentilis (Alacsony)", "warning"
            if z
