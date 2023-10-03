from models.model_interface import ModelInterface
import replicate
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")
pre_prompt=""
class ModelLLAMA2(ModelInterface):
    
    
    def interact(self, prompt):
        
        print('Loading LLAMA2...')
        try:
            output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                            input={"prompt": f"{pre_prompt} {prompt}", # Prompts
                            "temperature":0.1, "top_p":0.9, "max_length":24096, "repetition_penalty":1})  # Model parameters


            full_response = ""

            for item in output:
                full_response += item

            print("LLAMA2:",full_response)
            return "<h3>LLAMA2</h3>" +full_response
        
        except KeyError:
            return "No result"
        except Exception as e:
            return f"An error occurred: {e}"
    
    def getName(self):
        return "LLAMA2"