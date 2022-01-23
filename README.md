# Project: Build Closed Source Severless Service that uses AWS Sagemaker Classifier Model to Predict How Likely Customers Are To Purchase Long-Term Deposits.

# Domain: Financial Institutions (especially Banks)

# Date: 11/19/2021

## Team Members
* Godwin Anguzu
* Tego Chang
* Himangshu Raj Bhantana
* John Owusu Duah

## Outline of Readme
1. Problem Statement
2. Preamble 
3. Data
4. Project Flowchart
5. Instructions on How to Use Closed Source Service
6. Project Implementation Steps


## 1. Problem Statement
Long-term deposits are the life-blood of all financial institutions, especially banks. As a result, banks deploy a lot of resources to sell long-term deposits to customers. The status quo is that the marketing of these plans are not targeted to customers who are likely to deposit funds on a long-term basis. Thus, a lot money and time is spent selling these plans to large swathes of customers in an ineffective manner. 

Can C-suite executives of banks leverage advances in machine learning and data engineering practices to predict how likely customers, belonging different socio-economic demographic groups, are to purchase long-term deposits?


## 2. Preamble
This project was motivated by our curiosity to demonstrate how to extend the usefulness of machine learning models outside script or notebook environment and make them accessible via API for predictions. As a closed source service, a C-suite executive of a bank can make predictions from the binary classifier with Postman without having any technical knowledge of machine learning. By serving the model using serverless technology (specifically AWS Lambda) and AWS API Gateway, decision makers have access to the immense power of machine learning models to make key objective decisions that improve the bottom line of their businesses.


