# -*- coding: utf-8 -*-
import yaml

# with open(r'G:\Mon Drive\QCM\qcm.yml') as file:
#     question = yaml.load(file, Loader=yaml.FullLoader)
#     print(question)

with open(r'G:\Mon Drive\QCM\qcm.yml') as file:
    question = yaml.full_load(file)
    print(question)
