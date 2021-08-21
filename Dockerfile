FROM python:3.9

WORKDIR /python/app

ARG aws_access_key_id

ARG aws_secret_access_key

ENV AWS_ACCESS_KEY_ID=${aws_access_key_id}

ENV AWS_SECRET_ACCESS_KEY=${aws_secret_access_key}

RUN echo $AWS_ACCESS_KEY_ID

RUN echo $AWS_SECRET_ACCESS_KEY

COPY main.py .

RUN pip install --upgrade pip && pip install boto3

CMD ["/"]

ENTRYPOINT ["python3","main.py"]


