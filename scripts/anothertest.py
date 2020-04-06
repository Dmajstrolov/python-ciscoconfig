from git import Repo
repo = Repo('/home/pi/Examensarbete')

repo.index.add(['running-configs'])
repo.index.commit('New switch config')
origin = repo.remote('https://github.com/Dmajstrolov/python-ciscoconfig.git')
origin.push()
