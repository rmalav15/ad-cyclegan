#!/usr/bin/env bash
CUDA_VISIBLE_DEVICES=0 python main.py \
    --dataset_dir /mnt/069A453E9A452B8D/Ram/adGeneration/cyclegan \
    --input_nc 5 \
    --batch_size 4 \
    --epoch 400 \
    --encoder_freeze_epoch 10 \
    --ngf 64 \
    --lr 0.0001