import setuptools

with open("README.md", "r") as fh:
	long_desc = fh.read()

setuptools.setup(
	name = "scratchpad-deadmund",
	version = "1.1.0",
	author = "Ed Novak",
	author_email="enovak@fandm.edu",
	description = "Notepad with basic math functions",
	long_description = long_desc,
	long_description_content_type="text/markdown",
	url="https://github.com/fmresearchnovak/scratchpad",
	packages=setuptools.find_packages(),
	entry_points={'console_scripts':['scratchpad = scratchpad.__main__:main']},
	classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)