# pinheirocfc@gmail.com
#para criar tokens https://developer.twitter.com/en - DeveloperPortal - Projects - Keys and Tokens
#documentacao da biblioteca em : https://twittersearch.readthedocs.io/en/v1.0.2/advanced_usage_ts.html
#orientações em: https://youtu.be/8EWBke8ephA

from TwitterSearch import * #pip install TwitterSearch
import json
import datetime

#Variaveis Gerais
lista_tweets = [] #lista para guardar os tweets com atributos filtrados
lista_full = [] #lista para guardar os tweets com todos os atributos
iCONTADOR = 0 #condicao de parada

try:

    #consumer_key/consumer_secret em: 'API key & secret'
    #access_token/access_token_secret em: 'Access token & secret'
    iCONECTA = TwitterSearch(
        consumer_key = 'COLE AQUI',
        consumer_secret = 'COLE AQUI',
        access_token = 'COLE AQUI',
        access_token_secret = 'COLE AQUI'
     )
   
    #atribudos de busca
    iATRIBUTO = TwitterSearchOrder()
    iATRIBUTO.set_keywords(['Palmeiras','Internacional'])
    iATRIBUTO.set_language('pt')    
    iATRIBUTO.set_geocode(-23.601002, -46.541939, 5, imperial_metric=False) #Geolocalizacao{long,lati,raio,metrica(True=Milhas/False=KM)} - opcional
    iATRIBUTO.set_since(datetime.date(2020,12,19)) #de(data) - opcional
    iATRIBUTO.set_until(datetime.date(2020,12,20)) #ate(data) - opcional
    #iATRIBUTO.set_result_type('recent') #tipo de resultados {mixed,recent,popular} - opcional
    #iATRIBUTO.set_positive_attitude_filter() #traz os resultados com perfil positivo - opcional
    #iATRIBUTO.set_negative_attitude_filter() #traz os resultados com perfil negativo - opcional
    #iATRIBUTO.set_question_filter() #traz os resultados que contenham perguntas - opcional

    for tweet in iCONECTA.search_tweets_iterable(iATRIBUTO):
        lista_full.append(tweet)
        lista_tweets.append((
                            "@" + str(tweet['user']['screen_name'])
                            ,tweet['user']['name']
                            ,tweet['text']
                            ,tweet['created_at']
                            ,tweet['source']
                            ,tweet['user']['profile_image_url']
                            )) 

        iCONTADOR += 1
        if iCONTADOR > 5: #condicao de parada, quantidade de resultados
            break

    json_full = json.dumps(lista_full, indent = 4, ensure_ascii=False) #guarda a lista no formato JSON
    json_filtro = json.dumps(lista_tweets, indent = 4, ensure_ascii=False) 
    #print(json_full)   
    print(json_filtro)   

except TwitterSearchException as e:
    print(e)
