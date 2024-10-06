import pickle
from pydantic import BaseModel
import numpy as np
from detection_model import DetectionModel
model_path='C:/Users/DavideSavoia/Documents/ASAP_Backend/export_models/svc_model.pkl'
scaler_path='C:/Users/DavideSavoia/Documents/ASAP_Backend/export_models/scaler.pkl'
yolo_path="C:/Users/DavideSavoia/Documents/ASAP_Backend/export_models/best.pt"
pca_path='C:/Users/DavideSavoia/Documents/ASAP_Backend/export_models/pca.pkl'

class ClassificationModel:
    def __init__(self):
        self.detector = self.importmodel(model_path)
        self.scaler = self.importmodel(scaler_path)
        self.pca = self.importmodel(pca_path)
        self.activeDetections = []

    def predictResult(self,query):
        if len(self.activeDetections)>0:
            for detector in self.activeDetections:
                detector.stop()
                detector.join()
                self.activeDetections.remove(detector)
        emergency_email=query.emergency_email
        querylist= np.array([
            query.gender,
            query.height_cm,
            query.blood_pressure_high,
            query.blood_pressure_low,
            query.cholesterol,
            query.glucose,
            query.smoker,
            query.alcohol,
            query.physical_activity,
            query.age_years,
            query.bmi,
            query.blood_pressure_category
        ]).reshape(1,-1)
        patient_data = self.scaler.transform(querylist)
        patient_data = self.pca.transform(patient_data)
        prediction = self.detector.predict(patient_data)
        result=Prediction()
        if prediction[0] >= 0:
            result.prediction="High risk"
            detector=DetectionModel(yolo_path,emergency_email)
            detector.start()
            self.activeDetections.append(detector)
        else:
            result.prediction="No risk"
        return result


    def importmodel(self,filename):
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        return model


class HealthData(BaseModel):
    name: str
    emergency_email: str
    blood_pressure_high: int | None =None
    blood_pressure_low: int | None=None
    glucose: int | None=None # 1: Normal, 2: Above Normal, 3: Well Above Normal
    cholesterol: int | None=None # 1: Normal, 2: Above Normal, 3: Well Above Normal
    age_years: int | None=None
    gender: int | None=None # 1 female, 2 male
    height_cm: float | None=None
    bmi: float | None=None
    smoker: int | None=None # 0: Non-smoker, 1: Smoker
    alcohol: int | None=None # 0: Non-drinker, 1: Drinker
    physical_activity: int | None=None # 1 : "active", 0 : "inactive"
    blood_pressure_category: int | None=None # 1: Hypert 1, 2: Hypert 2, 3: Normal, 4: Elevated


class Prediction(BaseModel):
    prediction: str | None = None
