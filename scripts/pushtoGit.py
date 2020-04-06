from subprocess import call

call('git add .', shell=True)
call('git commit -m "Switch config" .', shell=True)
call('git push', shell=True)

