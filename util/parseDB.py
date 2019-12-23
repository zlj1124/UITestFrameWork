import configparser
from config.conf import DB_PATH


class ParseDB(object):

    def __init__(self):
        self.file = DB_PATH
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='utf-8')

    def get_option_value(self,section,option):
        """获取指定section下的指定option和对应的数据""" 
        values = self.conf.get(section, option)  
        return values
    def get_all_option_value(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value

if __name__ == '__main__':
    parse=ParseDB()
    print(parse.get_option_value('jing5DB','host'))
    print(parse.get_all_option_value('jing5DB'))
