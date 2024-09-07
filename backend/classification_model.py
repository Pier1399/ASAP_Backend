import pickle
import re
from pydantic import BaseModel

def predictResult(review):
    model=importmodel('../export_models/lr_cv0.pkl')
    vect=importmodel('../export_models/cv_save.pkl')

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

class HealthData(BaseModel):
    name: str
    emergency_email: str
    blood_pressure_high: int
    glucose: int #1: Normal, 2: Above Normal, 3: Well Above Normal
    cholesterol: int #1: Normal, 2: Above Normal, 3: Well Above Normal
    age_years: int
    gender: int # 1 female, 2 male
    height_cm: int
    bmi : float
    smoker: bool # 0: Non-smoker, 1: Smoker
    alcohol: bool # 0: Non-drinker, 1: Drinker
    phisical_activity: bool # "active" or "inactive"
    cardiovascular_disease: bool # 0: No, 1: Yes
    bp_category: int # 1: Hypert 1, 2: Hypert 2, 3: Normal, 4: Elevated


class Prediction(BaseModel):
    prediction: str | None= None
    video_monitoring_active: bool | None= None
"""
class Preprocessing:
    def createstopw(self):
        stopwords = []
        with open('../export_models/StopWords_Geographic.txt', 'r') as f:
            sw_g = f.readlines()
        with open('../export_models/StopWords_DatesandNumbers.txt', 'r') as f:
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
"""
class YoloRecon:
