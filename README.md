
<h2>Deploying-a-ML-Model</h2>

This repository contains procedure to deploy a machine learning model. First we build a logistic regression classifier based on the car purchase prediction problem(https://www.kaggle.com/code/casper6290/car-purchase-prediction) Then we build the api using FastApi and serve with Uvicorn.

Steps: 

1. Create a new envionment using the environment.yaml file and activate it.
2. Use the dev.in file to install the dependecies. prod.in file is for production dependencies.

   For above steps refer to this https://github.com/arav4450/Structuring-ML-Project  repository  for details
  
3. Build the classifier. Code for the same is provided in the train folder. Here we are saving both the model as well as transform in pickle format

4. Refer the model folder in api where we are saving the final model. In main.py file, code to accept the request and provide the response is given.

5. In the test_connection  file sample code to send request and obtain the response is provided

6. Finally, refer the Dockerfile which makes it easier to deploy the application across   environments without much additional integration steps. Use below codes to build and run the image.Docker should be installed before running the code
        
        docker build -t api_image ./
        docker run -d --name mycontainer -p 80:80 api_image
