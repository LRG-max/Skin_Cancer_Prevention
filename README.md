# Skin Cancer Prevention

## Project Overview

This project aims to provide tools and resources for the prevention of skin cancer through data analysis and machine learning.

### Description

The project leverages image processing and machine learning techniques to predict the risk of skin cancer from images.

### Data Source

- [Specify your data sources here]

### Type of Analysis

- Image processing
- Machine learning model training and evaluation

## Getting Started

### Initial Setup

To set up the project, follow these steps:

1. **Create a virtual environment and install dependencies:**

   ```bash
   sudo apt-get install virtualenv python-pip python-dev
   deactivate; virtualenv ~/venv; source ~/venv/bin/activate
   pip install pip -U; pip install -r requirements.txt
   ```

2. **Run unit tests:**

   ```bash
   make clean install test
   ```

3. **Set up the project on GitHub:**
   - Check for `Skin_Cancer_Prevention` in `github.com/{group}`. If your project is not set up, please add it.
   - Create a new project on `github.com/{group}/Skin_Cancer_Prevention` and populate it:
     ```bash
     git remote add origin git@github.com:{group}/Skin_Cancer_Prevention.git
     git push -u origin master
     git push -u origin --tags
     ```

### Functional Test with a Script

To run a functional test, execute the following script:

```bash
cd
mkdir tmp
cd tmp
Skin_Cancer_Prevention-run
```

## Installation

1. **Visit the Project Repository:**
   Go to `https://github.com/{group}/Skin_Cancer_Prevention` to see the project, manage issues, and set up your SSH public key.

2. **Create and activate a Python 3 virtual environment:**

   ```bash
   sudo apt-get install virtualenv python-pip python-dev
   deactivate; virtualenv -ppython3 ~/venv; source ~/venv/bin/activate
   ```

3. **Clone the project and install dependencies:**

   ```bash
   git clone git@github.com:{group}/Skin_Cancer_Prevention.git
   cd Skin_Cancer_Prevention
   pip install -r requirements.txt
   make clean install test
   ```

4. **Run a functional test with a script:**
   ```bash
   cd
   mkdir tmp
   cd tmp
   Skin_Cancer_Prevention-run
   ```

## Usage

### Running the Frontend

To run the Streamlit frontend, use the following command:

```bash
streamlit run frontend.py
```

This will start a web application where you can upload images and get predictions.

### Utilities

The project includes utility functions for image processing and prediction. See `scripts/utils.py` for more details.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
