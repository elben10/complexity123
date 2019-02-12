from setuptools import find_packages, setup

docs_requirements = [
    "sphinx",
]

installation_requirements = []

setup_requirements = [
    "pytest-runner"
]

test_requirements = [
    "pytest",
]

setup(
    name='complexity',
    version='0.1.1',
    url='https://github.com/AudreyRoy/complexity.git',
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    description='Refreshingly simple static site generator.',
    packages=find_packages(),    
    install_requires=installation_requirements,
    setup_requires=setup_requirements,
    extras_require={
        'docs': docs_requirements,
        'test': test_requirements,
    }
)
