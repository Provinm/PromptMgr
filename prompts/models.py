from django.db import models

# Create your models here.

class Program(models.Model):
    '''项目
    '''
    name = models.CharField("项目名", max_length=200)
    
    def __str__(self):
        return self.name


class Prompt(models.Model):
    '''prompt 
    '''
    name = models.CharField("prompt名", max_length=200)
    description = models.CharField("prompt描述", max_length=200)
    private = models.BooleanField("私有",default=False)
    replace = models.TextField()
    data = models.TextField("常规模式数据")
    simple_data = models.TextField("简单模式数据")
    show_hmi = models.BooleanField("显示界面",default=False)
    play_beep = models.BooleanField("播放BEEP音",default=False)
    can_omit = models.BooleanField(default=True)
    barge_in = models.BooleanField(default=True)
    async = models.BooleanField(default=True)
    _type = models.IntegerField(default=2)
    modify_date = models.DateTimeField(auto_now=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.name
