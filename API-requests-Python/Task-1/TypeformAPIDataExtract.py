'''
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html

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

#customer_response_data = open('C:/Users/Administrator/Documents/1-Python/customer_response.csv', 'w')
#csvwriter = csv.writer(customer_response_data, delimiter = ',')        



#u = urlopen('https://api.typeform.com/v1/form/cZGxu9?key=e7bb023ae21d04db5cd517fb6829ef979697a5e7')
response = json.loads(webpage.read().decode('utf-8'))

#pprint(response)

typeform_data = open('C:/Users/Administrator/Documents/1-Python/CustFeedback.json', 'w')

json.dump(response, typeform_data)

typeform_data.close() 
        


#customer_data_questions = "questions":[{"id":"listimage_W4p6_choice","question":"From what kind of device did you place your order?","field_id":46723636},{"id":"group_KO2t","question":"How would you rate our online store, based on...","field_id":46723634}, ..}]
#customer_data_answers = "answers":{"listimage_W4p6_choice":"Smartphone","rating_wYTo":"5","opinionscale_BNVc":"10","textarea_By2g":"Very good","email_NfJm":"pat.ainkaran@gmail.com"}}, .. 

with open('C:/Users/Administrator/Documents/1-Python/CustFeedback.json', encoding='utf-8') as customer_data:


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

      customer_response_data = open('C:/Users/Administrator/Documents/1-Python/customer_response.csv', 'w')

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

                        #print(sortedheaderlistQ[0])
                        #print(sortedheaderlistQ[1])
                        #print(sortedheaderlistQ[2])

                        #print(sortedheaderlistA[0])
                        #print(sortedheaderlistA[1])
                        #print(sortedheaderlistA[2])
                        
                        '''
                        #csvwriter.writerow(sortedheaderlistQ[0])
                        #csvwriter.writerow(sortedheaderlistQ[1])
                        #csvwriter.writerow(sortedheaderlistQ[2])
                        '''

                        count += 1
                        

                  '''
                  #print(type(custQ.values()))
                  #print(type(custA.values()))
                  '''

                  valueslistQ = list(custQ.values())
                  valueslistA = list(custA.values())
                  

                  #valueslist.pop(0)
                  #valueslist.pop()
                  
                  '''
                  #print(type(valueslistQ))
                  #print(type(valueslistA))
                  '''
                  
                  #newvalueslist = [s for s in valueslist if s.isdigit()]
                  
                  #sortedvalueslist = sorted(valueslist)
                  #print(type(valueslist))
                                 

                  
                  for k, v in cust_data_questions.items():
                          print(k, v)
                          
                          
                  #print(v)
                  
                          
                          #if (valueslistQ[count] == k):
                                  #d=csvwriter.writerow([value])
                          #else:
                                  #csvwriter.writerow(["NaN"])  
                  
                  a=csvwriter.writerow([valueslistQ[0]])
                  b=csvwriter.writerow([valueslistQ[1]])
                  c=csvwriter.writerow([valueslistQ[2]])

                  
                  

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

                  '''
                  #rex1  = re.compile('(?<=\'rating_wYTo\': \")[a-zA-Z_\- ]+(?=\")')

                  #rex1  = re.compile('rating_wYTo:')
                  #rex2 = rex1.findall(customer_data.read())  
                  #print(rex2)
                  '''
                                  

                  for key,value in customer_parsed['responses'][1]['answers'].items():
                          
                          #print(key, value)
                  
                          
                          if (valueslistQ[count] == key):
                                  d=csvwriter.writerow([value])
                          #else:
                                  #csvwriter.writerow(["NaN"])               
                               
                              
                  

                  '''
                  if (valueslistA != ""):
                        csvwriter.writerow([valueslistA[1]])
                  else:
                        csvwriter.writerow("NaN")
                  if (valueslistA != ""):
                        csvwriter.writerow([valueslistA[2]])
                  else:
                        csvwriter.writerow("NaN")
                  '''

                  
customer_response_data.close()
