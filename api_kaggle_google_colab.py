# Kaggle  API in Google Colab

# Install Kaggle API$
!pip install kaggle
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 /root/.kaggle/kaggle.json

# Put your key credentials in the json fomrat
import json

kaggle_json = """
{
  "username": "kaggle_user_name",
  "key": "token_number"
}
"""

# Salvando o conteúdo em um arquivo de configuração
# Saving in a configuration file
with open('/root/.kaggle/kaggle.json', 'w') as json_file:
    json_file.write(kaggle_json)

# Permissions
!chmod 600 /root/.kaggle/kaggle.json

# Download the zip file from kaggle
!kaggle datasets download -d lsind18/euro-exchange-daily-rates-19992020

# Unzip the file
!unzip euro-exchange-daily-rates-19992020.zip

# Now you can import the dataset
import pandas as pd
df = pd.read_csv("/content/euro-daily-hist_1999_2022.csv", sep=",")
