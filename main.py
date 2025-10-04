import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langsmith import traceable

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key)

class State(TypedDict):
    application:str
    experience_level:str
    skill_match:str
    response:str

workflow = StateGraph(State)

@traceable(name="categorize_experience")
def categorize_experience(state:State) -> State:
    print('\nCategorizing the experience level of the candidate')
    prompt = ChatPromptTemplate.from_template("Based on the following job application, categorize the candidate as 'Entry-level', 'Mid-level' or 'Senior-level'"
      "Application : {application}")
    chain = prompt | llm 
    experience_level = chain.invoke({"application":state["application"]}).content
    return {"experience_level":experience_level}

@traceable(name="assess_skillset")
def assess_skillset(state:State) -> State:
    print("\nAssessing the skillset of candidate : ")
    prompt = ChatPromptTemplate.from_template(
      "Based on the job application for a Python Developer, assess the candidate's skillset"
      "Respond with either 'Match' or 'No Match'"
      "Application : {application}"
    )
    chain = prompt | llm
    skill_match = chain.invoke({"application": state["application"]}).content
    print(f"Skill Match : {skill_match}")
    return {"skill_match" : skill_match}


@traceable(name="schedule_hr_interview")
def schedule_hr_interview(state:State) -> State:
    print("\nScheduling the interview : ")
    return {"response" : "Candidate has been shortlisted for an HR interview."}

@traceable(name="escalate_to_recruiter")
def escalate_to_recruiter(state:State) -> State:
    print("\nEscalating to the recruiter")
    return {"response":"Candidate has been escalated to the recruiter."}

@traceable(name="rejection_email")
def rejection_email(state:State) -> State:
    print("Sending Rejection Email")
    return {"response":"Sending the rejection email as the candidate does not match the JD"}

workflow.add_node("categorize_experience",categorize_experience)
workflow.add_node("assess_skillset",assess_skillset)
workflow.add_node("schedule_hr_interview",schedule_hr_interview)
workflow.add_node("escalate_to_recruiter",escalate_to_recruiter)
workflow.add_node("rejection_email",rejection_email)

def route(state:State) -> str:
    if state["experience_level"] == "Senior-level":
        return "escalate_to_recruiter"
    elif state["skill_match"] == "Match":
        return "schedule_hr_interview"
    else:
        return "rejection_email"

workflow.add_edge("categorize_experience","assess_skillset")
workflow.add_conditional_edges("assess_skillset",route)
workflow.add_edge(START,"categorize_experience")
workflow.add_edge("schedule_hr_interview",END)
workflow.add_edge("escalate_to_recruiter",END)
workflow.add_edge("rejection_email",END)

app = workflow.compile()


def run_candidate_screening(application: str):
  results = app.invoke({"application" : application})
  return {
      "experience_level" : results["experience_level"],
      "skill_match" : results["skill_match"],
      "response" : results["response"]
  }

config = {
    "run_name":"candidate_screening"
}

application_text = "I have 10 years of experience in software engineering with expertise in C#"
results = run_candidate_screening(application_text)
print("\n\nComputed Results :")
print(f"Application: {application_text}")
print(f"Experience Level: {results['experience_level']}")
print(f"Skill Match: {results['skill_match']}")
print(f"Response: {results['response']}")

