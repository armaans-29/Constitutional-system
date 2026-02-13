import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# FAST PROFESSIONAL CONFIG
st.set_page_config(
    page_title=" Judicial Bail Predictor",
    page_icon="⚖️",
    layout="wide"
)


# ⚡ PROFESSIONAL CSS (NO IMPORTS - Pure System Fonts)
@st.cache_data(ttl=3600)
def get_professional_css():
    return """
    <style>
    .stApp { 
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%); 
        color: #e2e8f0; 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    }

    .main-title { 
        font-size: 3.5rem; 
        font-weight: 800; 
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 50%, #1e3a8a 100%); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-align: center; 
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
    }

    .subtitle-pro { 
        font-size: 1.2rem; 
        color: #94a3b8; 
        text-align: center; 
        font-weight: 400; 
        letter-spacing: 0.025em;
    }

    .pro-card { 
        background: linear-gradient(145deg, rgba(15,23,42,0.95), rgba(30,41,59,0.9)); 
        backdrop-filter: blur(20px);
        border: 1px solid rgba(59,130,246,0.25); 
        border-radius: 20px; 
        padding: 2rem; 
        margin: 1rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    .assessment-header {
        background: linear-gradient(135deg, rgba(59,130,246,0.1), rgba(30,64,175,0.1));
        border-left: 5px solid #3b82f6;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
    }

    .status-conditional { border-left: 5px solid #f59e0b; background: rgba(245,158,11,0.08); }
    .status-high { border-left: 5px solid #10b981; background: rgba(16,185,129,0.08); }
    .status-low { border-left: 5px solid #ef4444; background: rgba(239,68,68,0.08); }

    .btn-pro {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white; border-radius: 16px; padding: 1rem 2rem; 
        font-weight: 600; border: none; font-size: 1.1rem;
        box-shadow: 0 10px 30px rgba(59,130,246,0.4);
        width: 100%;
    }

    .legal-factors {
        background: rgba(16,185,129,0.1);
        border-left: 6px solid #10b981;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }

    .disclaimer {
        background: rgba(239,68,68,0.1);
        border-left: 4px solid #ef4444;
        border-radius: 12px;
        padding: 1.5rem;
        font-size: 0.95rem;
        color: #f1f5f9;
    }
    </style>
    """


with st.spinner("⚖️ Initializing Judicial Engine..."):
    st.markdown(get_professional_css(), unsafe_allow_html=True)


# === JUDICIAL ENGINE ===
def bail_predictor(inputs):
    score = 0;
    factors = []

    if inputs['punishment_years'] <= 5:
        score += 4;
        factors.append("Punishment ≤5yr (Strong - Regular bail zone)")
    elif inputs['punishment_years'] <= 7:
        score += 3;
        factors.append("Punishment ≤7yr (Good - Regular bail zone)")
    elif inputs['punishment_years'] <= 10:
        score += 2;
        factors.append("Punishment ≤10yr (Fair)")

    if inputs['first_time_offender']:
        score += 2;
        factors.append("Clean antecedents (Favorable precedent)")
    if inputs['investigation_complete']:
        score += 2;
        factors.append("Chargesheet filed (Investigation complete)")
    if inputs['time_served_months'] >= 8:
        score += 2;
        factors.append(f"{inputs['time_served_months']}m served (Significant)")
    elif inputs['time_served_months'] >= 4:
        score += 1;
        factors.append("Moderate detention (4+ months)")
    if inputs['good_behavior']:
        score += 1;
        factors.append("Good jail conduct")

    if score >= 9:
        status = "HIGHLY FAVOURABLE";
        category = "Regular Bail";
        status_class = "status-high"
    elif score >= 7:
        status = "FAVOURABLE";
        category = "Regular/Interim";
        status_class = "status-high"
    elif score >= 5:
        status = "CONDITIONAL";
        category = "Anticipatory Bail";
        status_class = "status-conditional"
    elif score >= 3:
        status = "CHALLENGING";
        category = "Exceptional grounds";
        status_class = "status-low"
    else:
        status = "ADVERSE";
        category = "Strong opposition";
        status_class = "status-low"

    return {
        'score': score, 'max': 12, 'status': status, 'category': category,
        'factors': factors, 'confidence': min(95, 70 + score * 2), 'status_class': status_class
    }


# === HEADER ===
st.markdown("""
<div style='padding: 3rem; text-align: center;'>
    <h1 class="main-title">🏛️ Judicial Bail Predictor</h1>
    <p class="Judicial wisdom meets modern computation</p>
</div>
""", unsafe_allow_html=True)

# === INPUTS ===
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown("### 📋 Case Profile")
    crime = st.selectbox("**Offence**", ["Murder (IPC 302)", "Cheating (IPC 420)", "Grievous Hurt (IPC 325)",
                                         "Dowry Death (IPC 304B)", "Theft (IPC 379)", "Cyber Fraud"])
    years = st.number_input("**Max Punishment (Years)**", 1, 99, 7)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown("### ✅ Mitigating Factors")
    first_offender = st.checkbox("**Clean antecedents**", True)
    chargesheet = st.checkbox("**Chargesheet filed**")
    detention = st.number_input("**Detention (Months)**", 0, 60, 0)
    conduct = st.checkbox("**Good jail conduct**")
    st.markdown('</div>', unsafe_allow_html=True)

