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
    hdmedians \
    matplotlib \
    pandas \
    pip \
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
    descartes \
    redis \
    sklearn-xarray \
    rioxarray 
	
# ------------------------------------------

COPY workflows/utils /utils

COPY worker-s2.py /worker-s2.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker-s2.py" ]

