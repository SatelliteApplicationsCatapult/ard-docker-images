FROM continuumio/miniconda3:4.7.10

LABEL maintainer="Luigi Di Fraia"

RUN conda install --quiet --yes --freeze-installed \
    boto3 \
    geopandas \
    hdmedians \
    matplotlib \
    pandas \
    pyyaml \
    rasterio \
    requests \
    scikit-learn \
    xarray \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN pip install --no-cache-dir \
    asynchronousfilereader \
    redis 

# ------------------------------------------

#COPY workflows/utils /utils

#COPY worker-Water.py /worker-Water.py

#COPY rediswq.py /rediswq.py

#CMD [ "python", "worker-Water.py" ]

# ------------------------------------------

#RUN conda install --quiet --yes --freeze-installed \
#    jupyter \
#    && conda clean --all -f -y \
#    && find /opt/conda/ -follow -type f -name '*.a' -delete \
#    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
#    && find /opt/conda/ -follow -type f -name '*.js.map' -delete \
#    && mkdir /opt/notebooks

#COPY workflows /opt/notebooks

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

CMD jupyter lab \
    --allow-root \
    --notebook-dir=/opt/notebooks \
    --NotebookApp.ip='0.0.0.0' \
    --NotebookApp.port='8888' \
    --NotebookApp.token='secretpassword' \
    --NotebookApp.open_browser='False'

