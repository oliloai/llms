import openai
import os
from models.model_interface import ModelInterface

from dotenv import load_dotenv
load_dotenv()
pre_prompt=""

#get key from dotenv
openai.api_key = os.getenv("OPENAI_API_KEY")
class ModelOPENAI(ModelInterface):
   
    def interact(self, prompt):
        print('Loading ChatGPT...')
        try:
            response = openai.ChatCompletion.create(
                  model="gpt-4",
                  messages=[
                      {"role": "system", "content": pre_prompt},
                      {"role": "user", "content": prompt}
                  ]
            )
            print ("ChatGPT:",response["choices"][0]["message"]["content"])
            return "<h3>ChatGPT4</h3>" +response["choices"][0]["message"]["content"]
        except KeyError:
            return "<h3>ChatGPT4</h3>" +"No result"
        except Exception as e:
            return f"An error occurred: {e}"
        
    def getName(self):
        return "CHATGPT4"