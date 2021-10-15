FROM centos:latest
MAINTAINER Miguel Chenge "chenge97@gmail.com"

USER root

RUN dnf -y install gcc openssl-devel bzip2-devel libffi-devel && cd /opt && yum -y install wget && wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && tar xzf Python-3.7.9.tgz && cd Python-3.7.9 && ./configure --enable-optimizations && yum -y install make && make altinstall && rm Python-3.7.9.tgz

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "runapp.py" ]

