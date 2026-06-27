from workflows.leadership_workflow import leadership_workflow

def run(query):
    return leadership_workflow(query)

# from agents.lyzr_agent import get_requirements
# from qdrant.search_members import search_members
# from agents.analysis_agent import analyze_candidates
# from agents.recommendation_agent import recommend_candidate
# from agents.summary_agent import summarize_result


# def run(query):
#     # Step 1: Lyzr extracts requirements
#     requirements = get_requirements(query)

#     # Step 2: Search members from Qdrant
#     candidates = search_members(requirements)

#     # Step 3: Gemini Analysis
#     analysis = analyze_candidates(query, candidates)

#     # Step 4: Gemini Recommendation
#     recommendation = recommend_candidate(query, analysis)

#     # Step 5: Gemini Summary
#     summary = summarize_result(query, recommendation)

#     return summary