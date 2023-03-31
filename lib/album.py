class Album:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.release_year == None or not int(self.release_year):
            return False
        if self.artist_id == None or self.artist_id == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release year can't be blank")
        if self.artist_id == None or self.artist_id == "":
            errors.append("Artist ID can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)