"""
This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

You can also change the default language your pads are created with
in your account settings: https://coderpad.io/settings

Enjoy your interview!
"""

"""
Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn" instead.
"""

def sol(n):
    for i in xrange(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            print("LinkedIn")
        elif i % 4 == 0:
            print("Linked")
        elif i % 6 == 0:
            print("In")
        else:
            pass

def parser(file, fields):
    dic = {}
    res = ["minute, number_of_messages"]
    
    with open(file, r) as f:
        for line in f:
            L = line.split()
            key = L[:3][:-3]
            log = L[5:]
            
            i = 0
            while i < len(log):
                if i not in "":
                    break
                i += 1
            process_name = log[:i]
            
            
            if key not in dic:
                dic[key] = { total_count: 0}
            else:
                dic[key]["total_count"] += 1
                dic[key][process_name] = dic[key].get(process_name, 0) + 1
            
                
             
                
            
            
            dic[key] = dic.get(key, 0) + 1

    sdic = sorted(dic.items())
    
    for k, v in sdic:
        line = k + "," + str(v)
        res.append(line)
    
    return res

def countOccurences(log, s):
    pass
            
"""
Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information The employee information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:
  - 'name'  refers to a String that contains the employee's first and last name
  - 'title' refers to a String that contains the employee's job title
  - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.
 
-----------Begin Sample Output--------------
Flynn Mackie - Senior VP of Engineering
  Wesley Thomas - VP of Design
    Randall Cosmo - Director of Design
      Brenda Plager - Senior Designer
  Nina Chiswick - VP of Engineering
    Tommy Quinn - Director of Engineering
      Jake Farmer - Frontend Manager
        Liam Freeman - Junior Software Engineer
      Sheila Dunbar - Backend Manager
        Peter Young - Senior Code Cowboy
-----------End Sample Output--------------
"""

import requests, json
from collections import deque
def sol(eid):
    data = getData(eid)
    reports = data["reports"]
    
    d = deque()
    
    for report in reports:
        d.appendleft([report, 1])
    
    res = []
    res.append(data['name'] + " - " + data['title'])
    
    while d:
        cur, dep = d.pop()
        d = getData(cur)
        while len(res) <= dep:
            res.append([])
        
        line = " " * dep + cur['name'] + " - " + cur['title']
        res[dep].append(line)
        
        cureids = cur['reports']
        for eid in cureids:
            d.appendleft([eid, dep + 1])
    
    return res
        


def getData(eid):
    url = "http://www.linkedin.corp/api/employee/" + eid
    resp = requests.get(url=url)
    return json.loads(resp.text)
    
