FROM centos:latest
MAINTAINER Miguel Chenge "chenge97@gmail.com"

USER root

RUN dnf -y install gcc openssl-devel bzip2-devel libffi-devel && cd /opt && yum -y install wget && wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && tar xzf Python-3.7.9.tgz && cd Python-3.7.9 && ./configure --enable-optimizations && yum -y install make && make altinstall && yum -y install epel-release && curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py && python3.7 get-pip.py

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3.7" ]

CMD [ "runapp.py" ]

