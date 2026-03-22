import streamlit as st
import pandas as pd

# --- Core logic imports ---
from ai_prioritizer import prioritize_tasks_with_ai
from scoring import calculate_score, calculate_risk, get_recommendation, get_reason
from styles import load_css

# --- App setup ---
st.set_page_config(page_title="AI Workload Predictor", layout="wide")

st.markdown(load_css(), unsafe_allow_html=True)

# ---------- Header UI ----------
st.markdown('<div class="main-title">WorkLoad Prioritizer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">AI helps students decide what to work on first.</div>',
    unsafe_allow_html=True
)

# ---------- Session State (persistent data) ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []  # store user tasks

if "ai_result" not in st.session_state:
    st.session_state.ai_result = ""  # store AI output

if "demo_loaded" not in st.session_state:
    st.session_state.demo_loaded = False  # track demo usage

st.markdown("---")

# ---------- Add Task Form ----------
st.markdown('<div class="section-title">➕ Add Task</div>', unsafe_allow_html=True)

with st.form("task_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    # --- Input fields ---
    with col1:
        name = st.text_input("Task Name")
        deadline = st.number_input("Deadline (days)", min_value=0, step=1)

    with col2:
        difficulty = st.slider("Difficulty", 1, 10)
        time_required = st.number_input("Hours Needed", min_value=1, step=1)
        weight = st.slider("Importance", 1, 10)

    submitted = st.form_submit_button("➕ Add Task")

    # --- Handle form submission ---
    if submitted:
        if name.strip():
            # clear demo data if user starts adding real tasks
            if st.session_state.demo_loaded:
                st.session_state.tasks = []
                st.session_state.demo_loaded = False

            # store task
            st.session_state.tasks.append({
                "name": name.strip(),
                "deadline": int(deadline),
                "difficulty": int(difficulty),
                "time": int(time_required),
                "weight": int(weight),
            })

            st.session_state.ai_result = ""  # reset AI output
            st.success("Task added.")
        else:
            st.warning("Please enter a task name.")

# ---------- Control Buttons ----------
col1, col2 = st.columns(2)

# --- Reset all data ---
with col1:
    if st.button("🗑 Reset", use_container_width=True):
        st.session_state.tasks = []
        st.session_state.ai_result = ""
        st.session_state.demo_loaded = False
        st.success("Tasks cleared.")

# --- Load demo data ---
with col2:
    if st.button("📂 Demo", use_container_width=True):
        st.session_state.tasks = [
            {"name": "Weekly Assignment", "deadline": 3, "difficulty": 6, "time": 3, "weight": 7},
            {"name": "Quiz Review", "deadline": 4, "difficulty": 4, "time": 2, "weight": 5},
            {"name": "Final Project Submission", "deadline": 1, "difficulty": 9, "time": 6, "weight": 10},
            {"name": "Midterm Exam Preparation", "deadline": 2, "difficulty": 8, "time": 5, "weight": 9},
            {"name": "Lecture Notes Revision", "deadline": 7, "difficulty": 3, "time": 1, "weight": 3}
        ]
        st.session_state.ai_result = ""
        st.session_state.demo_loaded = True
        st.success("Demo data loaded.")

st.markdown("")

# ---------- Backend Scoring ----------
# compute score for each task before AI processing
for task in st.session_state.tasks:
    task["score"] = calculate_score(task)

# ---------- AI Trigger ----------
if st.button("🤖 Prioritize with AI", use_container_width=True):
    if st.session_state.tasks:
        with st.spinner("Analyzing..."):
            st.session_state.ai_result = prioritize_tasks_with_ai(st.session_state.tasks)
    else:
        st.warning("Add tasks first.")

# ---------- AI Output Display ----------
st.markdown("---")
st.markdown('<div class="section-title">🧠 AI Prioritization</div>', unsafe_allow_html=True)

if st.session_state.ai_result:
    lines = st.session_state.ai_result.split("\n")

    summary = None
    ranking_lines = []

    # --- separate summary and ranked results ---
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        if clean_line.lower().startswith("summary:"):
            summary = clean_line.replace("Summary:", "").strip()
        else:
            ranking_lines.append(clean_line)

    # --- show summary ---
    if summary:
        st.markdown('<div class="section-title">🔍 AI Reasoning Summary</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="ai-card">{summary}</div>',
            unsafe_allow_html=True
        )

    # --- show ranked tasks ---
    for line in ranking_lines:
        if "Recommended first task" in line:
            st.markdown(
                f'<div class="ai-card-recommended">{line}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="ai-card">{line}</div>',
                unsafe_allow_html=True
            )
else:
    st.info("Click 'Prioritize with AI' to generate the ranked task order.")

# ---------- Task List + Analysis ----------
st.markdown("---")
st.markdown('<div class="section-title">📝 Task List</div>', unsafe_allow_html=True)

results = []

# --- compute risk + recommendation for each task ---
for i, task in enumerate(st.session_state.tasks, start=1):
    risk = calculate_risk(task)
    action = get_recommendation(risk)
    reason = get_reason(task)

    results.append({
        "Task #": i,
        "Task": task["name"],
        "Deadline": task["deadline"],
        "Difficulty": task["difficulty"],
        "Hours": task["time"],
        "Weight": task["weight"],
        "Risk": risk,
        "Action": action,
        "Reason": reason
    })

# ---------- Table Display ----------
if results:
    df = pd.DataFrame(results)

    # --- highlight rows based on risk ---
    def highlight_risk(row):
        if row["Risk"] == "HIGH":
            return ["background-color: #3A2323; color: #FCA5A5"] * len(row)
        elif row["Risk"] == "MEDIUM":
            return ["background-color: #3A3322; color: #FCD34D"] * len(row)
        else:
            return ["background-color: #223A2E; color: #86EFAC"] * len(row)

    styled_df = (
        df.style
        .apply(highlight_risk, axis=1)
        .set_properties(**{
            "border": "1px solid #2F3B4F",
            "text-align": "center"
        })
    )

    st.dataframe(styled_df, use_container_width=True)
else:
    st.info("No tasks added.")