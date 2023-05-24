FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive
SHELL ["/bin/bash", "-c"] 
WORKDIR /app

RUN apt update -y && \
    apt install software-properties-common -y && \
    add-apt-repository universe && \
    apt update -y && apt install curl -y && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null && \
    apt update -y && \
    apt upgrade -y && \
    apt install ros-humble-desktop -y && \
    apt install ros-humble-ros-base -y && \
    apt install ros-dev-tools -y && \
    source /opt/ros/humble/setup.bash

RUN apt update -y && \ 
    apt-get install python3-pip -y
    # apt update -y && \
    # apt install python3-pip \
    # apt update -y

# install ros package
# RUN apt-get update -y && apt-get install -y && \
#     ros-${ROS_DISTRO}-demo-nodes-cpp && \
#     ros-${ROS_DISTRO}-demo-nodes-py && \
#     rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# launch ros package
CMD ["python3", "app.py"]
EXPOSE 3000