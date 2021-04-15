import setuptools

setuptools.setup(
    name="leetcode",  # Replace with your own username
    version="0.0.1",
    author="yuhanShi53",
    author_email="yuhanshi53@outlook.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "leetcode"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
