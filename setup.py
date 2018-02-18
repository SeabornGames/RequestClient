from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='seaborn-request-client',
    version='1.0.0',
    description='Request Client is a helper library around the request '
                'package to help make cleaner code that is easier to debug.',
    long_description=long_description,
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/RequestClient',
    install_requires=[
        'seaborn-meta',
        'pyopenssl',
        'gevent',
        'requests',
    ],
    packages = ['seaborn_request_client'],
    extras_require={'test': ['test-chain',
                             'seaborn-flask'],
                    },
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
