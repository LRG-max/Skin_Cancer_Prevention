from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='skin_cancer_prevention',
      version="0.0.1",
      description="Project Description",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
    #   scripts=['scripts/skin_cancer_prevention-run'],# issue to bluild container with
      zip_safe=False)
