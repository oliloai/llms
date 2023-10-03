# LLM Multi Model

We are unlocking the power of different large language models, and you can compare the output for the same input prompt.

This is an PpenSource Project with the folling language model support added.

* GPT4
* LLAMA2
* StableLM
* PalM2

This repository is intended as a minimal example to load [Olilo LLM]([http://llms.olilo.ai/). 

## Installation Steps

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
