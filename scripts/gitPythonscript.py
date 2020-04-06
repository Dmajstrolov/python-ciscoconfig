import schedule
import time

def gitPush(t):

	exec(open('AutoGetConfig.py').read()),t
	exec(open('pushtoGit.py').read()),t

	return

schedule.every().day.at("01:00").do(gitPush,'It is 01:00')


while True:
	schedule.run_pending()
	time.sleep(60)
