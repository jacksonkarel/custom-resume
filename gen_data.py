import json

from rasa.shared.nlu.training_data.formats.rasa_yaml import RasaYAMLWriter
from rasa.shared.nlu.training_data.training_data import TrainingData

from data import NLP, ONTOLOGY

def gen_data():
    lookup_data = TrainingData()
    ent_syn_data = TrainingData()

    skills_path = "data/skills.json"
    with open(skills_path) as json_file:
        skills = json.load(json_file)
    
    new_json = {}
    ent_syn = {}
    skill_lookup = {'name': 'skill', 'elements': []}
    roles = [NLP, ONTOLOGY]
    for role in roles:
        low_skills = {}
        for skill in skills[role].items():
            s_value = skill[1]
            if skill[0].islower():
                s_name = skill[0]
            else:
                s_value["capitalized"] = skill[0]
                s_name = skill[0].lower()

            low_skills[s_name] = s_value

        new_json[role] = low_skills
    
        for skill in low_skills:
            if "synonym" in low_skills[skill]:
                ent_syn[skill] = low_skills[skill]["synonym"]
            
            skill_lookup["elements"].append(skill)
    
    ent_syn_data.entity_synonyms = ent_syn
    lookup_data.lookup_tables = [skill_lookup]
    yaml_writer = RasaYAMLWriter()
    yaml_writer.dump("nlu/data/synonyms.yml", ent_syn_data)
    yaml_writer.dump("nlu/data/skill_lookup.yml", lookup_data)

    with open(skills_path, 'w') as outfile:
        json.dump(new_json, outfile)