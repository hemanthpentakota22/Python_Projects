'''
Programming Assignent 27th JanCreate driver.json file, which consist of
driver.json
{
"app": [{
"program": "sqlWorldCup.sql",
"argument": ""
},
 {
 "program": "MaxProductOfThree.py",
 "argument": ""
}
 ]
}Based on the Configuration in driver.json your program will execute.
Write ShellScript/Python script to read and execute the program.
'''
import json
import os


f = open('driver.json')
data = json.load(f)
for i in range(len(data['app'])):
    k=data['app'][i]['program']
    os.system('python {}'.format(k))

