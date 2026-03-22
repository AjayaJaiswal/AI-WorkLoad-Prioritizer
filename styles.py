def load_css():
    return """
    <style>
    .stApp {
        background: #0B1220;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 0.25rem;
        letter-spacing: -0.5px;
    }

    .sub-text {
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 1.75rem;
    }

    .section-title {
        color: #E2E8F0;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 0.9rem;
    }

    .card {
        background: linear-gradient(180deg, #172033 0%, #131C2B 100%);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #263247;
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.22);
        margin-bottom: 1rem;
    }

    .card-title {
        color: #F8FAFC;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
    }

    .card-text {
        color: #CBD5E1;
        font-size: 0.97rem;
        line-height: 1.7;
    }

    /* -------- AI boxes (minimal, sharp, clean) -------- */
.ai-card {
    background: #121A2B;
    padding: 10px 12px;
    border-radius: 2px;          /* almost sharp */
    border: 1px solid #2A3954;
    color: #E5EDF8;
    margin-bottom: 0.4rem;
    font-size: 0.9rem;
    line-height: 1.5;
    box-shadow: none;            /* remove glow */
}

.ai-card-recommended {
    background: #13281F;
    padding: 10px 12px;
    border-radius: 2px;
    border: 1px solid #2F5E46;
    color: #EAF8F0;
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
    font-weight: 500;
    line-height: 1.5;
    box-shadow: none;
}

    hr {
        border: none;
        border-top: 1px solid #223048;
        margin: 1.6rem 0;
    }

    /* Inputs */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="base-input"] > div {
        background-color: #111A2B !important;
        border: 1px solid #2A3954 !important;
        border-radius: 12px !important;
    }

    input, textarea {
        color: #F8FAFC !important;
    }

    /* Number input / slider labels */
    label, .stSlider label {
        color: #CBD5E1 !important;
        font-weight: 500;
    }

    /* Buttons - softer aesthetic */
.stButton > button, .stFormSubmitButton > button {
    width: 100%;
    background: #1E293B;   /* muted dark blue */
    color: #E2E8F0;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 0.55rem 1rem;
    font-weight: 600;
    box-shadow: none;
    transition: all 0.18s ease;
}

/* Hover - subtle, not flashy */
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #243244;
    border-color: #3B4A63;
    transform: translateY(-1px);
}

/* Active */
.stButton > button:active, .stFormSubmitButton > button:active {
    transform: translateY(0px);
}

/* Primary (AI button only) */
div.stButton:nth-of-type(3) > button {
    background: #334155;
    border-color: #475569;
}

/* Primary hover */
div.stButton:nth-of-type(3) > button:hover {
    background: #3B4A63;
}

    .stButton > button:hover, .stFormSubmitButton > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(180deg, #2563EB 0%, #1D4ED8 100%);
        border-color: #4F75E6;
    }

    .stButton > button:active, .stFormSubmitButton > button:active {
        transform: translateY(0px);
    }

    /* Dataframe container */
    div[data-testid="stDataFrame"] {
        border: 1px solid #263247;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    }

    /* Info / success / warning boxes */
    div[data-testid="stAlert"] {
        border-radius: 14px;
    }
    </style>
    """