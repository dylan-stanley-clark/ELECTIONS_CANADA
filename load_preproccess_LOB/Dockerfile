FROM python:3-alpine

RUN pip3 install pandas

ADD . /CED/load_preproccess_LOB
WORKDIR /CED/load_preproccess_LOB/src

ENTRYPOINT ["python3", "-m", "main"]
