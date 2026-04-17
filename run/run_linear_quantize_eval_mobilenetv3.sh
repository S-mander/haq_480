export CUDA_VISIBLE_DEVICES=0,1,2,3
python -W ignore finetune.py     \
 -a qmobilenet_v3                \
 --resume checkpoints/mobilenetv3/qmobilenetv3_0.6_best.pth.tar         \
 --workers 32                    \
 --test_batch 512                \
 --gpu_id 0,1,2,3                \
 --free_high_bit False           \
 --linear_quantization           \
 --eval                          \
