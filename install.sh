echo "Installing necessary packages..."
apt-get install python3 python3-tk -y

echo "Moving files..."
cp calculator.py /usr/bin
cp calculator.sh /usr/bin

echo "Setting Permissions..."
cd /usr/bin
chmod +x calculator.py
chmod +x calculator.sh

echo "Adding final touches..."
mv calculator.sh calculator

echo "If you want to run the calculator, just type in 'calculator' in the terminal!"
echo "If you encountered any problems, try again as sudo superuser."