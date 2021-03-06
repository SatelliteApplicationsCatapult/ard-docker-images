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
    dask \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN pip install --no-cache-dir \
    asynchronousfilereader \
    redis \
    salem \
    sklearn-xarray \
    rioxarray

# ------------------------------------------

COPY workflows/utils /utils

COPY worker-MLWater.py /worker-MLWater.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker-MLWater.py" ]
