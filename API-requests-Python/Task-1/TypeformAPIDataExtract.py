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

        count = 0

        for custQ in cust_data_questions:

                #countA = 0
                for custA in cust_data_answers:

                        if count == 0:

                                headerQ = custQ.keys()
                                headerA = custA.keys()

                                headerlistQ = list(headerQ)
                                headerlistA = list(headerA)
                               
                                sortedheaderlistQ = sorted(headerlistQ)
                                sortedheaderlistA = sorted(headerlistA)

                                print(sortedheaderlistQ[1])
                                #print(sortedheaderlistQ[1])
                                #print(sortedheaderlistQ[2])

                                #print(sortedheaderlistA[0])
                                #print(sortedheaderlistA[1])
                                #print(sortedheaderlistA[2])
                                
                                #csvwriter.writerow(sortedheaderlistQ[0])
                                #csvwriter.writerow(sortedheaderlistQ[1])
                                #csvwriter.writerow(sortedheaderlistQ[2])                        

                        count += 1                        

                        #print(type(custQ.values()))
                        #print(type(custA.values()))                  

                        valueslistQ = list(custQ.values())
                        valueslistA = list(custA.values())
                  

                        #valueslist.pop(0)
                        #valueslist.pop()
                  
                  
                        #print(type(valueslistQ))
                        #print(type(valueslistA))
                  
                  
                        #newvalueslist = [s for s in valueslist if s.isdigit()]
                  
                        #sortedvalueslist = sorted(valueslist)
                        #print(type(valueslist))                                 

                  
                        #for k, v in cust_data_questions.items():
                        #print(k, v)                         
                        #print(v)                  
                          
                        #if (valueslistQ[count] == k):
                                #d=csvwriter.writerow([value])
                        #else:
                                #csvwriter.writerow(["NaN"])  
                  
                        csvwriter.writerow([valueslistQ[0]])
                        csvwriter.writerow([valueslistQ[1]])
                        csvwriter.writerow([valueslistQ[2]])                 

                        #csvwriter.writerow([valueslistA[0]])
                        #csvwriter.writerow([valueslistA[1]])
                        #csvwriter.writerow([valueslistA[2]])
                                 
                        #if any(row[key] in ('NaN', "")

                        #csvwriter.writerow(headerlistA.values())                        

                        #print(sortedheaderlistQ[1])
                        #print(valueslistQ[1])

                        #print(sortedheaderlistA[len(custQ)])
                        #print(valueslistA[len(custQ)])

                        #print(len(cust_data_questions))
                        #print(len(custQ))

                        #print(len(custA))
                  
                        #rex1  = re.compile('(?<=\'rating_wYTo\': \")[a-zA-Z_\- ]+(?=\")')
                        #rex1  = re.compile('rating_wYTo:')
                        #rex2 = rex1.findall(customer_data.read())  
                        #print(rex2)                 
                                  

                        #a=sorted(list(cust_data_questions['responses'][0]['answers'].keys()))
                        #a=sorted(list(cust_data_answers.keys()))

                        #print(sortedheaderlistA[0])
                        #print(customer_parsed['questions'][12]['id'])
                        #print(sorted(valueslistA))
                
                        #for i in cust_data_questions:
                        for key,value in customer_parsed['responses'][1]['answers'].items():                                                                                 

                                #print(customer_parsed['responses'][1]['answers'].items())
                                #print(cust_data_questions[i]['id'])                                                                         
                                                                
                                #print(customer_parsed['questions'][0]['id'])
                                #print(key,value)
                                if (customer_parsed['questions'][12]['id'] == sortedheaderlistA[0]):                                        
                                        csvwriter.writerow([valueslistA[0]])
                                        #print(valueslistA[4])
                                        #print(key)
                                        print(value)                          
                                else:
                                        csvwriter.writerow(["NaN"])
  
customer_response_data.close()
