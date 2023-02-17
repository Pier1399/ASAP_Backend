# SentimentAnalysis_Backend
This Repository contains the implmentation of the backend server used to access to the final product of the Sentimental Analysis project of group "I Sentimentalysti" realized for the course of Software Engineering @ Politecnico di Bari. We started with a 50k reviews dataset from IMDB (found on Kaggle) and created a model which can be used for a binary classification o user reviews in two categories (positive or negative).<br>
The implementation of the backend server made by <b>Uvicorn and FastAPI</b>, and it can be used to access to the ML model implementation via HTML request on local port 5555. The server implements a "/healt_check" access point (GET method only) and a "/prediction" feature (POST method only) which receives in input the sentence and returns the prediction result and the confidence score.
1. INPUT:<br>
  METHOD - GET<br>
  ROUTE NAME - /health_check<br>
  REQUEST BODY -	Non necessario<br>
  OUTPUT:<br>
  RESPONSE - STATUS CODE 200	{ “status”: “OK” }<br>
1. INPUT:<br>
  METHOD - POST<br>
  ROUTE NAME - /prediction<br>
  REQUEST BODY -	{ "query":"Input sentence of the review" }<br>
  OUTPUT:<br>
  RESPONSE - STATUS CODE: 200	{ “prediction”: “negative” or "positive"; "confidence_score":"82%" }<br>
             STATUS CORE: 500 { "status": "Error" }<br>

Previous repository: <a href="https://github.com/davexhardware/SentimentAnalysis_ModelTesting">Model_Testing</a><br>
Next repository: implementation of the website with a landing page used to send Reviews and receive back the results of the prediction, from the backend server. (Angular Material needed): <a href="https://github.com/davexhardware/SentimentAnalysis_Frontend">Frontend</a>
