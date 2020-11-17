FROM python:3.6

# Create app directory
WORKDIR /app

ENV port_expose=4444
ENV host_db="127.0.0.1"
ENV port_db=3306
ENV user_db=""
ENV pass_db=""
 
# Install app dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt
# Bundle app source
COPY src /app
EXPOSE 4444
CMD [ "python3", "exporter.py" ]
