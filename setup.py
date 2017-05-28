from setuptools import setup

setup(
    cmdclass={},

    name='pyssml',
    packages=['pyssml'],
    version='0.1.3',

    install_requires=[],

    description='Python library for building SSML for Amazon Alexa',

    long_description=
    """
    pyssml

    Python 3 SSML builder for Alexa.

    Inspired by and based on JavaScript project https://github.com/mandnyc/ssml-builder
    """,

    url='https://github.com/sumsted/pyssml',

    author='Scott Umsted',
    author_email='scott@wildidea.xyz',
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='ssml python pyssml amazon alexa',
)
