from git import Repo

repo = Repo('/home/pi/Examensarbete')

repo.index.add(['scripts'])
repo.index.commit('Testing')
origin = repo.create_remote('https://github.com/Dmajstrolov/python-ciscoconfig.git',repo.remotes.origin.url)
origin.push()
