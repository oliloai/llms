# olilomulti
Run with multi model llm

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