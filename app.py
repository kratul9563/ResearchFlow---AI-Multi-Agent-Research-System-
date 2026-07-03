import streamlit as st
from pipeline import run_research_pipeline
import time

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.big-title{
    font-size:42px;
    font-weight:700;
    color:white;
}

.subtitle{
    font-size:18px;
    color:#9CA3AF;
}

.agent-card{
    padding:20px;
    border-radius:15px;
    background:#1E293B;
    text-align:center;
}

.report-box{
    padding:25px;
    border-radius:15px;
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
"""
<div class='big-title'>
🔬 ResearchFlow AI
</div>

<div class='subtitle'>
Multi-Agent Research System ↗
(Agentic AI + Multi-Agent)
</div>
""",
unsafe_allow_html=True
)

st.divider()

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.title("⚙ Settings")

    provider = st.selectbox(
        "LLM Provider",
        [
            "Groq"
        ]
    )

    model = st.selectbox(
        "Model",
        [
           "openai/gpt-oss-20b"
        ]
    )

    search_provider = st.selectbox(
        "Search Engine",
        [
            "Tavily"
        ]
    )

    st.divider()

    st.subheader("🤖 Agents")

    st.success("Search Agent")
    st.success("Reader Agent")
    st.success("Writer Agent")
    st.success("Critic Agent")

# =========================
# INPUT
# =========================
topic = st.text_area(
    "Research Topic",
    placeholder="Example:\nFuture of Agentic AI in Software Engineering",
    height=120
)

run = st.button(
    "🚀 Start Research",
    use_container_width=True,
    type="primary"
)

# =========================
# EXECUTION
# =========================
if run:

    progress = st.progress(0)

    status = st.empty()

    status.info("🔎 Search Agent Running...")
    progress.progress(25)

    time.sleep(1)

    status.info("📚 Reader Agent Running...")
    progress.progress(50)

    time.sleep(1)

    status.info("✍ Writer Agent Running...")
    progress.progress(75)

    time.sleep(1)

    status.info("🧐 Critic Agent Running...")
    progress.progress(90)

    result = run_research_pipeline(topic)

    progress.progress(100)

    status.success("✅ Research Completed")

    st.divider()

    tab1,tab2,tab3,tab4 = st.tabs([
        "📄 Report",
        "🔍 Sources",
        "📚 Research Data",
        "🧐 Critic"
    ])

    with tab1:

        st.subheader("Final Research Report")

        st.markdown(
            f"""
            <div class='report-box'>
            {result['report']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            "⬇ Download Report",
            result["report"],
            file_name="research_report.md"
        )

    with tab2:
        st.write(result["search_results"])

    with tab3:
        st.write(result["scraped_content"])

    with tab4:
        st.write(result["feedback"])