from qdrant.search_members import search_members
from agents.analysis_agent import analyze_candidates
from agents.recommendation_agent import recommend_candidate
from agents.summary_agent import summarize_result

def leadership_workflow(query):

    candidates = search_members(query)

    analysis = analyze_candidates(
        query,
        candidates
    )

    recommendation = recommend_candidate(
        query,
        analysis
    )

    summary = summarize_result(
        query,
        recommendation
    )

    return summary