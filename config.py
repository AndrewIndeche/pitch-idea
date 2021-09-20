class Config:
    '''
    General configuration parent class
    '''
    pass



class ProductionConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevelopmentConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig

}
