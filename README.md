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

1. CodeCommit 
2. CodeBuild 
3. CodeDeploy 
4. CodePipeline 

