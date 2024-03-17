
FROM sequenceiq/pyspark:2.4.0

# Install dependencies for Python 
USER root
RUN yum install -y which make
RUN pip install jupyter matplotlib pandas scikit-learn

# Set up environment variables for Hadoop and PySpark
ENV HADOOP_HOME /usr/local/hadoop
ENV PYSPARK_PYTHON python3
ENV PATH $PATH:$HADOOP_HOME/bin

# Copy  files into the Docker image
COPY ingestion /app/ingestion
COPY scripts /app/scripts
COPY shell_scripts /app/shell_scripts
COPY PysparkPreprocessing.ipynb /app/PysparkPreprocessing.ipynb

COPY Makefile /app/Makefile

WORKDIR /app

# Expose port for Jupyter Notebook and Hadoop
EXPOSE 8888 9870 8088

RUN chmod +x /app/shell_scripts/*.sh

# Start-up script to initialize Hadoop, run Jupyter Notebook, or other commands
CMD ["sh", "-c", "service ssh start; $HADOOP_HOME/sbin/start-dfs.sh; $HADOOP_HOME/sbin/start-yarn.sh; jupyter notebook --allow-root --ip='0.0.0.0' --NotebookApp.token='' --NotebookApp.password=''"]
