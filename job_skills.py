import json
import pickle

from rasa.core.processor import MessageProcessor
from rasa.core.channels.channel import UserMessage

def job_skills(job):
    with open('data/job.txt') as f:
        job_text = f.read()
    
    job_lines = job_text.split("/n")
    
    with open('data/skills.json') as json_file:
        skills = json.load(json_file)

    skill_rank = []
    for skill in skills:
        if "necessary" in skills[skill]:
            if skills[skill]["necessary"] == job:
                skill_rank.append(skills[skill]["capitalized"])

    message_processor = MessageProcessor("models/resume.tar.gz", None, None, None)

    for tl in job_lines: 
        user_message = UserMessage(tl)
        nlu = message_processor._parse_message_with_graph(user_message)
        for ent in nlu["entities"]:
            lower_value = ent["value"].lower()
            if lower_value in skills:
                if "synonym" in skills[lower_value]:
                    lower_value = skills[lower_value]["synonym"]
                
                capitalized = skills[lower_value]["capitalized"]
                if capitalized not in skill_rank:
                    skill_rank.append(capitalized)
    
    return skill_rank

def pickle_js(job):
    skill_rank = job_skills(job)
    print(skill_rank)
    with open("skill_rank.pickle", 'wb') as f:
        pickle.dump(skill_rank, f)
    
    
