# XXE-File-Generator
This script read an `export.xml` file and create several `output*.xml ` with a payload to read `/etc/passwd` or any file given with argument `--file "flagtxt"`

### Install some addition libraries
```
pip install lxml
```

### Usage
Default it will create a payload for `/etc/passwd`
```
python3 XXE-Generator.py
```
Otherwise you could create a different payload to read a file like the example below
```
python3 XXE-Generator.py --file "/flag.txt" 
```
It will generate for every field a new XML file with the payload.
![image](https://github.com/eMVee-NL/XXE-File-Generator/assets/45883753/039b56a2-be51-4659-a7e3-2b97a618f72f)

They files should be tested manually on the target.


### Disclaimer
----------
This script is for educational purposes only. It is not intended to be used for malicious or harmful activities. With great power comes great responsibility, and you are solely responsible for any consequences that may arise from your actions.
By using this script, you acknowledge that you will not use it to harm or exploit others. You understand that any illegal or unethical activities are strictly prohibited and may result in legal consequences.
You are responsible for your own actions, and you will not hold the creators or maintainers of this script liable for any damages or consequences that may arise from your use of this script.
Remember, with great power comes great responsibility. Use this script wisely and ethically.
