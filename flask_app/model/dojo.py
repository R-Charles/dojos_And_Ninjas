# This is where all my class files go starting with "class dojos and __init__ defined"
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.ninja import Ninja
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * "
        query += "FROM dojos "
        query += "LEFT JOIN ninjas "
        query += "ON dojos.id = ninjas.dojos_id "
        query += "WHERE dojos_id = %(id)s;"

        result = connectToMySQL( 'dojos_and_ninjas_schema' ).query_db(query, data)
        
        print ("result: ",result)
        if len(result) == 0:
            return True
        dojo = cls(result[0])
        print("dojo:", dojo)
        for row_from_db in result:

            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }

            dojo.ninjas.append( Ninja( ninja_data ) )

        return dojo

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at) "
        query += "VALUES (%(name)s, NOW(), NOW()); "
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return result