'''
Created on Jan 6, 2017

@author: jamey

Desc: get lacrosse ranks from www.laxpower.com
      Write to hs_lax_ranks.tsv and
      lax.high_schools
'''
import urllib.request
import psycopg2
from http.cookiejar import EPOCH_YEAR
from multiprocessing.managers import State

'''
From http://stackoverflow.com/questions/32978365/how-do-i-run-psycopg2-on-el-capitan-without-hitting-a-libssl-error
sudo ln -s /Library/PostgreSQL/9.6/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PostgreSQL/9.6/lib/libcrypto.1.0.0.dylib /usr/local/lib
sudo ln -s /tmp/.s.PGSQL.5432 /var/pgsql_socket/
'''
class UrlRecord:
    def __init__(self, url, year, gender):
        self.url = url
        self.year = year
        self.gender = gender
        
    def getUrl(self):
        return self.url
    
    def getYear(self):
        return self.year
    
    def getGender(self):
        return self.gender
    
class HSRankRecord:
    def __init__(self, url, gender, year, rank, hs, state):
        self.url = url
        self.gender = gender
        self.year = year
        self.rank = rank
        self.hs = hs
        self.state = State
        
    def getUrl(self):
        return self.url
    
    def getGender(self):
        return self.gender
    
    def getYear(self):
        return self.year
    
    def getRank(self):
        return self.rank
    
    def getHS(self):
        return self.hs
    
    def getState(self):
        return self.state

def getConnection():
    conn = psycopg2.connect(
                        dbname='lax',
                        user='lax',
                        port = 5432,
                        host='/tmp/', #added to avoid 'connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?'
                        password='cloudera')
    return conn

def runSQL(conn, sql):
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

def generateUrlRecords(startYear, endYear):
    # example: http://www.laxpower.com/update16/binboy/natlccr.php
    urlRecords = []
    gender = ['boy', 'grl'] 
    for year in range(startYear, endYear + 1):
        for gndr in gender:
            strYear = str(year)[2:]
            url = ("http://www.laxpower.com/update" + strYear + "/bin" + gndr + "/natlccr.php")
            urlRecord = UrlRecord(url, year, gndr)
            urlRecords.append(urlRecord)
    return (urlRecords)   # a dictionary of {url:, year:, gender:}

def getHSRankRecords(urlDict):
    response = urllib.request.urlopen(urlDict['url'])
      
    for line in response:
        row = str(line.rstrip())
        if row.find(".PHP") > 0:
            #print (row)
            lax_rank = eval(row[row.find("b'")+3:row.find("<A")])
            school = (row[(row.find('.PHP">')+6):row.find("</A>")].strip()).replace("\\","")
            # replace single-quote with two single-quote for the insert
            school = school.replace("'", ",,")
            # sometimes HS is embedded in the name
            school = school.replace(" HS ", " ")
            # sometimes there is a , STATE in the name
            if school.find(',') > 0:
                school = school[:school.find(',')]
            state = row[row.find("</A>") + 4:row.find("<span") - 12].strip()
            print(
                 urlDict['url'], '\t',
                 urlDict['gender'], '\t',
                 urlDict['year'], '\t',
                 str(lax_rank), '\t',
                 school, '\t',
                 state)
        elif row.find("padding-bottom") > 0:
            response.close()
    return (None)
   
def writeHSRank(url, gender, year, lax_rank, high_school, state):
    
    conn = getConnection()
  
    sql = (
           "INSERT INTO hs_ranks (" +
           "url," +
           "gender, " +
           "year, " +
           "lax_rank, " +
           "high_school, " +
           "state) VALUES (" +
           "'" + url + "', " +
           "'" + gender + "', " +
           str(year) + ", " +
           str(lax_rank) + ", " +
           "'" + high_school + "', " +
           "'" + state + "')" )
    runSQL(conn, sql)

    conn.close()
   
def main():   
    START_YEAR = 2005
    END_YEAR = 2005 #2016
    
    # urlList is a list of url dictionaries
    urls = []
    urls = generateUrlRecords(START_YEAR, END_YEAR)   
    
    for urlRecord in urls:
        print(urlRecord.getUrl())
    
    print('done')
    
    #for urlRecord in urls:
    #   hs_record = getHSRankRecords(urlRecord)
        
                    # writeHSRank(urlDict['url'], urlDict['gender'], urlDict['year'], str(lax_rank), school, state)
    
if __name__ == '__main__':
    main()
