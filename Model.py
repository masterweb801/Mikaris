# --------      Download The Model      -------------
# from huggingface_hub import snapshot_download
# snapshot_download(repo_id="deepset/roberta-base-squad2", cache_dir="./models/")

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import wikipedia

model_name = "models\models--deepset--roberta-base-squad2\snapshots\e84d19c1ab20d7a5c15407f6954cef5c25d7a261/"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
cont = ""
with open("./context.txt", "r") as f:
    cont += f.read()
    f.close()

def getKnowledge(query: str):
    results = wikipedia.summary(query, sentences=10)
    cont += " " + results

def answerQuestion(question: str):
    global cont
    if cont == "":
        return "Please Train Me!"
    else:
        QA_input = {
            'question': question,
            'context': cont
        }
        res = nlp(QA_input)
        return res['answer']

if __name__=="__main__":
    cont += "The Solar System is the gravitationally bound system of the Sun and the objects that orbit it. The largest of these objects are the eight planets, which in order from the Sun are four terrestrial planets (Mercury, Venus, Earth and Mars); two gas giants (Jupiter and Saturn); and two ice giants (Uranus and Neptune). The Solar System developed 4.6 billion years ago when a dense region of a molecular cloud collapsed, forming the Sun and a protoplanetary disc."
    print(answerQuestion("what is solar system?"))