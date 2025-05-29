**Welcome to my project**


In this task I am creating Python Package, command line tool to interact with input file,search words and count their occurance,then it should be in output file.

I have implemented **logging for better clarification**

 
 
 1. First we need to activate virtual environment For mac,let's call it
    env `python3 -m venv env`
 2. Then we need to activate it
                       `source env/bin/activate`
 3. Then we need to install the package
	        `pip install -e .`
  
 4. To run specific the tool ,you should use
    `my-cli -i <filename> -w <words> -o <output filename>`

   To be more specific we could use:
  `my-cli -i some.txt -w giorgi,epam,s,jane,doe,Doe,company -o txt.txt`
    
  For this we need to mention the
     -i input file, which program will open
     -o output file,the filename in which output should be written
     -w the words seperated by comma.
I have used logging.error and logging.info
In every execution log file is created mentioning the tool process.

