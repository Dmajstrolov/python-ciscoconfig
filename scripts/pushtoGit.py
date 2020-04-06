from subprocess import call

call('git add running-configs', shell=True)
call('git commit -m "Switch config" .', shell=True)
call('git push', shell=True)

