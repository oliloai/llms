from models.model_interface import ModelInterface
import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as palm
palm_api_key = os.getenv("PALM_API_KEY")
palm.configure(api_key=palm_api_key)

class ModelPalM2(ModelInterface):
    def interact(self, prompt):
        
        print('Loading PalM2...')
        try:
            completion = palm.generate_text(
                model="models/text-bison-001",
                prompt=prompt,
                temperature=1,
                max_output_tokens=28000,
            )

            print("PalM2:",completion.result)
            return "<h3>PalM2</h3>" + completion.result
        except KeyError:
            return "No result"
        except Exception as e:
            return f"An error occurred: {e}"
    
    def getName(self):
        return "PalM2"