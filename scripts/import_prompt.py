#coding=utf-8

import os, django
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PromptMgr.settings')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruitment.settings")
django.setup()

import json
from prompts.models import Program, Prompt


'''
导入现有的 prompts

'''

class ImportFile(object):

    def __init__(self, program="", file_path=""):

        assert program, "空项目名"
        assert file_path, '无效文件地址'

        self.program = self.init_program(program)
        self.file_path = file_path

    def init_program(self, program):
        '''查看目前数据库是否存在该 program
        '''
        obj, created = Program.objects.get_or_create(
            name=program
        )
        return obj


    def loads_file(self, path):
        '''导入文件
        '''
        with open(path, "r", encoding="utf-8")as f:
            data = f.read()

        return json.loads(data)

    def dump_anything(self, obj):
        '''将其他对象转换为 str
        '''
        if isinstance(obj, (list, dict, tuple)):
            return json.dumps(obj)
        else:
            return obj

    def convert_key_value(self, value):
        '''转换目前字典为数据兼容
        '''
        dct = {}
        for k, v in value.items():
            if k == "type":
                dct["_type"] = v
            else:
                dct[k] = self.dump_anything(v)
            
        return dct

    def handle_item(self, key, value):
        '''处理单条数据
        '''
        value = self.convert_key_value(value)

        objs = Prompt.objects.filter(
            name=key,
            program=self.program
        )
        if objs:
            obj = objs[0]
            # 更新其他的属性
            for k, v in value.items():
                setattr(obj, k, v)

            # 更新外键
            setattr(obj, "program", self.program)

            # 保存
            obj.save()
        else:
            Prompt.objects.create(
                name=key,
                program=self.program,
                **value
            )

    def run(self):
        
        data = self.loads_file(self.file_path)
        for k,v in data.items():
            self.handle_item(k, v)


if __name__ == "__main__":

    imf = ImportFile(
        "2.0high",
        r"D:\codedir\work\asdev\asdev\asapdev\data\dialog\prompt.txt"
    )
    imf.run()