# robo-advisor

This is a stock robo-advisor made to practice the use of APIs and CSV data analysis.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/connorkeyes/robo-advisor) under your own control, then clone your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

First, [you must get an API key from Alpha Vantage](https://www.alphavantage.co/), whose API is being used to pull current stock data online. Click "Get Your Free API Key Today" and create an account to receive your key. Copy this key for later use.

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to hold your Alpha Vantage API Key:

    ALPHAVANTAGE_API_KEY = "<Paste API Key Here>"

## Usage

Run the robo-advisor script:

```py
python app/robo_advisor.py
```

The program will not work until you acquire an API Key. Data from stocks that you analyze will be saved as .csv files in the "data" directory of this repo.