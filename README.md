# SmartLab
---
[![Build Status](https://travis-ci.org/Bye-lemon/SmartLab.svg?branch=master)](https://travis-ci.org/Bye-lemon/SmartLab)
[![codebeat badge](https://codebeat.co/badges/ccfe67ae-b831-411c-9779-bb2cee86d557)](https://codebeat.co/projects/github-com-bye-lemon-smartlab-master)
![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)


This repository contains files necessary for building a Docker image of Nginx + Gunicorn + Flask.


### Base Docker Image

* [python](https://hub.docker.com/_/python/)


### Installation

1. Install Docker.

```bash
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get -y update
sudo apt-get -y install docker-ce
```

2. Install Docker-compose:

```bash
sudo -i
curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

3. Build :

```bash
sudo mkdir -p /etc/docker
sudo vim /etc/docker/daemon.json
{
  "registry-mirrors": ["https://8jlc7x0d.mirror.aliyuncs.com"]
}
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo docker build -t smartlab:latest .
```

### Usage

```bash
# start service
sudo docker-compose up
# stop service
sudo docker-compose down
```

After few seconds, open `http://<host>` to see the Flask app.
