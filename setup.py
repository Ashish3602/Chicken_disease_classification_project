import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classification_project"
AUTHOR_USER_NAME = "ashishkr"
SRC_REPO = "cnnClassifier-Chicken_disease"
AUTHOR_EMAIL = "ashishofficial3602@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Small project to learn End to End Project implementation",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Ashish3602/Chicken_disease_classification_project",
    project_urls = {
        "Bug Tracker" :f"https://github.com/Ashish3602/Chicken_disease_classification_project/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
