FROM python:3.12

# Make directories suited to your application
RUN mkdir -p /home/docker_test
WORKDIR /home/docker_test

# Copy and install requirements
COPY prod.in /home/docker_test/prod.in
RUN pip install pip-tools
RUN pip-compile /home/docker_test/prod.in
RUN pip-sync /home/docker_test/prod.txt

# Copy contents from your local to your docker container
COPY ./api /home/docker_test/api
