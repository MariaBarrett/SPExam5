from TwitterSearch import *
try:
	tso = TwitterSearchOrder() 
	tso.setKeywords(['Obama']) 
	tso.setLanguage('en') #language (but it doesn't work)
	tso.setCount(10) 
	tso.setIncludeEntities(False)

	ts = TwitterSearch(
		consumer_key = '7d8lM6XzKGzn4fehSo64Q',
		consumer_secret = 'tJ5UxGI9EZyS4ZNnI5vppEplAUMKOqgNDcIE63OQc4',
		access_token = '35699187-tLjYIhF2KsAqlJaD1iB9qjeUHOS2zFi7pN89QbEdq',
		access_token_secret = 'y5YzkuPipvNJElpnyKcKGB1J5qObgRE8Z6AOr0a4g6so2'
		)


	for tweet in ts.searchTweetsIterable(tso): 
		print(unicode('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'])))

except TwitterSearchException as e: #in case of errors
	print (e)