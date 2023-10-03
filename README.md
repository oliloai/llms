# LLM Multi Model

![Olilo Logo](https://olilo.ai/images/logo.png)

We are unlocking the power of different large language models, and you can compare the output for the same input prompt.

This is an PpenSource Project with the folling language model support added.

* GPT4
* LLAMA2[^1]
* StableLM[^1]
* PalM2

This repository is intended as a minimal example to load [Olilo LLM](https://llms.olilo.ai/) 

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

## Recommended Virtual Environment for PIP
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

[^1]: Used replicated.com service for this.

