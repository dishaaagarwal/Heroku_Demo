# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:45:39 2020

@author: This PC
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())