FROM ubuntu:14.04

RUN apt-get update && \
    apt-get -y install openssh-server \
                       python-pip \
                       python-virtualenv \
                       nano vim \
                       build-essential python-dev && \
    apt-get clean

COPY run.sh /usr/local/bin/eve-workshop.sh

CMD /usr/local/bin/eve-workshop.sh
