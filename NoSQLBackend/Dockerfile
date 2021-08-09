FROM python:3.8-slim
WORKDIR /NOSQLBACKEND
COPY . /NOSQLBACKEND
# to install the requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
RUN cd /usr/local/bin
RUN aws configure set aws_access_key_id "AKIA5J7ASQOTBFK2DCAA"
RUN aws configure set aws_secret_access_key "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"
RUN aws configure set default.region "ap-south-1"
CMD ["python3", "app.py"]