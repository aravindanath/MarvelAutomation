from configparser import ConfigParser

# config = ConfigParser()
# filePath =  "../testdata/data.ini"
# config.add_section("[Tc03]")
# config.set("[Tc03]","url","https://www.flipkart.com")
# with open(filePath,'a') as dt:
#     config.write(dt)
#

def writeToIni(filePath,header,key,value):
    config = ConfigParser()
    config.add_section(header)
    config.set(header, key, value)
    with open(filePath, 'a') as dt:
        config.write(dt)



w = writeToIni("../testdata/data.ini","TC005","search","macbook pro")
