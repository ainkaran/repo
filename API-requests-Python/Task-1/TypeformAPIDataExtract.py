'''
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html
https://docs.python.org/3/tutorial/datastructures.html
http://stackoverflow.com/questions/33308538/how-to-extract-specific-multiple-values-in-json-using-python
https://www.codecademy.com/ja/courses/python-intermediate-en-6zbLp/0/4?curriculum_id=50ecb8cb058fd2ebda00003b

'''
"""
Task #1
Purpose
To display API requests skills in Python

Business requirement
The customer has some marketing responses in Typeform. We need to extract the data in the form of CSV for further use.

Steps
Figure out form available and get submitted responses
Produce a single table which contains all responses. Use NaN in the case of missing response on some questions

Technical details
Omit manual work
Please use Python as your tool, using Requests library is preferred
Submit work and the files via git repository (ideally with a commit history)
Typeform API key: ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d

"""

'''
-This is Python version 3.4.4
-this program will import Customer Responses from Typform site using API request in Python
-CREATED two separate list objects for questions and answers
-CONVERTED dict to list object
-a final table (.csv) 
-have to remove 'id' and 'field_id' from questions object (in JSON)
-have to pivot rows into columns
-have to fix the code to remove the duplicate response value from the table
-have an issue matching a correct answer (value) to each question (value)   

'''

import json
import csv
from pprint import pprint
import re
import urllib.request

try:
        #webpage = urllib.request.urlopen('http://www.google.com')
        webpage = urllib.request.urlopen('https://api.typeform.com/v1/form/cZGxu9?key=e7bb023ae21d04db5cd517fb6829ef979697a5e7')
except:
        print ('Could not access webpage!')

#for line in webpage:
#        print(line)

response = json.loads(webpage.read().decode('utf-8'))

#pprint(response)

typeform_data = open('C:/Users/Administrator/Documents/1-Python/CustFeedback.json', 'w')

json.dump(response, typeform_data)

typeform_data.close()         


#customer_data_questions = {"questions":[{"id":"listimage_W4p6_choice","question":"From what kind of device did you place your order?","field_id":46723636},{"id":"group_KO2t","question":"How would you rate our online store, based on...","field_id":46723634}, ..}]}
#customer_data_answers = "answers":{"listimage_W4p6_choice":"Smartphone","rating_wYTo":"5","opinionscale_BNVc":"10","textarea_By2g":"Very good","email_NfJm":"pat.ainkaran@gmail.com"}}, .. 

with open('C:/Users/Administrator/Documents/1-Python/CustFeedback.json', encoding='utf-8') as customer_data:

        #print(customer_data)

        customer_parsed = json.loads(customer_data.read())
      
        cust_data_questions = customer_parsed['questions']
        #print(cust_data_questions)

        #print(type(cust_data_questions))
        #print(len(cust_data_questions))
      
        cust_data_answers = [customer_parsed['responses'][1]['answers']]
        #print(cust_data_answers)

        #print(type(cust_data_answers))
        #print(len(cust_data_answers))

        # open a file for writing

        customer_response_data = open('C:/Users/Administrator/Documents/1-Python/CustomerResponse.csv', 'w')

        # create the csv writer object

        csvwriter = csv.writer(customer_response_data, delimiter = ',')


        '''
        count = 0

        #for i in (0,1,2,3,4,5):
        #for Qkey,Qvalue in customer_parsed['questions']['question'].items():
        for custQ in cust_data_questions:

                if count == 0:
                        
                        
                        headerQ = custQ.keys()
                        headerlistQ = list(headerQ)
                        sortedheaderlistQ = sorted(headerlistQ)
                        valueslistQ = list(custQ.values())
                        #print(len(cust_data_questions))

                        #count += 1

                        
                        csvwriter.writerow([valueslistQ[0]])
                        csvwriter.writerow([valueslistQ[1]])
                        csvwriter.writerow([valueslistQ[2]])                        
                        

                        
                        some_dict = {1: "Hello", 2: "Goodbye", 3: "You say yes", 4: "I say no"}
                        value_to_remove = "You say yes"
                        key_to_remove = 3

                        some_dict = {key: value for key, value in some_dict.items() if key is not key_to_remove}
                        

                        #print(valueslistQ)
                        
                        #print(customer_parsed)
                        #print(cust_data_questions[1]['id'])
                                                
                        sortedheaderlistQ = sorted(list(customer_parsed['responses'][1]['answers'].keys()))
                        #valueslistQ = sorted(list(customer_parsed['responses'][1]['answers'].values()))

                        
                        #print(customer_parsed['questions'][0].keys())
                        
                        sortedheaderlistA = sorted(list(customer_parsed['responses'][1]['answers'].keys()))
                        valueslistA = sorted(list(customer_parsed['responses'][1]['answers'].values()))

                        #print(sorted(list(customer_parsed['questions'][0].keys()))[0])
                        #print(sorted(list(customer_parsed['questions'][0].values()))[0])
                
                        #for i in cust_data_questions:

                        '''
                        
        for i in range(len(cust_data_questions)):
                for key,value in customer_parsed['responses'][1]['answers'].items():                                                                        

                                        
                        #print(customer_parsed['responses'][1]['answers'].items())
                        #print(cust_data_questions[i]['id'])                                                                         
                                                                        
                        #print(customer_parsed['questions'][0]['id'])
                        #print(key,value)

                                        
                        if (customer_parsed['questions'][i]['id'] == key ):                                        
                                csvwriter.writerow([list(customer_parsed['questions'][i].values())])
                                csvwriter.writerow([value])
                                                       
                                #print([sorted(list(customer_parsed['questions'][0].values())[2])])
                                print(cust_data_questions[0]['id'])
                                #print(key)
                                #print(sortedheaderlistQ)
                                #print(value)
                                #print(valueslistQ)
                        else:
                                csvwriter.writerow([list(customer_parsed['questions'][i].values())])
                                csvwriter.writerow(["NaN"])
                                #print('NaA')
                                #print(key)
                                #print(sortedheaderlistQ)

                                                
  
customer_response_data.close()
