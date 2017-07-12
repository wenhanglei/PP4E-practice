"""
模拟cgi.FieldStorage()调用结果的工具；
用来测试CGI脚本输出；
"""
class FieldMockup:
    def __init__(self, str):
        self.value = str

def formMockup(**Kwargs):
    mockup = {}
    for (key, value) in kwargs.items():
        if type(value) != list:
            mockup[key] = FieldMocku(str(value))
        else:
            mockup[key] = []
            for pick in value:
                mockup[key].append(FieldMockup(pick))
    return mockup

def selftest():
    form = formMockup(name='Bob', job='hacker', food=['Spam', 'eggs', 'ham'])
    print(form['name'].value)
    print(form['job'].value)
    for item in form['food']:
        print(item.value, end=' ')
    print()
    form = {'name': FieldMockup('Brain'), 'age': FieldMockup(38)}
    for key in form.keys():
        print(form[key].value)

if __name__ == '__main__': selftest()




























