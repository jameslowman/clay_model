#!/bin/bash

# install tmux
sudo apt-get install tmux

# Create a new tmux session
tmux new -s data_creation

# Checkout the 'james-dev' branch
git checkout james-dev

# Install Python dependencies from your requirements file
pip install -r code-editor-reqs.txt

# Configure the Planetary Computer, replace "YOUR_API_CODE" with your actual API code
# Note: This step might require manual input or a different approach if your API code cannot be passed as a simple argument
echo "760282a20d7a400b960db25c069000c0" | planetarycomputer configure

# Make your data creation script executable
chmod 777 run_random_data_creation.sh

# Execute your data creation script
./run_random_data_creation.sh

