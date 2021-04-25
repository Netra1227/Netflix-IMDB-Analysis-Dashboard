import pandas as pd
data = pd.read_csv("netflix_titles.csv")
movies = data[data['type'] == 'Movie']
df = movies[['title', 'release_year', 'listed_in', 'country']]
df = df.rename(columns={'release_year': 'year'})
imdb_movies = pd.read_csv('IMDb movies.csv')
imdb_movies = imdb_movies[['imdb_title_id', 'title', 'year']]
imdb_ratings = pd.read_csv('IMDb ratings.csv')
imdb = pd.merge(imdb_movies, imdb_ratings, on='imdb_title_id')
imdb = imdb[['title', 'year', 'weighted_average_vote', 'allgenders_0age_avg_vote', 'allgenders_0age_votes', 'allgenders_18age_avg_vote', 'allgenders_18age_votes',
             'allgenders_30age_avg_vote', 'allgenders_30age_votes', 'allgenders_45age_avg_vote', 'allgenders_45age_votes',
             'males_allages_avg_vote', 'males_allages_votes', 'males_0age_avg_vote', 'males_0age_votes',
             'males_18age_avg_vote', 'males_18age_votes', 'males_30age_avg_vote', 'males_30age_votes', 
             'males_45age_avg_vote', 'males_45age_votes', 'females_allages_avg_vote', 'females_allages_votes',
             'females_0age_avg_vote', 'females_0age_votes', 'females_18age_avg_vote', 'females_18age_votes',
             'females_30age_avg_vote', 'females_30age_votes', 'females_45age_avg_vote', 'females_45age_votes']]
imdb = imdb.fillna(0)

def weighted_averages(number, avg, row):
    if row[number] != 0.0:
        wr = ((row[number]/(row[number]+1000))*row[avg]) + ((1000/(row[number]+1000))*5.9)
    else:
        wr = 0
    return wr
weighted_allgenders_0age = []
weighted_allgenders_18age = []
weighted_allgenders_30age = []
weighted_allgenders_45age = []
weighted_males_allages = []
weighted_males_0age = []
weighted_males_18age = []
weighted_males_30age = []
weighted_males_45age = []
weighted_females_allages = []
weighted_females_0age = []
weighted_females_18age = []
weighted_females_30age = []
weighted_females_45age = []

for i in range(len(imdb)):
    weighted_allgenders_0age.append(weighted_averages('allgenders_0age_votes', 'allgenders_0age_avg_vote', imdb.iloc[i]))
    weighted_allgenders_18age.append(weighted_averages('allgenders_18age_votes', 'allgenders_18age_avg_vote', imdb.iloc[i]))
    weighted_allgenders_30age.append(weighted_averages('allgenders_30age_votes', 'allgenders_30age_avg_vote', imdb.iloc[i]))
    weighted_allgenders_45age.append(weighted_averages('allgenders_45age_votes', 'allgenders_45age_avg_vote', imdb.iloc[i]))
    weighted_males_allages.append(weighted_averages('males_allages_votes', 'males_allages_avg_vote', imdb.iloc[i]))
    weighted_males_0age.append(weighted_averages('males_0age_votes', 'males_0age_avg_vote', imdb.iloc[i]))
    weighted_males_18age.append(weighted_averages('males_18age_votes', 'males_18age_avg_vote', imdb.iloc[i]))
    weighted_males_30age.append(weighted_averages('males_30age_votes', 'males_30age_avg_vote', imdb.iloc[i]))
    weighted_males_45age.append(weighted_averages('males_45age_votes', 'males_45age_avg_vote', imdb.iloc[i]))
    weighted_females_allages.append(weighted_averages('females_allages_votes', 'females_allages_avg_vote', imdb.iloc[i]))
    weighted_females_0age.append(weighted_averages('females_0age_votes', 'females_0age_avg_vote', imdb.iloc[i]))
    weighted_females_18age.append(weighted_averages('females_18age_votes', 'females_18age_avg_vote', imdb.iloc[i]))
    weighted_females_30age.append(weighted_averages('females_30age_votes', 'females_30age_avg_vote', imdb.iloc[i]))
    weighted_females_45age.append(weighted_averages('females_45age_votes', 'females_45age_avg_vote', imdb.iloc[i]))
    
imdb['weighted_allgenders_0age'] = weighted_allgenders_0age
imdb['weighted_allgenders_18age'] = weighted_allgenders_18age
imdb['weighted_allgenders_30age'] = weighted_allgenders_30age
imdb['weighted_allgenders_45age'] = weighted_allgenders_45age
imdb['weighted_males_allages'] = weighted_males_allages
imdb['weighted_males_0age'] = weighted_males_0age
imdb['weighted_males_18age'] = weighted_males_18age
imdb['weighted_males_30age'] = weighted_males_30age
imdb['weighted_males_45age'] = weighted_males_45age
imdb['weighted_females_allages'] = weighted_females_allages
imdb['weighted_females_0age'] = weighted_females_0age
imdb['weighted_females_18age'] = weighted_females_18age
imdb['weighted_females_30age'] = weighted_females_30age
imdb['weighted_females_45age'] = weighted_females_45age

imdb = imdb[['title', 'year', 'weighted_average_vote', 'weighted_allgenders_0age', 'weighted_allgenders_18age', 'weighted_allgenders_30age', 'weighted_allgenders_45age',
            'weighted_males_allages', 'weighted_males_0age', 'weighted_males_18age', 'weighted_males_30age', 'weighted_males_45age',
            'weighted_females_allages', 'weighted_females_0age', 'weighted_females_18age', 'weighted_females_30age', 'weighted_females_45age']]

merged = df.merge(imdb, how="inner", left_on=['title', 'year'], right_on=['title', 'year'])
merged.to_csv('merged.csv')
print("CSV Generated")
