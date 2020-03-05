# xilinx-dnndk-training

## Getting Started
This work is following the [xilinx DNNDK user-guide](https://www.xilinx.com/support/documentation/sw_manuals/ai_inference/v1_6/ug1327-dnndk-user-guide.pdf).

### Development Environment
Currently there are two docker-based development environments, one for caffe and one for tensorflow. The environment requirements can be found at the corresponding `builder/Dockerfile.*`.

Prerequisites:
- Install [docker](https://docs.docker.com/install/)
- Install [dnndk v3.1](https://www.xilinx.com/products/design-tools/ai-inference/ai-developer-hub.html#edge) at project's dnndk directory

Tensorflow:
- `docker build -t xilinx-dnndk-builder-tensorflow -f builder/Dockerfile.tensorflow builder`
- `docker run --rm -it -v $(pwd):/workdir xilinx-dnndk-builder-tensorflow`

Caffe:
- `docker build -t xilinx-dnndk-builder-caffe -f builder/Dockerfile.caffe builder`
- `docker run --rm -it -v $(pwd):/workdir xilinx-dnndk-builder-caffe`


### Running Applications using ZedBoard
Prerequisites:
- (Windows Only) Install [MobaXterm](https://mobaxterm.mobatek.net/)
- Install [Etcher](https://www.balena.io/etcher/)

Setup:
- Download [DNNDK Linux image](https://www.xilinx.com/member/forms/download/design-license-xef.html?filename=xilinx-zedboard-dnndk3.1-image-20190812.zip)
- Install the DNNDK image on an SD-card (at leat 8GB) using etcher
- Place the SD card at the ZedBoard and turn on (make sure SD-card boot mode is enabled)
- Connect the ZedBoard to a LAN using ethernet
- Find the ZedBoard IP (either by connecting to its UART console or using a LAN scan tool like nmap)
- Transfer DNNDK tools to Zedboard: `scp -r dnndk/ZedBoard root@<zedboard-ip>:~/`
- Login to ZedBoard: `ssh root@<zedboard-ip>:~/` (default password is **root**)
- Install the DNNDK tools to Zedboard: `cd ZedBoard && ./install.sh`

Execute Resnet50 Sample (Windows Only for now):
- Open MobaXterm shell
- Login to ZedBoard with X11 Forwarding Enabled (MobaXterm forwards X11 by default): `ssh root@<zedboard-ip>:~/`
- `cd ZedBoard/samples/resnet50`
- Compile the sample: `make`
- Run the sample: `./resnet50`
 
 If everything was done correctly a new X11 application will open at your Host Machine that displays the input images and at the shell you can see the corresponding image classes.
