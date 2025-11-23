from setuptools import setup, find_packages
setup(
    name="plotterai",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    description="plotterai: natural language to plots with Ollama",
    license="MIT",
    python_requires=">=3.8",
    install_requires=["pandas", "matplotlib", "requests"],
)