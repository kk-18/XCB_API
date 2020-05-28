from elasticsearch import Elasticsearch

class ESclient:

    def  search(self,index,body):
        #连接es时host只写ip
        es_host = 'http://114.116.136.190'
        es = Elasticsearch(hosts=es_host,port=9200,timeout=15000)
        res = es.search(index=index, body=body)
        #获取返回数据总量
        ques_count = res['hits']['total']
        #获取返回数据
        data = res['hits']['hits']
        return(ques_count,data)

    def  update(self,index,body):
        #连接es时host只写ip
        es_host = 'http://114.116.136.190'
        es = Elasticsearch(hosts=es_host,port=9200,timeout=15000)
        res = es.update_by_query(index=index, body=body)
        #获取更新数据总量
        ques_count = res['updated']
        #获取返回数据
        return(ques_count)

    def  delete(self,index,body):
        #连接es时host只写ip
        es_host = 'http://114.116.136.190'
        es = Elasticsearch(hosts=es_host,port=9200,timeout=15000)
        res = es.delete_by_query(index=index, body=body)
        #获取更新数据总量
        ques_count = res['deleted']
        #获取返回数据
        return(ques_count)

