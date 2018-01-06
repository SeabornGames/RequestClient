from setuptools import setup, find_packages

setup(
    name='seaborn_request_client',
    version='0.0.1',
    description='Request Client creates and maintains connections using '
                'the request library, but make each url endpoint a remote'
                'procedure call with the response content returned.  '
                'These function calls can made from a "connection" which has'
                'a hierarchy of objects that mirrors the hierarchy of the '
                'API.',
    long_description='',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/RequestClient',
    packages=['seaborn']+['seaborn.'+i for i in find_packages(where = './seaborn')],
    install_requires=[
        'seaborn_meta',
        'pyopenssl',
        'gevent',
        'requests',
    ],
    extras_require={'test': ['test-chain',
                             'seaborn-flask'],
                    },
    license='MIT License',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
