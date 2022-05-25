# Links
GITHUB = "https://github.com/jacksonkarel"
HF_PAGE = "https://huggingface.co/jacksonkarel"

# Jobs
JUICEBOX = "juicebox"
AH = "anchor health"

# Roles
NLP = "nlp"
ONTOLOGY = "ontology"

class Duty:
  def __init__(self, description, jobs=[], roles=[], text_adds={}):
    self.jobs = jobs
    self.roles = roles
    self.description = description
    self.text_adds = text_adds

just_jbox = [JUICEBOX]

class Jbox_duties:
    man_nlp = Duty("Managed the NLP {}for a virtual assistant that went from 13,000 to 100,000 current subscribers while working on the project.", text_adds={NLP: "", ONTOLOGY: "and ontology "})

    nlu = Duty("Trained natural language understanding (NLU) models with text/intent classification and entity extraction.")

    ent_num = Duty("Took an NLP system that could recognize 55 intents and 450 entities to one that can recognize 101 intents and {}+ entities. This included increasing the number of sex act and body part entities from 10 to 5000+.", text_adds={NLP: "100,000", ONTOLOGY: "8850"})

    sex_name = Duty("Built syntactic parsing pipelines to extract complex sex names from users.")
    consent = Duty("Worked on the task of training AI models to recognize sexual consent.")
    research = Duty("Researched and experimented with state of the art/cutting-edge language models and pipelines.")
    nlg = Duty("Experimented with natural language generation.")
    nlp_roadmap = Duty("Worked on NLP roadmap.")
    no_code = Duty("Created an initiative to build internal no-code tools to cut down on engineering time.")


user_data = Duty("Analyzed user data.", [JUICEBOX, AH])

