from git import Repo

repo = Repo('/home/pi/Examensarbete')

repo.index.add(['scripts'])
repo.index.commit('Testing')
origin = repo.remote('https://github.com/Dmajstrolov/python-ciscoconfig.git')
origin.push()
