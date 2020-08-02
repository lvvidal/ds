FROM puckel/docker-airflow:latest

USER root

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        openssh-server \
        openssh-client \
        vim \
        nmon \
        bwm-ng \
        htop \
        netcat \
        telnet \
        net-tools \
    && pip install --upgrade pip \
    && pip install \
        boto3 \
        awscli \
        hurry.filesize \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man  \
        /usr/share/doc \
        /usr/share/doc-base

COPY ./requirements.txt /requirements.txt
COPY ./airflow.cfg /usr/local/airflow
COPY ./postgres_conn.py /postgres_conn.py
COPY ./entrypoint.sh /entrypoint.sh

RUN pip install -r /requirements.txt

RUN ln -s /usr/local/airflow /home/airflow

ARG AIRFLOW_USER_HOME=/usr/local/airflow

ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

RUN chown -R airflow: ${AIRFLOW_USER_HOME}
RUN chmod +x /entrypoint.sh

USER airflow

ENTRYPOINT ["/entrypoint.sh"]

CMD ["webserver"]





