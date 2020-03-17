import json
import urllib.request

models = ['bm25', 'dfr', 'lm']

#running code for all models
for i in models:

	count = 1
	with open('test_queries.txt', encoding="utf-8") as f:
		for q in f:
			line=q[4:]
			query = line.strip('\n').replace(':','')
			print("query",len(query))
			if(len(query) > 0):
				query = urllib.parse.quote(query)
				query = "text_en:(" + query + ")%20OR%20text_de:(" + query + ")%20OR%20text_ru:(" + query + ")"
				inurl = 'http://ec2-18-222-26-114.us-east-2.compute.amazonaws.com:8983/solr/'+ i +'/select?q='+ query +'&fl=id%2Cscore&wt=json&indent=true&rows=20'
				print(inurl)
				qid = str(count).zfill(3)
				outf = open(i.upper() +'/' + str(count) + '.txt', 'w')
				data = urllib.request.urlopen(inurl).read()
				docs = json.loads(data.decode('utf-8'))['response']['docs']
				rank = 1
			
				fout = open( i+ 'Test.txt', 'a+')
				for doc in docs:
					outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + i + '\n')
					fout.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + i + '\n')
					rank += 1
				count += 1
				fout.close()
