{\rtf1\ansi\ansicpg1250\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import matplotlib.pyplot as plt\
import numpy as np\
import math\
\
# --- OLDAL BE\'c1LL\'cdT\'c1SOK ---\
st.set_page_config(page_title="Urol\'f3giai Nomogram", layout="wide")\
\
# St\'edlus (Emojik n\'e9lk\'fcl, letisztult)\
st.markdown("""\
    <style>\
    .main \{ background-color: #F5F5F7; \}\
    h1, h2, h3 \{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; \}\
    .stButton>button \{ width: 100%; border-radius: 8px; height: 3em; background-color: #0071E3; color: white; border: none; \}\
    .stButton>button:hover \{ background-color: #005BB5; color: white; \}\
    .result-box \{\
        padding: 20px;\
        background-color: white;\
        border-radius: 10px;\
        border-left: 5px solid #0071E3;\
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);\
        margin-bottom: 20px;\
    \}\
    .metric-label \{ font-size: 0.9em; color: #666; margin-bottom: 5px; \}\
    .metric-value \{ font-size: 1.4em; font-weight: bold; color: #333; \}\
    </style>\
""", unsafe_allow_html=True)\
\
# --- SEG\'c9DF\'dcGGV\'c9NYEK GRAFIKONHOZ ---\
def create_plot(title, xlabel, ylabel, x_max, y_max):\
    fig, ax = plt.subplots(figsize=(8, 5))\
    ax.set_title(title, fontsize=12, fontweight='bold')\
    ax.set_xlabel(xlabel)\
    ax.set_ylabel(ylabel)\
    ax.set_xlim(0, x_max)\
    ax.set_ylim(0, y_max)\
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)\
    return fig, ax\
\
def plot_patient_point(ax, x, y):\
    ax.scatter(x, y, color='red', s=100, zorder=10, marker='x', label='P\'e1ciens \'e9rt\'e9ke')\
    ax.legend(loc='upper left')\
\
# --- 1. LIVERPOOL NOMOGRAM ---\
def liverpool_nomogram():\
    st.header("Liverpool Nomogram")\
    st.markdown("F\'e9rfiak")\
\
    c1, c2, c3 = st.columns([1, 1, 2])\
    \
    with c1:\
        vol = st.number_input("\'dcr\'edtett t\'e9rfogat (ml)", min_value=0.0, value=400.0, step=10.0)\
    with c2:\
        qmax = st.number_input("Maxim\'e1lis \'e1raml\'e1s (Qmax - ml/s)", min_value=0.0, value=25.0, step=1.0)\
        qave = st.number_input("\'c1tlagos \'e1raml\'e1s (Qave - ml/s)", min_value=0.0, value=15.0, step=1.0)\
\
    # Sz\'e1m\'edt\'e1s\
    if vol > 0:\
        # Percentilisek meghat\'e1roz\'e1sa\
        def get_band_text(val, limits):\
            # limits: [5p, 10p, 25p, 50p, 75p, 90p, 95p]\
            if val < limits[0]: return "< 5. percentilis (K\'f3ros)", "error"\
            if val < limits[1]: return "5-10. percentilis (Alacsony)", "warning"\
            if val < limits[2]: return "10-25. percentilis (M\'e9rs\'e9kelt)", "info"\
            if val < limits[3]: return "25-50. percentilis (\'c1tlagos)", "success"\
            if val < limits[4]: return "50-75. percentilis (J\'f3)", "success"\
            if val < limits[5]: return "75-90. percentilis (Kiv\'e1l\'f3)", "success"\
            if val < limits[6]: return "90-95. percentilis (Kiemelked\uc0\u337 )", "success"\
            return "> 95. percentilis (Magas)", "success"\
\
        # Liverpool k\'e9plet: Q / sqrt(V)\
        # Hat\'e1rok (Haylen et al): \
        qmax_limits = [0.75, 0.95, 1.20, 1.50, 1.80, 2.10, 2.35]\
        qave_limits = [0.45, 0.55, 0.70, 0.875, 1.05, 1.20, 1.30]\
\
        res_qmax_val = qmax / math.sqrt(vol)\
        res_qave_val = qave / math.sqrt(vol)\
\
        txt_max, col_max = get_band_text(res_qmax_val, qmax_limits)\
        txt_ave, col_ave = get_band_text(res_qave_val, qave_limits)\
