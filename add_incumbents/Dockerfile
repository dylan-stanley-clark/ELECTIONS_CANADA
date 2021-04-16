FROM python:3-alpine

RUN pip3 install pandas

ADD . /CED/add_incumbents
WORKDIR /CED/add_incumbents

ENTRYPOINT ["python3", "-m", "main"]
