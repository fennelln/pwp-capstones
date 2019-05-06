class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}   # maps books objects  to rating

    def get_email(self):
        return self.email

    def change_email(self, address):
        if "@" in address and ".com" in address:
            self.email = address
            return " Your email has been updated to " + self.email
        elif "@" in address and ".org" in address:
            self.email = address
            return " Your email has been updated to " + self.email
        elif "@" in address and ".edu" in address:
            self.email = address
            return " Your email has been updated to " + self.email    
        else:
            return "Email entered is not valid. Please try again."


    def __repr__(self):
        return "User = " + self.name + ", email = " + self.email + ", books read = " + str(len(self.books))

    
        ###NEED TO COME BACK TO
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
         return " User already exists"

    ##add new method to USER class read_book
    def read_book(self, book, rating = None):
        self.books[book] = rating
        return self.books

    ##add new method to USER class read_book
    def get_average_rating(self):
        average_rating = 0
        for rating in self.books.values():
            average_rating += rating
        return average_rating/len(self.books)



# create a Book class
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "The books ISBN has been updated to : {isbn}".format(isbn= self.isbn)
    
    def add_rating(self,rating):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        return self.ratings

    #add new get average_rating method
    def get_average_rating(self):
        book_average_rating = 0
        for rating in self.ratings:
            book_average_rating += rating
        return book_average_rating/len(self.ratings)

    # codecademy code for making the book objects hashable
    def __hash__(self):
        return hash((self.title, self.isbn))
            

#create a new Fiction subclass

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


# define the non fiction class

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title} , a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
        


# Create the TomeRater class

class TomeRater():
    def __init__(self):
        self.users = {}     # maps the email to the User object
        self.books = {}     # map a Book object to the number of Users that have read it.

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = 0):
        if email in self.users:  
            new_user = self.users.get(email)
            new_user.read_book(book, rating)
            book.add_rating(rating) ## is this in the right location??? UPDATE Yes it is.
            if book not in  self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    


    def add_user(self, name, email, user_books = None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    


    #add in print catalogue method

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    #add in print users method
    def print_users(self):
        for user in self.users.keys():
            print(user)

    #add most_read_book method
    def most_read_book(self):
        most_read = 0
        most_read_book = ""
        for book, count in self.books.items(): # go through books and count in self.books dictionary
            if count > most_read:
                most_read = count
                most_read_book = book
        return "The most read book is {most_read_book} .It has been read by {most_read} users.".format(most_read_book=most_read_book,most_read= most_read)

    #add in highest_rated_book method

    def highest_rated_book(self):
        h_book_rating = 0
        h_book = ""
        for book in self.books.keys():  # go through the book objects
            max_rating = book.get_average_rating() # get the average rating and assign it to a variable
            if max_rating > h_book_rating: # check if this variable is the highest
                h_book_rating = max_rating # if yes, assign that to highest book rating and get the book object.
                h_book = book
        return "The book with the highest average rating is {h_book}, with an average rating of {h_book_rating}".format(h_book=h_book, h_book_rating=h_book_rating)

    # add in most positive user method

    def most_positive_user(self):
        most_pos_user = ""
        most_pos_rating = 0

        for user in self.users.values():
            max_user_rating = user.get_average_rating()
            if max_user_rating > most_pos_rating:
                most_pos_rating = max_user_rating
                most_pos_user = user
        return " The user with the most postive rating is {most_pos_user}, with an an average rating of {most_pos_rating}".format(most_pos_user = most_pos_user, most_pos_rating = most_pos_rating )























