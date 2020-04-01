from git import Repo

repo = Repo('/home/pi/Examensarbete')

repo.index.add(['scripts'])
repo.index.commit('Auto-commit')
origin = repo.create_remote('Dmajstrolov/python-ciscoconfig.git',repo.remotes.origin.url)
origin.push()