\
        # Eredm\'e9ny ki\'edr\'e1sa\
        with c3:\
            st.markdown(f"""\
            <div class="result-box">\
                <div class="metric-label">Qmax Eredm\'e9ny</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_max=='error' else '#f57c00' if col_max=='warning' else '#388e3c'\};">\{txt_max\}</div>\
                <br>\
                <div class="metric-label">Qave Eredm\'e9ny</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_ave=='error' else '#f57c00' if col_ave=='warning' else '#388e3c'\};">\{txt_ave\}</div>\
            </div>\
            """, unsafe_allow_html=True)\
\
        # GRAFIKON RAJZOL\'c1S\
        st.subheader("Grafikus \'e1br\'e1zol\'e1s")\
        g1, g2 = st.columns(2)\
\
        # X tengely gener\'e1l\'e1sa\
        x_vals = np.linspace(50, 600, 100)\
        \
        # Qmax Plot\
        with g1:\
            fig1, ax1 = create_plot("Liverpool Qmax Nomogram", "T\'e9rfogat (ml)", "Qmax (ml/s)", 600, 40)\
            percentiles = [5, 10, 25, 50, 75, 90, 95]\
            factors = qmax_limits \
            \
            for p, factor in zip(percentiles, factors):\
                y_vals = factor * np.sqrt(x_vals)\
                ax1.plot(x_vals, y_vals, label=f'\{p\}. pc', alpha=0.6, linewidth=1)\
                ax1.text(605, factor * np.sqrt(600), f'\{p\}%', fontsize=8)\
            \
            plot_patient_point(ax1, vol, qmax)\
            st.pyplot(fig1)\
\
        # Qave Plot\
        with g2:\
            fig2, ax2 = create_plot("Liverpool Qave Nomogram", "T\'e9rfogat (ml)", "Qave (ml/s)", 600, 25)\
            factors_ave = qave_limits\
            \
            for p, factor in zip(percentiles, factors_ave):\
                y_vals = factor * np.sqrt(x_vals)\
                ax2.plot(x_vals, y_vals, label=f'\{p\}. pc', alpha=0.6, linewidth=1)\
                ax2.text(605, factor * np.sqrt(600), f'\{p\}%', fontsize=8)\
            \
            plot_patient_point(ax2, vol, qave)\
            st.pyplot(fig2)\
