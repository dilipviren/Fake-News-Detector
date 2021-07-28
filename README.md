# YouAreFakeNews

NLP algorithm to detect fake news

Raw data source : https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset

youarefakenews.joblib is the pipeline of the workflow 

Data preparation is present in dataset_prep and full_code 

Dataset was too large to run and sample was taken for training and new sample for testing

Text process contains the function used to break down the raw string into bags of words and used as analyzer for count vectorization

fake_news_algorithm contains the condensed code that can be used for training, testing or predictions

Training dataset was wholly taken from US news. 

external_test_data and fake_news_test_external is the test of analyzer, transformer, algorithm, pipeline and joblib

Code/algorithm implementation?