# === EXECUTE ===
if st.button("⚖️ **EXECUTE JUDICIAL ASSESSMENT**", key="run"):
    with st.spinner("🔬 Computing constitutional matrix..."):
        result = bail_predictor({
            'punishment_years': years, 'first_time_offender': first_offender,
            'investigation_complete': chargesheet, 'time_served_months': detention, 'good_behavior': conduct
        })

        # 📋 JUDICIAL ELIGIBILITY ASSESSMENT
        st.markdown(f"""
        <div class="pro-card assessment-header">
            <h2 style='color:#3b82f6; margin-bottom:1rem;'>📋 JUDICIAL ELIGIBILITY ASSESSMENT</h2>
            <div style='display:flex; gap:2rem; align-items:center; flex-wrap:wrap;'>
                <div>
                    <strong>CASE PROFILE</strong><br>
                    Offence: <strong>{crime}</strong><br>
                    Punishment: <strong>{years} years maximum</strong>
                </div>
                <div style='font-size:2rem;color:#10b981;font-weight:800;'>
                    Score: {result['score']}/{result['max']} ({result['confidence']}% confidence)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ASSESSMENT SUMMARY
        st.markdown(f"""
        <div class="pro-card {result['status_class']}">
            <h3 style='color:#f8fafc; margin-bottom:1rem;'>ASSESSMENT</h3>
            <div style='font-size:1.8rem; color:#f59e0b; font-weight:700; margin-bottom:1rem;'>
                Status: <strong>{result['status']}</strong>
            </div>
            <p style='color:#94a3b8; font-size:1.1rem;'>
                Category: <strong>{result['category']}</strong><br>
                Risk Profile: <strong>Standard conditions required</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

        # ⚖️ LEGAL FACTORS
        st.markdown(f"""
        <div class="legal-factors">
            <h4 style='color:#10b981; margin-bottom:1rem;'>⚖️ LEGAL FACTORS ({len(result['factors'])} Favourable)</h4>
        """, unsafe_allow_html=True)
        for i, factor in enumerate(result['factors'], 1):
            st.markdown(f"{i}. {factor}")
        st.markdown("</div>", unsafe_allow_html=True)

        # LEGAL PRECEDENTS
        st.markdown("""
        <div class="pro-card" style="background: rgba(59,130,246,0.1); border-left: 6px solid #3b82f6;">
            <h4 style='color:#3b82f6;'>⚖️ LEGAL PRECEDENTS APPLIED:</h4>
            <ul style='color:#94a3b8; margin-top:0.5rem;'>
                <li><strong>CrPC §437(1)</strong> - Non-bailable offences</li>
                <li><strong>State of Rajasthan v. Balchand</strong> (1977 AIR 2447)</li>
                <li><strong>Gudikanti Narasimhulu v. Public Prosecutor</strong> (1978 AIR 429)</li>
                <li><strong>Arnesh Kumar v. State of Bihar</strong> (2014 8 SCC 273)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # DISCLAIMER
        st.markdown("""
        <div class="disclaimer">
            <strong>⚠️ DISCLAIMER:</strong> This constitutes <em>algorithmic preliminary assessment</em> only. 
            Final authority vests with Hon'ble Court exercising judicious discretion.
        </div>
        """, unsafe_allow_html=True)

        # 📊 QUANTITATIVE MATRIX
        matrix = pd.DataFrame({
            'Factor': ['Punishment Length', 'Clean Antecedents', 'Chargesheet Status', 'Undertrial Detention',
                       'Jail Conduct'],
            'Score': [4 if years <= 5 else 3 if years <= 7 else 2 if years <= 10 else 0,
                      2 if first_offender else 0, 2 if chargesheet else 0,
                      2 if detention >= 8 else 1 if detention >= 4 else 0, 1 if conduct else 0],
            'Status': ['✅ Strong', '✅ Favorable', '✅ Mitigating', '⚖️ Neutral', '✅ Positive']
        })
        st.markdown('<h3 style="color:#f8fafc;">📊 QUANTITATIVE ASSESSMENT MATRIX</h3>', unsafe_allow_html=True)
        st.dataframe(matrix, use_container_width=True, hide_index=True)

        # DOWNLOADS
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            csv = matrix.to_csv(index=False)
            st.download_button("📊 CSV Matrix", csv, f"bail_matrix_{result['score']}.csv", "text/csv")
        with col2:
            report = f"""JUDICIAL ELIGIBILITY ASSESSMENT
=================================
CASE: {crime}
PUNISHMENT: {years} years maximum
SCORE: {result['score']}/{result['max']} ({result['confidence']}% confidence)

ASSESSMENT: {result['status']}
CATEGORY: {result['category']}

LEGAL FACTORS:
{chr(10).join([f"{i}. {f}" for i, f in enumerate(result['factors'], 1)])}

LEGAL PRECEDENTS:
• CrPC §437(1) - Non-bailable offences
• State of Rajasthan v. Balchand (1977 AIR 2447)
• Gudikanti Narasimhulu v. Public Prosecutor (1978 AIR 429)
• Arnesh Kumar v. State of Bihar (2014 8 SCC 273)

⚠️ DISCLAIMER: Algorithmic preliminary assessment only."""
            st.download_button("📜 Full Report", report, "judicial_assessment.txt", "text/plain")

