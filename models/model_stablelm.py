from models.model_interface import ModelInterface
import replicate
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")
pre_prompt=""

class ModelStableLM(ModelInterface):
    
    def interact(self, prompt):
        
        print('Loading StableLM...')
        try:
            output = replicate.run('stability-ai/stablelm-tuned-alpha-7b:c49dae362cbaecd2ceabb5bd34fdb68413c4ff775111fea065d259d577757beb', # LLM model
                            input={"prompt": f"{pre_prompt} {prompt}", # Prompts
                            "temperature":0.8, "top_p":0.9, "max_length":24096, "repetition_penalty":1})  # Model parameters


            full_response = ""

            for item in output:
                full_response += item

            print("StableM:", full_response)
            return "<h3>StableLM</h3>" +full_response
        except KeyError:
            return "No result"
        except Exception as e:
            return f"An error occurred: {e}"
    
    def getName(self):
        return "StableLM"