from configparser import ConfigParser

class ReadConfig:
    parser = ConfigParser()
    parser.read('config/config.properties.prod')
    url = parser.get('prod_ui', 'url')
    loginUserName = parser.get('prod_ui', 'username')
    loginPassword = parser.get('prod_ui', 'password')


if __name__ == '__main__':
    print(ReadConfig().url)
