import random
import os
from spot import Keyword_Spotting_Service
import json

file_name = "yes.wav"

def predict():
	"""Endpoint to predict keyword
    :return (json): This endpoint returns a json file with the following format:
        {
            "keyword": "down"
        }
	"""
  

	# instantiate keyword spotting service singleton and get prediction
	kss = Keyword_Spotting_Service()
	predicted_keyword = kss.predict(file_name)

	# we don't need the audio file any more - let's delete it!
	# os.remove(file_name)

	# send back result as a json file
	result = {"keyword": predicted_keyword}
    return  
    
    

if __name__ == "__main__":
    print(result)