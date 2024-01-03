FROM ubuntu:latest

COPY ./run_fanc_example.sh .

# Update the system and install related packages
# vim and tmux are for development purposes
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    bowtie2 \
    vim \
    tmux

# Install the 'fanc' Python package via pip
# note that `fanc` should be installed with `biopython` version 1.75
RUN pip install fanc==0.9.27
RUN pip uninstall -y biopython
RUN pip install biopython==1.75
