# This is where all my class files go starting with "class dojos and __init__ defined"
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.age = data['age']
        self.updated_at = data['updated_at']
        # self.dojos_id = data['dojos_id']
        # self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojos_id) "
        query += "VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojos_id)s); "
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return result