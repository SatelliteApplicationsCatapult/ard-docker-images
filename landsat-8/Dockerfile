FROM continuumio/miniconda3:4.7.10

LABEL maintainer="Luigi Di Fraia"

RUN conda install --quiet --yes --freeze-installed \
    boto3 \
    geopandas \
    pyyaml \
    rasterio \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN pip install --no-cache-dir \
    redis 

# ------------------------------------------

#COPY workflows/utils /utils

#COPY worker-ls.py /worker-ls.py

#COPY rediswq.py /rediswq.py

#CMD [ "python", "worker-ls.py" ]

# ------------------------------------------

#RUN conda install --quiet --yes --freeze-installed \
#    jupyter \
#    && conda clean --all -f -y \
#    && find /opt/conda/ -follow -type f -name '*.a' -delete \
#    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
#    && find /opt/conda/ -follow -type f -name '*.js.map' -delete \
#    && mkdir /opt/notebooks

#COPY workflows /opt/notebooks

#COPY rediswq.py /opt/notebooks

#COPY worker-ls.ipynb /opt/notebooks

#CMD jupyter notebook \
#    --allow-root \
#    --notebook-dir=/opt/notebooks \
#    --NotebookApp.ip='0.0.0.0' \
#    --NotebookApp.port='8888' \
#    --NotebookApp.token='secretpassword' \
#    --NotebookApp.open_browser='False'

# ------------------------------------------

RUN conda install --quiet --yes --freeze-installed \
    jupyterlab \
    notebook \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

CMD jupyter lab \
    --allow-root \
    --notebook-dir=/opt/notebooks \
    --NotebookApp.ip='0.0.0.0' \
    --NotebookApp.port='8888' \
    --NotebookApp.token='secretpassword' \
    --NotebookApp.open_browser='False'

