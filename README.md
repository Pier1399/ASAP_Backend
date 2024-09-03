# Fall Detection ASAP Backend
This Repository contains the implementation of the backend server that performs  an "Elderly Patients Fall Prevention and Detection" task,
through machine learning and deep learning models.<br>
The datasets to train these models were found on kaggle, and the model training repository is available at this link: <a href="https://github.com/davexhardware/fall_detection_project_SAPD">Fall Detection ASAP</a><br>
The implementation of the backend server made with <b>Uvicorn and FastAPI</b> can be used to access to the ML model implementation via HTML request on local port 5555. The server implements a <code>GET /healt_check</code> access point and a <code>POST /prediction</code> feature which receives 
patient's collected daily health informations about different parameters (pressure, hearth rate, glucose, age, etc..) and responds if the fall risk is high or low.<br>
Using the result of the risk classification model, the server will choose whether to send an alert to the patient's family or not, and in the first case it also activates the 
webcam stream of the computer that is then analyzed by a Neural Network (Yolov8 model) in order to recognize fall events in the room, and eventually sending an alert to the emergency contacts.<br>
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
  REQUEST BODY:	{ //TODO }</li>
  <li>  OUTPUT:<br>
    RESPONSE - STATUS CODE 200	{ “prediction”: “negative” or "positive"; "confidence_score":"82%" }<br>
              STATUS CODE: 500 { "status": "Error" }<br>
  </li>
  </ul>
  </tc></tr>
</table>