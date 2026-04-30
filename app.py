import streamlit as st

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Portafolio | Interfaces Multimodales",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Projects data ─────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "INTRO",
        "emoji": "📡",
        "desc": "Introducción al curso de Creación de Interfaces Multimodales. Primera interfaz desplegada en Streamlit: exploración del entorno de desarrollo y estructura básica de una app interactiva.",
        "tags": ["Streamlit", "Python", "Interfaz"],
        "url": "https://gwvr56pnwfqfosnjqtziws.streamlit.app/",
        "color": "#FF6B6B",
    },
    {
        "title": "IMM1",
        "emoji": "🖥️",
        "desc": "Primera práctica de Interfaces Multimodales. Construcción de una interfaz que integra múltiples canales de entrada y salida de datos para el usuario.",
        "tags": ["Multimodal", "Interfaz", "Streamlit"],
        "url": "https://xh64y7bekcxgq5fkwgdiaz.streamlit.app/",
        "color": "#4ECDC4",
    },
    {
        "title": "TRADUCTOR",
        "emoji": "🌐",
        "desc": "Interfaz multimodal de traducción de texto entre idiomas. El usuario interactúa con la app a través de entradas de texto y recibe salidas en tiempo real, demostrando la integración de APIs externas en interfaces web.",
        "tags": ["Interfaz", "API", "Web"],
        "url": "https://traductorclase.streamlit.app/",
        "color": "#45B7D1",
    },
    {
        "title": "ANÁLISIS DE TEXTO",
        "emoji": "📊",
        "desc": "Interfaz para el análisis y visualización de texto. Demuestra cómo presentar datos textuales de forma gráfica e interactiva: estadísticas, frecuencias y métricas accesibles desde una sola pantalla.",
        "tags": ["Visualización", "Texto", "Dashboard"],
        "url": "https://3fvjcwghfpziwlbkzb76rd.streamlit.app/",
        "color": "#96CEB4",
    },
    {
        "title": "OCR",
        "emoji": "🔍",
        "desc": "Interfaz de captura y lectura de imágenes mediante reconocimiento óptico de caracteres. El usuario carga una imagen como entrada y la app devuelve el texto extraído, integrando visión por computadora en una interfaz accesible.",
        "tags": ["OCR", "Imagen", "Entrada Visual"],
        "url": "https://7ddscsw9wkqigw6gfrsh9u.streamlit.app/",
        "color": "#FFEAA7",
    },
    {
        "title": "OCR AUDIO",
        "emoji": "🎙️",
        "desc": "Interfaz multimodal que combina entrada visual (imagen) y salida auditiva (audio). Extiende el OCR convirtiendo el texto extraído en voz, ilustrando cómo múltiples canales sensoriales coexisten en una sola app.",
        "tags": ["OCR", "Audio", "Multimodal"],
        "url": "https://ocraudio123.streamlit.app/",
        "color": "#DDA0DD",
    },
    {
        "title": "SENTIMENT A",
        "emoji": "💬",
        "desc": "Interfaz para el análisis de sentimientos de textos. El usuario ingresa contenido y la app clasifica el tono emocional, mostrando resultados con visualizaciones claras e intuitivas.",
        "tags": ["Análisis", "Visualización", "Texto"],
        "url": "https://sentimenta-zgj9xbbussvpvwxup6sqmc.streamlit.app/",
        "color": "#F0A500",
    },
    {
        "title": "TDF_ESP",
        "emoji": "🗂️",
        "desc": "Interfaz para calcular y visualizar relevancia de términos en documentos en español usando TF-IDF. Presenta tablas y gráficas interactivas que facilitan la exploración de corpus textuales.",
        "tags": ["Visualización", "Español", "Dashboard"],
        "url": "https://tdfesp-lzgmqy9b2grfpuxx3iwfje.streamlit.app/",
        "color": "#E17055",
    },
    {
        "title": "TF-IDF",
        "emoji": "📈",
        "desc": "Interfaz interactiva para explorar el algoritmo TF-IDF sobre cualquier colección de textos. El usuario introduce documentos y visualiza en tiempo real la importancia de cada término.",
        "tags": ["Interactivo", "Algoritmo", "Dashboard"],
        "url": "https://movl6nt93wmqsujmlajxsa.streamlit.app/",
        "color": "#00B894",
    },
    {
        "title": "WORDCLOUD",
        "emoji": "☁️",
        "desc": "Generador interactivo de nubes de palabras. A partir de texto ingresado por el usuario, produce una representación visual inmediata — ejemplo claro de cómo una interfaz puede transformar datos crudos en comunicación visual efectiva.",
        "tags": ["Visualización", "Interactivo", "Gráficas"],
        "url": "https://wordcloud-whywh4ohajhswjtyfxfoge.streamlit.app/",
        "color": "#6C5CE7",
    },
]

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #0A0A0F;
    color: #E8E8F0;
}

.block-container {
    padding: 2rem 3rem 4rem 3rem;
    max-width: 1400px;
}