## 3. Data
The original data set was sourced from ![UCI Irvine's Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank%2BMarketing) and is a real world data set of Portuguese bank (name withheld for privacy reasons) that collected data of a campaign to sell long-term deposit plans to customers between 2008 to 2013. The classification goal is to predict if the client will subscribe (yes/no) to the term deposit (variable y). 

The following predictor variables were selected:

* age : age of customer   

* balance (account balance in US$ Dollars): numeric

* housing (has housing loan?) : 0 - no, 1 - yes

* loan (has personal loan?) : 0 - no, 1 - yes


The target variable is:

* decision or y : 0 - no, 1 - yes

A preview of the data set is as follows:

![data_preview](https://user-images.githubusercontent.com/67676957/142749563-d6af5a2d-805b-4f14-9f7f-39983b5aadc1.png)


After carrying Exploratory Data Analysis (EDA) we selected age, balance (i.e. account balance in US$ dollars), housing (i.e. whether customer has housing loan) and loan (i.e. whether customer has personal loan) as predictor variables for training and testing/prediction of sagemaker linear learner model.


The emphasis of this project is on deployment of machine learning model so the sagemaker notebook has been provided in this repository via this [link.](https://github.com/Tego-Chang/Predicting-if-customers-will-purchase-long-term-deposit-/blob/main/sagemaker_longtermdecision_model.ipynb) for easy referencing.


## 4. Project Flowchart

The data engineering architecture has been outline below:

![flowchart](https://user-images.githubusercontent.com/67676957/142749811-007dfa12-2c89-4e37-bcdb-d600928e1e3a.png)


## 5. Instructions on How to Use Closed Source Service

#### Note
Since we currently do not have the funds to keep sagemaker notebook instances and endpoints running in the cloud, we delete endpoints and notebook instances immediately after demonstrating the project. If you wish to use the closed source service, kindly contact one of the participants of the group, John Owusu Duah on 9843779696 to reinstate sagemaker enpoints and notebook instances temporarily.

#### How To
To access the closed source service, kindly use ```Postman```, an API platform for building and using APIs and provide the predictor variables of age, account balance, housing loan status and personal loan status in that order. 

After executing ```Postman```, select ```POST``` from the drop-down menu, past the following url created by AWS API Gateway to the ```POST``` url field:

$https://8xka5w97z6.execute-api.us-east-2.amazonaws.com/bank_predict_2/bank_model_resource

Select the ```Body``` sub-menu and type the predictor variables in a dictionary with key named "data" in the following format:

Example:

>{"data":"55,4200,0,1"}

>where:

>55 = customer of age 55

>4200 = customer with account balance of $4,200.00

>0 = customer does not have housing loan (if 1, then customer has housing loan)

>1 = customer has personal loan (if 0, then customer does not have personal loan)

An example of the above dictionary with parsed response in Postman can be seen below:

![postman](https://user-images.githubusercontent.com/67676957/142763292-ac045df8-6f5b-4d9a-bddc-916df7b458dc.png)


## 6. Project Implementation Steps

1. Step 1: Build AWS Sagemaker Linear Learner Machine Learner Model with involves the following sub-tasks showin in the jupyter notebook [here](https://github.com/Tego-Chang/Predicting-if-customers-will-purchase-long-term-deposit-/blob/main/sagemaker_longtermdecision_model.ipynb) in this repository:

> i.Upload Data from UCI Machine Learning Repository 

> ii.Carry out EDA and Data Preprocessing 

> iii.Carry out Feature and Target Variables Selection and Convert to Numpy Array

> iv.Split Data into Training and Testing Data

> v.Convert Training and Testing Data to Record I/O format and upload to AWS S3 Bucket

> vi.Specify Location of Model Artifacts in AWS S3 Bucket

> vii.Select, Tune and Train AWS Sagemaker's Linear Learner Binary Classifier on Training Data

> viii.Deploy Model to AWS Sagemaker Endpoint

> ix.Evaluate the Model

> x.Make Predictions with Test Data



2. Step 2: Invoke Trained Model Via Sagemaker Endpoint in a Serverless Fashion using AWS Lambda. The code for the AWS Lambda function that invokes the enpoint (every time you deploy the model, the endpoint changes so the name of the endpoint has to be updated in the lambda function) can be found [here](https://github.com/Tego-Chang/Predicting-if-customers-will-purchase-long-term-deposit-/blob/main/lambda_code.py) in this repository:

Note: AWS Lambda function can be tested with the same input made into ```Postman```.



3. Step 3: Create REST API URL with AWS API Gateway to invoke lambda function following the following steps:

  i. Open AWS API Gateway and create new REST API and type a name in the API field as shown in the image below:
  ![create_restapi](https://user-images.githubusercontent.com/67676957/142767065-5f7858a1-cb6e-4f5b-b6af-8cfe7c114f28.png)
  
  
 ii. After creating the API, select the method to call API, in our case we selected the POST method:
  ![post_method1](https://user-images.githubusercontent.com/67676957/142767453-89c49d30-f786-458d-bba2-f53b28bcc686.png)
  
  ![post_method1](https://user-images.githubusercontent.com/67676957/142767512-0eb7ec02-8a90-4774-8fef-1f9a6b24511f.png)
  
  
iii. Connect AWS Lambda function to POST API by selecting Lambda function integration type and the name of the lambda function created in Step 2
 ![connect_lambda](https://user-images.githubusercontent.com/67676957/142767660-a32ee79c-b72a-4da8-aeef-bc6a126bd814.png)
 
 ![permission](https://user-images.githubusercontent.com/67676957/142767816-a1a5313f-1a71-49c5-b893-372497a6a02a.png)
 
iv. Deploy API and create resource URL
 ![deploy_api1](https://user-images.githubusercontent.com/67676957/142767982-7c446a66-c837-420b-854d-30b1f797e5b9.png)
 
v.Select new stage and specify a stage name.
  ![deploy_api2](https://user-images.githubusercontent.com/67676957/142768073-09943b7c-b23c-4406-8226-a5c84e67ae91.png)
  
vi.Click Stage Drop Down Menu and Select POST method (marked with red). Copy ```Invoke URL``` into ```Postman```
  ![deploy_api2](https://user-images.githubusercontent.com/67676957/142768502-9336f91b-adc9-49db-905e-74c0f2b1ceea.png)
  
vii.Make a Prediction with Model Using Postman following the example below:
  ![postman_2](https://user-images.githubusercontent.com/67676957/142763292-ac045df8-6f5b-4d9a-bddc-916df7b458dc.png)

