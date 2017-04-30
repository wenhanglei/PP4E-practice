import os
print('setenv...', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'LeiWenhang'
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python ehcoenv.py').read())
