import json
import csv
from pprint import pprint

#try:
#customer_data_questions = "questions":[{"id":"listimage_W4p6_choice","question":"From what kind of device did you place your order?","field_id":46723636},{"id":"group_KO2t","question":"How would you rate our online store, based on...","field_id":46723634}, ..}]
#customer_data_answers = "answers":{"listimage_W4p6_choice":"Smartphone","rating_wYTo":"5","opinionscale_BNVc":"10","textarea_By2g":"Very good","email_NfJm":"pat.ainkaran@gmail.com"}}, .. 

with open('C:/Users/Administrator/Documents/1-Python/CustFeedback.json', encoding='utf-8') as customer_data:


      customer_parsed = json.loads(customer_data.read())
      
      cust_data_questions = customer_parsed['questions']
      print(cust_data_questions)

      print(type(cust_data_questions))
      
      cust_data_answers = customer_parsed['responses'][1]['answers']
      print(cust_data_answers)

      print(type(cust_data_answers))

      # open a file for writing

      customer_response_data = open('C:/Users/Administrator/Documents/1-Python/customer_response.csv', 'w')

      # create the csv writer object

      csvwriter = csv.writer(customer_response_data, delimiter = ',')

      count = 0

      for custQ in cust_data_questions:
            for custA in cust_data_answers:

                  if count == 0:

                        headerQ = custQ.keys()
                        #headerA = custA.keys()

                        headerlistQ = list(headerQ)
                        headerlistA = custA

                        #sortedheaderlist = list(header)
                        #sortedheaderlist = sorted(headerlist)

                        print(headerlistQ[0])
                        print(headerlistQ[1])
                        print(headerlistQ[2])

                        print(headerlistA)
                        #print(headerlistA[1])
                        #print(headerlistA[2])


                        #if (headerlistQ[0] == headerlistA[0]):
                        csvwriter.writerow(headerlistQ[0])
                        #if (headerlistQ[1] == headerlistA[1]):
                        csvwriter.writerow(headerlistQ[1])
                        #if (headerlistQ[0] == headerlistA[2]):
                        csvwriter.writerow(headerlistQ[2])

                        #csvwriter.writerow(headerlistA[0])
                        #csvwriter.writerow(headerlistA[1])
                        #csvwriter.writerow(headerlistA[2])
                        #csvwriter.writerow(headerlistA[3])
                        #csvwriter.writerow(headerlistA[4])
                        #csvwriter.writerow(headerlistA[5])
                        #csvwriter.writerow(headerlistA[6])
                        #csvwriter.writerow(headerlistA[7])
                        #csvwriter.writerow(headerlistA[8])
                        #csvwriter.writerow(headerlistA[9])
                        #csvwriter.writerow(headerlistA[10])
                        #csvwriter.writerow(headerlistA[11])
                        #csvwriter.writerow(headerlistA[12])

                        count += 1

                  print(type(custQ.values()))
                  print(type(custA))
                  valueslistQ = list(custQ.values())
                  #valueslistA = custA.values()

                  #valueslist.pop(0)
                  #valueslist.pop()
                  
                  print(type(valueslistQ))
                  #print(type(valueslistA))
                  
                  #newvalueslist = [s for s in valueslist if s.isdigit()]
                  
                  #sortedvalueslist = sorted(valueslist)
                  #print(type(valueslist))

                  print(valueslistQ)
                  #print(valueslistA)
                  

                  csvwriter.writerow([valueslistQ[0]])
                  csvwriter.writerow([valueslistQ[1]])
                  csvwriter.writerow([valueslistQ[2]])
                                 
                  #if any(row[key] in ('NaN', "")

                  csvwriter.writerow(custA.values())
                        
                  """if (valueslistA != ""):
                        csvwriter.writerow([valueslistA[1]])
                  else:
                        csvwriter.writerow("NaN")
                  if (valueslistA != ""):
                        csvwriter.writerow([valueslistA[2]])
                  else:
                        csvwriter.writerow("NaN")
                  """                                           
                  
customer_response_data.close()   
