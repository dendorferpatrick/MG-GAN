from setuptools import setup, find_packages


setup(
    name = "mggan_quvadis",
    version = "0.0.1",
    author = "Patrick Dendorfer",
    author_email = "patrick.dendorfer@tum.de",
    include_package_data=True,
    description="MG-GAN Fork for Quo Vadis Tracker",
    url = "package URL",
    project_urls = {
        "Repository": "https://github.com/dendorferpatrick/MG-GAN.git",
        "Original Repository": "https://github.com/selflein/MG-GAN"
    },
    package_dir = {"": "."},
    packages = find_packages(where="."),
    python_requires = ">=3.6"
)