"a person object: fields + behavior"

class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = payy

    def tax(self):
        if attr =='tax':
            return self.pay * 0.30
        else:
            raise AttributeError()

    def info(self):
        return self.name, self.job, self.pay, self.tax()