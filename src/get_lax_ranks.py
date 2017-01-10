'''
Created on Jan 6, 2017

@author: jamey

Desc: get lacrosse ranks from www.laxpower.com
      Write to hs_lax_ranks.tsv and
      lax.high_schools
'''
import urllib.request
import psycopg2
# from http.cookiejar import EPOCH_YEAR
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
        self.state = state
        
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

def getHSRankRecords(urlRecord):
    response = urllib.request.urlopen(urlRecord.getUrl())
    
    HSRankRecords = []
    
    for line in response:
        row = str(line.rstrip())
        if row.find(".PHP") > 0:
            lax_rank = eval(row[row.find("b'")+3:row.find("<A")])
            school = (row[(row.find('.PHP">')+6):row.find("</A>")].strip()).replace("\\","")
            if school.find(',') > 0:
                school = school[:school.find(',')]
            school = school.replace("'", "''")  #PostgreSQL double ticks [''] are escapes for single ticks [']
            state = row[row.find("</A>") + 4:row.find("<span") - 12].strip()
            hsRankRecord = HSRankRecord(urlRecord.getUrl(), urlRecord.getGender(), urlRecord.getYear(), str(lax_rank), school, state)
            HSRankRecords.append(hsRankRecord)
        elif row.find("padding-bottom") > 0:
            response.close()
    return (HSRankRecords)

def writeHSRankRecord(HSRankRecord, conn):    
    sql = '''
INSERT INTO lax.hs_ranks (
    url,
    gender,
    year,
    rank,
    raw_hs_name,
    state) VALUES (''' + (
    "'" + HSRankRecord.getUrl() + "', " +
    "'" + HSRankRecord.getGender() + "', " +
    str(HSRankRecord.getYear()) + ", " +
    str(HSRankRecord.getRank()) + ", " +
    "'" + HSRankRecord.getHS() + "', " +
    "'" + HSRankRecord.getState() + "');")
    
    runSQL(conn, sql)
    #conn.close()

def populateHighSchools(conn, num_schools_per_year):
    sql = '''
INSERT INTO lax.high_schools (
   raw_name,
   state) 
   (SELECT DISTINCT
     raw_hs_name,
     state
   FROM lax.hs_ranks
   WHERE rank <= ''' + str(num_schools_per_year) + ');'
    
    runSQL(conn, sql)
    
def updateHSRanks(conn):
    sql = '''
 UPDATE lax.hs_ranks AS hr
 SET hs_id = (
   SELECT hs.id
   FROM lax.high_schools hs
   WHERE hs.raw_name = hr.raw_hs_name
   AND hs.state = hr.state);'''
    
    runSQL(conn, sql)
   
def main():   
    START_YEAR = 2003
    END_YEAR = 2016
    num_schools_per_year = 1500
    conn = getConnection()
    
    # urlList is a list of url dictionaries
    urls = []
    urls = generateUrlRecords(START_YEAR, END_YEAR)
    
    hsRankRecords = []
    
    for urlRecord in urls:
        hsRankRecords = getHSRankRecords(urlRecord)
        
        for HSRankRecord in hsRankRecords:
            writeHSRankRecord(HSRankRecord, conn)
        
        print('Completed ', HSRankRecord.getGender(), ':', str(HSRankRecord.getYear()))
    
    populateHighSchools(conn, num_schools_per_year)
    print('Populated lax.high_schools')
    
    updateHSRanks(conn)
    print('Updated lax.hs_ranks')
        
    conn.close()
    print('All done')
if __name__ == '__main__':
    main()
