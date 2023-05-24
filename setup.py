from setuptools import setup, find_packages


setup(
    name="text2tags-lib",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["editdistance", "llama-cpp-python", "wget"],
    package_data={"text2tags": ["tags.txt"]},
)
