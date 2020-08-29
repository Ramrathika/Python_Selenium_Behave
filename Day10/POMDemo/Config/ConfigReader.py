from jproperties import Properties

class ReadProperties():
    def configReader(self,value):
        self.value = value
        #Opening Config File
        config = Properties()
        with open("C:/Users/vignesh/PycharmProjects/PythonTutorials/AugBatch/POMDemo/Config/config.properties", 'rb') as config_file:
            config.load(config_file)

        for items in config.items():
            if 'url' in self.value:
                val = items[1].data
                break
        return val

Read = ReadProperties()
print(Read.configReader("url"))