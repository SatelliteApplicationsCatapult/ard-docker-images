FROM continuumio/miniconda3:4.8.2

LABEL maintainer="Luigi Di Fraia"

RUN conda update conda --quiet --yes \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN conda install --quiet --yes \
    boto3 \
    geopandas \
    pip \
    pyyaml \
    rasterio \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN pip install --no-cache-dir \
    google-cloud-storage \
    asynchronousfilereader \
    redis \
    sentinelsat
	
RUN wget --quiet http://step.esa.int/thirdparties/sen2cor/2.5.5/Sen2Cor-02.05.05-Linux64.run && \
    /bin/sh ./Sen2Cor-02.05.05-Linux64.run && \
    rm ./Sen2Cor-02.05.05-Linux64.run	

#RUN apt-get install -y --no-install-recommends xmlstarlet && \
#    rm -rf /var/lib/apt/lists/*

#RUN xmlstarlet edit -L -u "//Downsample_20_to_60" -v "FALSE" $HOME/sen2cor/2.8/cfg/L2A_GIPP.xml

# ------------------------------------------

COPY workflows/utils /utils

COPY worker-s2.py /worker-s2.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker-s2.py" ]

