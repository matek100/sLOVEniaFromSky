python3 test.py
crontab -l > newcron
sed "/test.sh/d" ./newcron
NUMBER_HOUR=$(shuf -i9-20 -n1)
NUMBER_MIN=$(shuf -i0-59 -n1)
echo $NUMBER_MIN $NUMBER_HOUR "* * * /path/to/controller.sh" >> newcorn

