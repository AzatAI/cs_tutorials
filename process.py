import os
import subprocess
# update to Github
os.system('git add .')
returned = subprocess.check_output(['git','status']).decode('utf-8')
messages = []
if 'Changes to be committed:' in returned:
    comm_list = returned.strip().strip(' ').strip('\t').split('\n')
    for each in comm_list:
        if each.startswith('\tmodified') or each.startswith('\tdeleted') or each.startswith('\tnew file'):
            messages.append(each)
comment_message = ','.join(messages)
os.system(f'git commit -m "{comment_message}"')
os.system('git push origin master')