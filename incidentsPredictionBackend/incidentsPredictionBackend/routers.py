class PredictionModelRouter(object):
    """
    A router to control all database operations on models in
    the in modelDB database.
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on predictionmodel app to 'predictionmodel_db'
        """
        if model._meta.app_label == 'predictionmodel':
            return 'predictionmodel_db'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on predictionmodel app to 'other'
        """
        if model._meta.app_label == 'predictionmodel':
            return 'predictionmodel_db'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the predictionmodel app only appears on the 'other' db
        """
        if db == 'predictionmodel_db':
            return model._meta.app_label == 'predictionmodel'
        elif model._meta.app_label == 'predictionmodel':
            return False
        return None

class GroupamaSIRouter(object):
    """
    A router to control all database operations on models in
    the in groupamasiDB database.
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations to 'groupamasi_db'
        """
        if model._meta.app_label == 'groupamasi':
            return 'groupamasi_db'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations to 'other'
        """
        if model._meta.app_label == 'groupamasi':
            return 'groupamasi_db'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure  only appears on the 'other' db
        """
        if db == 'groupamasi_db':
            return model._meta.app_label == 'groupamasi'
        elif model._meta.app_label == 'groupamasi':
            return False
        return None