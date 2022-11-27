'''
这三个需要按照顺序引用,因为后边的依赖前边的执行完成
'''
from time import sleep
from VediosToMatrixs import generate_training_sets

generate_training_sets()
sleep(1)

from Training import training

training()
sleep(1)

from Test import test

test()

