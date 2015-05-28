load_data.py:
1. Database is populated directly ( without use of any CSV or JSON format intermediate file ) using load_data.py
	Limitation : 
		Extracted Movie name is  <['The Shawshank Redemption (1994) ']>  instead of  <The Shawshank Redemption (1994)>. Same way, Extracted Movie Rating is <[' 9.3']> instead of <9.3> although order is maintained in sorting and other operations but It may makes searching inefficient for large data sets.
	Reason of limitation: 
		regex used for extracting Movie Name: name_regex = '<title>(.+?)- IMDb</title>' 
		Whenever I tried to use  '<title>[\'(.+?)\']- IMDb</title>' in order to remove <[' ']> this part it started giving NULL values..same in case of Movie_Rating too..

admin.py :
	username: deepakverma20120274@gmail.com
	password: 12345
	
	CRUD operations can only be performed by "admin" not by client side user.. User is only supposed to see data on demand.

models.py :
	Three Models are created:
		1. Rating (movie_name,movie_rating)
		2. Cast (movie_name,movie_rating,cast1,cast2,cast3,cast,cast5,cast6,cast7)
		3. Storyline(movie_name,movie_rating,movie_story)
	No Foreign Key is used to avoid complexity and faster processing (tables are not connected and sufficient data is already present in table)'.

Thank You for your time.
Yours Faithfully
Deepak Verma
























