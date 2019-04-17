vec_log = None

def logInit(name):
    global vec_log
    vec_log = open('{}.log'.format(name),'w')

def logAppend(vec_info):  
    global vec_log
    vec_log.write('{}\n'.format(vec_info))
    
def logClose():
    global vec_log
    vec_log.close()

