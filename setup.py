from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="fcalc",
    version="1.0.2",
    author="Edneudo Barros",
    author_email="franciscoelb@gmail.com",
    description="Módulos para matemática financeira",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BarrosEdneudo/fcalc",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)