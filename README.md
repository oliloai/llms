# LLM Multi Model

We are unlocking the power of different large language models, and you can compare the output for the same input prompt.

This is an PpenSource Project with the folling language model support added.

* GPT4
* LLAMA2
* StableLM
* PalM2

This repository is intended as a minimal example to load [Olilo LLM]([http://llms.olilo.ai/). 

## Installation Steps

## Install
```bash
git clone git@github.com:sajithamma/olilomulti.git

cd olilomulti

### Edit ENV file
nano .env

Add your API keys


# Server Installation


### edit the service here
sudo nano /etc/systemd/system/llms_olilo.service

### Restart service
sudo systemctl restart llms_olilo.service

###See logs
journalctl -u  llms_olilo.service
