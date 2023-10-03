# LLM Multi Model Querying System 🥳


<img src="https://olilo.ai/images/logo.png" alt="mypy logo" width="130px"/>

We are unlocking the power of different large language models, and you can compare the output for the same input prompt.

This is an OpenSource Project with the folling language model support added.

* GPT4
* LLAMA2[^1]
* StableLM[^1]
* PalM2

This repository is intended as a minimal example and a working demo is hosted at [Olilo LLM](https://llms.olilo.ai/) 


## 🌆 Screenshot
![Screenshot](/screencast.gif)

## 🚀 Every Model Runs in Parallel (Faster)

```python
with ThreadPoolExecutor() as executor:                    
      # Start the threads for each model
      futures = [executor.submit(model.interact, prompt) for model in models]
      # Retrieve and display the results
      for i, future in enumerate(as_completed(futures)):
          progress.progress((i+1)/len(models))
          cols[i].write(future.result(), unsafe_allow_html=True)
```

## </> Simple abstract class interface for all models
```python
from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def interact(self, prompt):
        pass
  
    @abstractmethod
    def getName(self):
        pass
```

## ☰ Separate File / Class for each models
``` python
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
```

## 🛠️ Installation Steps

### Clone the Git Repo
```bash
git clone git@github.com:oliloai/llms.git
cd llms

```

### Edit ENV file and add API KEYS
```bash
cp .env.example .env
nano .env 
```

### Install PIP Packages

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

## Recommended Virtual Environment for PIP
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```


[^1]: Used replicated.com service for this.