\
# --- 2. MISKOLC NOMOGRAM ---\
def miskolc_nomogram():\
    st.header("Miskolci Nomogram")\
    st.markdown(\'93fi\'fa gyermekek.")\
\
    c1, c2, c3 = st.columns([1, 1, 2])\
    \
    with c1:\
        vol = st.number_input("\'dcr\'edtett t\'e9rfogat (ml)", min_value=0.0, value=150.0, step=10.0, key="m_v")\
        bsa_sel = st.selectbox("Testfelsz\'edn (BSA)", options=[1, 2, 3], \
                               format_func=lambda x: \{1:"< 0.92 m\'b2 (Kicsi)", 2:"0.92 - 1.42 m\'b2 (K\'f6zepes)", 3:"> 1.42 m\'b2 (Nagy)"\}[x])\
    with c2:\
        qmax = st.number_input("Maxim\'e1lis \'e1raml\'e1s (Qmax)", min_value=0.0, value=18.0, step=1.0, key="m_qm")\
        qave = st.number_input("\'c1tlagos \'e1raml\'e1s (Qave)", min_value=0.0, value=10.0, step=1.0, key="m_qa")\
\
    if vol > 0:\
        ln_v = math.log(vol + 1)\
        \
        # Miskolc param\'e9terek (A \'e9s B)\
        # Strukt\'fara: \{BSA_KAT: \{'max': (A5, B5, A95, B95), 'ave': (A5, B5, A95, B95)\}\}\
        params = \{\
            1: \{'max': (5.7244, -13.6033, 3.8131, 6.5131), 'ave': (3.4010, -7.4933, 4.9999, -7.8369)\},\
            2: \{'max': (5.2440, -14.1997, 4.9923, 3.4560), 'ave': (3.1713, -8.5399, 4.0800, -2.6337)\},\
            3: \{'max': (5.4150, -16.1122, 8.5447, -7.4559), 'ave': (4.3957, -14.5260, 6.8810, -11.0350)\}\
        \}\
        \
        p_curr = params[bsa_sel]\
\
        # Sz\'e1m\'edt\'f3 f\'fcggv\'e9ny\
        def calc_miskolc_percentile(val, A5, B5, A95, B95):\
            # Limit \'e9rt\'e9kek az adott t\'e9rfogatra\
            L5 = A5 * ln_v + B5\
            L95 = A95 * ln_v + B95\
            \
            # Z-score becsl\'e9s\
            mean = (L95 + L5) / 2\
            sd = (L95 - L5) / 3.29\
            z = (val - mean) / sd\
            \
            if z < -1.645: return "< 5. percentilis (K\'f3ros)", "error"\
            if z < -1.28: return "5-10. percentilis (Alacsony)", "warning"\
            if z < -0.675: return "10-25. percentilis (M\'e9rs\'e9kelt)", "info"\
            if z < 0: return "25-50. percentilis (\'c1tlagos)", "success"\
            if z < 0.675: return "50-75. percentilis (J\'f3)", "success"\
            if z < 1.28: return "75-90. percentilis (Kiv\'e1l\'f3)", "success"\
            if z < 1.645: return "90-95. percentilis (Kiemelked\uc0\u337 )", "success"\
            return "> 95. percentilis (Magas)", "success"\
\
        txt_max, col_max = calc_miskolc_percentile(qmax, *p_curr['max'])\
        txt_ave, col_ave = calc_miskolc_percentile(qave, *p_curr['ave'])\
\
        with c3:\
            st.markdown(f"""\
            <div class="result-box">\
                <div class="metric-label">Qmax Becsl\'e9s</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_max=='error' else '#f57c00' if col_max=='warning' else '#388e3c'\};">\{txt_max\}</div>\
                <br>\
                <div class="metric-label">Qave Becsl\'e9s</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_ave=='error' else '#f57c00' if col_ave=='warning' else '#388e3c'\};">\{txt_ave\}</div>\
            </div>\
            """, unsafe_allow_html=True)\
\
        # --- GRAFIKON ---\
        st.subheader("Miskolc g\'f6rb\'e9k")\
        mg1, mg2 = st.columns(2)\
        \
        x_vals = np.linspace(20, 600, 100)\
        ln_x = np.log(x_vals + 1)\
\
        def plot_miskolc_curves(ax, title, A5, B5, A95, B95, patient_y, y_limit):\
            ax.set_title(title)\
            ax.set_ylim(0, y_limit)\
            \
            # Interpol\'e1l\'e1s a percentilisekhez (Z-score alapj\'e1n)\
            # 5% (Z=-1.645), 10% (-1.28), 25% (-0.675), 50% (0), 75%, 90%, 95%\
            z_scores = [-1.645, -1.28, -0.675, 0, 0.675, 1.28, 1.645]\
            labels = [5, 10, 25, 50, 75, 90, 95]\
            \
            # Line\'e1ris interpol\'e1ci\'f3 az A \'e9s B param\'e9terek k\'f6z\'f6tt\
            mean_A = (A95 + A5) / 2\
            mean_B = (B95 + B5) / 2\
            sd_A = (A95 - A5) / 3.29\
            sd_B = (B95 - B5) / 3.29\
\
            for z, lab in zip(z_scores, labels):\
                A_z = mean_A + z * sd_A\
                B_z = mean_B + z * sd_B\
                y_vals = A_z * ln_x + B_z\
                ax.plot(x_vals, y_vals, label=f'\{lab\}. pc', linewidth=1, alpha=0.7)\
                ax.text(605, y_vals[-1], f'\{lab\}%', fontsize=8)\
\
            plot_patient_point(ax, vol, patient_y)\
\
        with mg1:\
            figm1, axm1 = create_plot("Qmax (Fi\'fa)", "T\'e9rfogat (ml)", "ml/s", 600, 50)\
            plot_miskolc_curves(axm1, "Qmax Nomogram", *p_curr['max'], qmax, 50)\
            st.pyplot(figm1)\
\
        with mg2:\
            figm2, axm2 = create_plot("Qave (Fi\'fa)", "T\'e9rfogat (ml)", "ml/s", 600, 30)\
            plot_miskolc_curves(axm2, "Qave Nomogram", *p_curr['ave'], qave, 30)\
            st.pyplot(figm2)\
\
# --- 3. TOGURI NOMOGRAM ---\
def toguri_nomogram():\
    st.header("Toguri Nomogram (Fi\'fak)")\
    st.markdown("Kifejezetten az **alacsony \'e1raml\'e1s (obstrukci\'f3)** sz\uc0\u369 r\'e9s\'e9re. A grafikon csak az als\'f3 tartom\'e1nyt (5-25%) mutatja.")\
\
    c1, c2, c3 = st.columns([1, 1, 2])\
    \
    with c1:\
        vol = st.number_input("\'dcr\'edtett t\'e9rfogat (ml)", min_value=0.0, value=140.0, step=10.0, key="t_v")\
        bsa_sel = st.selectbox("Testfelsz\'edn (BSA)", options=[0, 1], \
                               format_func=lambda x: \{0:"< 1.1 m\'b2 (Kicsi)", 1:"\uc0\u8805  1.1 m\'b2 (Nagy)"\}[x])\
    with c2:\
        qmax = st.number_input("Maxim\'e1lis \'e1raml\'e1s (Qmax)", min_value=0.0, value=12.0, step=1.0, key="t_qm")\
        qave = st.number_input("\'c1tlagos \'e1raml\'e1s (Qave)", min_value=0.0, value=8.0, step=1.0, key="t_qa")\
\
    if vol > 0:\
        # Toguri Adatok (Table 3) - L\'e9pcs\uc0\u337 zetes hat\'e1rok\
        # Form\'e1tum: [Vol_Max, 5p, 10p, 15p, 20p, 25p]\
        limits_max_small = [\
            (62.5, 4.0, 4.5, 5.0, 5.5, 6.0),\
            (112.5, 7.3, 9.0, 10.0, 8.5, 10.0), # Figyelem: az eredeti cikk adatai ingadoznak, de haszn\'e1ljuk a t\'e1bl\'e1zatot\
            (162.5, 10.0, 12.5, 11.5, 13.0, 14.0),\
            (9999, 11.0, 14.0, 13.5, 13.0, 15.0)\
        ]\
        limits_max_large = [\
            (62.5, 5.5, 8.0, 6.0, 7.0, 8.0),\
            (112.5, 11.0, 13.0, 13.5, 13.0, 14.0),\
            (162.5, 14.0, 16.0, 15.0, 17.0, 18.0),\
            (9999, 16.0, 19.0, 17.0, 19.0, 20.0)\
        ]\
        # Qave adatok\
        limits_ave_small = [\
            (62.5, 3.4, 3.8, 4.5, 4.9, 5.0),\
            (112.5, 4.9, 5.6, 6.0, 6.6, 6.9),\
            (162.5, 7.9, 8.3, 8.9, 9.3, 9.6),\
            (9999, 7.4, 7.9, 9.4, 9.7, 10.0)\
        ]\
        limits_ave_large = [\
            (62.5, 6.0, 6.3, 6.6, 6.8, 7.4),\
            (112.5, 8.2, 8.8, 9.1, 9.4, 10.1),\
            (162.5, 10.1, 11.4, 11.7, 12.0, 12.0),\
            (9999, 11.1, 11.5, 11.7, 12.4, 13.2)\
        ]\
\
        current_limits_max = limits_max_large if bsa_sel == 1 else limits_max_small\
        current_limits_ave = limits_ave_large if bsa_sel == 1 else limits_ave_small\
\
        # \'c9rt\'e9kel\'e9s\
        def evaluate_toguri(val, v_in, table):\
            # Megkeress\'fck a megfelel\uc0\u337  t\'e9rfogat s\'e1vot\
            row = next(r for r in table if v_in < r[0])\
            # row[1]=5p, row[2]=10p ... row[5]=25p\
            # Biztons\'e1gi rendez\'e9s a percentilisekhez (ha az eredeti cikkben anom\'e1lia van)\
            thresholds = sorted(row[1:]) \
            \
            if val < thresholds[0]: return "< 5. percentilis (K\'f3ros)", "error"\
            if val < thresholds[1]: return "5-10. percentilis (Nagyon Alacsony)", "warning"\
            if val < thresholds[2]: return "10-15. percentilis (Alacsony)", "warning"\
            if val < thresholds[3]: return "15-20. percentilis (Alacsony)", "warning"\
            if val < thresholds[4]: return "20-25. percentilis (M\'e9rs\'e9kelt)", "info"\
            return "> 25. percentilis (Norm\'e1l)", "success"\
\
        txt_max, col_max = evaluate_toguri(qmax, vol, current_limits_max)\
        txt_ave, col_ave = evaluate_toguri(qave, vol, current_limits_ave)\
\
        with c3:\
            st.markdown(f"""\
            <div class="result-box">\
                <div class="metric-label">Qmax Sz\uc0\u369 r\'e9s</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_max=='error' else '#f57c00' if col_max=='warning' else '#388e3c'\};">\{txt_max\}</div>\
                <br>\
                <div class="metric-label">Qave Sz\uc0\u369 r\'e9s</div>\
                <div class="metric-value" style="color: \{'#d32f2f' if col_ave=='error' else '#f57c00' if col_ave=='warning' else '#388e3c'\};">\{txt_ave\}</div>\
            </div>\
            """, unsafe_allow_html=True)\
\
        # --- TOGURI GRAFIKON (Step Chart) ---\
        st.subheader("Als\'f3 tartom\'e1ny grafikon (Sz\uc0\u369 r\'e9s)")\
        tg1, tg2 = st.columns(2)\
\
        def plot_toguri_steps(ax, table, patient_y, y_top):\
            # X tengely pontok a l\'e9pcs\uc0\u337 h\'f6z\
            x_steps = [0, 62.5, 112.5, 162.5, 300] # Utols\'f3 pont kiterjesztve\
            \
            colors = ['#d32f2f', '#e64a19', '#f57c00', '#ff9800', '#ffd54f'] # 5, 10, 15, 20, 25 pc sz\'ednek\
            labels = ['5 pc', '10 pc', '15 pc', '20 pc', '25 pc']\
            \
            # Percentilisek rajzol\'e1sa (5 db vonal)\
            for i in range(5): \
                y_steps = []\
                # Minden t\'e9rfogat s\'e1vhoz kiveszsz\'fck az i-edik percentilist (index i+1)\
                vals = [r[i+1] for r in table]\
                \
                # L\'e9pcs\uc0\u337 fokok rajzol\'e1sa\
                # A matplotlib 'step' function-je 'post' opci\'f3val\
                # De a Toguri bin-ek fixek, \'edgy manu\'e1lisan egyszer\uc0\u369 bb szakaszokat rajzolni\
                ax.hlines(vals[0], 0, 62.5, colors=colors[i], linestyles='-', label=labels[i] if i==0 or i==4 else "")\
                ax.hlines(vals[1], 62.5, 112.5, colors=colors[i], linestyles='-')\
                ax.hlines(vals[2], 112.5, 162.5, colors=colors[i], linestyles='-')\
                ax.hlines(vals[3], 162.5, 300, colors=colors[i], linestyles='-', label=labels[i] if i==4 else "") # Label csak a 25-n\'e9l\
                \
                # F\'fcgg\uc0\u337 leges \'f6sszek\'f6t\u337 k (opcion\'e1lis, de szebb n\'e9lk\'fcle orvosilag a bin-ek miatt)\
            \
            # Norm\'e1l tartom\'e1ny jel\'f6l\'e9se\
            ax.text(10, table[0][5] + 2, "NORM\'c1L TARTOM\'c1NY (>25pc)", color='green', fontweight='bold', fontsize=9)\
            \
            ax.set_xlim(0, 300)\
            ax.set_ylim(0, y_top)\
            plot_patient_point(ax, vol, patient_y)\
\
        with tg1:\
            figt1, axt1 = create_plot("Qmax Sz\uc0\u369 r\u337  (5-25. percentilis)", "T\'e9rfogat (ml)", "ml/s", 300, 25)\
            plot_toguri_steps(axt1, current_limits_max, qmax, 25)\
            st.pyplot(figt1)\
\
        with tg2:\
            figt2, axt2 = create_plot("Qave Sz\uc0\u369 r\u337  (5-25. percentilis)", "T\'e9rfogat (ml)", "ml/s", 300, 20)\
            plot_toguri_steps(axt2, current_limits_ave, qave, 20)\
            st.pyplot(figt2)\
\
\
# --- F\uc0\u336 MEN\'dc (TABOK) ---\
tabs = st.tabs(["Liverpool", "Miskolc", "Toguri"])\
\
with tabs[0]:\
    liverpool_nomogram()\
with tabs[1]:\
    miskolc_nomogram()\
with tabs[2]:\
    toguri_nomogram()}