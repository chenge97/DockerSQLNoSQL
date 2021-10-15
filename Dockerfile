FROM centos8
MAINTANER Miguel Chenge "chenge97@gmail.com"

USER root

RUN sudo dnf install gcc openssl-devel bzip2-devel libffi-devel && cd /opt && wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz && tar xzf Python-3.7.9.tgz && cd Python-3.7.9
&& sudo ./configure --enable-optimizationsv && sudo make altinstall && sudo rm Python-3.7.9.tgz

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "runapp.py" ]

