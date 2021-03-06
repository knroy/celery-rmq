import setuptools

NAME = "celery-rmq"
DESCRIPTION = "Celery and RabbitMQ producer and consumer made easy with celery-rmq"
URL = "https://github.com/knroy/celery-rmq"
EMAIL = "rax.komol@gmail.com   "
AUTHOR = "Komol Nath Roy"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.0.2"

# What packages are required for this module to be executed?

REQUIRED = [
    "celery==4.4.2",
    "kombu==4.6.8"
]

# What packages are optional?

EXTRAS = {

}

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "screenshots"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
    python_requires=REQUIRES_PYTHON
)
