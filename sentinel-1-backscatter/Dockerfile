FROM continuumio/miniconda3:4.7.12

LABEL maintainer="Luigi Di Fraia"

RUN conda update conda --quiet --yes --freeze-installed \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

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
    asynchronousfilereader \
    redis \
    sentinelsat

RUN wget --quiet http://step.esa.int/downloads/7.0/installers/esa-snap_sentinel_unix_7_0.sh \
    && /bin/sh ./esa-snap_sentinel_unix_7_0.sh -q \
    && rm ./esa-snap_sentinel_unix_7_0.sh \
    && /opt/snap/bin/snap --nosplash --nogui --modules --update-all

# ------------------------------------------

COPY workflows/utils /utils

COPY worker-s1.py /worker-s1.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker-s1.py" ]
