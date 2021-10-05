from setuptools import setup, find_packages

VERSION = '0.0.0'
with open('VERSION', 'r') as version:
    VERSION = version.read().replace("\n", "")

setup(
    name="nexus",
    version=VERSION,
    description="A Telnet-Based Archive of Gates to the Multiverse",
    author="Sean Shookman",
    author_email="sms112788@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    setup_requires=["pytest-runner"],
    install_requires=[ ],
    entry_points={
        'console_scripts': [
            'nexus = nexus:main',
        ],
    }
)
