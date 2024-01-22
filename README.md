# SentimentAnalysis_Backend
This Repository contains the implmentation of the backend server used to access to the final product of the Sentimental Analysis project of group "I Sentimentalysti" realized for the course of Software Engineering @ Politecnico di Bari.<br>
We started with a 50k reviews dataset from IMDB (found on Kaggle) and created a model which can be used for a binary classification of user reviews in two categories (positive or negative).<br>
The implementation of the backend server made with <b>Uvicorn and FastAPI</b> can be used to access to the ML model implementation via HTML request on local port 5555. The server implements a <code>GET /healt_check</code> access point and a <code>POST /prediction</code> feature which receives in input the sentence and returns the prediction result and the confidence score.
<table><tr><tc><ul>
  <li>
  METHOD: GET</li> 
  <li>
  ROUTE NAME: /health_check</li>
  <li>
  REQUEST BODY:	Not required</li>
  <li>  OUTPUT:<br>
    RESPONSE - STATUS CODE 200	{ “status”: “OK” }
  </li>
  </ul></tc></tr>
  <tr><tc>
    <ul>
  <li>
  METHOD: POST</li> 
  <li>
  ROUTE NAME: /prediction</li>
  <li>
  REQUEST BODY:	{ "query":"Input sentence of the review" }</li>
  <li>  OUTPUT:<br>
    RESPONSE - STATUS CODE 200	{ “prediction”: “negative” or "positive"; "confidence_score":"82%" }<br>
              STATUS CODE: 500 { "status": "Error" }<br>
  </li>
  </ul>
  </tc></tr>
</table>
Previous repository: <a href="https://github.com/davexhardware/SentimentAnalysis_ModelTesting">Model_Testing</a><br>
Next repository: implementation of the website with a landing page used to send Reviews and receive back the results of the prediction, from the backend server. (Angular Material needed): <a href="https://github.com/davexhardware/SentimentAnalysis_Frontend">Frontend</a>
