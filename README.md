# 🚀 ClubMind AI - Intelligent Community Leadership Recommendation System

ClubMind AI is an AI-powered recommendation system that helps clubs, student communities, and organizations identify the most suitable members for leadership roles, event management, workshops, and team responsibilities.

The system uses semantic search, vector embeddings, and agent-based workflows to analyze member profiles and provide intelligent recommendations.

---

## 📌 Problem Statement

In clubs and communities, assigning responsibilities is often based on manual judgment and limited visibility into member contributions.

As communities grow, it becomes difficult to:

* Identify the best candidate for leadership roles
* Recognize active contributors
* Match responsibilities with member skills
* Make data-driven decisions

ClubMind AI solves this by analyzing member information and recommending the most suitable candidates for specific roles.

---

## ✨ Features

* 🔍 Semantic member search using embeddings
* 🤖 AI-powered candidate analysis
* 📊 Leadership recommendation engine
* 🏆 Skill and achievement matching
* 🎯 Role-based candidate suggestions
* ⚡ Fast vector retrieval using Qdrant
* 🌐 Streamlit web interface

---

## 🏗️ Architecture

```text
User Query
    │
    ▼
Qdrant Vector Search
    │
    ▼
Analysis Agent
    │
    ▼
Recommendation Agent
    │
    ▼
Summary Agent
    │
    ▼
Final Recommendation
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & NLP

* Google Gemini
* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* Qdrant

### Agent Framework

* Google ADK

### Language

* Python

---

## 📂 Project Structure

```text
community-agent/
│
├── app.py
│
├── agents/
│   ├── analysis_agent.py
│   ├── recommendation_agent.py
│   └── summary_agent.py
│
├── workflows/
│   └── leadership_workflow.py
│
├── adk/
│   └── orchestrator.py
│
├── qdrant/
│   ├── ingest_members.py
│   └── search_members.py
│
├── data/
│   └── members.json
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/community-agent.git

cd community-agent
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 📊 Load Member Data

Initialize Qdrant collection and embeddings:

```bash
python qdrant/ingest_members.py
```

Expected Output:

```text
Collection created successfully
Successfully inserted members
Qdrant setup completed
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💬 Example Queries

### Leadership Recommendation

```text
Who should lead the AI Workshop?
```

### Event Management

```text
Who can organize a Hackathon?
```

### Technical Lead

```text
Who is suitable for an AI Project Lead role?
```

### Community Management

```text
Who can manage community engagement activities?
```

---

## 🎯 Use Cases

* Student Clubs
* Technical Communities
* Hackathon Teams
* Event Organizing Committees
* Professional Networks
* Volunteer Organizations

---

## 📚 Key Learnings

This project provided hands-on experience with:

* Vector Databases (Qdrant)
* Embedding Models
* Semantic Search
* Agentic AI Systems
* Google ADK
* Streamlit Deployment
* Cloud Debugging
* LLM Integration

---

## 🔮 Future Enhancements

* Member performance analytics
* Explainable recommendation scores
* Multi-community support
* Real-time contribution tracking
* Dashboard for administrators
* Advanced leadership prediction

---

## 👨‍💻 Author

**Nirmalkumar V**

B.Tech Artificial Intelligence & Data Science

Karpagam College of Engineering

Passionate about Agentic AI, Machine Learning, and Intelligent Systems.

---

⭐ If you found this project useful, consider giving it a star!
