from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='linabsspec',
      version='0.1',
      description='Calculates Linear Absorption Spectrum',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.0',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
      ],
      url='https://bitbucket.org/marickmanrho/linabsspec',
      author='Marick Manrho',
      author_email='m.manrho@rug.nl',
      license='MIT',
      packages=['linabsspec'],
      install_requires=[
          'numpy','matplotlib','system',
      ],
      include_package_data=True,
      zip_safe=False)
