import streamlit as st
import pandas as pd
import numpy as np
import io
from datetime import datetime

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OLYMATH – Seleksi Olimpiade Matematika",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); min-height: 100vh; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1100px; }

/* Hero */
.hero { background: linear-gradient(135deg,rgba(255,255,255,.08),rgba(255,255,255,.03));
    border:1px solid rgba(255,255,255,.15); border-radius:24px; padding:2rem 3rem;
    text-align:center; margin-bottom:1.5rem; backdrop-filter:blur(10px); }
.hero-logo { font-size:2.8rem; font-weight:900; letter-spacing:-1px;
    background:linear-gradient(90deg,#f7971e,#ffd200); -webkit-background-clip:text;
    -webkit-text-fill-color:transparent; }
.hero-sub { color:rgba(255,255,255,.55); font-size:.95rem; margin-top:.3rem; }
.hero-badge { display:inline-block; background:linear-gradient(90deg,#f7971e,#ffd200);
    color:#000; font-size:.7rem; font-weight:700; padding:3px 12px; border-radius:99px;
    margin-bottom:.8rem; letter-spacing:1px; text-transform:uppercase; }

/* Cards */
.card { background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.13);
    border-radius:18px; padding:1.5rem 1.6rem; margin-bottom:1rem;
    backdrop-filter:blur(8px); }
.sec-title { color:#fff; font-size:1rem; font-weight:700; margin-bottom:.9rem;
    display:flex; align-items:center; gap:7px; }

/* Inputs */
.stNumberInput input, .stTextInput input {
    background:rgba(255,255,255,.08)!important; border:1px solid rgba(255,255,255,.2)!important;
    border-radius:10px!important; color:#fff!important; }
.stNumberInput label, .stTextInput label, .stFileUploader label {
    color:rgba(255,255,255,.8)!important; font-weight:500!important; font-size:.88rem!important; }

/* Buttons */
.stButton>button { background:linear-gradient(135deg,#f7971e,#ffd200)!important;
    color:#000!important; font-weight:700!important; border:none!important;
    border-radius:12px!important; width:100%!important; font-size:.97rem!important; }
.stButton>button:hover { transform:translateY(-2px)!important;
    box-shadow:0 8px 24px rgba(247,151,30,.4)!important; }
.stDownloadButton>button { background:linear-gradient(135deg,#11998e,#38ef7d)!important;
    color:#000!important; font-weight:700!important; border:none!important;
    border-radius:12px!important; width:100%!important; }

/* Result status cards */
.res-siap { background:linear-gradient(135deg,rgba(56,239,125,.15),rgba(17,153,142,.15));
    border:1.5px solid #38ef7d; border-radius:18px; padding:1.6rem; text-align:center; margin-bottom:.8rem; }
.res-pot  { background:linear-gradient(135deg,rgba(247,151,30,.15),rgba(255,210,0,.15));
    border:1.5px solid #ffd200; border-radius:18px; padding:1.6rem; text-align:center; margin-bottom:.8rem; }
.res-no   { background:linear-gradient(135deg,rgba(255,75,75,.15),rgba(200,50,50,.15));
    border:1.5px solid #ff4b4b; border-radius:18px; padding:1.6rem; text-align:center; margin-bottom:.8rem; }
.res-emoji { font-size:2.8rem; line-height:1; }
.res-status { font-size:1.7rem; font-weight:800; color:#fff; margin:.4rem 0 .2rem; }
.res-name { color:rgba(255,255,255,.6); font-size:.88rem; }

/* Score bars */
.srow { display:flex; align-items:center; margin-bottom:.65rem; gap:10px; }
.slabel { color:rgba(255,255,255,.75); font-size:.8rem; font-weight:500; min-width:165px; }
.sbg { flex:1; background:rgba(255,255,255,.1); border-radius:99px; height:9px; overflow:hidden; }
.sval { color:#fff; font-size:.8rem; font-weight:700; min-width:36px; text-align:right; }

/* Prob bars */
.prow { margin-bottom:.85rem; }
.plabel-row { display:flex; justify-content:space-between; margin-bottom:4px; }
.pbg { background:rgba(255,255,255,.1); border-radius:99px; height:13px; overflow:hidden; }
.pnote { color:rgba(255,255,255,.38); font-size:.72rem; margin-top:3px; }

/* Chips */
.chip-row { display:flex; gap:.8rem; margin-bottom:.8rem; }
.chip { background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.14);
    border-radius:10px; padding:.55rem .9rem; flex:1; text-align:center; }
.chip-val { font-size:1.25rem; font-weight:800; color:#ffd200; }
.chip-lbl { font-size:.72rem; color:rgba(255,255,255,.5); margin-top:2px; }

/* Rec box */
.rec { background:rgba(255,255,255,.05); border-left:3px solid #ffd200;
    border-radius:0 10px 10px 0; padding:.7rem .9rem; margin-bottom:.5rem;
    color:rgba(255,255,255,.85); font-size:.88rem; line-height:1.5; }
.rev-text { color:rgba(255,255,255,.8); font-size:.93rem; line-height:1.7; margin-bottom:.8rem; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { background:rgba(255,255,255,.06); border-radius:14px;
    padding:5px; gap:4px; border:1px solid rgba(255,255,255,.12); }
.stTabs [data-baseweb="tab"] { background:transparent; border-radius:10px;
    color:rgba(255,255,255,.6); font-weight:600; padding:.45rem 1.4rem; }
.stTabs [aria-selected="true"] { background:linear-gradient(135deg,#f7971e,#ffd200)!important; color:#000!important; }

/* Uploader */
[data-testid="stFileUploader"] { background:rgba(255,255,255,.04);
    border:1.5px dashed rgba(255,255,255,.2); border-radius:14px; padding:1rem; }

/* info callout */
.info-box { background:rgba(255,210,0,.08); border:1px solid rgba(255,210,0,.3);
    border-radius:12px; padding:.8rem 1rem; color:rgba(255,255,255,.75);
    font-size:.83rem; line-height:1.6; margin-bottom:.8rem; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SCORING ENGINE  (rule-based, 100 % transparan & monoton)
# ══════════════════════════════════════════════════════════════════════════════
FEATURES   = ["aljabar","geometri","bilangan","data_ketidakpastian","menalar","literasi"]
FEAT_LABEL = ["Numerasi Aljabar","Numerasi Geometri","Numerasi Bilangan",
               "Data & Ketidakpastian","Menalar","Literasi"]
FEAT_COLOR = ["#f7971e","#38ef7d","#4facfe","#a18cd1","#ffd200","#f093fb"]

def composite_score(vals: dict) -> float:
    """
    Skor komposit 0-100 yang SELALU naik bila salah satu nilai naik.
    Formula:
      - Basis : rata-rata ke-6 skor
      - Bonus : +1.5 poin per aspek yang ≥ 75  (maks +9)
      - Penalti: -3 poin per aspek yang < 50   (maks -18)
    Dikliping ke [0, 100].
    """
    scores   = [vals[f] for f in FEATURES]
    avg      = np.mean(scores)
    bonus    = sum(1.5 for s in scores if s >= 75)
    penalty  = sum(3.0 for s in scores if s < 50)
    return float(np.clip(avg + bonus - penalty, 0, 100))


def classify(vals: dict):
    """
    Kembalikan (label 0/1/2, skor_komposit, pct_siap, pct_pot, pct_tidak).
    Threshold deterministik — tidak ada zona abu-abu antar kategori:
      ≥ 72  → Siap Olimpiade   (label 2)
      ≥ 50  → Potensial        (label 1)
      < 50  → Tidak Siap       (label 0)
    Probabilitas dihitung dari jarak ke batas.
    """
    cs = composite_score(vals)

    # ── Label ──
    if cs >= 72:
        label = 2
    elif cs >= 50:
        label = 1
    else:
        label = 0

    # ── Probabilitas (smooth, monoton, jumlah = 100) ──
    # Batas bawah/atas tiap kelas
    def softmax_dist(cs):
        # Jarak ke 3 titik pusat kelas: 25 (tidak siap), 61 (potensial), 86 (siap)
        centers = np.array([25.0, 61.0, 86.0])
        d = np.abs(cs - centers)
        # Semakin dekat ke pusat → bobot lebih besar
        w = np.exp(-d / 18)
        w = w / w.sum()
        return w  # [p_tidak, p_pot, p_siap]

    w = softmax_dist(cs)
    p_tidak, p_pot, p_siap = w * 100

    return label, cs, p_siap, p_pot, p_tidak


LABELS = {0:"Tidak Siap", 1:"Potensial", 2:"Siap Olimpiade"}
EMOJIS = {0:"❌", 1:"⚡", 2:"🏆"}
CSS_RES = {0:"res-no", 1:"res-pot", 2:"res-siap"}


# ── Helpers ───────────────────────────────────────────────────────────────────
def get_review(label, vals, cs):
    scores = [vals[f] for f in FEATURES]
    weak   = [FEAT_LABEL[i] for i, v in enumerate(scores) if v < 55]
    strong = [FEAT_LABEL[i] for i, v in enumerate(scores) if v >= 78]
    avg    = np.mean(scores)

    if label == 2:
        review = (f"Siswa ini menunjukkan performa sangat baik dengan rata-rata {avg:.1f} "
                  f"dan Skor Kesiapan {cs:.1f}/100. "
                  f"{'Unggul di: ' + ', '.join(strong) + '. ' if strong else ''}"
                  f"Siswa layak diikutsertakan dalam seleksi olimpiade matematika.")
    elif label == 1:
        review = (f"Siswa ini berpotensi dengan rata-rata {avg:.1f} "
                  f"dan Skor Kesiapan {cs:.1f}/100. "
                  f"{'Unggul di: ' + ', '.join(strong) + '. ' if strong else ''}"
                  f"{'Perlu penguatan di: ' + ', '.join(weak) + '. ' if weak else ''}"
                  f"Dengan latihan terstruktur, siswa ini dapat mencapai level Siap Olimpiade.")
    else:
        review = (f"Siswa ini memerlukan pembinaan lebih lanjut. Rata-rata {avg:.1f} "
                  f"dan Skor Kesiapan {cs:.1f}/100 masih di bawah standar minimum. "
                  f"{'Aspek yang paling perlu diperbaiki: ' + ', '.join(weak) + '.' if weak else ''}"
                  f" Diperlukan program belajar intensif sebelum mengikuti seleksi.")
    return review, weak, strong


def get_recs(label, weak):
    tips = {
        "Numerasi Aljabar":      "Latih soal persamaan, pertidaksamaan, dan pola bilangan.",
        "Numerasi Geometri":     "Perbanyak soal bangun ruang, kesebangunan, dan transformasi.",
        "Numerasi Bilangan":     "Fokus pada FPB, KPK, bilangan prima, dan operasi dasar.",
        "Data & Ketidakpastian": "Pelajari statistika dasar, peluang, dan interpretasi grafik.",
        "Menalar":               "Tingkatkan logika lewat soal pola, analogi, dan deduksi.",
        "Literasi":              "Latih membaca soal kontekstual dan merumuskan solusi tertulis.",
    }
    if label == 2:
        return ["✅ Daftarkan ke seleksi olimpiade tingkat kabupaten/kota.",
                "🎯 Ikuti pelatihan intensif olimpiade matematika.",
                "📚 Pelajari soal OSN tahun-tahun sebelumnya.",
                "🤝 Bergabunglah dengan klub/komunitas matematika."]
    elif label == 1:
        recs = ["⚡ Ikuti bimbingan belajar matematika terstruktur."]
        for w in weak:
            recs.append(f"📌 {w}: {tips.get(w,'')}")
        recs.append("🔄 Evaluasi ulang dalam 1–2 bulan setelah program peningkatan.")
        return recs
    else:
        recs = ["📖 Mulai dari materi dasar sesuai kurikulum."]
        for w in weak:
            recs.append(f"📌 {w}: {tips.get(w,'')}")
        recs += ["👨‍🏫 Konsultasikan program remedial dengan guru.",
                 "🗓️ Buat jadwal belajar harian minimal 1 jam."]
        return recs


def render_score_bars(vals):
    html = ""
    for key, label, color in zip(FEATURES, FEAT_LABEL, FEAT_COLOR):
        v = vals[key]
        html += f"""
        <div class="srow">
            <div class="slabel">{label}</div>
            <div class="sbg"><div style="width:{min(v,100):.1f}%;height:100%;background:{color};border-radius:99px"></div></div>
            <div class="sval">{v:.1f}</div>
        </div>"""
    st.markdown(html, unsafe_allow_html=True)


def render_prob_bars(p_siap, p_pot, p_tidak, cs):
    if cs >= 85:
        kalimat = "Sistem sangat yakin siswa ini Siap Olimpiade. 🎉"
    elif cs >= 72:
        kalimat = "Sistem yakin siswa ini Siap Olimpiade — terus pertahankan!"
    elif cs >= 62:
        kalimat = "Siswa ini mendekati level Siap — sedikit lagi bisa lolos seleksi!"
    elif cs >= 50:
        kalimat = "Siswa masuk Potensial. Dengan latihan konsisten bisa naik ke Siap Olimpiade."
    elif cs >= 38:
        kalimat = "Belum siap, namun ada potensi. Perlu bimbingan intensif."
    else:
        kalimat = "Perlu program belajar mendasar sebelum bisa mengikuti seleksi."

    st.markdown(f"""
    <div class="card" style="padding:1.3rem 1.5rem">
        <div class="sec-title">📊 Skor Kesiapan Olimpiade</div>
        <div style="text-align:center;margin-bottom:1rem">
            <span style="font-size:2.8rem;font-weight:900;
                background:linear-gradient(90deg,#f7971e,#ffd200);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent">
                {cs:.1f}
            </span>
            <span style="color:rgba(255,255,255,.45);font-size:1rem"> / 100</span>
            <div style="color:rgba(255,255,255,.5);font-size:.8rem;margin-top:2px">
                Semakin tinggi = semakin siap
            </div>
        </div>

        <!-- progress bar keseluruhan -->
        <div style="background:rgba(255,255,255,.1);border-radius:99px;height:16px;overflow:hidden;margin-bottom:1.2rem">
            <div style="width:{min(cs,100):.1f}%;height:100%;
                background:linear-gradient(90deg,#ff4b4b,#ffd200,#38ef7d);
                border-radius:99px;transition:width .6s"></div>
        </div>

        <div class="sec-title" style="margin-top:.2rem">🎯 Peluang Masuk Setiap Kategori</div>
        <div style="color:rgba(255,255,255,.45);font-size:.78rem;margin-bottom:.9rem">
            Semakin besar persentase, semakin besar kemungkinan siswa masuk kategori tersebut.
        </div>

        <div class="prow">
            <div class="plabel-row">
                <span style="color:#38ef7d;font-weight:700;font-size:.87rem">🏆 Siap Olimpiade</span>
                <span style="color:#38ef7d;font-weight:800">{p_siap:.0f}%</span>
            </div>
            <div class="pbg"><div style="width:{p_siap:.1f}%;height:100%;background:linear-gradient(90deg,#11998e,#38ef7d);border-radius:99px"></div></div>
            <div class="pnote">Rata-rata tinggi, tidak ada nilai yang sangat rendah</div>
        </div>

        <div class="prow">
            <div class="plabel-row">
                <span style="color:#ffd200;font-weight:700;font-size:.87rem">⚡ Potensial</span>
                <span style="color:#ffd200;font-weight:800">{p_pot:.0f}%</span>
            </div>
            <div class="pbg"><div style="width:{p_pot:.1f}%;height:100%;background:linear-gradient(90deg,#f7971e,#ffd200);border-radius:99px"></div></div>
            <div class="pnote">Perlu peningkatan di beberapa aspek</div>
        </div>

        <div class="prow">
            <div class="plabel-row">
                <span style="color:#ff6b6b;font-weight:700;font-size:.87rem">❌ Belum Siap</span>
                <span style="color:#ff6b6b;font-weight:800">{p_tidak:.0f}%</span>
            </div>
            <div class="pbg"><div style="width:{p_tidak:.1f}%;height:100%;background:linear-gradient(90deg,#c0392b,#ff6b6b);border-radius:99px"></div></div>
            <div class="pnote">Butuh program belajar lebih intensif</div>
        </div>

        <div style="background:rgba(255,255,255,.06);border-radius:10px;padding:.6rem .9rem;
                    margin-top:.4rem;color:rgba(255,255,255,.8);font-size:.83rem;text-align:center">
            💬 {kalimat}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Template Excel builder ────────────────────────────────────────────────────
def make_template():
    df_tmpl = pd.DataFrame(columns=["Nama","NUM_ALJ","NUM_GEO","NUM_BIL","NUM_DAT","NUM_L3","LIT"])
    examples = [
        ["Contoh Siswa 1", 85, 80, 88, 82, 87, 90],
        ["Contoh Siswa 2", 62, 58, 65, 60, 63, 70],
        ["Contoh Siswa 3", 40, 45, 38, 42, 50, 35],
    ]
    for e in examples:
        df_tmpl.loc[len(df_tmpl)] = e
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as w:
        df_tmpl.to_excel(w, index=False, sheet_name="Data Siswa")
    return buf.getvalue()


# ══════════════════════════════════════════════════════════════════════════════
# UI
# ══════════════════════════════════════════════════════════════════════════════

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-badge">🔬 Data Mining · Klasifikasi · Pendidikan Matematika</div>
    <div class="hero-logo">OLYMATH</div>
    <div class="hero-sub">Sistem Cerdas Seleksi Awal Calon Peserta Olimpiade Matematika</div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["👤  Input Satu Siswa", "📂  Upload File Excel"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    col_form, col_res = st.columns([1, 1], gap="large")

    with col_form:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">📋 Data Siswa</div>', unsafe_allow_html=True)
        nama = st.text_input("Nama Siswa", placeholder="Contoh: Budi Santoso")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">📊 Skor Kemampuan (0–100)</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            alj = st.number_input("🔢 Numerasi Aljabar",    0.0, 100.0, 65.0, 0.1)
            bil = st.number_input("🔣 Numerasi Bilangan",   0.0, 100.0, 65.0, 0.1)
            men = st.number_input("🧠 Menalar",             0.0, 100.0, 65.0, 0.1)
        with c2:
            geo = st.number_input("📐 Numerasi Geometri",   0.0, 100.0, 65.0, 0.1)
            dat = st.number_input("📈 Data & Ketidakpastian",0.0,100.0, 65.0, 0.1)
            lit = st.number_input("📖 Literasi",            0.0, 100.0, 65.0, 0.1)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        📌 <b>Cara penilaian:</b> Sistem menghitung <b>Skor Kesiapan</b> berdasarkan rata-rata 
        ke-6 nilai, bonus untuk nilai unggul (≥75), dan pengurang untuk nilai lemah (&lt;50).
        Makin tinggi nilai → Skor Kesiapan makin tinggi → kategori makin baik.
        </div>
        """, unsafe_allow_html=True)

        btn = st.button("🔍 Analisis Kesiapan Siswa")

    with col_res:
        if btn:
            vals = {"aljabar":alj,"geometri":geo,"bilangan":bil,
                    "data_ketidakpastian":dat,"menalar":men,"literasi":lit}
            label, cs, p_siap, p_pot, p_tidak = classify(vals)
            review, weak, strong = get_review(label, vals, cs)
            recs = get_recs(label, weak)
            avg  = np.mean(list(vals.values()))
            display_name = nama.strip() or "Siswa"

            # Status card
            st.markdown(f"""
            <div class="{CSS_RES[label]}">
                <div class="res-emoji">{EMOJIS[label]}</div>
                <div class="res-name">{display_name}</div>
                <div class="res-status">{LABELS[label]}</div>
            </div>""", unsafe_allow_html=True)

            # Prob & score bars
            render_prob_bars(p_siap, p_pot, p_tidak, cs)

            # Chips
            st.markdown(f"""
            <div class="chip-row">
                <div class="chip"><div class="chip-val">{avg:.1f}</div><div class="chip-lbl">Rata-rata Skor</div></div>
                <div class="chip"><div class="chip-val">{len(strong)}/6</div><div class="chip-lbl">Aspek Unggul (≥78)</div></div>
                <div class="chip"><div class="chip-val">{len(weak)}/6</div><div class="chip-lbl">Aspek Lemah (&lt;55)</div></div>
            </div>""", unsafe_allow_html=True)

            # Score bars
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">📊 Profil Kemampuan</div>', unsafe_allow_html=True)
            render_score_bars(vals)
            st.markdown('</div>', unsafe_allow_html=True)

            # Review
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">📝 Review</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="rev-text">{review}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Recs
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">💡 Rekomendasi & Saran</div>', unsafe_allow_html=True)
            for r in recs:
                st.markdown(f'<div class="rec">{r}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card" style="text-align:center;padding:3rem 2rem">
                <div style="font-size:3rem;margin-bottom:1rem">📊</div>
                <div style="color:rgba(255,255,255,.45);font-size:.93rem">
                    Masukkan skor siswa di sebelah kiri,<br>
                    lalu klik <b style="color:#ffd200">Analisis Kesiapan Siswa</b>
                </div>
            </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2
# ══════════════════════════════════════════════════════════════════════════════
with tab2:

    # ── Template download ──────────────────────────────────────────────────────
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📥 Download Template Excel</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:rgba(255,255,255,.55);font-size:.85rem;margin-bottom:.9rem">
    Belum punya file data siswa? Download template di bawah ini, isi datanya, lalu upload kembali.
    Pastikan nama kolom <b style="color:#ffd200">tidak diubah</b>.
    </div>""", unsafe_allow_html=True)
    st.download_button(
        label="⬇️ Download Template Excel",
        data=make_template(),
        file_name="template_data_siswa_olymath.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="dl_template",
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Upload ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📂 Upload File Excel Siswa</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:rgba(255,255,255,.55);font-size:.83rem;margin-bottom:.8rem">
    Kolom wajib: <b style="color:#ffd200">NUM_ALJ · NUM_GEO · NUM_BIL · NUM_DAT · NUM_L3 · LIT</b><br>
    Kolom opsional: <b style="color:#ffd200">Nama</b>
    </div>""", unsafe_allow_html=True)
    uploaded = st.file_uploader("Pilih file Excel (.xlsx)", type=["xlsx"])
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded:
        try:
            df_up = pd.read_excel(uploaded)
            # Normalize columns
            col_map = {}
            for c in df_up.columns:
                cu = c.upper().strip().replace(" ","_")
                if cu in ["NUM_ALJ","ALJABAR","NUM_ALJABAR"]:           col_map[c]="aljabar"
                elif cu in ["NUM_GEO","GEOMETRI","NUM_GEOMETRI"]:       col_map[c]="geometri"
                elif cu in ["NUM_BIL","BILANGAN","NUM_BILANGAN"]:       col_map[c]="bilangan"
                elif cu in ["NUM_DAT","DATA","NUM_DATA","DATA_KETIDAKPASTIAN"]: col_map[c]="data_ketidakpastian"
                elif cu in ["NUM_L3","MENALAR","NUM_MENALAR","NALAR"]:  col_map[c]="menalar"
                elif cu in ["LIT","LITERASI"]:                          col_map[c]="literasi"
                elif cu in ["NAMA","NAME","SISWA"]:                     col_map[c]="nama"
            df_up = df_up.rename(columns=col_map)

            missing = [f for f in FEATURES if f not in df_up.columns]
            if missing:
                st.error(f"❌ Kolom tidak ditemukan: {', '.join(missing)}")
            else:
                df_valid = df_up.dropna(subset=FEATURES).copy()
                n_total, n_valid = len(df_up), len(df_valid)

                st.markdown(f"""
                <div class="chip-row">
                    <div class="chip"><div class="chip-val">{n_total}</div><div class="chip-lbl">Total Data</div></div>
                    <div class="chip"><div class="chip-val">{n_valid}</div><div class="chip-lbl">Data Valid</div></div>
                    <div class="chip"><div class="chip-val">{n_total-n_valid}</div><div class="chip-lbl">Data Kosong</div></div>
                </div>""", unsafe_allow_html=True)

                if st.button("🚀 Proses Semua Data", key="btn_batch"):
                    with st.spinner("Menganalisis data siswa..."):
                        results = [classify({f: row[f] for f in FEATURES})
                                   for _, row in df_valid.iterrows()]

                        df_valid = df_valid.copy()
                        df_valid["Skor_Kesiapan"]      = [round(r[1],1) for r in results]
                        df_valid["Status_Kesiapan"]    = [LABELS[r[0]] for r in results]
                        df_valid["Peluang_Siap_%"]     = [round(r[2],1) for r in results]
                        df_valid["Peluang_Potensial_%"]= [round(r[3],1) for r in results]
                        df_valid["Peluang_BelumSiap_%"]= [round(r[4],1) for r in results]
                        df_valid["Rata_rata_Skor"]     = df_valid[FEATURES].mean(axis=1).round(2)

                        def quick_review(row):
                            lbl = [k for k,v in LABELS.items() if v==row["Status_Kesiapan"]][0]
                            cs  = row["Skor_Kesiapan"]
                            avg = row["Rata_rata_Skor"]
                            weak = [FEAT_LABEL[i] for i,f in enumerate(FEATURES) if row[f]<55]
                            if lbl==2: return f"Siap Olimpiade (Skor {cs}, avg {avg:.1f})."
                            elif lbl==1:
                                w = ', '.join(weak) if weak else "semua aspek cukup"
                                return f"Potensial (Skor {cs}, avg {avg:.1f}). Perkuat: {w}."
                            else:
                                w = ', '.join(weak) if weak else "semua aspek"
                                return f"Belum Siap (Skor {cs}, avg {avg:.1f}). Fokus: {w}."

                        df_valid["Review"] = df_valid.apply(quick_review, axis=1)

                    vc    = df_valid["Status_Kesiapan"].value_counts()
                    siap  = vc.get("Siap Olimpiade", 0)
                    pot   = vc.get("Potensial", 0)
                    tidak = vc.get("Tidak Siap", 0)

                    st.markdown(f"""
                    <div class="card">
                        <div class="sec-title">📊 Ringkasan Hasil</div>
                        <div class="chip-row">
                            <div class="chip"><div class="chip-val" style="color:#38ef7d">{siap}</div><div class="chip-lbl">🏆 Siap Olimpiade</div></div>
                            <div class="chip"><div class="chip-val" style="color:#ffd200">{pot}</div><div class="chip-lbl">⚡ Potensial</div></div>
                            <div class="chip"><div class="chip-val" style="color:#ff4b4b">{tidak}</div><div class="chip-lbl">❌ Tidak Siap</div></div>
                        </div>
                    </div>""", unsafe_allow_html=True)

                    # Preview
                    cols_show = (["nama"] if "nama" in df_valid.columns else []) + \
                                FEATURES + ["Skor_Kesiapan","Status_Kesiapan",
                                            "Peluang_Siap_%","Peluang_Potensial_%","Peluang_BelumSiap_%","Review"]
                    df_show = df_valid[[c for c in cols_show if c in df_valid.columns]]
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<div class="sec-title">📋 Preview Hasil (10 baris pertama)</div>', unsafe_allow_html=True)
                    st.dataframe(df_show.head(10), use_container_width=True, hide_index=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Download
                    out = io.BytesIO()
                    with pd.ExcelWriter(out, engine="openpyxl") as writer:
                        df_show.rename(columns={
                            "aljabar":"Skor Aljabar","geometri":"Skor Geometri",
                            "bilangan":"Skor Bilangan","data_ketidakpastian":"Skor Data & KT",
                            "menalar":"Skor Menalar","literasi":"Skor Literasi",
                            "nama":"Nama Siswa","Skor_Kesiapan":"Skor Kesiapan (0-100)",
                            "Status_Kesiapan":"Status Kesiapan Olimpiade",
                            "Rata_rata_Skor":"Rata-rata Skor",
                        }).to_excel(writer, index=False, sheet_name="Hasil Seleksi")
                        pd.DataFrame({
                            "Status":["Siap Olimpiade","Potensial","Tidak Siap","TOTAL"],
                            "Jumlah":[siap,pot,tidak,n_valid],
                            "Persen (%)":[round(siap/n_valid*100,1) if n_valid else 0,
                                          round(pot/n_valid*100,1)  if n_valid else 0,
                                          round(tidak/n_valid*100,1)if n_valid else 0, 100.0],
                        }).to_excel(writer, index=False, sheet_name="Ringkasan")

                    st.download_button(
                        label="⬇️ Download Hasil Excel",
                        data=out.getvalue(),
                        file_name=f"Hasil_Seleksi_OLYMATH_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )

        except Exception as e:
            st.error(f"❌ Gagal membaca file: {e}")

# Footer
st.markdown("""
<div style="text-align:center;margin-top:3rem;color:rgba(255,255,255,.2);font-size:.75rem">
    OLYMATH · Sistem Seleksi Olimpiade Matematika · Data Mining · Pendidikan Matematika
</div>""", unsafe_allow_html=True)
