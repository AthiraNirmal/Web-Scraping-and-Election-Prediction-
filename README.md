# Web-Scraping-and-Election-Prediction-

The project involved collecting election related posts from 4Chan API in JSON format through HTTP requests. After collecting the data, sentiment analysis was conducted on the posts to extract the emotions and opinions of the users towards the election.

Using the insights gained from the sentiment analysis, the project predicted the results of the election. The prediction was then visualized through a web-based user interface. The interface allowed users to search for posts related to specific keywords and view the prediction and the sentiment analysis of the posts.

To improve the speed of the search feature, the project implemented Redis caching. This caching technology allowed frequently searched posts to be stored in memory, reducing the time it took to retrieve the data from the database. This resulted in a 2x increase in the speed of the search feature.

The technologies used in the project included MongoDB for storing the data, Python for data processing, Flask for the web framework, HTTP requests for data collection, HTML for the user interface, Docker for containerization, and Redis for caching. Overall, this project demonstrated the ability to use modern technologies to collect, analyze, and visualize large amounts of data from social media platforms.

#*** System Architecture ****

