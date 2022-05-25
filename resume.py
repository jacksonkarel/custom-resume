# Links
GITHUB = "https://github.com/jacksonkarel"
HF_PAGE = "https://huggingface.co/jacksonkarel"

# Jobs
JUICEBOX = "juicebox"
AH = "anchor health"

# Roles
NLP = "nlp"
ONTOLOGY = "ontology"
CHATBOT = "chatbot"

just_jbox = [JUICEBOX]

user_data = {"desc": "Analyzed user data."}
train_models = {"desc": "Trained {} models for various clients.", "template": {NLP: "NLP", CHATBOT: "AI"}}
jbox_duties = [
    {
        "desc": "Managed the NLP {}for a virtual assistant that went from 13,000 to 100,000 current subscribers while working on the project.", 
        "template": {NLP: "", ONTOLOGY: "and ontology "}, 
        "moveable": False
    },

    {
        "desc": "Took an NLP system that could recognize 55 intents and 450 entities to one that can recognize 101 intents and {}+ entities. This included increasing the number of sex act and body part entities from 10 to 5000+.",
        "template": {NLP: "100,000", ONTOLOGY: "8850"}
    },

    {"desc": "Trained natural language understanding (NLU} models with text/intent classification and entity extraction."},
    {"desc": "Built syntactic parsing pipelines to extract complex sex names from users."},
    {"desc": "Worked on the task of training AI models to recognize sexual consent."},
    user_data,
    {"desc": "Researched and experimented with state of the art/cutting-edge language models and pipelines."},
    {"desc": "Experimented with natural language generation."},
    {"desc": "Worked on NLP roadmap."},
    {"desc": "Created an initiative to build internal no-code tools to cut down on engineering time."},
    {"desc": "Set up automated testing of NLU."},
    {"desc": "Advised management on technical NLP topics and strategies for communicating them to investors."},
]

nlp_skills = ["Natural Language Processing/Understanding", "Conversational AI", "Semantic/Syntactic Parsing", "Machine Learning", "Natural Language Generation", "Text Analytics", "Natural Language Inference", "Language Modeling", "Transformers", "Transfer Learning", "Research", "SQL", "Text/Intent Classification", "Python", "Named Entity Recognition", "Hugging Face", "Anomaly/Novelty Detection", "spaCy", "Semantic Search"]

onto_skills = ["Ontologies and Taxonomies", "OWL", "RDF", "SPARQL", "Protégé", "Owlready2", "Basic Formal Ontology (BFO)"]
