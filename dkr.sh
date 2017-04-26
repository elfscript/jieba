#!/bin/bash
docker run -it --rm  --name myjieba \
  -v $(pwd):/mnt/work  -w /mnt/work \
  3hdeng/jieba:2.7 \
  /bin/bash

