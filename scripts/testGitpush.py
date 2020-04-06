import subprocess as cmd

def git_push_automation():

	try:
	  cp = cmd.run("/home/pi/Examensarbete", check=True, shell=True)
	  print("cp", cp)
	  cmd.run('git commit -m "Switch config"', check=True, shell=True)
	  cmd.run("git push -u origin master -f", check=True, shell=True)
	  print("success")
	  return True

	except:
	  print("Error git automation")
	  return False
