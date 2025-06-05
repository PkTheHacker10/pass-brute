from setuptools import setup, find_packages

setup(
    name='hash-brute',
    version='1.0.0',
    description='A multi-threaded hash cracking tool supporting MD5, SHA-1, SHA-256, and SHA-512.',
    author='Pevinkumar A',
    author_email='pevinbalaji@gmail.com',
    url='https://github.com/pevinkumar10/hash-brute',
    packages=find_packages(),
    install_requires=[
        'hashid',
        'tqdm',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'hashbrute=hashbrute.hashbrute:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
)
