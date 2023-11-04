# Repository Updater

![License](https://img.shields.io/github/license/AlexPT2k22/Auto-Updater)
![Last Commit](https://img.shields.io/github/last-commit/AlexPT2k22/Auto-Updater)

This is a simple repository updater script for managing updates to your project. It checks the latest release on GitHub and updates your local files accordingly.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically checks for the latest release on GitHub.
- Downloads and updates your project files to the latest version.
- Supports both source code and zip archive releases.
- Easy to use.

## Supported Languages:

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/), more coming soon! (if you feel so, you can open an issue with the code of the language you want to see here!)

## Getting Started

You can follow these instructions to get your project up and running with the repository updater.

### Prerequisites

- Python 3.x
- Requests library (you can install it using `pip`)

### Installation

1. Install the requisites:

   ```bash
   pip install requests

2. Clone the repositorie:

   ```bash
   git clone https://github.com/AlexPT2k22/Repository-Updater.git
   
3. Add the code to your project:
    - You can add the code directly to your own code, or import it as a .py file

## Configuration

To configure the updater for your specific project, you need to customize the following variables in the auto_updater.py script:

- GITHUB_REPO_OWNER: Your GitHub username or organization.
- GITHUB_REPO_NAME: The name of your repository.
- release_type: Specify whether your release is "source_code" or "zip_archive" in your package.json file.

## Contributing:

Contributions are welcome! If you have any improvements or feature suggestions, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
