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