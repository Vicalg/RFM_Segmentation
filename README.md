# RFM Segmentation, PostgreSQL and Unsupervised Machine Learning

This repository contains code to create an RFM segmentation by connecting to a PostgreSQL database, processing the data, creating the scores and finally using unsupervised machine learning models for exploring the RFM segmentation according to the clusters created. **This is the first version of the readme file, Some files and folder names might be different**.

## Getting Started

To get started with this project, you will need to have access to a PostgreSQL database containing your customer data. You will also need to install the required dependencies listed in the `requirements.txt` file.

## Usage

1. The `info.json` file with your PostgreSQL connection details.
2. Run the `rfm_segmentation.py` script to connect to your database, process the data and create the RFM scores.
3. Run the `unsupervised_ml.py` script to explore the RFM segmentation using unsupervised machine learning models.

## Bash Scripts

This repository also includes a folder for bash scripts that can be used to preprocess your data and return a smaller csv file. To use these scripts, navigate to the `bash_scripts` folder and run them from there.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
