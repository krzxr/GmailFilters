# Productivity Project: Generate Gmail Filters

## Problem Statement

Our inbox contains too many unorganized email, and to remedy that, we can add labels to our emails. However, gmail label UI is not very user friendly: 

(1) Its location is not very accessible. It is in Setting - See All Settings - Filters and Blocked Addresses. 

(2) Gmail supports filtering the following properties: from, to, subject, hasTheWord, doesNotHaveTheWord. However, these properties 
are related in an AND relationship. That means that creating a filter with from "emailX" or contains the word "Y" requires two separate rules. That also makes 
creating a filter to add from emailX or to emailY or contains word Z a lot of works - we need 3 separate rules. 

The above problems call for a simpler way of creating filter rules. The goal of this tool is to

(1) Make accessing filter editor a one time event.

(2) Make creating a filter for a label whose property are in OR relationship easy

## User Guide
(0) Installed Python3 and pandas.

(1) Open emailFiltersInput.csv and make approperiate changes.

 - To include a phrase, we can use ( ) - EX: to include emails containg the phrase "X Y", we use (X Y), and put it under hasTheWord.
   
 - To include multiple words, we can use OR - EX: to include emails containing the word "X" or the word "Y", we put (X) OR (Y) under hasTheWord.
 
 - More info see: https://support.google.com/mail/answer/7190?hl=en
   
(2) Run "python3 generateGmailFilters.py"  

(3) The result is in emailFilters.xml. 

(4) Open Gmail. We import emailFilters.xml to "Setting - See All Settings - Filters and Blocked Addresses". After importing the rules, we can 
click "Apply new filters to existing email" to apply the rules to existing files. 

Note: The emailFiltersInput.csv and emailFilters.xml contain examples of inputs and outputs, respectively.

