# # read operation
# with open('file.txt','r') as file:
#     content=file.read()
#     print(content)
    
# # write operation    
# with open('file.txt','w') as file:
#    file.write('hi hello')    
   
# get environment variable
# from dotenv import load_dotenv
# import os

# load_dotenv()  # This loads the .env file
# # db_user = os.getenv('DB_USER')
# # print(db_user)

# # set environment variable 
# os.environ["DB_USER"]='12345'
# print(os.environ['DB_USER']) 

# #subprocess
# import subprocess
# result=subprocess.run(['ls','l'],capture_output=True,text=True)
# print(result.stdout)

# # api request
# import requests
# response=requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(response.json())

# #json handling read
# import json
# with open('data.json','r') as file:
#     data=json.load(file)
#     print(data)

# # json write
# data={'name':'Devops','type':'Workflow'}
# with open('data.json','w') as file:
#     json.dump(data,file,indent=4)

# #work with databases
# import dynamoDB
# connect=dynamoDB.connect('myz-table')

# #docker integration
# import docker
# client=docker.from_env()
# containers=client.containers.list()
# for container in containers:
#     print(container.name)
    
# #yml file
# import yaml
# with open('file.yml','r') as file:
#     config=yaml.safe_load(file)
#     print(config)
# with open('file.yml','w') as file:
#     config=yaml.safe_dump(file)
#     print(config)    
  
#  monitoring
import psutil
print(f"cpu usage :{psutil.cpu_count()}%")
print(f"memory usgae:{psutil.virtual_memory().percent}%")

