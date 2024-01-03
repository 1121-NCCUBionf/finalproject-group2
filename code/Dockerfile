FROM ubuntu:latest

COPY ./run_fanc.sh .

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    bowtie2 \
    vim \
    tmux

# biopython needs to use the version 1.75.
RUN pip install fanc==0.9.27
RUN pip uninstall -y biopython
RUN pip install biopython==1.75
