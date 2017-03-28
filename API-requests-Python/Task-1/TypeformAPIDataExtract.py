'''
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html
https://docs.python.org/3/tutorial/datastructures.html
http://stackoverflow.com/questions/33308538/how-to-extract-specific-multiple-values-in-json-using-python
https://www.codecademy.com/ja/courses/python-intermediate-en-6zbLp/0/4?curriculum_id=50ecb8cb058fd2ebda00003b
https://www.youtube.com/watch?v=uYlgOFsnxEk
https://github.com/ainkaran/repo/blob/master/API-requests-Python/Task-1/TypeformAPIDataExtract.py

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
-have to remove 'id' and 'field_id' from questions object (in JSON), DONE
-have to fix the code to remove the duplicate response value from the table, DONE
-have an issue matching a correct answer (value) to each question (value), DONE
--a final table (.csv)
-have to pivot rows into columns, DONE, there could be other way we can display the questions and answers in a table 

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
                   

        #print(type(customer_parsed['questions'][0]))
        #print(type(customer_parsed['responses'][1]['answers']))

        #print(customer_parsed['questions'][1])
        #print(customer_parsed['responses'][1]['answers'])


        questions = customer_parsed['questions'][0]
        #answers = customer_parsed['responses'][1]['answers']

        answers = customer_parsed['responses']

        #print(type(answers))
        #print(len(answers))

        #print(answers)
                
        for i in range(len(cust_data_questions)):

                questions = customer_parsed['questions'][i]
                #print(questions['id'])
                #print(customer_parsed['questions'][i]['question'])
                #print(answers[questions['id']][i])
                                    
                array = []

                #print(range(len(answers)))

                for j in range(len(answers)):

                        #print(list(answers))
                        #print(customer_parsed['responses'])

                        #print(answers[j]['answers'].get(questions['id']))
                        #print(questions['id'] in answers[j]['answers'])

                        if questions['id'] in answers[j]['answers']:
                                #print(customer_parsed['questions'][i]['question'])                        
                                #print(answers[j]['answers'].get(questions['id']))

                                #print(answers[j]['answers'])

                                q1 = customer_parsed['questions'][i]['question']                        
                                a1 = answers[j]['answers'].get(questions['id'])
                                
                                array.append(q1)
                                array.append(a1)
                                #print(array)
                                
                                #csvwriter.writerow([customer_parsed['questions'][i]['question']])
                                #csvwriter.writerow([answers[questions['id']]])
                        elif len(answers[j]['answers']) != 0:
                                #print(customer_parsed['questions'][i]['question'])
                                #print('NaN')
                                print(answers[j]['answers'])

                                q2 = customer_parsed['questions'][i]['question']                        
                                a2 = ['NaN']                        
                                
                                array.append(q2)
                                array.append(a2)
                                #print(array)

                                #csvwriter.writerow([customer_parsed['questions'][i]['question']])
                                #csvwriter.writerow(['NaN'])

                csvwriter.writerow(array)
                
  
customer_response_data.close()
