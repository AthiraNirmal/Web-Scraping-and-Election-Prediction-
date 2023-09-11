# Web-Scraping-and-Election-Prediction-

The project involved collecting election related posts from 4Chan API in JSON format through HTTP requests. After collecting the data, sentiment analysis was conducted on the posts to extract the emotions and opinions of the users towards the election.

Using the insights gained from the sentiment analysis, the project predicted the results of the election. The prediction was then visualized through a web-based user interface. The interface allowed users to search for posts related to specific keywords and view the prediction and the sentiment analysis of the posts.

To improve the speed of the search feature, the project implemented Redis caching. This caching technology allowed frequently searched posts to be stored in memory, reducing the time it took to retrieve the data from the database. This resulted in a 2x increase in the speed of the search feature.

The technologies used in the project included MongoDB for storing the data, Python for data processing, Flask for the web framework, HTTP requests for data collection, HTML for the user interface, Docker for containerization, and Redis for caching. Overall, this project demonstrated the ability to use modern technologies to collect, analyze, and visualize large amounts of data from social media platforms.

# *** System Architecture ****

<img width="1000" alt="Screen Shot 2023-09-11 at 6 14 53 PM" src="https://github.com/AthiraNirmal/Web-Scraping-and-Election-Prediction-/assets/63495996/044ee8e8-27e4-4bcd-97bf-0e6af3dfb814">

# Election Results graph on Web UI
<img width="698" alt="Screen Shot 2023-09-11 at 6 15 18 PM" src="https://github.com/AthiraNirmal/Web-Scraping-and-Election-Prediction-/assets/63495996/f7dc255a-d741-47d0-a387-791d4ac67449">

# Outcome after Sentimental Analysis 
-------------------------------------------------------------------------------------------------------
<img width="804" alt="Screen Shot 2023-09-11 at 6 25 50 PM" src="https://github.com/AthiraNirmal/Web-Scraping-and-Election-Prediction-/assets/63495996/dcecfc59-d7b3-401f-a0c5-03a47440c0d6">

<img width="494" alt="Screen Shot 2022-11-28 at 11 55 36 AM" src="https://github.com/AthiraNirmal/Web-Scraping-and-Election-Prediction-/assets/63495996/d0550df2-0ce5-420b-bd5f-e23e77581d8e">