/* ── Hero ── */
.hero-section {
    text-align: center;
    padding: 4rem 2rem 2rem;
    position: relative;
}

.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(100, 100, 255, 0.3);
    color: #8888FF;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    padding: 0.4rem 1.2rem;
    border-radius: 2rem;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(2.8rem, 6vw, 5.5rem);
    font-weight: 800;
    line-height: 1.05;
    background: linear-gradient(135deg, #E8E8F0 30%, #8888FF 70%, #FF6B6B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.hero-sub {
    font-size: 1.1rem;
    color: #888899;
    max-width: 560px;
    margin: 0 auto 3rem;
    line-height: 1.7;
    font-weight: 400;
}

/* ── Stats bar ── */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 3rem;
    padding: 1.5rem 2rem;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 1rem;
    margin-bottom: 3.5rem;
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: #8888FF;
    display: block;
}

.stat-label {
    font-size: 0.75rem;
    color: #666677;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}

/* ── Section title ── */
.section-title {
    font-size: 0.72rem;
    font-family: 'Space Mono', monospace;
    letter-spacing: 0.25em;
    color: #8888FF;
    text-transform: uppercase;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(136,136,255,0.4), transparent);
}

/* ── Project cards ── */
.proj-card {
    background: #0F0F1A;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 1.25rem;
    padding: 1.8rem 1.8rem 1.4rem;
    height: 100%;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
}

.proj-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--accent);
    opacity: 0.8;
}

.proj-card:hover {
    border-color: rgba(255,255,255,0.18);
    transform: translateY(-4px);
    box-shadow: 0 24px 48px rgba(0,0,0,0.5);
}

.proj-num {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #444455;
    letter-spacing: 0.1em;
    margin-bottom: 0.8rem;
}

.proj-emoji {
    font-size: 2.4rem;
    margin-bottom: 0.6rem;
    display: block;
}

.proj-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: #E8E8F0;
    margin-bottom: 0.65rem;
    letter-spacing: -0.01em;
}

.proj-desc {
    font-size: 0.85rem;
    color: #777788;
    line-height: 1.65;
    margin-bottom: 1.1rem;
    font-weight: 400;
}

.tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1.2rem;
}

.tag {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: #888899;
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    padding: 0.25rem 0.65rem;
    border-radius: 0.4rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.proj-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--accent);
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    text-decoration: none;
    font-weight: 700;
    letter-spacing: 0.05em;
    opacity: 0.85;
    transition: opacity 0.2s;
}

.proj-link:hover {
    opacity: 1;
    text-decoration: underline;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 3rem 0 1rem;
    color: #444455;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 4rem;
}

/* ── Streamlit overrides ── */
header[data-testid="stHeader"] { background: transparent; }
.stApp { background-color: #0A0A0F; }

/* hide default streamlit branding */
#MainMenu, footer { visibility: hidden; }

a { color: inherit !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">📡 Portafolio Académico — Interfaces Multimodales</div>
    <h1 class="hero-title">Interfaces<br>Multimodales</h1>
    <p class="hero-sub">
        Colección de aplicaciones desarrolladas en el curso de
        Creación de Interfaces Multimodales, desplegadas en Streamlit Cloud.
        Cada proyecto explora distintos canales de entrada y salida para el usuario.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── Stats ─────────────────────────────────────────────────────────────────────
total = len(PROJECTS)
tags_all = set(t for p in PROJECTS for t in p["tags"])
multimodal_count = sum(1 for p in PROJECTS if any(t in ["Multimodal", "OCR", "Audio", "Imagen", "Entrada Visual"] for t in p["tags"]))

st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item">
        <span class="stat-number">{total}</span>
        <span class="stat-label">Proyectos</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">{len(tags_all)}</span>
        <span class="stat-label">Tecnologías</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">{multimodal_count}</span>
        <span class="stat-label">Apps Multimodales</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">☁️</span>
        <span class="stat-label">Streamlit Cloud</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Grid of projects ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Interfaces desplegadas</div>', unsafe_allow_html=True)

cols_per_row = 3
rows = [PROJECTS[i:i+cols_per_row] for i in range(0, len(PROJECTS), cols_per_row)]

for row in rows:
    cols = st.columns(len(row), gap="medium")
    for col, proj in zip(cols, row):
        with col:
            idx = PROJECTS.index(proj) + 1
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])
            st.markdown(f"""
            <div class="proj-card" style="--accent: {proj['color']}">
                <div class="proj-num">#{idx:02d}</div>
                <span class="proj-emoji">{proj['emoji']}</span>
                <div class="proj-title">{proj['title']}</div>
                <div class="proj-desc">{proj['desc']}</div>
                <div class="tags-row">{tags_html}</div>
                <a class="proj-link" href="{proj['url']}" target="_blank">
                    Abrir app →
                </a>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Construido con Streamlit · Creación de Interfaces Multimodales · 2024–2025
</div>
""", unsafe_allow_html=True)
