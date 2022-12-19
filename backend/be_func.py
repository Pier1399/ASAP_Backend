import pickle
import re
import nltk.tokenize as tok
from pydantic import BaseModel
import spacy as sp

def predictResult(review):
    model=importmodel('../export/lr_cv0.pkl')
    vect=importmodel('../export/cv_save.pkl')
    pcs=Preprocessing()
    prev=pcs.text_preproc(review)
    if(prev==""):
        raise IOError()
    vrev=vect.transform([prev])
    p=Prediction()
    p.prediction,cs=model.predict(vrev)[0],model.predict_proba(vrev)[0]
    if p.prediction == "positive":
        p.confidence_score = round(cs[1] * 100,6)
    else:
        p.confidence_score = round(cs[0] * 100,6)
    return p.dict()

def importmodel(filename):
    with open(filename,'rb') as file:
        model=pickle.load(file)
    return model
def exportmodel(model, filename):
    with open(filename,'wb') as file:
        pickle.dump(model,file)

class Prediction(BaseModel):
    prediction: str | None= None
    confidence_score: float |None= None
class Preprocessing:
    def createstopw(self):
        stopwords = []
        with open('../export/StopWords_Geographic.txt', 'r') as f:
            sw_g = f.readlines()
        with open('../export/StopWords_DatesandNumbers.txt', 'r') as f:
            sw_d = f.readlines()
        [stopwords.append(sw.strip('\n').lower()) for sw in sw_g]
        [stopwords.append(sw.strip('\n').lower()) for sw in sw_d]
        return stopwords

    def text_preproc(self, tokrev):
        if not self.stopw:
            self.stopw = self.createstopw()
        tokrev = re.sub(r"[^A-Za-z]+", " ", tokrev)
        renot = re.compile("|".join(map(re.escape, self.notwords)))
        tokrev = renot.sub("not", tokrev)
        tokrev = tok.word_tokenize(tokrev, "english")  # tokenizzo la prima review
        tokrev = [token.lemma_ for token in self.nlp(str(tokrev)) if
                  (not token.is_punct)]  # pulisco dalla punteggiatura
        tokrev = [word for word in tokrev if (
                word != '' and word != ' ' and word != "\'s" and word != 'br' and word != 'em' and word not in self.stopw and len(
            word) > 1)]
        stoken = " ".join(tokrev)
        return stoken

    notwords = [
        "nor",
        "don t",
        "won t",
        "couldn",
        "didn",
        "doesn",
        "hasn",
        "hadn",
        "haven",
        "isn",
        'mightn',
        'mustn',
        'needn',
        'shan',
        'shouldn',
        'wasn',
        'weren',
        'wouldn',
    ]

    def __init__(self):
        self.nlp = sp.load("en_core_web_md")
        self.stopw = self.createstopw()
