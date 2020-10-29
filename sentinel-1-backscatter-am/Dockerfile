FROM satapps/ard-workflow-s1:1.2.1

LABEL maintainer="Luigi Di Fraia"

RUN conda update conda --quiet --yes --freeze-installed \
    && conda clean --all -f -y \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

RUN pip install --no-cache-dir \
    xmltodict \
    scipy \
    matplotlib \ 
    timeout-decorator \
    utility \    
    sentinelsat

COPY workflows/utils/s1am/snap/bin/gpt.vmoptions /opt/snap/bin/
COPY workflows/utils/s1am/snap/etc/snap.auxdata.properties /opt/snap/etc/

# ------------------------------------------

COPY workflows/utils /utils

COPY worker-s1-am.py /worker-s1-am.py

COPY rediswq.py /rediswq.py

CMD [ "python", "worker-s1-am.py" ]

