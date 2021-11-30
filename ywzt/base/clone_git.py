from git import Repo
from git.repo.fun import is_git_dir
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
Repo.clone_from('https://github.com/hongliao1/hongliao1.git',to_path=r'C:\Users\92075\Desktop\test_1')
Repo.init(r'C:\Users\92075\Desktop\test_1')
