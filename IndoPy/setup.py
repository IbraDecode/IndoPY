from setuptools import setup

setup(
    name='indopy',
    version='1.0',
    py_modules=['indopy', 'translator'],
    entry_points={
        'console_scripts': [
            'indopy = indopy:__main__',
        ],
    },
    author="IbraDecode",
    description="Bahasa pemrograman Indonesia sederhana berbasis Python",
    long_description="IndoPy adalah bahasa pemrograman dengan sintaks Bahasa Indonesia, ditujukan untuk edukasi dan pembelajaran logika dasar.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
