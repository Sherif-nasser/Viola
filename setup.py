from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in viola/__init__.py
from viola import __version__ as version

setup(
	name="viola",
	version=version,
	description="viola",
	author="sherif",
	author_email="sherif",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
