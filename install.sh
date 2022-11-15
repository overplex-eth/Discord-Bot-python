#!/bin/sh

echo "Installing bot requirements..."
python3 pip install -r ./requirements.txt
echo "python3 ./bot.py" >> ./start.sh
echo "Once config.json is loaded, open the file"
