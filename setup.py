from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='fcalc',
    version='1.0.3',
    license='MIT License',
    author='Edneudo Barros',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='franciscoelb@gmail.com',
    keywords='matematica matemática financeira financeiro juro juros taxa taxas',
    description=u'Cálculos relativos à matemática financeira',
    packages=['fcalc'],
    install_requires=[],)