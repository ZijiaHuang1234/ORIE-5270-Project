from setuptools import setup, find_packages

setup(
    name="taxi_demand",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas>=2.0",
        "scikit-learn>=1.0",
        "pyarrow>=15.0",
        "numpy>=1.24",
        "pytest>=7.0",
    ],
)