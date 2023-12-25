import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valBB", # Replace with your own username
    version="1.0.0",
    author="Sattawat Arab",
    author_email="support@vallarismaps.com",
    description="A package to processing Vallaris Maps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://v2k.vallarismaps.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= ['jsonschema','ndjson','geojson','requests','geopandas','pandas', 'rtree', 'numpy','shapely','tqdm', 'python-dotenv', 'matplotlib', 'earthpy', 'uuid'],
    python_requires='>=3.6',
)

# python3 -m twine upload --repository gitlab dist/*
