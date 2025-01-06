from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload dist/*
setup(
    name="answer_college_supplemental",
    version="0.5",
    packages=find_packages(),
    install_requires=["requests>=2.32"],
    author="Vishwesswaran Gopal",
    author_email="vishy1290@gmail.com",
    description="A CLI tool for gaining inspiration for college supplementals. Do NOT submit these generated essays to colleges.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "answer_college_supplemental = answer_college_supplemental.main:main",
        ],
    },
)
