# Data Science Model Deployment Project

## `Project Title` - Bank Marketing

## `Problem-Statement` 
This data is related with direct market campaings (i.e. Phone calls) of a portuguese banking instituition. The classification goal is to predict if the client will subscribe a term deposit.
The marketing campaings were based on phone calls. Often, more than one contact to the same client was required in order to access if the product (bank term deposit) would be `yes` or `no`

## Dataset Description and its Attributes

This dataset has the data ordered by date (from May 2008 to November 2010)
dataset info - dataset has 41188 entries and 20 columns 

Input variables:
#### Bank client data:
1. - Age : Age
2. - job : Type of Job 
3. - marital : marital status
4. - education 
5. - default: has credit in default?
6. - balance: average yearly balance, in euros  
7. - housing: has housing loan? 
8. - loan: has personal loan? 
#### Related with the last contact of the current campaign:
9. - contact: contact communication type 
10. - day: last contact day of the month 
11. - month: last contact month of year 
12. - duration: last contact duration, in seconds 
#### Other attributes:
13. - campaign: number of contacts performed during this campaign and for this client 
14. - pdays: number of days that passed by after the client was last contacted from a previous campaign 
15. - previous: number of contacts performed before this campaign and for this client
16. - poutcome: outcome of the previous marketing campaign 

#### Output variable (desired target):
17. - y - has the client subscribed a term deposit? (binary: "yes","no")

## Here will be using AWS Services to deploy our Web-Application into production server
### Services Used 

![alt text](<src/AWS Deploy cycle.png>)

1. Amazon CodeCommit 
2. Amazon CodeBuild 
3. Amazon CodeDeploy 
4. Amazon CodePipeline 
5. Amazon (Simple Storage Service) S3 Bucket
6. Amazon CloudWatch Events now called EventBridge
7. AWS Key Management Service (AWS KMS)

## Workflow 
In summary, the solution has the following workflow:

1. A change or commit to the code in the CodeCommit application repository triggers CodePipeline with the help of a EventBridge event.
2. The pipeline downloads the code from the CodeCommit repository, initiates the Build and Test action using CodeBuild, and securely saves the built artifact on the S3 bucket.
3. This solution uses CodeBuild to build and test the code. CodeBuild in AWS is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready for deployment. A `buildspec` is a collection of `build commands` and related settings, in `YAML format`, that CodeBuild uses to run a build

4. CodeDeploy 

* Create EC2 with IAM roles attached (S3) with tags assigned 
* Create application on code deploy 
* push code revision to s3 bucket 
* create deployment group and validate code deploy agent installed with SSM 
* deploy the application to EC2 instances 

* We have to give the access of the S3READONLY to the IAM user , so that it can read from the s3 and we will be creating multiple instances , and by connecting to every instances CLI we will be running some commands to install and check whether it is working , by doing this or by running the commands we will be running the code deploy agents 
Now this code deploy agent will be having direct connection to the s3 bucket 
Code deploy agent will be installed in each of the EC2 instances 

We will be creating `s3 bucket` with `versioning enabled` 

Now to say that for which set of instances we will be deploying the code , for that we will be configuring the deployment group and them we will be pushing the code version to the deployment group 

code deploy agent will be communicating with the code deploy services, code deploy agent updates the code deploy service the status of the code and ec2 instance

Whenever any new request comes to the code deploy service , this request will be passed to the code deploy agent\
Now let us assume we have pushed new version code to the repository (it could be an s3 bucket) then this code deploy service is going to initiate the request . Once the request is issued the code deploy agent within every ec2 instance will pick the latest version code from the s3 bucket. And then we will be performing the deployment on each of the instances 
