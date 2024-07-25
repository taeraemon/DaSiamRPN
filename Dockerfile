# Base image
FROM ubuntu:16.04

# Set the maintainer label
LABEL maintainer="tykim512@snu.ac.kr"

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    pkg-config \
    libjpeg8-dev \
    libtiff5-dev \
    libjasper-dev \
    libpng12-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libatlas-base-dev \
    gfortran \
    python2.7 \
    python2.7-dev \
    python-pip \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip==20.3.4

# Install Python packages
RUN pip install numpy==1.16.4
RUN pip install opencv-python==4.2.0.32

# Install PyTorch 0.3.1 and torchvision 0.2.0
RUN pip install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl

# Default command to run when container starts
CMD ["bash"]
