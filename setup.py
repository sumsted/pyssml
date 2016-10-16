from setuptools import setup

setup(
    cmdclass={},

    name='pyssml',
    packages=['pyssml'],
    version='0.1.0',

    install_requires=[],

    description='Python library for generating SSML for Amazon Alexa',

    long_description=
    """
    pyssml

    Python 3 SSML generator for Alexa.
    """,

    url='http://wildidea.xyz',

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
