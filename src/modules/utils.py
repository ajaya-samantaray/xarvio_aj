import json
class Utils():
    def getSettings(self, settingsFile):
        try:
            settings = open( settingsFile, "r" )
            return json.load( settings )
        except FileNotFoundError:
            print('Error: Settings file ' + settingsFile + " not found")
        return {}


    def executeDBScript(db, sql_cmd, sql_params):
        try:
            cur = db.cursor()
            cur.execute(sql_cmd, sql_params)
            return
        except Exception as e:
            print ('Error ', e )
            raise