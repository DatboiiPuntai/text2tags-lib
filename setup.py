from setuptools import setup, find_packages

setup(
    name="text2tags-lib",
    version="0.0",
    packages=find_packages(),
    install_requires=["editdistance", "llama-cpp-python", "wget"],
    # other metadata and configurations
)
