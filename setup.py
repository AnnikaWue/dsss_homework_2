from setuptools import setup, find_packages

setup(
    name="math_quiz", 
    version="0.1.0",
    author="Annika",
    author_email="annika.email@example.com",
    description="Math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnnikaWue/dsss_homework_2",  
    packages=find_packages(),
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
