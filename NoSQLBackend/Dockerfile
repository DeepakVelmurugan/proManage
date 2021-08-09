FROM python:3.8-slim
WORKDIR /NOSQLBACKEND
COPY . /NOSQLBACKEND
# to install the requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
RUN cd /usr/local/bin
RUN aws configure set aws_access_key_id ""
RUN aws configure set aws_secret_access_key ""
RUN aws configure set default.region "ap-south-1"
CMD ["python3", "app.py"]