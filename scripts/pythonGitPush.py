from git import Repo

repo = Repo('/home/pi/Examensarbete/scripts')

repo.index.add(['/running-configs'])
repo.index.commit('Auto-commit')
origin = repo.remote('Dmajstrolov/python-ciscoconfig.git')
origin.push()
