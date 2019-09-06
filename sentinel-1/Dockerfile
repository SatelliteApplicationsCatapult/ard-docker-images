FROM continuumio/miniconda3:4.7.10

LABEL maintainer="Luigi Di Fraia"

RUN conda install --quiet --yes \
    boto3 \
    geopandas \
    pyyaml \
    rasterio \
    && conda clean --all -f -y

RUN pip install --no-cache-dir \
    redis

RUN wget --quiet http://step.esa.int/downloads/7.0/installers/esa-snap_sentinel_unix_7_0.sh && \
    /bin/sh ./esa-snap_sentinel_unix_7_0.sh -q && \
    rm ./esa-snap_sentinel_unix_7_0.sh && \
    ./snap/bin/snap --nosplash --nogui --modules --update-all -q

# ------------------------------------------

COPY utils /utils

COPY worker.py /worker.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker.py" ]

# ------------------------------------------

#RUN conda install --quiet --yes \
#    jupyter \
#    && conda clean --all -f -y && \
#    mkdir /opt/notebooks

#COPY utils /opt/notebooks/utils

#COPY rediswq.py /opt/notebooks

#COPY worker.ipynb /opt/notebooks

#CMD jupyter notebook \
#    --allow-root \
#    --notebook-dir=/opt/notebooks \
#    --NotebookApp.ip='0.0.0.0' \
#    --NotebookApp.port='8888' \
#    --NotebookApp.token='secretpassword' \
#    --NotebookApp.open_browser='False'
